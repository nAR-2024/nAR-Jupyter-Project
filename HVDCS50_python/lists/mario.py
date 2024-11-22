#def main():
    #print_row(3)
    

# this prints a vertical column
#def print_column(height):
#    for _ in range(height):
#        print("#\n" * height, end="")
#        
#main()


# this prints a horizontal row
#def print_row(width):
#    print("?" * width)
#main()


# how to print a square
def main():
    print_square(3)
def print_square(size): 
    for i in range(size):
        print("#" * size)  
        
main()
