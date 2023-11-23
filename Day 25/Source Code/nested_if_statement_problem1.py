# get name 
# contain 5 char or less than 10 char
# start from 'a' char

name = input("Enter your name")
#print(len(name))
if(len(name) == 5 or len(name) < 10):
    if(name.startswith('a')):
        print("Your name is "+name)
