# 1 TO 20, odd , add all the number
# 2O TO 1 , EVEN, add all the number 
# odd + even 

odd_sum = 0
even_sum = 0
for i in range(1,21):
    if i%2 != 0:
        odd_sum += i # 1 + 3 + 5 + 7 ..... 19 
        #print(i)
#print(odd_sum)
#print("2nd loop")
for j in range(20, 0, -1):
    if j%2 == 0:
        even_sum += j
        #print(j)

print("Total result = "+str(even_sum + odd_sum))
#print(even_sum)