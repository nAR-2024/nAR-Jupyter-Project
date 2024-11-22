# ask user for their name
# the input symbol lets you capture something and then nstore it in  
# the variable name

name = input("what is your name?  ")
print("Hello,",  name)

# improving on the function:
	
age = input("whats your age?  ")
print("You are:", age, "years young!")

# using the two variables and creating them through ind inputs
# the end="" stops the automatic line break

print("Your ID will be, ", end="")
print(name, end="")
print(age)

#The f adds a function that allows you to use the curly brackets with #the variables>
print(f"Hello {name}, i belive you are {age}!")




