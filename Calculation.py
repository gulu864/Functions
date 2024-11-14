def add(z,y):
     return z + y

def substract(z,y):
     return z - y

def multiply(z,y):
     return z * y

def divide(z,y):
     return z / y

print("What opration do you want (a/b/c/d)?:")
print("a.Addition")
print("b.Subtraction")
print("c.Multiplication")
print("d.Division")

choice=input("Enter you option:")

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

if choice == "a":
     print("sum:", add(num1,num2))

elif choice == "b":
     print("sum:", substract(num1,num2))

elif choice == "c":
     print("sum:", multiply(num1,num2))

elif choice == "d":
     print("sum:", divide(num1,num2))

else:
     print("invalid input")