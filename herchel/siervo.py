class GradeManagementSystem:
    def __init__(self):
        self.students = {}  
        self.subjects = [] 
        self.MAX_GRADE = 100 

    def add_grade(self):
        name = input("Enter the student's name: ").strip().lower()
        if name not in self.students:
            self.students[name] = {}

        subject = input("Enter the subject: ").strip().lower()              
        if subject not in self.subjects:
            self.subjects.append(subject)
        
        try:
            grade = float(input(f"Enter the grade for {subject}: "))
            if 0 <= grade <= self.MAX_GRADE:
                self.students[name][subject] = grade
                print(f"Grade {grade} added for {name} in {subject}.")
            else:
                print(f"Invalid. Must be between 0 and {self.MAX_GRADE}.")
        except ValueError:
            print("Invalid input. Grade must be a number.")

    def view_grades(self):
        name = input("Enter the student's name: ").strip().lower()
        if name not in self.students:
            print("Student not found.")
            return
        
        print(f"Grades for {name}:")

        grades = self.students[name]
        if not grades:
            print("No grades recorded.")
        else:
            for subject, grade in grades.items():
                print(f"  {subject}: {grade}")
 
    def update_grade(self):
        name = input("Enter the student's name: ").strip().lower()
        if name not in self.students:
            print("Student not found.")
            return
        
        subject = input("Enter subject to update: ").strip().lower()
        if subject not in self.students[name]:
            print("No grade recorded for this subject.")
            return
        
        try:
            grade = float(input(f"Enter the new grade for {subject}: "))
            if 0 <= grade <= self.MAX_GRADE:
                self.students[name][subject] = grade
                print(f"Grade updated to {grade} for {name} in {subject}.")
            else:
                print(f"Invalid. Must be between 0 and {self.MAX_GRADE}.")
        except ValueError:
            print("Invalid input. Grade must be a number.")

    def calculate_average(self):
        name = input("Enter the student's name: ").strip().lower()
        if name not in self.students:
            print("Student not found.")
            return
        
        grades = [grade for grade in self.students[name].values() 
                  if grade is not None]
        
        if not grades:
            print("No grades recorded for this student.")
        else:
            average = sum(grades) / len(grades)
            print(f"Average grade for {name}: {average:.2f}")

    def delete_grades(self):
        name = input("Enter Student's Name: ").strip().lower()
        if name not in self.students:
            print("Student not found.")
            return
        
        subject = input("Enter the subject to delete grades for: "
                        ).strip().lower()
        
        if subject in self.students[name]:
            del self.students[name][subject]
            print(f"Grade for {subject} deleted for {name}.")
        else:
            print("No grades found for this subject.")

    def display_menu(self):
        UNSET_OPTION = 0
        BACK_TO_MAIN_MENU_OPTION = 6
        choice = UNSET_OPTION

        while choice != BACK_TO_MAIN_MENU_OPTION:
            print("\nGrade Management System Menu:")
            print("1. Add Student Grade")
            print("2. View Grades")
            print("3. Update Grade")
            print("4. Calculate Average Grade")
            print("5. Delete Grades")
            print("6. Main menu")
            choice = input("Enter your choice: ")

            match choice:
                case '1':
                    self.add_grade()
                case '2':
                    self.view_grades()
                case '3':
                    self.update_grade()
                case '4':
                    self.calculate_average()
                case '5':
                    self.delete_grades()
                case '6':
                    return
                case _:
                    print("Invalid choice. Please try again.")

