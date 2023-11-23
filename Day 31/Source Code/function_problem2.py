# get num
# send to function as parameter
# find table in reverse mode

def table(num):
    print("Table of number")
    # 4 * 10 = 40
    # 4 * 9  = 36
    #.....
    for i in range(10,0, -1):
        print(str(num)+" * "+str(i)+" = "+str(num*i))

x = int(input("Enter a number"))
table(x)