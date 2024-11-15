def factorial(var1):
    if var1 == 1 or var1 == 0:
        return 1
    else:
        return var1 * factorial(var1 - 1)
var2=int(input("Enter a number:"))
print(factorial(var2))