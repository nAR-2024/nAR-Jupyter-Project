#, -, *, /, %,
#this returns a BOOL a True or False response returned to the user

def main():
  x = int(input("Whats x? "))
  if is_even(x):
        print("Even")
  else:
          print("odd")
 
def is_even(n):
#    if n % 2 == 0:
#       return True if n % 2 == 0 else False
#     else:
#       return False

  return n % 2 == 0
main()
