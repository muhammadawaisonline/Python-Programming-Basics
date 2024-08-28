    #Parity
""" x = int(input("What's x? "))

if x % 2==0:
    print("Even")
else:
    print("Odd")  """


    # Bool
def main():
    x = int(input("What's x? "))
    if is_Even(x):
        print("Even")
    else:
        print("Odd")
def is_Even(n):
    """ if n % 2 ==0:
        return True
    else:
        return False """
    

    """ return True if n % 2 == 0 else False """
    return n % 2 == 0


main()
