from bank_system.account import *
from bank_system.bank import *
from bank_system.check_account import *
from bank_system.customer import *
from bank_system.loan import *
from bank_system.Saving_account import *



if __name__=="__main__":
    attempts=0
    response=input("do you want to play (y,n)")

    while response != 'n':
        guess_the_shap(attempts)
        attempts +=1

        if attempts> len(shaps)-1:
            break