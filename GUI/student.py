# student.py


class Student:
    def __init__(self):
        self.roll = 0
        self.name = ""
        self.per = 0

    def add_record(self, roll, name, per):
        self.roll = roll
        self.name = name.upper()
        self.per = per

    def display_record(self):
        return f"Roll Number: {self.roll}\nName: {self.name}\nPercentage: {self.per}"
