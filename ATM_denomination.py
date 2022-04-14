"""
Assume an ATM has currency notes of denominations 100,500 and1000. If the amount to be withdrawn is input through the ATM keyboard panel, find the total number of currency notes under each denomination that the ATM has to dispense.
Boundary conditions : 100 <= amount <= 100000
"""
amt = eval(input("Enter amount to withdraw(amount should be multiple of 100)"))
temp = amt
if temp % 100 != 0:
    print("Please enter the amount that is multiple of 100")
else:
    if 100 <= amt and amt <= 100000:
        cash_1000 = temp // 1000 # 5900 // 1000 = 5
        temp = temp % 1000 # 5900 % 1000 = 900
        cash_500 = temp // 500
        temp = temp % 500
        cash_100 = temp // 100
        print("1000 rupees notes {} \n500 rupees notes {} \n100 rupees notes {} \n".format(cash_1000,cash_500,cash_100))
    else:
        print("Amount should be in range between 100 and 100000")
