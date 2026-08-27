class StudentProfile:
    platform = "KodNest"
    total_students = 0

    def __init__(self,student_id,name,branch,score):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.__score = score
        StudentProfile.total_students+=1
    
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,new_score):
        if 0<=new_score<=100:
            self.__score = new_score
        else:
            print("Invalid score. Score must be between 0 and 100.")
    @staticmethod
    def is_valid_score(score):
        if 0<=score<=100:
            return True
        else:
            return False
    
    @staticmethod
    def normalize_name(name):
        name = name.strip().title()
        return name

    def get_placement_status(self):
        if 80<= self.score <=100:
            print("Placement Ready")
        elif 60<=self.score <=79:
            print("Needs More Practise")
        else:
            print("Not Ready")

    def display_profile(self):
        print("Student ID:",self.student_id)
        print("Name:",self.name)
        print("Branch:",self.branch)
        print("Mock Score:",self.score)
        print("Placement Status:",self.get_placement_status())
        print("Platform:",StudentProfile.platform)
    @classmethod
    def from_string(cls,student_data):
        student_id,name,branch,score=student_data.split(",")
        name = cls.normalize_name(name)
        return cls(student_id,name,branch,int(score))
    @classmethod
    def change_platform(cls, new_platform):
        cls.platform = new_platform

    @classmethod
    def show_total_students(cls):
        print("Total Students:",cls.total_students)
students = []


while True:

    print("===== Student Placement Tracker =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Score")
    print("4. Change Platform")
    print("5. Show Total Students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    
    if choice == "1":

        student_data = input(
            "Enter student details (ID,Name,Branch,Score): "
        )

        student = StudentProfile.from_string(student_data)

        students.append(student)

        print("Student added successfully.")
        print()

    
    elif choice == "2":

        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                student.display_profile()

    
    elif choice == "3":

        student_id = input("Enter Student ID: ")

        found = False

        for student in students:

            if student.student_id == student_id:

                new_score = int(input("Enter new score: "))

                student.score = new_score

                found = True
                break

        if not found:
            print("Student not found.")

        print()

   
    elif choice == "4":

        new_platform = input("Enter new platform name: ")

        StudentProfile.change_platform(new_platform)

        print("Platform changed successfully.")
        print()

    
    elif choice == "5":

        StudentProfile.show_total_students()
        print()


    elif choice == "6":

        print("Thank you for using Student Placement Tracker.")
        break

    else:

        print("Invalid choice. Please try again.")
        print()