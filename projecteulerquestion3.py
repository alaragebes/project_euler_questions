# find the numbers the factors

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
