import sqlite3
from person import Person


class DbAgent:

    def __init__(self, db_name: str = "../db/health_tracker.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def get_person(self, person_id: int=0) -> Person:
        person = Person()
        query = f"SELECT * FROM person where person_id = {person_id}"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if result:
            person.set_person_id(result[0])
            person.set_first_name(result[1])
            person.set_last_name(result[2])
            person.set_birth_date(result[3])
            person.set_gender(result[4])
            person.set_height(result[5])
            person.set_email(result[6])
            person.set_weights(self.get_weights(person_id))
            person.set_calories(self.get_calories(person_id))
        else:
            person = None
        return person

    def insert_weight(self, date, weight, person_id=0):
        """Insert a weight entry into the database for person_id"""
        # Make sure the entry doesn't already exist
        query = """
            SELECT *
            FROM measurement
            WHERE person_id = ? AND measurement_datetime = ? AND type = 'weight' and value = ?
        """
        self.cursor.execute(query, (person_id, date, weight))
        rows = self.cursor.fetchall()
        if not rows:
            query = f"INSERT INTO measurement VALUES (?, ?, ?, ?)"
            self.cursor.execute(query, (person_id, date, 'weight', weight))
            self.conn.commit()

    def get_weights(self, person_id: int=0) -> list[tuple[str, float]]:
        """Return a list of tuples in the format (datetime, weight) for person_id from the database"""
        query = """
            SELECT DISTINCT measurement_datetime, value 
            FROM measurement 
            WHERE person_id = ? AND type='weight'
            ORDER BY datetime(measurement_datetime) ASC
        """
        self.cursor.execute(query, (person_id, ))
        rows = self.cursor.fetchall()
        weights = [(row[0], row[1]) for row in rows]
        return weights

    def update_weight(self, measurement_datetime: str, old_weight: float, new_weight: float, person_id: int=0) -> None:
        """Update an existing weight in the database"""
        query = """
            UPDATE measurement
            SET value = ?
            WHERE person_id = ? AND type = 'weight' AND measurement_datetime = ? AND value = ?
        """
        self.cursor.execute(query, (new_weight, person_id, measurement_datetime, old_weight))
        self.conn.commit()

    def delete_weight(self, measurement_datetime: str, weight: float, person_id: int=0) -> None:
        """Delete an existing weight entry from the database"""
        query = """
            DELETE FROM measurement
            WHERE person_id = ? AND measurement_datetime = ? AND type = 'weight' AND value = ?
        """
        self.cursor.execute(query, (person_id, measurement_datetime, weight))
        self.conn.commit()

    def get_calories(self, person_id: int=0) -> list[tuple[str, str, float]]:
        """
        Return a list of tuples in the format (datetime, name, calories) for person_id from the database.
        The name is the name of the food item consumed and calories is the total number of calories.
        """
        query = """
            SELECT DISTINCT consumed_datetime, food, calories
            FROM consumed
            WHERE person_id = ?
            ORDER BY datetime(consumed_datetime) ASC
        """
        self.cursor.execute(query, (person_id, ))
        rows = self.cursor.fetchall()
        calories = [(row[0], row[1], row[2]) for row in rows]
        return calories


    def clean_table(self, table_name: str) -> None:
        """
        Remove duplicate entries from the specified table

        Args:
            table_name (str): The name of the table from which duplicates will be removed
        """
        self.cursor.execute(f"CREATE TABLE {table_name}_temp AS SELECT DISTINCT * FROM {table_name}")
        self.cursor.execute(f"DROP TABLE {table_name}")
        self.cursor.execute(f"ALTER TABLE {table_name}_temp RENAME TO {table_name}")
        self.conn.commit()

    def clean_all_tables(self) -> None:
        """Remove duplicate entries from all tables"""
        tables = ["person", "measurement", "consumed"]
        for table in tables:
            self.clean_table(table)

    def close(self) -> None:
        self.clean_all_tables()
        self.conn.close()


if __name__ == "__main__":
    db = DbAgent()
    person = db.get_person()

    print("\nInserting weights")
    db.insert_weight("2023-09-28 09:57:00", 218.4)
    db.insert_weight("2023-08-12 09:43:23", 223.8)
    weights = db.get_weights()
    for d, w in weights:
        print(f"{d}: {w}")

    print("\nDeleting a weight entry")
    db.delete_weight("2023-09-28 09:57:00", 218.4)
    weights = db.get_weights()
    for d, w in weights:
        print(f"{d}: {w}")

    # What happens if there's no entry in the database?
    weights = db.get_weights(31325)
    for d, w in weights:
        print(f"{d}: {w}")

    db.close()