numbers = [
    {'value': 2}, 
    {'value': 3}, 
    {'value': 4}
]

kvadrat = list(map(lambda x : {'value': x['value'] ** 2} , numbers))
print(kvadrat)