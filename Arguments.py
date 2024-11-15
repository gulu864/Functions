''' This is doc string
 This is used to write comented multiple lines'''

def bill_calculate(paid,bill):
    due=bill - paid
    return due
var1= int(input("Enter the bill amount:"))
var2= int(input("Enter what you paid:"))

print("Due amount left", bill_calculate(var1,var2))