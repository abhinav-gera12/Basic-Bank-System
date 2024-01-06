'''
Banking System Using OOPs
Parent Class : User
1) User class holds all the relevant information about the customer
2) It has a function to show the details 
Child Class : Bank
1) It stores the information about the account balance and the amount
2) It allows a user to deposit, withdraw or view the current balance of an account
'''

#Parent Class
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_info(self):
        print(f'''\n\t\t Personal Details \n
                Name : {self.name}
                Age: {self.age}
                Gender: {self.gender} ''')
        
#Child Class
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0
        
    def deposit(self,deposit_amount):
        self.deposit_amount = deposit_amount
        self.balance = self.balance + self.deposit_amount
        print(f"The account balance has been updated | Current Balance : {self.balance}")
        
    def withdraw(self,withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if self.balance < self.withdraw_amount:
            print(f"Insuffient Funds | Current Balance: {self.balance}")
        else:
            self.balance = self.balance - self.withdraw_amount        
            print(f"The account balance has been upadted | Current Balance : {self.balance}")
        
    def view_balance(self):
        self.show_info()
        print(f"Current Balance : {self.balance}")
        
Abhinav = Bank("Abhinav", 21, "Male")
#print(Abhinav.deposit(500))
#Abhinav.withdraw(700)
print(Abhinav.view_balance())

