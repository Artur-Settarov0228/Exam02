with open('Input/numbers.txt', 'r') as nums:
    numbers = [int(line.strip()) for line in nums if line.strip()]

total = sum(numbers)

with open('Output/output08.txt', 'w') as output:
    output.write(f"Yig'indi: {total}")
