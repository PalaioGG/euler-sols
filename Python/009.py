# Problem 9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# From mathsisfun.com:
#     a = n^2 - m^2
#     b = 2nm
#     c = n^2 + m^2

n = 2
m = 1

a, b, c = 1, 1, 1

while a + b + c != 1000:
    n += 1
    while m <= n:
        a = n**2 - m**2
        b = 2*n*m
        c = n**2 + m**2
        if a + b + c == 1000:
            break
        m += 1
    m = 1
print(a*b*c)
