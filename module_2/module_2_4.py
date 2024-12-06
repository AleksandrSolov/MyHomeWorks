numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
copi_numbers = []
primes = []  #  простые числа
not_primes = []  # не простые числа

for i in numbers:
    if i > 1:
        copi_numbers.append(i)
print(copi_numbers)
a = 0
while a < len(copi_numbers):
    for i in range(2, (copi_numbers[a] // 2) + 1):
        if (copi_numbers[a] % i) == 0:
            not_primes.append(copi_numbers[a])
            break
    else:
        primes.append(copi_numbers[a])
    a +=1
print('Primes:', primes)
print('Not Primes:', not_primes)


