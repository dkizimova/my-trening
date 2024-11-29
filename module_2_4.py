numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
n = 0 # Проверямое число

primes = []
not_primes = []
i = 0
for i in range(len(numbers)):
    is_prime = True
    n = numbers[i]  # Проверямое число

    if n < 2:   # не 0 и не 1
        print(n, '- не простое и не сложное число')
        continue
    else:

        f = n ** (1 / 2)  # Корень квадратный из n
    for a in range(2, int(f + 1)):
        if n % a == 0:
            is_prime = False
            break

    if not (is_prime):
        not_primes.append(n)
    else:
        primes.append(n)
is_prime = True  # признак простого числа
print('Простые числа ', primes)
print('Составные числа', not_primes)
