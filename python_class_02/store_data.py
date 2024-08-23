   ### Store names in a list
""" names = []


for _ in range(3):
    name = input("What's your name? ")
    names.append(name)

for name in sorted(names):
    print(f" My name is {name}") """


   ##Writing Names on file
""" name = input("What's your name? ")

file = open("names.txt", "w" )
file.write(name)
file.close() """

    #Witng and appending names
""" for _ in range(6):
    name = input("What's your name? ")
    file = open("names.txt", "a")
    file.write(f"{name}\n")
    
file.close() """


    ### "with" will close file automatecally
""" for _ in range(6):
    name = input("What's your name? ")
    with open("names.txt", "a") as file:
        file.write(f"{name}\n") """


    ### How to read the data fro file


""" names = [] """

""" with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello", line) """

   ## Remove gap between line
""" with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello", line, end="") """

  ## Second way to remove gap between data

""" with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello", line.rstrip()) """
    

    ###Append data into our list
""" names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip()) """

""" for name in sorted(names):
    print(f" Hello {name}") """

""" for name in sorted(names, reverse=True):
    print(f" Hello {name}") """


     ### CSV file for Two dimensional data
""" students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",") """
""" student = {}

        student["name"] = name
        student["house"] = house """

"""         student = { "name": name, "house": house}
        students.append(student)
     """

""" for student in students:
    print(student["name"]) """
#OR
""" def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"] """

""" for student in sorted(students, key=get_name, reverse=True):
    print(student) """
""" for student in sorted(students, key=get_house, reverse=True):
    print(student) """
""" for student in sorted(students, key= lambda student: student["name"] , reverse=True):
    print(student) """
""" for student in sorted(students, key= lambda student: student["house"] , reverse=True):
    print(student)


for student in students:
    print(f"{student["name"]} lives in {student["house"]}") """

    ### How to read CSV files
        ## Using reader()
""" import csv

students = []
with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home}) 
    
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student["name"]} lives in {student["home"]}") """

       ###using DictReader()

""" import csv

students = []
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({row["name"]: "name", row["house"]:"house"}) 
    
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student["name"]} lives in {student["house"]}")
     """


            ### How to write CSV file
""" import csv
name = input("What's your name? ")
house = input("Where's your house? ")
with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, house]) """

import csv
name = input("What's your name? ")
home = input("Where do you live? ")


with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home" ])
    writer.writerow({"name": name, "home": home })
    

