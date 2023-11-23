# to get username
# alpha or numaric
# ==8 or less than 20

user = input("Enter username")

if user.isalnum() and (len(user) == 8 and len(user) < 20):
    print("Your username is valid that is = "+user)
else:
    print("Username is invalid")