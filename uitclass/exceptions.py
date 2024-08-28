     #Syntax Error

""" print("Hello World) """

    #ValueError

""" x = int(input("What's your =ve integer? ")) #but user typed "cat"
print(f"{x} is your naumber") """

     #try and except

""" try:
    x = int(input("What's your +ve integer? "))
    print(f"{x} is your number")
except ValueError: 
        print("x is not an number") """



   ## NameError/Scope Issue
""" try:
    x = int(input("What's your +ve integer? "))
    
except ValueError: 
        print("x is not an number")

print(f"{x} is your number") """


    ### else

""" try:
    x = int(input("What's your +ve integer? "))
    
except ValueError: 
        print("x is not a number")

else:
        print(f"{x} is your number") """


   #infinte loop

""" while True:
    try:
        x = int(input("What's your +ve integer? "))

    except ValueError: 
            print("x is not a number")

    else:
            break

print(f"{x} is your number") """


""" while True:
    try:
        x = int(input("What's your +ve integer? "))
        break
    except ValueError: 
        print("x is not a number")

    
print(f"{x} is your number") """
    ######

""" def main():
    y = get_number()
    print(f"{y} is your number") """
    

""" def get_number():
    while True:
        try:
            x = int(input("Enter +ve integer? "))
        except ValueError:
            print("x is not number")
        else:
            #break
    #return x
            return x

main() """
   #####

""" def get_number():
    while True:
        try:
            x = int(input("Enter +ve integer? "))
            return x
        except ValueError:
            print("x is not number")
    
main() """
    ####

""" def main():
    y = get_number()
    print(f"{y} is your number")


def get_number():
    while True:
        try:
           
            return  int(input("Enter +ve integer? "))
        except ValueError:
            print("x is not number")
    
main() """



      ###pass

def main():
    y = get_number("Enter +ve integer? ")
    print(f"{y} is your number")

    
def get_number(prompt):
    while True:
        try:
            return  int(input(prompt))
        except ValueError:
            pass
    
main()

