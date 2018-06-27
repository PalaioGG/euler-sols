# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
# Two Solutions: 1. Recursive function
#                2. While loop

number = 600851475143

# 1. Recursive function

# import sys
# sys.setrecursionlimit(7000) # default recursion limit == 2000. Seriously Python?!

# def factorization(number, divider):
#     if number <= 2:
#         print(number, divider)
#         return
#     if (number / divider) % 2 == 1.0:
#         factorization(number/divider, divider)
#     else:
#         factorization(number, divider + 1)
#
# factorization(number, 2)


# 2. While loop
divider = 2
while(number >= 2):
    if number/divider % 2 == 1.0:
        number /= divider
    else:
        divider += 1
print(divider)
