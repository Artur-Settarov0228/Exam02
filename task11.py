import json

with open('Input/students.json' , 'r') as json_file:
    students = json.load(json_file)

count = len(students)

output_1 = {f"count" : count}

with open('Output/output11.json' , 'w') as output:
    json.dump(output_1,output, indent=4)
