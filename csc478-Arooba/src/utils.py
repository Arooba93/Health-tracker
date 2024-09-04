from datetime import datetime
import bcrypt
import base64
import hashlib


def calculate_age(birth_date_str: str) -> int:
    birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


def calculate_bmi(weight: float, height: float) -> float:
    return (weight / (height ** 2)) * 703


def calculate_bmr(weight: float, height: float, age: int, gender: str) -> float:
    if gender == "Male":
        return 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
    else:
        return 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)


def does_pw_match(password: bytes, salt: bytes, db_password_hash: bytes) -> bool:
    """Checks to see if password and salt match the data password hash"""
    pw_digest = base64.b64encode(hashlib.sha256(password)).digest()
    attempted_pw_hash = bcrypt.hashpw(pw_digest, salt)
    return bcrypt.checkpw(attempted_pw_hash, db_password_hash)


def get_salt() -> bytes:
    return bcrypt.gensalt()


#This is for set daily calorie tab in GUI.
def calculate_calories():
    age = int(age_entry_goal.get())
    weight = float(weight_entry_goal.get())
    feet = int(feet_entry_goal.get())
    inches = int(inches_entry_goal.get())
    gender_goal = gender_combobox_goal.get()
    weight_loss_goal = float(weight_loss_entry.get())

    # Convert height to inches
    height_inches = feet * 12 + inches

    # Calculate BMR (Basal Metabolic Rate)
    if gender_goal == 'Male':
        bmr_goal = 66 + (6.23 * weight) + (12.7 * height_inches) - (6.8 * age)
    else:
        bmr_goal = 655 + (4.35 * weight) + (4.7 * height_inches) - (4.7 * age)

    # Calculate daily calorie intake for weight loss
    calories_per_day = bmr_goal - (weight_loss_goal * 3500 / 7)

    result_label_goal.config(text=f"Recommended daily calories intake: {calories_per_day:.2f} calories")
