
def calculate_structure_sum(element):
    global summa
    for item in element:
        if isinstance(item, int | float):
            summa += item
        elif isinstance(item, str):
            summa += len(item)
        elif isinstance(item, list | set | tuple):
            calculate_structure_sum(item)
        elif isinstance(item, dict):
            calculate_structure_sum(item.items())
    return  summa

summa = 0
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

#99