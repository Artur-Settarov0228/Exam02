students = {'Ali': 5, 'Vali': 4, 'Hasan': 5, 'Husan': 3}

total = sum(students.values())
count = len(students)
average = total / count

print(f"ortacha baxo {average}")

print("ortacha baldan yuqori olgan talabalar ")
for name , grade in students.items():
    if grade > average:
        print(f"{name}: {grade}")
