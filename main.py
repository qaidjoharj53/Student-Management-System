import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

import pickle
import os
import time
from student import Student


def write_record():
    try:
        rec = Student()
        rec.add_rec()
        with open("stud.dat", "ab") as file:
            pickle.dump(rec, file)
        print("Record added in file!")
    except Exception as e:
        print("An error occurred:", e)


def display_all():
    print(40 * "=")
    print("\n\t    Student Records\n")
    print(40 * "=")
    try:
        with open("stud.dat", "rb") as file:
            while True:
                rec = pickle.load(file)
                rec.display_rec()
    except EOFError:
        print(40 * "=")
        input("Press Enter to continue....")
    except IOError:
        print("File could not be opened!!")


def search_roll():
    try:
        z = 0
        print(40 * "=")
        print("Record searching by roll number...")
        print(40 * "=")
        n = int(input("Enter roll number to search: "))
        with open("stud.dat", "rb") as file:
            while True:
                rec = pickle.load(file)
                if rec.roll == n:
                    z = 1
                    print("\nRecord found and details are:\n")
                    rec.disp_rec()
                    break
    except EOFError:
        if z == 0:
            print("Record is not present!!")
    except IOError:
        print("File could not be opened!!")
    input("Press Enter to continue....")


def search_name():
    try:
        z = 0
        print(40 * "=")
        print("Record searching by name...")
        print(40 * "=")
        n = input("Enter name to search: ")
        with open("stud.dat", "rb") as file:
            while True:
                rec = pickle.load(file)
                if rec.name == n.upper():
                    z = 1
                    print("\nRecord found and details are:\n")
                    rec.disp_rec()
                    break
    except EOFError:
        if z == 0:
            print("Record is not present!!")
    except IOError:
        print("File could not be opened!!")
    input("Press Enter to continue....")


def modify_roll():
    z = 0
    try:
        n = int(input("Enter roll number to modify: "))
        with open("stud.dat", "rb") as file, open("temp.dat", "wb") as temp:
            while True:
                rec = pickle.load(file)
                if rec.roll == n:
                    z = 1
                    print("\nRecord found and details are:\n")
                    rec.disp_rec()
                    print("\nEnter new data...")
                    rec.modify_rec()
                    pickle.dump(rec, temp)
                    print("Record updated!")
                else:
                    pickle.dump(rec, temp)
    except EOFError:
        if z == 0:
            print("Record not found!!")
    except IOError:
        print("File could not be opened!!")
    os.remove("stud.dat")
    os.rename("temp.dat", "stud.dat")
    input("Press Enter to continue....")


def delete_roll():
    z = 0
    try:
        n = int(input("Enter roll number to delete: "))
        with open("stud.dat", "rb") as file, open("temp.dat", "wb") as temp:
            while True:
                rec = pickle.load(file)
                if rec.roll == n:
                    z = 1
                    print("\nRecord to delete found and details are:\n")
                    rec.disp_rec()
                else:
                    pickle.dump(rec, temp)
    except EOFError:
        if z == 0:
            print("Record not found!!")
    except IOError:
        print("File could not be opened!!")
    os.remove("stud.dat")
    os.rename("temp.dat", "stud.dat")
    input("Press Enter to continue....")


class StudentManagementApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Student Management System")

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout()

        self.addButton = QPushButton("Add Student", self)
        self.addButton.clicked.connect(self.add_student)

        self.displayButton = QPushButton("Display All Students", self)
        self.displayButton.clicked.connect(self.display_students)

        self.searchButton = QPushButton("Search Student", self)
        self.searchButton.clicked.connect(self.search_student)

        self.modifyButton = QPushButton("Modify Student", self)
        self.modifyButton.clicked.connect(self.modify_student)

        self.deleteButton = QPushButton("Delete Student", self)
        self.deleteButton.clicked.connect(self.delete_student)

        self.exitButton = QPushButton("Exit", self)
        self.exitButton.clicked.connect(self.close)

        self.layout.addWidget(self.addButton)
        self.layout.addWidget(self.displayButton)
        self.layout.addWidget(self.searchButton)
        self.layout.addWidget(self.modifyButton)
        self.layout.addWidget(self.deleteButton)
        self.layout.addWidget(self.exitButton)

        self.centralWidget.setLayout(self.layout)

        self.show()

    def add_student(self):
        write_record()

    def display_students(self):
        display_all()

    def search_student(self):
        search_roll()

    def modify_student(self):
        modify_roll()

    def delete_student(self):
        delete_roll()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentManagementApp()
    sys.exit(app.exec_())
