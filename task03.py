def calculate_tax(salary):
    if salary > 5_000_000:
        soliq = salary * 0.20
    else:
        soliq=salary * 0.13
    return int(soliq)
    
def calculate_net_salary(salary): 
    soliq = calculate_tax(salary)
    net_salary = salary - soliq
    return int(net_salary)

salary = int(input("Miqdorni kiriting :"))
soliq = calculate_tax(salary)
net = calculate_net_salary(salary)


print(f"Soliq: {soliq:,}".replace(',', '_'))
print(f"Sof maosh: {net:,}".replace(',', '_'))