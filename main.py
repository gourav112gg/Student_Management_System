class Student:
    
    def __init__(self, student_id, name, age, marks):
        self.Student_id = student_id
        self.name = name 
        self.age = age
        self.marks = marks

    
    def display(self):
        print("STUDENT MANAGEMENT SYSTEM")
        print("\nStudent ID :", self.Student_id)
        print("Name         :", self.name)
        print("Age          :", self.age)
        print("Marks        :", self.marks)


class StudentManagementSystem:

    def __init__(self):
        self.student_list = []

    def add_student(self):
        try:
            student_id = int(input("Enter Student ID:"))
            name = input("Enter Student Name:")
            age = int(input("Enter Age:"))
            marks = float(input("Enter Marks:"))

            new_student = Student(student_id,name,age,marks)
            self.student_list.append(new_student)
            print("Stuent Added Successfully...")
        
        except Exception as e:
            print('You got this error :',e)

    def view_students(self):
        if len(self.student_list)==0:
            print("No Students Found!")
        else:
            for student in self.student_list:
                student.display()

    def search_student(self):
        student_id = int(input("Enter student ID to Search :"))

        for student in self.student_list:
            if student.student_id == student_id:
                print("Student Found!")
                student.display()
                return
            
        print("Studnet Not Found!")

    def update_marks(self):
        student_id = int(input("Enter Student ID:"))

        for student in self.student_list:
            if student.student_id == student_id:
                new_marks = float(input("Enter new marks:"))
                student.marks = new_marks
                print("Marks Updated Successfully!")
                return 

        print("Student not Found!")

    def delete_student(self):
        student_id = int(input("Enter Student ID:"))

        for student in self.student_list:
            if student.student_id == student_id:
                self.student_list.remove(student)
                print("Student Deleted Successfully!")
                return
            
        print("Student Not Found!")

    def display_topper(self):
        if len(self.student_list) == 0:
            print("No Student Available!")
        else:
            topper = self.student_list[0]

            for student in self.student_list:
                if student.marks > topper.marks:
                    topper = student

            print("\n Topper Details")
            topper.display()

sms = StudentManagementSystem()

while True:

    print("\n=== STUDENT MANAGEMENT SYSTEM ===")
    print("1. Add Stduent")
    print("2. View Stduents")
    print("3. Search Students")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Display Topper")
    print("7. Exit")

    choice = int(input("Enter Your Choce:"))

    if choice == 1:
        sms.add_student()
    
    elif choice ==2:
        sms.view_students()

    elif choice ==3:
        sms.search_student()

    elif choice ==4:
        sms.update_marks()
    
    elif choice ==5:
        sms.delete_student()

    elif choice ==6:
        sms.display_topper()
    
    elif choice ==7:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")