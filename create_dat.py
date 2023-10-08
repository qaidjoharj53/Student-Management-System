from fake import Faker
import random
import pickle

class Student:
    def __init__(self, roll, name, percentage):
        self.roll = roll
        self.name = name
        self.percentage = percentage

def generate_fake_records(n):
    fake = Faker()
    records = []

    for _ in range(n):
        roll = random.randint(1000, 9999)
        name = fake.name()
        percentage = round(random.uniform(50, 100), 2)

        student = Student(roll, name, percentage)
        records.append(student)

    return records

def save_to_dat(records):
    try:
        with open("fake_stud.dat", "wb") as file:
            for record in records:
                pickle.dump(record, file)
        print(f"{len(records)} fake records saved to fake_stud.dat")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    n = int(input("Enter the number of fake records to generate: "))
    fake_records = generate_fake_records(n)
    save_to_dat(fake_records)
