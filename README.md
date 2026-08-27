# KodNest Student Placement Tracker

A Python OOP-based console application for managing student placement profiles, mock scores, placement readiness, and student records.

## 📌 Project Overview

The **KodNest Student Placement Tracker** is an individual Python project designed to demonstrate fundamental Python and Object-Oriented Programming concepts.

The application allows users to:

* Add student profiles
* Display all student profiles
* Update student mock scores
* Validate scores between 0 and 100
* Determine placement readiness
* Change the shared platform name
* Display the total number of registered students

## 🛠️ Technologies Used

* Python 3
* Object-Oriented Programming
* Git
* GitHub

## 🧠 Python Concepts Used

This project demonstrates:

* Variables and Data Types
* Input and Output
* Conditional Statements
* Loops
* Functions
* Lists
* Classes and Objects
* Constructors
* Instance Variables
* Class Variables
* Instance Methods
* Encapsulation
* Private Attributes
* Properties and Setters
* Class Methods
* Alternative Constructors
* Static Methods

## 🏗️ Project Structure

```text
student-placement-tracker/
│
├── main.py
└── README.md
```

## ✨ Features

### 1. Add Student

Users can add a student by entering:

```text
Student ID, Name, Branch, Score
```

Example:

```text
K101,Aarav Sharma,CSE,85
```

### 2. Display All Students

Displays:

* Student ID
* Name
* Branch
* Mock Score
* Placement Status
* Platform

### 3. Update Student Score

Users can search for a student using their Student ID and update their mock score.

Scores are accepted only between **0 and 100**.

### 4. Placement Status

Placement readiness is determined based on the mock score:

| Score  | Placement Status    |
| ------ | ------------------- |
| 80–100 | Placement Ready     |
| 60–79  | Needs More Practice |
| 0–59   | Not Ready           |

### 5. Change Platform

The platform name is stored as a class variable and can be changed for all students.

### 6. Total Student Count

The application maintains the total number of created student objects using a class variable.

## 🔐 Encapsulation

The student's score is stored as a private attribute:

```python
self.__score
```

The score is accessed and updated through the `score` property.

The setter validates the score before updating it.

## 🧩 OOP Design

### Class Variables

```python
platform = "KodNest"
total_students = 0
```

### Private Attribute

```python
self.__score
```

### Property

The `score` property provides controlled access to the private score.

### Static Methods

The project uses static methods for:

* Score validation
* Name normalization

### Class Methods

The project uses class methods for:

* Creating an object from a string
* Changing the platform
* Displaying the total student count

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Open the project

```bash
cd student-placement-tracker
```

### 3. Run the application

```bash
python main.py
```

## 📋 Application Menu

```text
===== Student Placement Tracker =====
1. Add Student
2. Display All Students
3. Update Student Score
4. Change Platform
5. Show Total Students
6. Exit
```

## 🧪 Testing

The application should be tested with:

* At least three students
* Score below 60
* Score between 60 and 79
* Score between 80 and 100
* Duplicate Student ID
* Valid score update
* Invalid score update
* Non-existing Student ID
* Invalid menu option
* Platform name change

## 🚀 Future Improvements

Possible future improvements include:

* Search students by name
* Delete student profiles
* Store student data permanently
* Add a graphical user interface
* Add database support
* Generate placement reports

## 👩‍💻 Author

**Hemavathi**

This project was created as an individual Python OOP project to practice and demonstrate Object-Oriented Programming concepts.

