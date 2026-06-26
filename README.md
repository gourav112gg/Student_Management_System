# 🎓 Student Management System

A console-based **Student Management System** developed using **Python and Object-Oriented Programming (OOP)** principles. The application enables users to efficiently manage student records through an interactive menu-driven interface.

---

## 📌 Project Overview

This project demonstrates the practical implementation of OOP concepts such as:

* Classes and Objects
* Constructors (`__init__`)
* Encapsulation of student data
* List-based data management
* Method-driven operations
* User interaction through a command-line interface

The system allows administrators to perform essential student management tasks, including adding, viewing, searching, updating, and deleting student records.

---

## 🚀 Features

### ✅ Add New Student

Users can add a new student by entering:

* Student ID
* Student Name
* Age
* Marks

### ✅ View All Students

Displays the complete list of students along with their details.

### ✅ Search Student

Finds a student using their unique Student ID.

### ✅ Update Student Marks

Allows modification of marks for an existing student.

### ✅ Delete Student Record

Removes a student from the system permanently.

### ✅ Display Topper

Identifies and displays the student with the highest marks.

### ✅ Exit Application

Terminates the program safely.

---

## 🏗️ Project Structure

```text
StudentManagementSystem/
│
├── main.py
└── README.md
```

---

## 🧠 Object-Oriented Design

### Student Class

The `Student` class represents individual student records.

#### Attributes

| Attribute  | Description               |
| ---------- | ------------------------- |
| student_id | Unique student identifier |
| name       | Student's full name       |
| age        | Student's age             |
| marks      | Student's marks           |

#### Methods

* `display()` – Displays student details.

---

### StudentManagementSystem Class

The `StudentManagementSystem` class manages all student operations.

#### Methods

| Method             | Purpose                              |
| ------------------ | ------------------------------------ |
| `add_student()`    | Adds a new student                   |
| `view_students()`  | Displays all students                |
| `search_student()` | Searches by Student ID               |
| `update_marks()`   | Updates marks                        |
| `delete_student()` | Deletes a student record             |
| `display_topper()` | Displays the highest-scoring student |

---

## 🛠️ Technologies Used

* **Python 3**
* **Object-Oriented Programming (OOP)**
* **Command-Line Interface (CLI)**

---

## 📋 Menu Interface

```text
=== STUDENT MANAGEMENT SYSTEM ===

1. Add Student
2. View Students
3. Search Students
4. Update Marks
5. Delete Student
6. Display Topper
7. Exit
```

---

## ▶️ How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/student-management-system.git
```

### Step 2: Navigate to the Project Folder

```bash
cd student-management-system
```

### Step 3: Run the Program

```bash
python main.py
```

---

## 📷 Sample Output

```text
=== STUDENT MANAGEMENT SYSTEM ===

1. Add Student
2. View Students
3. Search Students
4. Update Marks
5. Delete Student
6. Display Topper
7. Exit

Enter Your Choice: 1

Enter Student ID: 101
Enter Student Name: Gourav
Enter Age: 19
Enter Marks: 92

Student Added Successfully...
```

---

## 🔍 Learning Outcomes

This project helps in understanding:

* Python classes and objects
* Constructor methods
* Data management using lists
* CRUD operations
* Exception handling
* Interactive menu-driven applications
* Problem-solving using OOP principles

---

## 🚧 Future Improvements

Potential enhancements include:

* Data persistence using files or databases
* Duplicate Student ID validation
* Sorting students by marks or name
* Exporting records to CSV files
* Graphical User Interface (GUI) using Tkinter or PyQt
* Attendance and grade management modules

---

## 👨‍💻 Author

**Gourav Garg**

B.Tech CSE (AI & DS) Student
Chandigarh Group of Colleges, Jhanjeri

GitHub: https://github.com/gourav112gg

---

## 📜 License

This project is developed for educational and academic purposes. It is free to use, modify, and distribute with proper attribution.

---

⭐ If you found this project helpful, consider giving it a star on GitHub!
