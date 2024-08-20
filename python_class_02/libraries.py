""" import random

coin = random.choice(["head", "tail"])
print(coin) """

""" from random import choice

coin = choice(["head", "tail"])
print(coin)
 """
   ###randint
""" from random import randint

guess_number = randint(3,4)
print(guess_number) """
  ###shuffle
""" from random import shuffle

name = ["Harry", "Hermione", "Ron", "Draco"]
shuffle(name)
print(name) """


""" from random import shuffle

names = ["Harry", "Hermione", "Ron", "Draco"]
shuffle(names)
for name in names: 
    print(name) """

    ###statistics
""" import statistics

mean = statistics.mean([100,250])
print(mean) """


    ### Comand-line-Argument
    
       #sys
""" import sys """

""" name = sys.argv[1]
print(f"My name is {name}") """


""" try:
  name = sys.argv[2]
  print(f"Hello my name is {name}")
except IndexError:
  print("too few arguments") """
#check for error
""" if len(sys.argv) < 2:
    print("Too few argumants")
#for long name
elif len(sys.argv) > 2:
    print("Too many Arguments")
#for Corner cases
else:
    print(f"Hello my name is {sys.argv[0]}") """ 

""" if len(sys.argv) < 2:
    print("Too few argumants")
#for long name
elif len(sys.argv) > 2:
    print("Too many Arguments")
#print name tags 
print(f"Hello my name is {sys.argv[0]}") """



    ##Exit Program


""" import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
print("Hello may name is ", sys.argv[0]) """

""" import sys

if len(sys.argv) < 2:
    sys.exit("Too many arguments")
for arg in sys.argv:
    print("Hello may name is ", arg) """


    #slice List

""" import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    print(sys.argv[1:]) """

   #print every sigle name of the list on single line
import sys
""" if len(sys.argv) < 2:
    sys.exit("Too few arguments") """

""" for name in sys.argv:
    print("My name is ", name) """

for name in sys.argv[1:-1]:
    print("My name is ", name)
