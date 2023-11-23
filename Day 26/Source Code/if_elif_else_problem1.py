# get a number
# check, whether it is +,- or equal to 0

num = int(input("Enter a number"))
if num > 0:
    print("Number "+str(num)+" is positive")
elif num < 0:
    print("Number "+str(num)+" is Negative")
else:
    print("Number is equal to 0")