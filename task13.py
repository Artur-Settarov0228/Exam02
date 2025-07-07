import json
with open('Input/students.json' ,'r') as json_file:
    students = json.load(json_file)


uzun_ism = []

for student in students:
    name = student['name']
    if len(name) > 5:
        uzun_ism.append(name)

with open('Output/output13.json', 'w') as output_file:
    json.dump({"uzun_ism" : uzun_ism} , output_file ,indent=4)