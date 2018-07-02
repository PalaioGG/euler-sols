# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

import math

n = 3
sum = 2

def isPrime(n):
    if n % math.sqrt(n) == 0:
        return False
    limit = int(math.sqrt(n)) + 1
    for i in range(2, limit):
        if n % i == 0:
            return False

    return True


while n < 2000000:
    if isPrime(n):
        sum += n
    n += 2
print(sum)
