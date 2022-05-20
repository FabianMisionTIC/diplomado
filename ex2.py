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

