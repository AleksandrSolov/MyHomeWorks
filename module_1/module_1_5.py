immutable_var = (1, 2, [3, 4], 'apple', 'banana', 'cherry', 'kiwi', 'swity')
print(immutable_var, type(immutable_var))
print(immutable_var[1], type(immutable_var[1]))
print(immutable_var[2], type(immutable_var[2]))
# immutable_var[1] = 17  #=> TypeError: 'tuple' object does not support item assignment
print(immutable_var)
# immutable_var[1][0] = 27 #=> TypeError: 'int' object does not support item assignment
print(immutable_var)
immutable_var[2][0] = 16
print(immutable_var)
mutable_list = ([3, 4, 'apple', 'banana', 'cherry', 'kiwi', 'swity'])
print(mutable_list)
mutable_list[2] = 'морковка'
mutable_list[1] = 7
print(mutable_list)
mutable_list[3:5] = ['fruits']*5
print(mutable_list)