first = input('Введите число №1:   ')
second = input('Введите число №2:   ')
third = input('Введите число №3:   ')
if first == second and second == third:
    print('Количество равных чисел: 3' )
elif first == second or third == first or second == third:
    print('Количество равных чисел: 2')
else: print('Равных чисел нет. 0')