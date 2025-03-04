from task1 import Human, Employee, Bank, Customer, Account

# Test Human and Employee
human = Human("Alice", 30)
print(human.speak())

employee = Employee("Bob", 25, "Software Engineer")
print(employee.speak())
print(employee.work())

# Test Bank System
bank = Bank()
customer1 = Customer("John Doe")
customer2 = Customer("Jane Doe")

account1 = Account("12345", 1000)
account2 = Account("67890", 500)

customer1.add_account(account1)
customer2.add_account(account2)


bank.add_customer(customer1)
bank.add_customer(customer2)

print(f"{customer1.name} has {len(customer1.accounts)} account(s).")
print(f"{customer2.name} has {len(customer2.accounts)} account(s).")

account1.deposit(200)
print(f"New balance for account 12345: {account1.balance}")

account2.withdraw(100)
print(f"New balance for account 67890: {account2.balance}")
