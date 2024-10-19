import pickle
import os
import student


def write_record(student):
    try:
        with open("stud.dat", "ab") as file:
            pickle.dump(student, file)  # Add the student object to the file
        print("New record added successfully.")
        return "Record added successfully."
    except Exception as e:
        return f"Error writing record: {e}"


def display_all_records():
    records = []
    try:
        with open("stud.dat", "rb") as file:
            while True:
                try:
                    student = pickle.load(file)  # Load the Student object
                    records.append(student.display_record())
                except EOFError:
                    break
        return records if records else ["No records found."]
    except FileNotFoundError:
        return ["File not found! Please add a record first."]
    except pickle.UnpicklingError:
        return ["Error in unpickling data! The file might be corrupted."]
    except IOError:
        return ["File could not be opened!"]


def update_record(roll_number, new_name=None, new_percentage=None):
    updated = False
    records = []

    try:
        # Open the file in read-binary mode
        with open("stud.dat", "rb") as file:
            while True:
                try:
                    student_obj = pickle.load(file)  # Load each student record
                    if student_obj.roll == roll_number:
                        # Update the student details
                        if new_name:
                            student_obj.name = new_name.upper()
                        if new_percentage is not None:
                            student_obj.per = new_percentage
                        updated = True
                    records.append(student_obj)
                except EOFError:
                    break

        # Rewrite the updated records
        with open("stud.dat", "wb") as file:
            for student_obj in records:
                pickle.dump(student_obj, file)

        if updated:
            return f"Record for Roll Number {roll_number} updated successfully."
        else:
            return f"Record with Roll Number {roll_number} not found."

    except FileNotFoundError:
        return "File not found! Please add a record first."
    except pickle.UnpicklingError:
        return "Error in unpickling data! The file might be corrupted."
    except Exception as e:
        return f"An error occurred: {e}"


def get_record(roll_number):
    try:
        with open("stud.dat", "rb") as file:
            while True:
                try:
                    student_obj = pickle.load(file)  # Load each student object
                    if student_obj.roll == roll_number:
                        return (
                            student_obj.display_record()
                        )  # Return the record if roll number matches
                except EOFError:
                    break
        return f"Record with Roll Number {roll_number} not found."
    except FileNotFoundError:
        return "File not found! Please add a record first."
    except pickle.UnpicklingError:
        return "Error in unpickling data! The file might be corrupted."
    except Exception as e:
        return f"An error occurred: {e}"


def clear_all_records():
    try:
        with open("stud.dat", "wb") as file:
            pass  # This will clear the file
        return "All records deleted."
    except Exception as e:
        return f"Error deleting records: {str(e)}"


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
