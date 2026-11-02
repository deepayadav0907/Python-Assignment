# 02/11/2026
# class Employee:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self._salary = salary


#     def get_salary(self):
#         return self._salary

#     def inc_salary(self, amount):
#         if amount >0:
#             self._salary += amount
#             print("Salary updated")
#         else:
#             print("Invalid amount")

# emp=Employee("Shailesh",25,50000)
# print("Salary:",emp.get_salary())

# emp.inc_salary(8000)
# print("New Balance:",emp.get_salary())
# -------------------------------------------------------

# inheritance

# single inheritance

# class Animal():
#     def property(self):
#         print("Animal has 4 legs")

# class Dog(Animal):
#     def bark(self): 
#         print("Dog barks")

# d=Dog()
# d.bark()
# d.property()


# Multiple Inheritance

# class Father():
#     def skill1(self):
#         print("Driving")

# class Mother():
#     def skill2(self):
#         print("cooking")

# class child(Father, Mother):
#     def Qualities(self):
#         print("Inherited skill from parens:")
# x=child()
# x.Qualities()
# x.skill1()
# x.skill2()


#  multilevel inheritance

# class Grandfather():
#     def house(self):
#         print("Grandfather's house'")

# class father(Grandfather):
#     def bike(self):
#         print("Father's bike")

# class Son(Grandfather):
#     def laptop(self):
#         print("Son's laptop")

# class Grandson(father,Son):
#     def car(self):
#         print("Grandson's car")


# g=Grandson()
# g.house()
# g.bike()
# g.laptop()


# Hierarchial Inheritance
# class Institute():
#     def name(self):
#         print("NSTIW Allahabad")
# class Teacher(Institute):
#     pass
# class Student(Institute):
#     pass
# class Housekeeping(Institute):
#     pass


# t=Teacher()
# s=Student()
# h=Housekeeping()

# s.name()
# t.name()
# h.name()

# Classwork

#Student Managment System
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# class Student(Person):
#     def __init__(self, name, age, roll_no, course):
#         super().__init__(name, age)
#         self.roll_no = roll_no
#         self.course = course

#     def display_student(self):
#         self.display_details()
#         print("Roll No:", self.roll_no)
#         print("Course:", self.course)


# s1 = Student("Deepa", 19, 33, "AIPA")
# s1.display_student()


# Bank Account System

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposit:", amount)


# class SavingAccount(BankAccount):
#     def __init__(self, account_number, balance, interest_rate):
#         super().__init__(account_number, balance)
#         self.interest_rate = interest_rate

#     def calculate_interest(self):
#         interest = self.balance * self.interest_rate / 100
#         print("Account Number:", self.account_number)
#         print("Balance:", self.balance)
#         print("Interest Rate:", self.interest_rate, "%")
#         print("Interest Earned:", interest)


# b1 = SavingAccount(43409, 60000, 5)
# b1.deposit(2000)
# b1.calculate_interest()

# Family Assets

# class Grandfather:
#     def car(self):
#         print("Grandfather has a car")


# class Father(Grandfather):
#     def BMW(self):
#         print("Father has a BMW")


# class Son(Father):
#     def Building(self):
#         print("Son has a Building")


# s1 = Son()
# s1.car()
# s1.BMW()
# s1.Building()

#Employee Hierarchy
# class Person:
#     def get_name(self):
#         print("Name: Deepa")


# class Employee(Person):
#     def salary(self):
#         print("Salary: 100000")


# class Manager(Employee):
#     def team_size(self):
#         print("Team Size: 10")


# m1 = Manager()
# m1.get_name()
# m1.salary()
# m1.team_size()

#Collage Managment System
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Student(Person):
#     def __init__(self, name, age, marks):
#         super().__init__(name, age)
#         self.marks = marks

#     def display(self):
#         print("Student Name:", self.name)
#         print("Age:", self.age)
#         print("Marks:", self.marks)


# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject

#     def display(self):
#         print("Teacher Name:", self.name)
#         print("Age:", self.age)
#         print("Subject:", self.subject)


# s1 = Student("Deepa", 19, 85)
# t1 = Teacher("Shailesh", 35, "Python")

# s1.display()
# print("--------------")
# t1.display()
              
#Vechicle Managment System
# class Vehicle:
#     def start(self):
#         print("Vehicle is starting")


# class Car(Vehicle):
#     def air_condition(self):
#         print("Car has Air Conditioner")


# class Bike(Vehicle):
#     def helmet_required(self):
#         print("Helmet is required")


# class Bus(Vehicle):
#     def passenger_capacity(self):
#         print("Passenger Capacity: 50")


# c1 = Car()
# b1 = Bike()
# bus1 = Bus()

# print("Car:")
# c1.start()
# c1.air_condition()

# print("Bike:")
# b1.start()
# b1.helmet_required()

# print("Bus:")
# bus1.start()
# bus1.passenger_capacity()

# # Smart Phone System
# class Camera:
#     def take_photo(self):
#         print("Taking Photo")


# class MusicPlayer:
#     def play_music(self):
#         print("Playing Music")


# class SmartPhone(Camera, MusicPlayer):
#     def make_call(self):
#         print("Making a Call")


# s1 = SmartPhone()
# s1.take_photo()
# s1.play_music()
# s1.make_call()

#Working Student
# class Student:
#     def study(self):
#         print("Student is studying")


# class Employee:
#     def work(self):
#         print("Employee is working")


# class WorkingStudent(Student, Employee):
#     def manage_time(self):
#         print("Managing Time")


# w1 = WorkingStudent()
# w1.study()
# w1.work()
# w1.manage_time()

#Company Structure
# class Employee:
#     def attendance(self):
#         print("Employee attendance marked")


# class Developer(Employee):
#     def write_code(self):
#         print("Developer is writing code")


# class Tester(Employee):
#     def test_software(self):
#         print("Tester is testing software")


# class TeamLead(Developer, Tester):
#     def manage_team(self):
#         print("Team Lead is managing the team")


# t1 = TeamLead()
# t1.attendance()
# t1.write_code()
# t1.test_software()
# t1.manage_team()

# Educational Institute
# class Person:
#     def display_name(self):
#         print("Name: Deepa")


# class Student(Person):
#     def study(self):
#         print("Student is studying")


# class Teacher(Person):
#     def teach(self):
#         print("Teacher is teaching")


# class Mentor(Student, Teacher):
#     def guide(self):
#         print("Mentor is guiding students")


# m1 = Mentor()
# m1.display_name()
# m1.study()
# m1.teach()
# m1.guide()