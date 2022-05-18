#conditionals
#consulting if a number is odd or even with one variable

'''x = 52
if x%2 == 0: #if result 
    print("X is even")
else:
    print("X is odd")'''
    
# with two variables, determine if is greater, less or equal

'''x = 84
y = 84

if x > y:
    print("X is greater than Y")
elif x < y:
    print("X is less than Y")
else:
    print("X is equal  Y")'''
    
# With letters

letter = "s"

if letter == "r":
    print("Wrong result")
elif letter == "s":
    print("Correct result")
elif letter == "t":
    print("close result but incorrect")

#nested conditions (anidadas)

h=54
j=78

if h == j:
    print("H is equal to j")
else:
    if h<j:
        print("H is less than to j")
    else:
        print("H is greater than j")

#TRY - EXCEPT convert temperature from degrees fahrenheit to degrees celsius

temp_fahr = input('Type temp in degrees fahr: ')
try:
    fahr = float(temp_fahr)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(str(fahr) + "degree fahrenhei is equal to  " + str(cel) + " degree celsius")
except:
    print("Invalid number")
