# Get age and name
# display age and name if age > 18

age = int(input("Enter a age "))
name = input("Enter your name")

if age > 18:
    print("Your age is : "+str(age))
    print("Your name is "+name)
else:
    print("Sorry, your age is less than 18")
