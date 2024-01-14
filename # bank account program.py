# simple bank account program

class Account():
    def __init__(self,a_name,balance=0):
        self.a_name=a_name
        #self.a_no=a_no
        self.balance=balance

    def add_amount(self,amount):

        self.balance=self.balance+amount
        print (f"amount is added to your account!. and total amount is {self.balance}")

    def amount_withdraw(self,withdraw):
        if withdraw > self.balance:
            print(f"Insuficient balance in your account and The accont balance is {self.balance}")
        else: 
            self.balance=self.balance-withdraw
            print (f"amount is withdraw from your account!. and Balance amount is {self.balance}")
    def __str__(self):
        return f"owner is {self.a_name} and Your balence is {self.balance}"
    
a=Account("Omkar",0)
print(a.a_name)
print(a.balance)
a.add_amount(5000)
a.amount_withdraw(6000)
print(a)


        
 