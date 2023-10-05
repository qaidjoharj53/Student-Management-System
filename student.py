class Student(object):
    def __init__(self):
        self.roll = 0
        self.name = ""
        self.per = 0

    def add_rec(self):
        self.roll = int(input("Enter roll number: "))
        self.name = input("Enter name: ")
        self.name = self.name.upper()
        self.per = float(input("Enter percentage: "))

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
