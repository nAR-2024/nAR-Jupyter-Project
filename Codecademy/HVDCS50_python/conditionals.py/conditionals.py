#. If OR AND

# >, <, <=, >=, ==, !=

# conditionals start with if statements
# the input allows the user to enter values

x = int(input('whats x ? '))
y = int(input('whats y ? '))

#if x < y: 
#   print('x is less than y')
#elif x > y:
#    print("x is greater than y")
#we dont have to ask the question, it is the only alternative
#else:
#     print("x is equal to y")        
     
   
if x < y or x > y:
    print("x is not equal to y")
else: 
    print("x is equal to y")
        
if x != y:
  print("x is not equal to y")
else:
  print("x is equal to y")     
