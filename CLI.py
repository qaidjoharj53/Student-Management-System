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

""" 
class used 
"""


class student(object):
    def __int__(s):
        s.roll = 0
        s.name = ""
        s.per = 0

    def add_rec(s):
        s.roll = int(input("Enter roll number: "))
        s.name = input("Enter name: ")
        s.name = s.name.upper()
        s.per = float(input("Enter percentage: "))

    def disp_rec(s):
        print("roll number: ", s.roll)
        print("name: ", s.name)
        print("percentage: ", s.per)

    def display_rec(s):
        print("%-10s" % s.roll, "%-20s" % s.name, "%-10s" % s.per)
        # print("in display_rec")

    def modify_rec(s):
        s.roll = int(input("Enter new roll number: "))
        s.name = input("Enter new name: ")
        s.name = s.name.upper()
        s.per = float(input("Enter new percentage: "))


def write_record():
    try:
        rec = student()
        file = open("stud.dat", "ab")
        rec.add_rec()
        pickle.dump(rec, file)
        file.close()
        print("Record added in file!")
        input("Press any key to continue....")
    except:
        pass


def display_all():
    print(40 * "=")
    print("\n\t    Student Records\n")
    print(40 * "=")
    try:
        file = open("stud.dat", "rb")
        while True:
            rec = pickle.load(file)
            rec.display_rec()
    except EOFError:
        file.close()
        print(40 * "=")
        input("Press any key to continue....")
    except IOError:
        print("File could not be opened!!")


def search_roll():
    try:
        z = 0
        print(40 * "=")
        print("Record searching by roll number...")
        print(40 * "=")
        n = int(input("Enter roll number to search: "))
        file = open("stud.dat", "rb")
        while True:
            rec = pickle.load(file)
            # print(rec.roll)
            if rec.roll == n:
                z = 1
                print("\nRecord found and details are:\n")
                rec.disp_rec()
                break
    except EOFError:
        file.close()
        if z == 0:
            print("Record is not present!!")
    except IOError:
        print("File could not be opened!!")
    input("Press any key to continue....")


def search_name():
    try:
        z = 0
        print(40 * "=")
        print("Record searching by name...")
        print(40 * "=")
        n = input("Enter name to search: ")
        file = open("stud.dat", "rb")
        while True:
            rec = pickle.load(file)
            # print(rec.roll)
            if rec.name == n.upper():
                z = 1
                print("\nRecord found and details are:\n")
                rec.disp_rec()
                break
    except EOFError:
        file.close()
        if z == 0:
            print("Record is not present!!")
    except IOError:
        print("File could not be opened!!")
    input("Press any key to continue....")


def modify_roll():
    z = 0
    try:
        n = int(input("Enter roll number to modify: "))
        file = open("stud.dat", "rb")
        temp = open("temp.dat", "wb")
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
        file.close()
        temp.close()
        if z == 0:
            print("Record not found!!")
    except IOError:
        print("File could not be opened!!")
    os.remove("stud.dat")
    os.rename("temp.dat", "stud.dat")
    input("Press any key to continue....")


def delete_roll():
    z = 0
    try:
        n = int(input("Enter roll number to delete: "))
        file = open("stud.dat", "rb")
        temp = open("temp.dat", "wb")
        while True:
            rec = pickle.load(file)
            if rec.roll == n:
                z = 1
                print("\nRecord to delete found and details are:\n")
                rec.disp_rec()
                # pickle.dump(rec,temp)
                print("Record updated!")
            else:
                pickle.dump(rec, temp)
    except EOFError:
        file.close()
        temp.close()
        if z == 0:
            print("Record not found!!")
    except IOError:
        print("File could not be opened!!")
    os.remove("stud.dat")
    os.rename("temp.dat", "stud.dat")
    input("Press any key to continue....")


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
        time.sleep(2)
        break
    else:
        print("Invalid choice!!")
        time.sleep(1)
