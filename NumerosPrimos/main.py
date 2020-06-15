import math

list_of_primes = [2]

for number in range(3, 1000000, 2):
    for last_prime in range(3, round(math.sqrt(number)), 2):
        if number % last_prime != 0:
            continue
        else:
            break
    else:
        list_of_primes.append(number)

print(list_of_primes)
