# find the numbers the factors
""""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def find_factors (n = 600851475143) :
    elements = []
    for i in range (2, 100000) :
        while n % i == 0 :
            elements.append(i)
            n /= i
            if n == 1 or n == i :
                return i



result = find_factors()
print result
