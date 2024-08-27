    #While
""" i = 3
while i != 0:
    print("meow")
    i = i- 1 """
   


""" i = 0
while i <= 3:
    print("meow")
    #i = i + 1
    i += 1 """

   #for

""" #for i in [0,1,2]:
for _ in range(3):
    print("meow") """



   ####

""" print("meow"* 3) """
""" print("meow\n"*3) """
""" print("mewo\n"*3, end="") """



    #+tive integer


""" while True:
    n = int(input("Enter +ve Integer Number "))
    if n > 0:
        break
for _ in range(n):
    print("meow") """


def main():
    number = get_Number()
    meow(number)

def get_Number():
    while True:
        n = int(input(" Enter +ve Number: "))
        #if n > 0:
        #    return n

        if n > 0:
             break
    return n
        

def meow(n):
    for _ in range(n):
        print("meow")
main()