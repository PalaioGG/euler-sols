# Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import math

n = 1
count = 0

def isPrime(n):
    if n % math.sqrt(n) == 0:
        return False
    limit = int(math.sqrt(n)) + 1
    for i in range(2, limit):
        if n % i == 0:
            return False

    return True


while count < 10001:
    n += 1
    if isPrime(n):
        count += 1

print(count,'st prime number: ', n, sep='')
