def cube(What_cube):
    return What_cube*What_cube*What_cube
var1=int(input("Enter a number to find the cube:"))

if var1 % 3 == 0:
    print("It is divisible by 3")
    print("Cube of that number is", cube(var1))

else:
    print("It is not divisible by 3")