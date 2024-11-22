# while loop counting down

#i = 3
#while i !=0:
#    print("meow")
#    i -= 1


# while loop counting up, starts at zero because of zero index

#n = 0
#while  n < 3:
#    print("meow")
#    n += 1


# for loop, the range lets us specify how many times we iterate #through
# introducing lists list[]

#for _ in range(3):
#    print("meow")
    
#simplified to print things out repetitively

#print("meow\n" * 3, end="")  

#while True:
#    n = int(input("Whats n? "))
#    if n > 0:
#        break
    
#for _ in range(n):
#     print("meow")   
     
# creating a function for a loop 


def main():
  number = get_number()
  meow(number)
  
def get_number():
    while True:
        n = int(input("Whats n? "))
        if n > 0:
            return n
    
def meow(n):
    for _ in range(n):
        print("meow")
        
main()
  
      
