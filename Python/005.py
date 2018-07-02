# Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


n = 2520
i = 1

while i < 20:
    if n % i == 0:
        i += 1
    else:
        i = 1
        n += 2520
print(n)
