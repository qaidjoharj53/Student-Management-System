"""to maintain student details
roll number
name
percentage
"""
"""
modules imported
"""
import pickle
import os
import time

import mysql.connector
connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="student_management"
)
cursor = connection.cursor()
"""
class used
"""


class student(object):
    def __init__(self):
        self.roll = 0
        self.name = ""
        self.per = 0

    def add_rec(self):
        self.roll = int(input("Enter roll number: "))
        self.name = input("Enter name: ")
        self.name = self.name.upper()
        self.per = float(input("Enter percentage: "))

        sql = "INSERT INTO students (roll, name, percentage) VALUES (%s, %s, %s)"
        values = (self.roll, self.name, self.per)
        cursor.execute(sql, values)
        connection.commit()

    def disp_rec(self):
        print("roll number: ", self.roll)
        print("name: ", self.name)
        print("percentage: ", self.per)

    def display_rec(self):
        print("%-10s" % self.roll, "%-20s" % self.name, "%-10s" % self.per)

    def modify_rec(self):
        self.roll = int(input("Enter new roll number: "))
        self.name = input("Enter new name: ")
        self.name = self.name.upper()
        self.per = float(input("Enter new percentage: "))

cursor.execute("CREATE TABLE IF NOT EXISTS students(roll int primary key,name varchar(100), percentage int )")



def write_record():
    rec = student()
    rec.add_rec()
    print("Record added in file!")
    input("Press any key to continue....")


def display_all():
    print(40 * "=")
    print("\n\t    Student Records\n")
    print(40 * "=")
    try:
        cursor.execute("SELECT * FROM students")
        records = cursor.fetchall()
        for row in records:
            rec = student()
            rec.roll, rec.name, rec.per = row
            rec.display_rec()
    except mysql.connector.Error as error:
        print("Error reading data from MySQL:", error)


def search_roll():
    try:
        z = 0
        print(40 * "=")
        print("Record searching by roll number...")
        print(40 * "=")
        n = int(input("Enter roll number to search: "))
        cursor.execute("SELECT * FROM students WHERE roll = %s", (n,))
        record = cursor.fetchone()
        if record:
            rec = student()
            rec.roll, rec.name, rec.per = record
            z = 1
            print("\nRecord found and details are:\n")
            rec.disp_rec()
    except mysql.connector.Error as error:
        print("Error reading data from MySQL:", error)
    if z == 0:
        print("Record is not present!!")
    input("Press any key to continue....")


def search_name():
    try:
        z = 0
        print(40 * "=")
        print("Record searching by name...")
        print(40 * "=")
        n = input("Enter name to search: ")
        n = n.upper()
        cursor.execute("SELECT * FROM students WHERE name = %s", (n,))
        records = cursor.fetchall()
        for record in records:
            rec = student()
            rec.roll, rec.name, rec.per = record
            z = 1
            print("\nRecord found and details are:\n")
            rec.disp_rec()
    except mysql.connector.Error as error:
        print("Error reading data from MySQL:", error)
    if z == 0:
        print("Record is not present!!")
    input("Press any key to continue....")

def modify_roll():
    z = 0
    try:
        n = int(input("Enter roll number to modify: "))
        cursor.execute("SELECT * FROM students WHERE roll = %s", (n,))
        record = cursor.fetchone()
        if record:
            rec = student()
            rec.roll, rec.name, rec.per = record
            z = 1
            print("\nRecord found and details are:\n")
            rec.disp_rec()
            print("\nEnter new data...")
            rec.modify_rec()
            sql = "UPDATE students SET name = %s, percentage = %s WHERE roll = %s"
            values = (rec.name, rec.per, rec.roll)
            cursor.execute(sql, values)
            connection.commit()
            print("Record updated!")
    except mysql.connector.Error as error:
        print("Error updating data in MySQL:", error)
    if z == 0:
        print("Record not found!!")
    input("Press any key to continue....")

def delete_roll():
    z = 0
    try:
        n = int(input("Enter roll number to delete: "))
        cursor.execute("SELECT * FROM students WHERE roll = %s", (n,))
        record = cursor.fetchone()
        if record:
            rec = student()
            rec.roll, rec.name, rec.per = record
            z = 1
            print("\nRecord to delete found and details are:\n")
            rec.disp_rec()
            sql = "DELETE FROM students WHERE roll = %s"
            cursor.execute(sql, (rec.roll,))
            connection.commit()
            print("Record deleted!")
    except mysql.connector.Error as error:
        print("Error deleting data in MySQL:", error)
    if z == 0:
        print("Record not found!!")
    input("Press any key to continue....")

cursor.execute("SELECT * FROM students LIMIT 1")
record = cursor.fetchone()
if record is None:
    print("'students' table is empty.")
    print("1 -> Generate some fake data")
    print("2 -> Go with empty table")

    print(40 * "=")
    choice = input("Enter your choice: ")
    print(40 * "=")

    if choice == "1":
        print("Generating fake data...")
        os.system("python create_data.py")
        print("Fake data generated.")
    elif choice != "2":
        print("Invalid choice!")
        time.sleep(1)



while True:
    os.system("cls")
    print(40 * "=")
    print(
        """              Main Menu
              ---------
        1. Add record
        2. Display all records
        3. Search by roll number
        4. Search by name
        5. Modify by roll number
        6. Delete by roll number
        7. Exit
    """
    )
    print(40 * "=")
    ch = int(input("Enter your choice: "))
    print(40 * "=")
    if ch == 1:
        write_record()
    elif ch == 2:
        display_all()
        time.sleep(2)
    elif ch == 3:
        search_roll()
    elif ch == 4:
        search_name()
    elif ch == 5:
        modify_roll()
    elif ch == 6:
        delete_roll()
    elif ch == 7:
        print("\n\t      !!!End!!!\n")
        connection.close()
        time.sleep(2)
        break
    else:
        print("Invalid choice!!")
        time.sleep(1)
