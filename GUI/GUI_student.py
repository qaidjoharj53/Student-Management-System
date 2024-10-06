from PyQt5.QtWidgets import *
from PyQt5 import uic
import student
import file_operations
import os  # Import os for file operations


class Mygui(QMainWindow):

    def __init__(self):
        super(Mygui, self).__init__()
        uic.loadUi("first_gui.ui", self)

        self.show()

        # Connect buttons to their respective methods
        self.pushButton.clicked.connect(self.add_record)         # Record Button
        self.pushButton_2.clicked.connect(self.display_records)  # Display Records Button
        self.pushButton_3.clicked.connect(self.delete_file)      # Delete All Records Button

    def add_record(self):
        # Retrieve input values from the GUI
        roll = self.lineEdit.text()
        name = self.lineEdit_2.text()
        percentage = self.lineEdit_3.text()

        # Ensure the inputs are valid (check if fields are not empty and percentage is numeric)
        if roll.isdigit() and percentage.replace('.', '', 1).isdigit():
            # Create a Student object
            student_obj = student.Student()
            student_obj.add_record(int(roll), name, float(percentage))

            # Write the student record to the file using file_operations
            result = file_operations.write_record(student_obj)
            self.statusBar().showMessage(result)  # Display result message in the status bar

            # Clear the input fields after adding the record
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
        else:
            self.statusBar().showMessage("Invalid input. Please check the fields.")

    def display_records(self):
        # Fetch all records from the file using file_operations
        records = file_operations.display_all_records()

        # Clear the textEdit area before displaying new records
        self.textEdit.clear()

        # Display all records in the textEdit widget
        if records:
            for record in records:
                self.textEdit.append(record + "\n")  # Display each record and add a new line
        else:
            self.textEdit.append("No records found.")

    def delete_file(self):
        try:
            if os.path.exists("stud.dat"):
                os.remove("stud.dat")  # Delete the file
                self.statusBar().showMessage("All records deleted successfully!")
                self.textEdit.clear()  # Clear the text area if needed
            else:
                self.statusBar().showMessage("File not found!")
        except Exception as e:
            self.statusBar().showMessage(f"Error: {str(e)}")


def main():
    app = QApplication([])
    window = Mygui()
    app.exec_()


if __name__ == '__main__':
    main()
