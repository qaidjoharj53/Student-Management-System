# Student-Management-System

For every school important task for administration department is to manage student information in a procedure oriented manner with latest updates for every year which need to be available for easy access. This can be provided by a simple Students Management system to help administration so to efficiently manage student’s details. To store data MySQL is used by connecting MySQL with Python using MySQL Connector. There is also a Login Panel where now admin can register themselves and can Login.

## Installation

##### 1. Install Mysql Python connector 

- [Mysql](https://dev.mysql.com/downloads/mysql/)
- [Mysql Python connector](https://dev.mysql.com/downloads/connector/python/)
 
##### 2. install Mysql in Python using below command
  ```bash
    pip install mysql
  ```
    
## Features

##### Student Class:

Defines a class called student to represent student records.
It has attributes for roll number (roll), name (name), and percentage (per).
Contains methods for adding a record, displaying a record, modifying a record, and displaying a formatted record.
##### File Handling:

Imports the pickle module for serializing and deserializing Python objects to/from a binary file.
Imports the os module for file and directory manipulation.
##### Main Menu Loop:

Utilizes a while loop to create a main menu for the user.
The user can choose from options to add, display, search, modify, or delete student records.
The loop continues until the user selects the "Exit" option.
##### Data Storage:

Records of student objects are stored in a binary file named "stud.dat".
Records can be added to the file using the "Add record" option.
##### Displaying Records:

The "Display all records" option reads and displays all the records stored in "stud.dat".
##### Searching Records:

The "Search by roll number" and "Search by name" options allow the user to find records based on roll number or name.
The program displays the found records if they exist.
##### Modifying Records:

The "Modify by roll number" option allows the user to change the data (roll number, name, percentage) of an existing record.
##### Deleting Records:

The "Delete by roll number" option allows the user to delete a record based on the roll number.

##### Error Handling:

The code includes some basic error handling, such as handling file-related exceptions.
Clearing Console:

Utilizes os.system("cls") to clear the console screen for better user interaction (Windows specific).


## Deployment

To deploy this project just run .py files.


