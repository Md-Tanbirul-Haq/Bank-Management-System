

class Bank:
    def __init__(self,balance):
        self.balance=balance
    def balance_(self):
        print(f"Balance = {self.balance}")
    def withdraw_balance(self,withdraw_balance_):
        if(withdraw_balance_ > self.balance):
            print('''Withdraw is not possible.''')
            print(f'Balance is {self.balance}')
        else:
            print(f'Withdraw balance {withdraw_balance_}')
            self.balance=self.balance-withdraw_balance_
            print(f'Balance {self.balance}')
    def deposite_balance(self,withdraw_balance_):
        self.balance=self.balance + withdraw_balance_
        print(f'Balance is {self.balance}')
            
def is_continue(balance):
    print('''
        Select option :
        1.Continue 
        2.Exit
        ''')
    
    print("Choice your option : ",end="")
    option = int(input())
    if(option == 1):
        bank(balance)
    else:
        exit()
    

def bank(bank_):
    print('''Select option :
        1. Balance 
        2. Withdraw Balance 
        3. Deposite Balance 
        4. Exit  
           
        ''') 
    
    print("Choice your option : ",end="")
    option = int(input())
    if(option == 1):
        bank_.balance_()
        is_continue(bank_)
    elif(option == 2):
        print("Enter withdraw balance : ",end="")
        b=int(input())
        bank_.withdraw_balance(b)
        is_continue(bank_)
    elif(option == 3):
        print("Enter deposite balance : ",end="")
        b=int(input())
        bank_.deposite_balance(b)
        is_continue(bank_)
    elif(option == 4):
        exit()
    else:
        print("Invalid Input")
        is_continue(bank_)   
def user():
    print("\n\n-------Bank Management System-------")
    print("**************************************\n\n")
    print("Enter first deposite balance : ",end="")
    b = int(input())
    bank_=Bank(b)
    bank(bank_)
user()



