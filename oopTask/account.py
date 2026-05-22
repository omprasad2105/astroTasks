class account:
    def __init__(self, accountHoldersName, accountNumber, balance = 0):
        self.accountHoldersName = accountHoldersName
        self.accountNumber = accountNumber
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def checkBalance(self):
        print(f"Current balance : {self.balance} INR\n")
    def displayDetails(self):
        print(f"\nAccount Holder's Name : {self.accountHoldersName}\nAccount Number : {self.accountNumber}\nCurrent Balance : {self.balance}\n")

accountDict = {}
option = -1
print("\nWelcome to the Banking System")
while True:
    option = input("\nWhat would you like to do?\n\
                   1 => Create a new account\n\
                   2 => Deposit\n\
                   3 => Withdraw\n\
                   4 => Check Account Balance\n\
                   5 => Display Account Details\n\
                   0 => Exit\n")
    if option.isnumeric():
        option = int(option)
    if option == 0:
        print("\nThank you for using our banking system. Goodbye\n")
        break
    match option:
        case 1: 
            name = input("Enter account holder's name : ")
            number = input("Enter account number : ")
            accountDict[number] = account(name, number)
            print("\nAccount created successfully!\n")
        case 2:
            number = input("Enter account number : ")
            if number in accountDict:
                amount = input("Enter the amount to be deposited : ")
                accountDict[number].deposit(float(amount))
                print("\nAmount deposited successfully!\n")
            else:
                print("\nAccount not found!\n")
        case 3:
            number = input("Enter account number : ")
            if number in accountDict:
                amount = input("Enter the amount to be withdrawn : ")
                if float(amount) <= accountDict[number].balance:
                    accountDict[number].withdraw(float(amount))
                    print("\nAmount withdrawn successfully!\n")
                else:
                    print("\nInsufficient balance!\n")
            else:
                print("\nAccount not found!\n")
        case 4:
            number = input("Enter account number : ")
            if number in accountDict:
                accountDict[number].checkBalance()
            else:
                print("\nAccount not found!\n")
        case 5:
            number = input("Enter account number : ")
            if number in accountDict:
                accountDict[number].displayDetails()
            else:
                print("\nAccount not found!\n")
        case _:
            print("\nInvalid option! Please try again.\n")
    input("Press Enter to continue...")
        