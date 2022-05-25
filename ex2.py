# check if the number has one, two, three or four digits and determine that value be dont negative: conditions "Cascadas"

num = input("Please insert a integer number: ")
num = int(num)

if num < 0:
    num = num * ( -1 )

if num >= 1 and num <= 9:
    print("The number has one digit")
else:
    if num >= 10 and num <= 99:
        print("The number has two digits")
    else:
        if num >= 100 and num <= 999:
            print("The number has three digits")
        else:
            if num >= 1000 and num <= 9999:
                print("The number has four digits")
            else:
                print("The number has more than four digits")

#check if the number is positive and it has two digits and if the number has three digits verify if it's negative
                
num = int(input("Type a integer number: "))
'''numP = str("The number typed is a postive number")
numN = str("The number typed is a negative number")'''

if num > 0:
    if num >= 10 and num <= 99:
        print("The number typed is a positive integer value and has two digits")
    else:
        print("The number typed is a postive integer value and doesnt have two digits")
else:
    if num >= -999 and num <= -100:
        print("The number typed is a negative integer value and has three digits")
    else:
        print("The number typed is a negative integer value and doesnt have three digits")
print(num)
    
