class atm:
    def __init__(self,balance=0):
        while True:
            self.name = input("Enter your name here: ")

            if self.name.replace(' ','').isalpha():
                break
            else:
                print("Name should be only contains Alphabets Character: Try Again!!")
        while True:
            
            self.accountNumber = input("Enter your Account Number: ")

            if self.accountNumber.isnumeric() and len(self.accountNumber)==10:
                break
            else:
                print("Enter a Valid Account Number:Try Again!!")
        while True:
            self.pin = input("Create your pin: ")

            if self.pin.isnumeric() and len(self.pin)==4:
                break
            else:
                print("Enter Pin only Numeric Value and check the lenght of PIN\n4-Digit PIN is Valid.")
        self.balance = balance
    # def details(self):
    #     print(f"Account Holder name is:{self.name}\nAccount Number is:{self.accountNumber}\nATM PIN is:XXXX\nCurrent Balance:{self.balance}")

    def details(self):
        """Display masked account details."""
        print(f"Account Holder Name: {self.name}")
        print(f"Account Number: {self.mask_account_number()}")
        print(f"Current Balance: ₹{self.balance}")
        print(f"ATM PIN is:XXXX")

    def deposite(self,depo):
        pin2 = input("Enter your current PIN :")
        if pin2 == self.pin :
            self.balance = self.balance+depo
            print(f"Your Updated Balance is:{self.balance}")
        else :
            print("Incorrect PIN Transaction failed ")
    def witt(self,witt):
        pin3 = input("Enter Your Current  PIN :")
        if pin3 == self.pin :
            if witt<self.balance:
                self.balance=self.balance-witt
                
                print(f"Please Collect your Cash:{witt}\nYour Updated Balance is:{self.balance}")
            elif witt>self.balance :
                print(f"Insufficient Funds!!-Your Current Balance is:{self.balance}")
        else :
            print("Invalid Print !! Transaction failed ")

    def checkBalance(self):
        print(f"Your current Balance is:{self.balance}")
    def changePin(self,oldPin,newPin=0):
        # while True:
        if oldPin == self.pin:
            newPin = input("Enter Your New PIN: ")
            if len(newPin) == 4:
                if newPin == oldPin:
                    print("New PIN and Old PIN can't be Same")
                else:
                    self.pin = newPin
                    print("Your PIN is Updated Successfully!!")
            else:
                print("Enter 4-Digit PIN only")
        else:
            print("Invalid Old PIN")
    def changeName(self):
        oldName = input("Enter your Current Username: ")
        oldPin = input("Enter your Current PIN: ")
        if oldName == self.name and oldPin == self.pin:
            newName = input("Enter your New Username: ")
            if newName.replace(' ', '').isalpha():
                self.name = newName
                print("Your Username is Updated Successfully!!")
            else:
                print("New Username must only contain Alphabet Characters.")
        else:
            print("Invalid Username or PIN")


    def mask_account_number(self):
        return self.accountNumber[:3] + "xxxxxx" + self.accountNumber[-2:]
    


    # def details(self):
    #     hide_account = self.accountNumber[:3] + "*****" + self.accountNumber[-3:]
    #     print("Account Holder name is: " + self.name +
    #           "\nAccount Number is: " + hide_account +
    #           "\nCurrent Balance: " + str(self.balance))

    def showFullAccountNumber(self):
        entered_pin = input("Enter your PIN to view the full account number: ")
        if entered_pin == self.pin:
            
            print("Your Full Account Number is: " + self.accountNumber)
        else:
            self.ShowPin()
           
    def ShowPin(self):
        choice = input("Would you like to see your PIN? (yes/no): ").lower()
        if choice in ["yes","y"]:
            entered_name = input("Enter the Account holder's name :")
            if entered_name == self.name :
                print("Your Current PIN is:",self.pin)
                self.showFullAccountNumber()
            else:
                print("Enter Valid Name")
        else:
            print("Returning to menu.")

    def show_pin(self):
        old_name=input("Enter you name: ")
        if old_name == self.name:
            while True:
                print(f"your PIN is: {self.pin}")
                break
        else:
            print("Invalid name! Try again.")
    def trans(self):
        print("""\nList of Options:
        \n1.Account Details:
        \n2.Account Balance
        \n3.Deposite Cash
        \n4.Withdraw Amount
        \n5.Change Name
        \n6.Show AccountNumber
        \n7.Change PIN
        \n8.Exit""")
        while True:
            try:
                opt = int(input("\nChoose an Options:"))
            except:
                print("Error: Choose a Correct Options.")
                continue
            else:
                if opt == 1:
                    atm.details(self)
                elif opt == 2:
                    atm.checkBalance(self)
                elif opt == 3:
                    try:
                        depo = int(input("Enter Your Deposite Amount: "))
                    except ValueError:
                        print("Enter a Correct Amount")
                    else:
                        atm.deposite(self,depo)
                elif opt == 4:
                    witt1 = int(input("Enter your withdrawal Amount: "))
                    atm.witt(self,witt1)
                elif opt == 5:
                    atm.changeName(self)
                elif opt == 6:
                    atm.showFullAccountNumber(self)
                elif opt == 7:
                    oldPin1 = input("Enter your Old PIN:")
                    atm.changePin(self,oldPin1)
                elif opt == 8:
                    print("Thanks for Using ATM.")
                    break         
user = atm()
user.trans()
