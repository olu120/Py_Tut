# get age 
# convert into second

age  = float(input("Enter your age in year")) # '32.2' -> 32.2
print("Your age is "+str(age))
one_year_sec = 365 * 24 * 60 * 60
age_into_sec = age * one_year_sec
print("Your age into seconds is : "+str(age_into_sec))