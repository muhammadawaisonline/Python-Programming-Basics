   #Print column
""" for _ in range(3):
    print("#") """


""" def main():
    column(3)

def column(height):
    for _ in range(height):
        print("#")

main() """


      # 

""" def main():
    column(3)

def column(height):
    
    print("#\n"*height, end="")

main() """ 


""" def main():
    print_row()

def print_row():
    print("?"*4)

main() """


    #

""" def main():
    print_row(4)

def print_row(length):
    for _ in range(length):
        print("?", end="")

main() """

    #
def main():
    print_square(30)
""" 
def print_square(height):
    
    #print column
    for _ in range(height):
        #print row
        for _ in range(height):
        # print brik
            print("#", end="")
        #print column/ newline
        print() """
""" 
main() """

def main():
    print_square(10)
    

def print_square(size):
    for _ in range(size):
        print_row(size)

def print_row(width):
    print("#"*width)

main()