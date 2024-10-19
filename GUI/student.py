class Student:
    def __init__(self):
        self.roll = 0
        self.name = ""
        self.per = 0.0

    def add_record(self, roll, name, per):
        self.roll = roll
        self.name = name.upper()
        self.per = per

    def display_record(self):
        return f"{self.roll},{self.name},{self.per}"

    def __str__(self):
        return f"Roll: {self.roll}, Name: {self.name}, Percentage: {self.per}"
