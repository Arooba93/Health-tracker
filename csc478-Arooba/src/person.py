from utils import *
import tkinter as tk
from tkinter import ttk


class Person:

    def __init__(self):
        self.person_id = None
        self.first_name = None
        self.last_name = None
        self.birth_date = None
        self.gender = None
        self.height = None
        self.email = None
        self.salt = None
        self.password_hash = None
        self.name = None
        self.weight = None
        self.weights = None
        self.calories = None
        self.age = None
        self.bmi = None
        self.bmr = None
        self.measurements = None
        self.goals = None

    def set_person_id(self, _person_id: int) -> None:
        self.person_id = _person_id

    def set_first_name(self, _first_name: str) -> None:
        self.first_name = _first_name

    def set_last_name(self, _last_name: str) -> None:
        self.last_name = _last_name
        self.name = " ".join([self.first_name, self.last_name])

    def set_birth_date(self, _birth_date: str) -> None:
        self.birth_date = _birth_date
        self.age = calculate_age(self.birth_date)

    def set_gender(self, _gender) -> None:
        self.gender = _gender

    def set_height(self, _height: int) -> None:
        self.height = _height

    def set_email(self, _email: str) -> None:
        self.email = _email

    def set_password_hash(self, _password: str) -> None:
        pass

    def set_weight(self, _weight: float) -> None:
        self.weight = _weight

    def set_weights(self, _weights: list[tuple[str, float]]) -> None:
        self.weights = _weights
        self.set_weight(self.weights[-1][1])

    def set_calories(self, _calories: list[tuple[str, str, float]]) -> None:
        self.calories = _calories

    def set_bmi(self) -> None:
        self.bmi = calculate_bmi(self.weight, self.height)

    def set_bmr(self) -> None:
        self.bmr = calculate_bmr(self.weight, self.height, self.age, self.gender)

    def set_measurements(self) -> None:
        pass

    def set_goals(self) -> None:
        pass

    def get_first_name(self) -> str:
        return self.first_name

    def get_last_name(self) -> str:
        return self.last_name

    def get_name(self) -> str:
        return self.name

    def get_birth_date(self) -> str:
        return self.birth_date

    def get_age(self) -> int:
        return self.age

    def get_gender(self) -> str:
        return self.gender

    def get_height(self) -> int:
        return self.height

    def get_weight(self) -> float:
        return self.weight

    def get_bmi(self) -> float:
        return self.bmi

    def get_bmr(self) -> float:
        return self.bmr

    def calculate_bmi(self) -> None:
        self.bmi = (self.weight / (self.height ** 2)) * 703

    def calculate_bmr(self) -> None:
        if self.gender == "Male":
            self.bmr = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
        else:
            self.bmr = 655 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age)
