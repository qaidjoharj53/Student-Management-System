# file_operations.py
import pickle


def write_record(student):
    try:
        with open("stud.dat", "ab") as file:
            pickle.dump(student, file)
        return "Record added in file!"
    except Exception as e:
        return f"Error: {str(e)}"


def display_all_records():
    records = []
    try:
        with open("stud.dat", "rb") as file:
            while True:
                student = pickle.load(file)
                records.append(student.display_record())
        return records
    except EOFError:
        return records
    except IOError:
        return ["File could not be opened!"]
