# to get six subjects marks
# find total, ave, percentage

subj1 = int(input("Enter subject1 marks"))
subj2 = int(input("Enter subject2 marks"))
subj3 = int(input("Enter subject3 marks"))
subj4 = int(input("Enter subject4 marks"))
subj5 = int(input("Enter subject5 marks"))
subj6 = int(input("Enter subject6 marks"))

total = subj1 + subj2 + subj3 + subj4 + subj5 + subj6
ave = total / 6
percentage = (total * 100) / 600
print("Total makrs = "+str(total))
print("Average = "+str(ave))
print("Percentage = "+str(percentage)+"%")