def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c = [1,2,3])

values_list = ['4-srik', 7, [3, 15]]
values_dict = {'a':9, 'b': 17, 'c':False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['two_strok', 11]
print_params(*values_list_2)
print_params(*values_list_2, 42)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
