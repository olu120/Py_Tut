# get age and name
# age should be greater or equal to 18
# makrs should be greater 90 or less than 100
# then select that user 

age = int(input("Enter your age"))
marks = int(input("Enter your marks"))

if(age >= 18):
    if(marks > 90 and marks < 100 ):
        print("You are selected ")
        print("Because your age is "+str(age)+" and your marks "+str(marks))
    else:
        print("marks issue")
else:
    print("Age issue")