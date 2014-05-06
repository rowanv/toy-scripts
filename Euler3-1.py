#Euler Problem 3

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def prime_test(n):
    is_prime = True
    if n == 1:
        return True
    elif n == 2:
        return True
    for i in range(2, n-1):
        if n % i == 0:
            is_prime = False
    return is_prime

def prime_factors(n):
    l1 = []
    for i in factors(n):
        if prime_test(i)==True:
            l1.append(i)
    return l1

def largest_prime_factor(n):
    return max(prime_factors(n))

#print largest_prime_factor(600851475143)
#this is not really a good solution, takes too long
