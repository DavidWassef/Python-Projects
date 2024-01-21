# Define the Student class to represent individual students
class Student:
    def __init__(self, name, mathGrade, scienceGrade, languageGrade, dramaGrade, musicGrade, biologyGrade):
        # Initialize student attributes
        self.name = name
        self.mathGrade = mathGrade
        self.scienceGrade = scienceGrade
        self.languageGrade = languageGrade
        self.dramaGrade = dramaGrade
        self.musicGrade = musicGrade
        self.biologyGrade = biologyGrade
        self.gpa = 0  # Placeholder for GPA
        self.school = ""  # Placeholder for assigned school

    # Getter methods for retrieving student information
    def getName(self):
        return self.name

    def getMathGrade(self):
        return self.mathGrade

    def getScienceGrade(self):
        return self.scienceGrade

    def getLanguageGrade(self):
        return self.languageGrade

    def getDramaGrade(self):
        return self.dramaGrade

    def getMusicGrade(self):
        return self.musicGrade

    def getBiologyGrade(self):
        return self.biologyGrade

    def getGPA(self):
        return self.gpa

    def getSchool(self):
        return self.school

    # Setter methods for updating GPA and assigned school
    def setGPA(self, gpa):
        self.gpa = gpa

    def setSchool(self, school):
        self.school = school


# Define the System class to manage student information and generate reports
class System:
    def __init__(self):
        self.numberOfStudent = 0
        self.studentList = []  # List to store student objects

    # Method to check the validity of a password
    def checkPassword(self, password):
        if len(password) < 10:
            print("Error -> Password should contain at least 10 characters", end="")
            return False

        countUpper = countNumber = countSpecial = 0
        for char in password:
            if char.isupper():
                countUpper += 1
            if char.isnumeric():
                countNumber += 1
            if not char.isalnum():
                countSpecial += 1

        if countUpper < 1:
            print("Error -> Password should contain at least 1 uppercase letter.", end="")
            return False
        if str(countNumber) not in "23":
            print("Error -> Password should contain two to three numbers only.", end="")
            return False
        if countSpecial != 1:
            print("Error -> Password should contain 1 special character only.", end="")
            return False

        return True

    # Method to generate a password with specific criteria
    def generatePassword(self):
        print("Please follow requirements before entering a password: ")
        print("\nPassword Requirements:")
        print("-> Password should not be less than 10 characters")
        print("-> Password should contain at least one uppercase letter.")
        print("-> Password Should contain two or three numbers")
        print("-> Password Should contain one special character.")

        for _ in range(3):
            password = input("\nPlease enter the password: ")
            if self.checkPassword(password):
                return
            else:
                print(", Remaining Attempt -> 2")

        print("System Shutdown, Password error")

    # Method to get a numerical grade from the user for a specific subject
    def getGrade(self, subject):
        while True:
            try:
                grade = int(input(f"Input student mark in {subject}: "))
                if 0 <= grade <= 100:
                    return grade
                else:
                    print("Error -> Marks should be in the range 0-100")
            except ValueError:
                print("Error -> Enter integer value only")

    # Method to get the number of students for the system
    def getNumberOfStudent(self):
        for _ in range(3):
            try:
                numberOfStudent = int(input("Enter number of students (1-50): "))
                if 1 <= numberOfStudent <= 50:
                    self.numberOfStudent = numberOfStudent
                    return
                else:
                    raise ValueError()
            except ValueError:
                print("Error -> Please enter a numeric value within the range 1-50, Remaining Attempt -> 2")

        print("System Shutdown, Number of students error")

    # Method to get details of each student from the user
    def getStudentDetails(self):
        for i in range(self.numberOfStudent):
            print(f"Enter {i + 1} student details:")
            name = input("Enter student name: ")
            mathGrade = self.getGrade("Math")
            scienceGrade = self.getGrade("Science")
            languageGrade = self.getGrade("Language")
            dramaGrade = self.getGrade("Drama")
            musicGrade = self.getGrade("Music")
            biologyGrade = self.getGrade("Biology")
            # Create a new Student object and add it to the studentList
            self.studentList.append(Student(name, mathGrade, scienceGrade, languageGrade, dramaGrade, musicGrade, biologyGrade))
            print()

    # Method to calculate the GPA for each student
    def calculateGPA(self):
        creditList = [4, 5, 4, 3, 2, 4]
        for student in self.studentList:
            gradeList = [student.getMathGrade(), student.getScienceGrade(), student.getLanguageGrade(),
                         student.getDramaGrade(), student.getMusicGrade(), student.getBiologyGrade()]
            result = [credit * grade for credit, grade in zip(creditList, gradeList)]
            gpa = sum(result) / sum(creditList)
            student.setGPA(gpa)

    # Method to assign a school to each student based on their GPA
    def assignSchool(self):
        for student in self.studentList:
            if student.getGPA() >= 90:
                student.setSchool("School of Engineering")
            elif student.getGPA() >= 80:
                student.setSchool("School of Business")
            elif student.getGPA() >= 70:
                student.setSchool("Law School")
            else:
                student.setSchool("Not accepted")

    # Method to print a report showing each student's name and assigned school
    def report1(self):
        for student in self.studentList:
            print(f"Student Name: {student.getName()}, School: {student.getSchool()}")

    # Method to print a report showing the distribution of accepted students per school
    def report2_and_3(self):
        distribution = {"School of Engineering": 0, "School of Business": 0, "Law School": 0, "Not accepted": 0}
        for student in self.studentList:
            distribution[student.getSchool()] += 1

        print(f"Report 2: Number of accepted students distribution per each school:")
        for school, count in distribution.items():
            print(f"{school}: {count}")

        print(f"\nReport 3: Number of not accepted students: {distribution['Not accepted']}")

    # Method to print a report showing each student's name and rounded GPA
    def report4(self):
        for student in self.studentList:
            print(f"Student Name: {student.getName()}, GPA: {round(student.getGPA())}")

# Main function to execute the program
def main():
    system = System()
    print("Welcome to Humber College")
    print()

    system.generatePassword()
    system.getNumberOfStudent()
    system.getStudentDetails()
    system.calculateGPA()
    system.assignSchool()

    print("Report 1: Student Name, School Name")
    system.report1()
    print()
    system.report2_and_3()
    print()
    system.report4()

# Calling main function to start the program
main()
