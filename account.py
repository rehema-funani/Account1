class Account:
    def __init__(self,number,pin,name):
        self.over_draft_limit = -200
        self.number = number
        self.__pin = pin
        self.__balance = 0
        self.name = name
    def show_balance(self,pin):
        if pin ==self.__pin:
            return self.__balance
        else:
            return "wrong pin"
    def deposit(self,amount):
        self.__balance+=amount
        
    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance-=amount
        else:
            print("insufficient funds")
    def view_account_details(self):
        print(f"Account Owner:{self.name}")
        print(f"Account number:{self.number}")
        print(f"Account Balance:{self.__balance}")
    def change_account_owner(self,new_owner):
        self.name = new_owner
    def interest_calculation(interest_rate):
        interest = interest_rate*balance
    def account_statement():
        print(f"you deposited {self.amount} on date 2-3-2024")
    def close_account(account_id):
        try:
            return "account with {account_id} successfully closed"
        except Exception as e:
            return f"error closing account"
    def freeze_account(amount):
        is_account_frozen = true
        if is_account_frozen:
            print("your account is frozen, no ongoing transactions allowed")
        elif self.__balance>=amount:
            self.__balance - amount
        else:
            print("insufficient funds in your account")
    def set_minimum_balance(self,minimum_balance):
        self.minimum_balance = minimum_balance
    def transfer_funds(self,recipient_account,amount):
        if self.balance>=amount:
            self.balance-=amount
            recipient_account.balance+=amount
        else:
            return "insufficient  funds "
    
    

            
             
             
             


