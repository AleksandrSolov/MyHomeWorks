my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n_index = 0
while n_index <= len(my_list):
     if my_list[n_index] > 0:
          print(my_list[n_index])
     elif my_list[n_index] < 0:
          print('Программа завершена. Список вычитан до первого "минуса"')
          break
     n_index += 1
