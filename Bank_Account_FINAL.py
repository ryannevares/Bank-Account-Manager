"""
Author: Ryan Nevares
Date: 18 October 2017
Title: Bank account

This program will use a Python class to manipulate a bank account.  The program will allow for deposits, withdrawls, and displaying the balance and details of the account.  This is just some early practice for me using classes, as well as file I/O, so it won't be too fancy.

This is the second version of this mini-project.  It is more complete and capable than the original and will include new features compared to the original version.  This program will also use a seperate file to make any changes to any accounts persistant

Please report any bugs to ryannevares@gmail.com
"""

from time import sleep
import sys
from ast import literal_eval

# I want this program to 'slow type' its messages rather than just dumping them all on the screen at once.
def print_slow(string):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(.03)

# Print the initial message to the user
print ""
print_slow("Account Management Program started successfully!")
sleep(.5)
print ""

# open the current dictionary of accounts
def read_in():
    f = open("accounts.txt", "r")
    dictionary = literal_eval(f.read())
    f.close()
    return dictionary

# save any changes made
def save(dictionary):
    f = open("accounts.txt", "w")
    f.write(str(dictionary))
    f.close()

# Keep track of which account is "active"
active_account = ""

# print out possible Options
def options():
    print ""
    options = ["I for Info","B for Balance","D for Deposit","W for Withdraw", "del for delete", "E for Exit"]
    print_slow ("Options:\n")
    sleep(.5)
    for i in options:
        print i
        sleep(.2)
    print ""

# create the class for bank accounts
class BankAccount(object):
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def __repr__(self):
        # This defines how the object BankAccount is represented when a user tries to call BankAccount
        return "This account belongs to %s and has $%.2f in it." % (self.name,self.balance)
    # Create a method to just print the balance (for anonymity)
    def show_balance(self):
        return self.balance

    # create a method to DEPOSIT funds
    def deposit(self, amount):
        if amount <= 0:
            print "You need to enter a dollar amount"
            return
        else:
            # Deposit the money
            print "You have deposited $%.2f" % amount
            self.balance += amount
            self.show_balance()
            sleep (.5)

    # Let the user get their money out!
    def withdraw(self,amount):
        if amount <= 0:
            print "You need to enter a dollar amount"
            return
        elif amount > self.balance:
            print "Insufficient funds"
            return
        else:
            print "You withdrew $%.2f" % amount
            self.balance -= amount
            self.show_balance()


def main_menu(active_account,dictionary):
    while True:
        print "Active Account: ", active_account.name
        options()
        choice = raw_input("Please select an option: ")
        # Create a new account instance
        if choice == "I" or choice == "i": # Info
            print active_account
            print "\n\n\n\n"
            sleep(.5)
        elif choice == "B" or choice == "b": # balance
            print "Balance: $%.2f" % active_account.balance
            print "\n\n\n\n"
            sleep(1)
        elif choice == "D" or choice == "d": # deposit
            amount = raw_input("Enter the amount you would like to deposit: ")
            if not amount.isdigit():
                print_slow("Invalid Input: You need to enter a dollar amount")
                print ""
                sleep(.5)
                return main_menu(active_account,dictionary)
            amount = float(amount)
            active_account.deposit(amount)
            dictionary[active_account.name] = active_account.balance
            sleep(2)
            print "Balance: $%.2f" % active_account.balance
            print "\n\n\n\n"
        elif choice == "W" or choice == "w": #withdraw
            amount = raw_input("Enter the amount you would like to withdraw: ")
            if not amount.isdigit():
                print_slow("Invalid Input: You need to enter a dollar amount")
                print ""
                sleep(.5)
                return main_menu(active_account,dictionary)
            amount = float(amount)
            active_account.withdraw(amount)
            dictionary[active_account.name] = active_account.balance
            sleep(2)
            print "Balance: ", active_account.balance
            sleep(.5)
            print "\n\n\n\n"
        elif choice == "E" or choice == "e": # exit
            print ""
            print_slow("Sorry to see you go, Exiting now.....")
            print ""
            sleep(1.5)
            break
        elif choice == "del":  # delete the account
            print ""
            print_slow("Are you sure you want to permanently delete your account?")
            sleep(1)
            print ""
            delete_account = raw_input("y/n: ")
            if delete_account == "n" or delete_account == "N":
                print_slow("Deletion cancelled")
                sleep(.5)
                print "\n \n"
                return main_menu(active_account, dictionary)
            elif delete_account == "Y" or delete_account == "y":
                del dictionary[active_account.name]
                print "\n \n"
                print_slow("Account successfully deleted!")
                print "\n\n\n\n"
                sleep (1)
                break
            else:
                print "Invalid Input:  Please choose yes or no"
                return main_menu(active_account, dictionary)
        else:
            print_slow("You must select a valid option from the list")
            print "\n\n\n\n\n"
            sleep(1)
            return main_menu(active_account,dictionary)

def main():
    accounts = read_in()
    # See if the customer is a returning customer or new
    returning_customer = raw_input("Do you have an existing account? (y/n): ")
    print ""
    # Create a new account
    if returning_customer == "n" or returning_customer == "N":
        print_slow ("Alright!  Lets get your account set up")
        print ""
        sleep(.5)
        customer_name = raw_input("Enter your name: ")
        my_account = BankAccount(customer_name,0)
        active_account = my_account
        accounts[my_account.name] = my_account.balance
        print "\n", my_account, "\n \n \n \n \n \n \n"
        sleep(1)
        main_menu(active_account,accounts)
        save(accounts)
    # Access an existing account
    elif returning_customer == "y" or returning_customer == "Y":
        print_slow("Welcome back!")
        print "\n\n"
        sleep(.5)
        user_account = raw_input("Enter your name to access your account: ")
        if user_account in accounts.keys():
            user_account = BankAccount(user_account,accounts[user_account])
            main_menu(user_account,accounts)
            save(accounts)
        else:
            print_slow("Could not locate your account, please try again")
            print "\n\n\n"
            sleep(1)
            return main()
    else:
        print_slow("Invalid option entered!")
        print "\n \n \n \n \n \n"
        sleep(1)
        return main()
# Call the main function to start the program
main()

"""
Future suggestions:

PASSWORDS
(encrypted?)
"""
