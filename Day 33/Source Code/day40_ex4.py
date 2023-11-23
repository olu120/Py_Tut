# to get total terms
# value to store in that terms
# find total or sum of values
# and divide by total terms

terms = int(input("Enter a total terms")) # 5

total_values = 0
for i in range(0, terms):
    values = int(input("Enter value for term")) # 30
    total_values +=  values

print("Total values = "+str(total_values))
ave = total_values / terms
print("Average = "+str(ave))