import json


with open('Input/students.json', 'r') as file:
    students = json.load(file)


names = []
for student in students:
    names.append(student['name'])


names.sort()

with open('Output/output12.json', 'w') as output_file:
    json.dump({'sorte_names': names}, output_file, indent=2)
