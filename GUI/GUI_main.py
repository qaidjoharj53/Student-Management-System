from PyQt5 import uic
import time
import student
import file_operations
from PyQt5.QtCore import QTimer,Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QProgressBar, QTextEdit, QTableWidget, QTableWidgetItem, QHeaderView,QLineEdit,QPushButton

class Mygui(QMainWindow):

    def __init__(self):
        super(Mygui, self).__init__()
        
        # Load the .ui file 
        uic.loadUi("Student-Management-System/GUI/pages.ui", self)

        self.tableWidget = self.findChild(QTableWidget, "tableWidget")
        self.pushButton_6.clicked.connect(self.display_records)

        header = self.tableWidget.horizontalHeader()
        header.setStretchLastSection(True) 
        header.setSectionResizeMode(QHeaderView.Fixed)
        # Connect button signals
        self.setup_buttons()
        self.progressBar.setValue(3)
        self.show()

    def setup_buttons(self):
        """Connect buttons to their specific actions."""
        # to switch between pages in a QStackedWidget
        
        self.pushButton_1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))  #first page
        self.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))  #second page
        self.pushButton_7.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))  #third page
        # To add details:
        self.pushButton.clicked.connect(self.add_record)
        # To Show the records:
        self.pushButton_6.clicked.connect(self.display_records)
        # To check the roll number: 
        self.pushButton_2.clicked.connect(self.check_records)
        # To update the records:
        self.pushButton_3.clicked.connect(self.update_student_record)
        # To delete all Records: 
        self.pushButton_8.clicked.connect(self.delete_all_records)
        # For buttons to work via enter key:
        # Update-1
        self.setTabOrder(self.lineEdit_4,self.pushButton_2)
        # Update-2
        self.setTabOrder(self.lineEdit_6,self.lineEdit_5)
        self.setTabOrder(self.lineEdit_5,self.pushButton_3)
        # Add
        self.setTabOrder(self.lineEdit,self.lineEdit_2)
        self.setTabOrder(self.lineEdit_3,self.pushButton)

    def mousePressEvent(self, event):
        """Reset the progress bar to zero when any part of the window is clicked."""
        self.progressBar.setValue(0)
        super(Mygui, self).mousePressEvent(event)
    def update_progress_bar(self):
        """fill the progress bar with a small delay."""
        for i in range(101):
            time.sleep(0.001)
            self.progressBar.setValue(i)

    def add_record(self):
        roll = self.lineEdit.text()
        name = self.lineEdit_2.text()
        percentage = self.lineEdit_3.text()

        #check if fields are not empty and percentage is numeric
        if roll.isdigit() and percentage.replace('.', '', 1).isdigit():
            student_obj = student.Student()
            student_obj.add_record(int(roll), name, float(percentage))

            self.textEdit.append("Details have been successfully added!")
            # Write the student record to the binary file using file_operations
            result = file_operations.write_record(student_obj)
            self.statusBar().showMessage(result)  
            # Progress bar:
            QTimer.singleShot(0, self.update_progress_bar)
            # Clear the input fields
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
        else:
            self.statusBar().showMessage("Invalid input. Please check the fields.")

    def check_records(self):
        """Check if the roll number exists and display the student details."""
        roll = self.lineEdit_4.text()

        if roll.isdigit():
            roll = int(roll)
            student_record = file_operations.get_record(roll)

            if student_record:
                # If student_record is a string, split it into components
                record_fields = student_record.split(",")
                if len(record_fields) == 3:  # Ensure there are exactly 3 fields
                    roll, name, percentage = record_fields
                    # Format the student data and display it in the textEdit widget
                    self.textBrowser.setText(f"Roll Number: {roll.strip()}\n"
                    f"Name: {name.strip()}\n"
                    f"Percentage: {percentage.strip()}")
                    self.statusBar().showMessage("Record found!")
                else:
                    self.textBrowser.setText("Error: Record format is incorrect.")
                    self.statusBar().showMessage("Record format error.")
            else:
                # If the roll number is not found, show an error message
                self.textBrowser.setText("No record found for this roll number.")
                self.statusBar().showMessage("Record not found.")
        else:
            self.statusBar().showMessage("Invalid roll number.")

    def update_student_record(self):
        # Get roll number, new name, and new percentage from the input fields
        roll = self.lineEdit_4.text()
        new_name = self.lineEdit_6.text()
        new_percentage = self.lineEdit_5.text()

        if roll.isdigit():
            roll = int(roll)
            if not new_name or not new_percentage:
                self.statusBar().showMessage("Please provide new details to update.")
                return

            # If percentage is provided, ensure it's valid
            if new_percentage and not new_percentage.replace('.', '', 1).isdigit():
                self.statusBar().showMessage("Invalid percentage value.")
                return

            new_percentage = float(new_percentage) if new_percentage else None
            
            # Call the update_record function
            result = file_operations.update_record(roll, new_name, new_percentage)
            print(f"Update result: {result}")

            # For a success pop-up dialog box
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"Record for Roll Number {roll} has been updated successfully.")
            msg.setWindowTitle("Success")
            msg.exec_()
            
            # Display the result of the update
            if result == "Record updated successfully.":
                self.display_records()
            else:
                self.statusBar().showMessage(result)

            # Clear the input fields after the update
            self.lineEdit_4.clear()
            self.lineEdit_6.clear()
            self.lineEdit_5.clear()
            self.textBrowser.clear()
        else:
            self.statusBar().showMessage("Invalid roll number.")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            # Get the currently focused widget
            focused_widget = self.focusWidget()
            
            # Check if the focused widget is a QLineEdit
            if isinstance(focused_widget, QLineEdit):
                # Move to the next input field or button if focus is on QLineEdit
                self.focusNextChild()
            elif isinstance(focused_widget, QPushButton):
                # Click the QPushButton if it is focused
                focused_widget.animateClick() 
            else:
                buttons = self.findChildren(QPushButton)
                for button in buttons:
                    if button.hasFocus():
                        button.animateClick()
                        break

        super(Mygui, self).keyPressEvent(event)
        
    def display_records(self):
        records = file_operations.display_all_records()  # Get all records from the file

        # Clear the table before displaying new records
        self.tableWidget.clearContents()
        
        # Reset row count to match the number of records
        self.tableWidget.setRowCount(0)  
        
        # Set the number of columns and headers
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Roll Number", "Name", "Percentage"])

        # Enable the grid and set grid style (if needed)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(1) 

        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setAlternatingRowColors(True)

        # Set column width to ensure text fits properly
        self.tableWidget.setColumnWidth(0, 150)  # Adjust the width for Roll Number
        self.tableWidget.setColumnWidth(1, 200)  # Adjust the width for Name
        self.tableWidget.setColumnWidth(2, 150)  # Adjust the width for Percentage

        if records and records[0] != "No records found.":
            # Set row count to the number of records
            self.tableWidget.setRowCount(len(records))
            for row, record in enumerate(records):
                fields = record.strip().split(",")
                if len(fields) == 3:
                    roll, name, percentage = fields
                    self.tableWidget.setItem(row, 0, QTableWidgetItem(roll.strip()))
                    self.tableWidget.setItem(row, 1, QTableWidgetItem(name.strip()))
                    self.tableWidget.setItem(row, 2, QTableWidgetItem(percentage.strip()))
        else:
            # If no records, ensure the table is empty
            self.tableWidget.setRowCount(1)
            self.tableWidget.setItem(0, 0, QTableWidgetItem("No records found"))

    # Delete all records with confirmation dialog
    def delete_all_records(self):
        """Show a confirmation dialog before deleting all records."""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Delete All Records")
        msg.setText("Are you sure you want to delete all records?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        
        # Show the confirmation dialog and check the user's choice
        result = msg.exec_()
        
        if result == QMessageBox.Yes:
            # Call the file operation to clear all records
            result = file_operations.clear_all_records()  # Make sure to implement this function
            if result == "All records deleted.":
                self.display_records()  # Refresh the table after deletion
                self.statusBar().showMessage("All records have been deleted.")
            else:
                self.statusBar().showMessage("Error deleting records.")
        else:
            self.statusBar().showMessage("Delete action canceled.")


def load_stylesheet(app, stylesheet_file):
    """Load the external QSS file."""
    try:
        with open(stylesheet_file, "r") as file:
            app.setStyleSheet(file.read())
    except Exception as e:
        print(f"Error loading stylesheet: {e}")

def main():
    app = QApplication([])

    # Load the external stylesheet
    load_stylesheet(app, "Student-Management-System/GUI/stylesheet.qss")
    window = Mygui()
    app.exec_()

if __name__ == '__main__':
    main()

