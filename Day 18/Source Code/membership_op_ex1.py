lst = ['red','gray','green','pink','black','white']
color_name = input("Enter a color name")

if(color_name in lst):
    print(color_name+" Color is present in the list")
    print(lst)
else:
    print("It did not match in the list")