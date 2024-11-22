# try \ except \ else \ pass \ raise
# using the while function to make something true until it is not true
# the try allows us to use the except to find the problems in the user # input
# allows you to look at exceptions


def main():
    x = get_int("whats x? ")
    print(f"x is {x}")
       
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))    
        except ValueError:
            pass # allows us to get the type of input we desire
main()
