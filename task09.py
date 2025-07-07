with open('Input/numbers.txt' , 'r') as nums:
    numbers = [int(line.strip()) for line in nums if line.strip() ]
    max_son = max(numbers)

with open('Output/output09.txt' , 'w') as output:
    output.write(F"max son {max_son}")
