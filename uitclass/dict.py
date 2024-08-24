""" students = {
    "Harry": "Gryffindor",
    "Hermione": "Gryffindor",
    "Ron": "Gryffindoe",
    "Draco": "Slytherin",

} """
""" print(students["Harry"])
print(students["Hermione"])
print(students["Ron"])
print(students["Draco"]) """

""" for i in students:
    print(students[i]) """


""" for i in students:
    print(i, students[i], sep=",") """


    # Same Keys but different values/ List of dictionaries
students = [
    {"name": "Harry", "house": "Gryffindoe", "patronus": "Otter"},
    {"name": "Hermione", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindoe", "patronus": "Jack Russel trerrier"},
    {"name": "Draco", "house": "Slutherin", "patronus": None},
]

for i in students:
    print(i["name"], i["house"], i["patronus"], sep=", ")

