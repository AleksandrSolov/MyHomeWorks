# дополнительное задание
# "Слишком древний шифр"

number_list = [ i + 3 for i in range(18)]
first_list = [ i for i in range(21) if i > 0]
alt_first_list = first_list[:]

for row in number_list:
    parol = f'{row} '
    for i in first_list:
        for j in alt_first_list:
            element = i + j
            if row  % element == 0:
                result_ctr = parol.count(f'{j}{i}')
                if result_ctr > 0:
                    continue
                else:
                    parol += f'{i}{j}'
    print(parol)





