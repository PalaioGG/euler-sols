# Problem 4
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def palindrome(n):
    n = str(n)
    validated = 0
    for k in range(len(n)):
        if n[k] == n[len(n)-1-k]:
            validated += True
        else:
            validated += False
    return True if validated == len(n) else False

def product():
    for i in range(999, 900, -1):
        for j in range(999, 900, -1):
            n = i * j
            if palindrome(n):
                return n

print(product())
