students = [
    {'name': 'Ali', 'age': 18},
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Muhammad', 'age': 21}
]

eng_qisqa_ism = min(students, key=lambda student : len(student['name']))['name']
print(eng_qisqa_ism)