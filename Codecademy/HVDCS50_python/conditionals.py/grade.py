# if elif and 

# top down checking goes through each iteration eliminating the option #from above, we use the elif to go through instead of just if, or it #will go through all.

score = int(input("Please enter score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
  print("Grade: F")  
        
