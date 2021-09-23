balance = 69420

class Atm:

    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print(" Your balance is $", balance)

    def withdrawl(self,amount):
        new_amount = balance - amount
        print(" You Withrawed $", amount, "\n Now You Have $", new_amount, " left")


def main():
    Card_number = input(" Insert Your Card Number : ")
    pin_number  = input(" Enter Your Pin Number : ")

    new_user =  Atm(Card_number ,pin_number)

    print(" Choose What Ya Want To Do : ")
    print(" \n ( 1 ) Balance Enquriy \n\n ( 2 ) withdrawl \n")
    something = input("\n Enter The Thing Something That You Want To Do : ")

    if (something == 1):
        new_user.check_balance()
    elif (something == "bal"):
        new_user.check_balance()
    elif (something == "balance"):
        new_user.check_balance()
    elif (something == 2):
        amount = int(input(" Enter The Amount You Wanna Withdraw: "))
        new_user.withdrawl(amount)
    elif (something == "with"):
        amount = int(input(" Enter The Amount You Wanna Withdraw: "))
        new_user.withdrawl(amount)
    elif (something == "withdraw"):
        amount = int(input(" Enter The Amount You Wanna Withdraw: "))
        new_user.withdrawl(amount)
    else:
        print("That Is NOT A Valid Input")


if __name__ == "__main__":
    main()