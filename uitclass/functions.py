#def hello():
#    print("Hello")
#hello()


      ## Taking User input
#def hello():
#    print("Hello")
#name = input("What's your Name? ")

#hello()
#print(name)


   #Positional Arguments of Function
#def hello(to):
#    print("Hello", to)
     
#name = input("What's your Name? ")
#hello(name)


        ###Named rguments of Function
 
#def hello(to = "world"):
#    print("Hello", to)
    
#name = input("What's your Name? ")
#hello()


        #NameError
#hello()
#name = input("What's your name? ")
#hello(name)


     #if you want yo use user input in different place of the code use function
#def main():
#    name = input("What's your name? ")
#    hello(name)
    
#def hello(to):
#    print("Hello", to)
#main()



    #Scope Issue
#def main():
#    name = input("What's your name? ")
    
#def hello(to):
#    print("Hello", to)
#hello(name)
#name is defined only in main() function 
#main()



      #return value
def main():
    x = int(input("What's x? "))

    print(f"square of {x} is", square(x))

def square(n):
    #return n*n
    #return n**2
    return pow(n,2)
main()
