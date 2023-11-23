# to get 2 number
# square + cube = > display to user

num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))

square_num = num1 * num1
cube_num = num2 * num2 * num2
addition = square_num + cube_num

print("User Entered Number num1 = "+str(num1))
print("User Entered Number num2 = "+str(num2))
print("Square of "+str(num1)+ " = "+str(square_num))
print("Cube of "+str(num2)+ " = "+str(cube_num))
print("Adittion of "+str(square_num)+ " and "+str(cube_num)+ " is = "+str(addition))
