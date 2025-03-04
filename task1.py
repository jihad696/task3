# Task 1: Human and Employee Classes
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} is speaking."


class Employee(Human):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def work(self):
        return f"{self.name} is working as a {self.job_title}."


# Task 2: Bank Account System
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)


class Bank:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
