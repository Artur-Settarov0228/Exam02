with open('Input/numbers.txt' , 'r') as nums:
    numbers = [int(line.strip()) for line in nums if line.strip() ]
    tartiblash = sorted(numbers)

with open('Output/output10.txt' , 'w') as output:
    output.write(f"tartiblangan {tartiblash}")    