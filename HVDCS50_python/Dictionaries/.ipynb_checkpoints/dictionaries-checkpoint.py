# creating a basic dictionary | curli braces for dict

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "slytherin",
}
#. creating a list of dict

students = [
    {"name": "Hermione", "house": "Gryffindor", "Patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "Patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "Patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "gryffindor", "Patronus": "None"}
  ]
  
# we use the for loop to accesss the dict, and go through each and
# prints the names

for student in students:
  print(student["name"], student["house"], student["Patronus"], sep= ", ")




