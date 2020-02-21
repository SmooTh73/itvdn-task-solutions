import math
def prime_numbers(n):     # n - число, до которого хотим найти простые числа 
    sieve = list(range(n + 1))
    sieve[1] = 0    # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    for number in sieve:
        if number != 0:
            yield number


n = 1000