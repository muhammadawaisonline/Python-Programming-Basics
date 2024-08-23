# asking name of user
#name = input("what's your name? ")
"""
 Second way to comment
"""
#print("Hello " + name)
#print(f"Hello {name}")
#print("Hello", name)
#print("Hello","", name)
#print("Hello")
#print(name)
#print("Hello", end=" ")
#print(name)
#print("Hello", name, sep="???" )
#print("Hello 'friend'")
#print("Hello \"friend\"")
   # f string
#print(f"Hello {name}")
   #Remove user input space
#name = name.strip()
   #Capitalize User name
##name = name.capitalize()
   #Capitalize User names
#name = name.title()
   #cleain code
#name =name.strip().title()
   #second way to dea with it
name = input("what's your name? ").strip().title()
   #Splliting Strig
first, second = name.split(" ")
print(f"Hello {second}")