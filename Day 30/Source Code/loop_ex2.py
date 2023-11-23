# starting num
# ending num
# starting <  ending

s_n = int(input("Enter a Starting number")) # 3
e_n = int(input("Enter a Ending number")) # 10
if s_n < e_n:
    i = s_n # 3
    while i <= e_n: # 10
        print(i)
        i += 1
else:
    print("Starting number should be less than ending number")