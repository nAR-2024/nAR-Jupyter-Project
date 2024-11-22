
#when receiving input it is always in string, so we have to convert it #to an math or integer for whole numbers using int()

#input() allows the user to enter their own numbers

x = int(input("Please give me a whole number for a X variable: "))
y = int(input("please give me a whole number for a Y variable: "))
print(x + y)


#making a float, through the use of float()

x = float(input("Please give me a X variable with a decimal: "))
y = float(input("Please give me a Y variable with a decimal: "))

print(x + y)

#to round the number you can round it to the closest integer using  #round()

number = round(x + y)
divided = round(x / y, 2)
print(number)

#this does the same thing as round

print(f"{number:,}")

# i can use division and then select the amount of decimals with a f #function
print(f"{number:.2f}")
