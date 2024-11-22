# how to create def a function in python
# the parameter in the hello function has a default vale of world if a #user does not enter their name


def main():
  name = input("Whats your name? ")
  hello(name)
  
def hello(hello_to = "world"):
	  print("Hello,", hello_to)
	  
#call the function	  
main()





  
  
