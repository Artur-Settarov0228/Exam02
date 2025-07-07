import json

with open('Input/students.json' , 'r') as json_file:
    students = json.load(json_file)

A_harf_boshlanadigan = []

for student in students:
    name = student['name']
    if name.startswith('A'):
        A_harf_boshlanadigan.append(name)

with open('Output/output14.json' , 'w') as output_file:
    json.dump({"A_harf_boshlanadigan" : A_harf_boshlanadigan} , output_file, indent=4)
 