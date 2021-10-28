from datetime import datetime
import pytz

WHITE='\033[00m'
GREEN='\033[0;92m'
RED='\033[1;31m'


class Acaunt:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.history=[]

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount):
        self.balance += amount
        self.show_balance()
        self.history.append([amount,self._get_current_time()])

    def wdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f'Spent {amount} units')
            self.show_balance()
            self.history.append([-amount, self._get_current_time()])
        else:
            print("No many")
        self.show_balance()

    def show_balance(self):
        print(f'Balance:{self.balance}')

    def show_history(self):
        for amount, date in self.history:
            if amount>0:
                transaction='deposited'
                color=GREEN
            else:
                transaction='withdrawn'
                color=RED
            print(f'{color} {amount}{WHITE} {transaction} on {date.astimezone()}')


a=Acaunt("Igor", 1000)
a.deposit(150)
a.wdraw(300)
a.deposit(2365)
a.wdraw(27)
a.show_history()















