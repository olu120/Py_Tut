# get 3 num
# find greatest number

def find_great(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        largest  = n1
        print("largest number is the "+str(largest)) 
    elif n2 > n1 and n2 > n3:
        largest = n2 
        print("largest number is the "+str(largest)) 
    else:
        print("largest number is the "+str(n3)) 

n1 = int(input("Enter 1st num"))
n2 = int(input("Enter 2nd num"))
n3 = int(input("Enter 3rd num"))
find_great(n1, n2, n3)