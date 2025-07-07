import csv

with open('Input/grades.csv' , 'r') as csv_file:
    grades = csv_file.readlines()

lines = grades[1:]

count_5 = 0
for line in lines:
    parts = line.strip().split(',')  
    if len(parts) == 2 and parts[1] == '5':
        count_5 += 1

with open('Output/output16.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(f"5 baho olganlar soni: {count_5} ta 0_0")