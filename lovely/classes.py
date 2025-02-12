from tarfile import fully_trusted_filter


class Person:
    first_name = "Clay"
    last_name = "Ham"
    gender = "male"
    age = 18

class Employee:
    def __init__(self, name, gender, age,basic_salary,position):
         self.name = name
         self.gender = gender
         self.age = age
         self.basic_salary = basic_salary
         self.position = position
    def full_salary(self):
        full_salary = self.basic_salary + 2500
        return full_salary
    def new_salary(self):
        new_salary = self.basic_salary +(27/100*self.basic_salary)
        return new_salary



class Car:
    def __init__(self, model, year,typ,price):
        self.model = model
        self.year = year
        self.typ = typ
        self.price = price

    def display(self):
        return f"Model:{self.model} Typ:{self.typ}"

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def perimeter(self):
        perimeter = (self.width +self.height)*2
        return perimeter
    def area(self):
        area= self.width*self.height
        return area

    def display(self):
     return f"Width:{self.width} Height:{self.height}"


class Emobilis_Employee:
    def __init__(self, name, gender, age,salary,qualification):
        self.name = name
        self.gender = gender
        self.age = age
        self.salary = salary
        self.qualification = qualification
    def promotion(self):
        if self.qualification == "Degree" or self.qualification == "Masters":
            return "you are promoted"
        else:
            return "you are not promoted"

class Developer(Emobilis_Employee):
    def __init__(self, name, gender, age,salary,qualification,specialization,prog_language):
        super().__init__(name,gender,age,salary, qualification)
        self.specialization = specialization
        self.prog_language = prog_language

class Teacher(Emobilis_Employee):
    def __init__(self, name, gender, age,salary,qualification,employment_year,speaking_language):
        super().__init__(name,gender,age,salary, qualification)
        self.employment_year = employment_year
        self.speaking_language = speaking_language


class Commission_Employee(Emobilis_Employee):
    def __init__(self, name, gender, age,salary,qualification,commission_rate,hours_worked):
        super().__init__(name,gender,age, salary, qualification)
        self.commission_rate = commission_rate
        self.hours_worked = hours_worked


    def commission_salary(self):
        commission_salary = (self.commission_rate * self.hours_worked)+self.salary
        return commission_salary


class BankAccount:
    def __init__(self, name, balance,payment,gender,year,duration):
        self.name = name
        self.balance = balance
        self.payment = payment
        self.gender = gender
        self.year = year
        self.duration = duration

class Transaction(BankAccount):
    def __init__(self, name, amount, payment, gender, year,deposit,balance):
        super().__init__(self,name,deposit,balance,gender, year)
      if amount > 0:
            return f'hello{name}, you have deposited {amount}'
      else:
            return f'hello{name}, you have not deposited'

class BankTransaction(BankAccount):
    def __init__(self, name, amount, payment):
        if amount > 0:
            return f'hello{name}, you have withdrawn {amount}'
        else:
            return f'hello{name}, you have not withdrawn'

    def withdrawal_charges(name, amount, charge_type):
        if amount <= 100:
            return f'hello{name}, you have withdrawn {amount} hence you will be charged {charge_type}'
        else:
            return f'hello{name}, you have not withdrawn'



































