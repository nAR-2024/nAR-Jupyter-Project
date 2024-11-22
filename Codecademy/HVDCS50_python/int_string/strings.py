#remove whit space from a string

#ask for name
name = input("Please enter your name: ")

#this cleans up the string of data entered by user

name = name.strip()

#to fix capatilizing first lettr
name = name.capitalize()

#to fix first and last name
name = name.title()

print(f"please verify your name is correct: {name} ")

#can be chained together instead of 
name = name.strip().title()


#ultimately you can write it like this
name = input("Please enter your name: ").strip().title()
print(f"Please verify Your Name: {name}")

#their is also the method .split().  
first, last = name.split(" ")
print(f"nice to meet you:, {first}")
