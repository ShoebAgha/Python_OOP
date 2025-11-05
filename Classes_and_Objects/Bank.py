from Accounts import Account

class Bank:
    def __init__(self):
        self.accountsDict={}
        self.nextAccountNumber=19790862

    def createAccount(self,theName, theBalance, thePassword):
        oAccount=Account(theName,theBalance,thePassword)
        newAccountNumber=self.nextAccountNumber
        self.nextAccountNumber+=1
        self.accountsDict[newAccountNumber]=oAccount
        return newAccountNumber
    
    def openAccount(self):
        print("****Opening New Account****")
        username=input('Enter name of Account Holder: ')
        userbalance=input('Enter Opening Balance Amount: ')
        userpassword=input('Enter Password for your Account: ')

        useraccountNumber = self.createAccount(username,userbalance,userpassword)

        print(f"Your Account number is: {useraccountNumber}")

newBank=Bank()
newBank.openAccount()

        