# make percentage cal
# total ammount, how much you need perncentage

total_ammount = float(input("Enter total ammount "))
requreid_percentage = float(input("How much percentage you need to get "))

per = (total_ammount * requreid_percentage) / 100
print("Total Amount = "+str(total_ammount))
print("Required Percentage = "+str(requreid_percentage)+"%")
print("Your Percentage Amount = "+str(per))