    # переменные
homework = 12
hour_works = 1.5
name_course = 'Python'
    # var1
print(f"Курс: {name_course}, всего задач:{homework}, затрачено часов: {hour_works}, среднее время выполнения " \
       f"{hour_works/homework} часа." )
    # var2
print('Курс: {}, всего задач:{}, затрачено часов: {}, среднее время выполнения {} часа.'.format(name_course, \
       homework, hour_works, hour_works/homework) )
