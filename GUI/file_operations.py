# file_operations.py
import pickle
import os
import student

def write_record(student):
    try:
        with open("stud.dat", "ab") as file:
            pickle.dump(student, file)  # Ensure student is a Student instance
        return "Record added in file!"
    except Exception as e:
        return f"Error: {str(e)}"


def display_all_records():
    records = []
    try:
        with open("stud.dat", "rb") as file:
            while True:
                try:
                    student = pickle.load(file)  # Load the Student object
                    records.append(student.display_record())  # Append the student's record
                except EOFError:
                    break 
        return records if records else ["No records found."]
    except FileNotFoundError:
        return ["File not found! Please add a record first."]
    except pickle.UnpicklingError:
        return ["Error in unpickling data! The file might be corrupted."]
    except IOError:
        return ["File could not be opened!"]
    
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