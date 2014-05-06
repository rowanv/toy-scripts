import math
#Finds the largest fibonacci divisor for some number n


#This function finds the (num)^th term of the fibonacci sequence
def fibonacci(num):

    fib_list = [1, 1]
    
    for i in range(3,num+1):
        fib_list.append(fib_list[-1]+fib_list[-2])
        
    
    if num == 1:
        return 1
    elif num == 2:
        return 1
    elif num >= 3:
        return fib_list[-1]

#This function finds the factors of some number n
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


f1 = fibonacci(12)
print f1
factorsf1 = factors(f1)
print factorsf1
print len(factorsf1)

#This function tests the factors of some number for its first 1000 factors
#It prints all of the fibonacci factors
def factors_test():
    factorsf = []
    i = 3
    while len(factorsf) < 1000:
        i += 1
        f2 = fibonacci(i)
        factorsf = factors(f2)
    print "Factors:", len(factorsf), i, "Fib number", fibonacci(i)

print factors_test()
