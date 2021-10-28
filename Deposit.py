WHITE='\033[00m'
GREEN='\033[0;92m'
RED='\033[1;31m'



class Acaunt:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.history=[]


    def deposit(self,amount):
        self.balance+=amount
        self.show_balance()
        self.history.append([amount, self.balance])


    def withdraw(self,amount):
        if amount> self.balance:
            print(f"{RED}Withdraw: amount={amount}, balance={self.balance} No many {WHITE}")
        else:
            self.balance-=amount
        self.show_balance()
        self.history.append([-amount, self.balance])


    def show_balance(self):
        print(f'Balance={self.balance}')

    def show_history(self):
        for amount,balance in self.history:
            if amount>0:
                tran="deposit"
                color=GREEN
            else:
                tran="whithdraw"
                color=RED
            print(f'{color} {tran} {WHITE} {amount} {balance}')


a=Acaunt('igor',1000)
a.deposit(1000)
a.withdraw(20)
a.withdraw(2000)
a.show_history()

