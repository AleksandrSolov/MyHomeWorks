grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)
q = len(students)
a = 0
dict_students = {}
while a < len(students):
    # dict_students = dict([(sorted_students[a], sum(grades[a])/len(grades[a]))])
    dict_students[sorted_students[a]] = sum(grades[a])/len(grades[a])
    a = a + 1
    pass
print(dict_students)

