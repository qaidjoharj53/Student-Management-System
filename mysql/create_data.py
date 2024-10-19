from faker import Faker
import random
import mysql.connector


class Student:
    def __init__(self, roll, name, percentage):
        self.roll = roll
        self.name = name
        self.percentage = percentage


connection = mysql.connector.connect(
    host="localhost", user="root", password="12345", database="student_management"
)
cursor = connection.cursor()


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


def save_to_database(records):
    try:
        for record in records:
            sql = "INSERT INTO students (roll, name, percentage) VALUES (%s, %s, %s)"
            values = (record.roll, record.name, record.percentage)
            cursor.execute(sql, values)

        connection.commit()
        print(f"{len(records)} records inserted into the database.")
    except mysql.connector.Error as e:
        print(f"Error inserting records into the database: {e}")


if __name__ == "__main__":
    n = int(input("Enter the number of fake records to generate: "))
    fake_records = generate_fake_records(n)
    save_to_database(fake_records)
