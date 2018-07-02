# Problem 6
#
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 102 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

p = 100
sumsq = 0
sqsum = 0

for i in range(1, p+1):
    sumsq += i**2
    sqsum += i

print((sqsum**2) - sumsq)
