from Accounts import *

accountsList=[]

oAccount=Account('Agha',5000,'password1')
accountsList.append(oAccount)

oAccount=Account('Panjabi',10000,'password2')
accountsList.append(oAccount)

accountsList[0].show()
print()
accountsList[1].show()

