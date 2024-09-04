CREATE TABLE person (
    person_id               INTEGER PRIMARY KEY, 
    first_name              TEXT, 
    last_name               TEXT,
    birth_date              TEXT,
    gender                  TEXT,
    height                  INTEGER,
    email                   TEXT,
    salt                    TEXT,
    password_hash           TEXT
);

CREATE TABLE measurement (
    person_id               INTEGER,
    measurement_datetime    TEXT, 
    type                    TEXT,
    value                   REAL
);

CREATE TABLE consumed (
    person_id               INTEGER,
    consumed_datetime       TEXT,
    food                    TEXT,
    calories                REAL
);

-- CREATE TABLE consumed (
--     person_id               INTEGER,
--     consumed_datetime       TEXT,
--     food_id                 INTEGER,
--     num_servings            REAL
-- );

-- CREATE TABLE food (
--     food_id                 INTEGER PRIMARY KEY,
--     name                    TEXT,
--     calories                REAL
-- );
