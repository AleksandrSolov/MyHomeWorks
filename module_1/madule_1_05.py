surname = input("Введите Вашу фамилию: ")
name = input("Введите Ваше имя: ")
patronymic = input("Введите Ваше отчество: ")
my_string = (f" {surname}" + f" {name}" + f" {patronymic}")
print("Здравствуйте,", my_string )
print(len(my_string))
print(my_string.upper())
print(my_string.lower())
my_string = my_string.replace(' ', '')
print(my_string[0])
print(my_string[-1])
