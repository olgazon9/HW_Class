class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def study(self, subject):
        print(f"{self.name} is studying {subject}.")
    
    def take_exam(self, subject):
        print(f"{self.name} is taking an exam in {subject}.")

# Example usage of the Student class
student1 = Student("Alice", 16, 11)
student1.study("Math")
student1.take_exam("History")
