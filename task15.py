import csv

with open('Input/grades.csv' , 'r') as csv_file:
    grades = csv.DictReader(csv_file)
    maxsimum = max(grades , key=lambda user : user['grade'])

with open('Output/output15.txt' ,'w') as output_file:
     output_file.write(f"Bahosi eng yuqori oquvchi: {maxsimum['name']} - {maxsimum['grade']}")    