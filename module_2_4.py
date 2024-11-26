primes = []
not_primes = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in numbers:
    for j in range(1, 15):
        a = f'{i}//{j}={i // j}'
        print(a)
        if i > 1 and (i % 2 != 0 or i == 2) and (i % 3 != 0 or i == 3):
            primes.append(i)
            break
        else:
            not_primes.append(i)
            break
print(not_primes)
print(primes)
