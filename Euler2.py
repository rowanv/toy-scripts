#Euler Problem 2

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms

def fibonacci(num):
    #yields the (num)^th term of the fibonacci sequence
    fib_list = [1, 1]
    
    for i in range(3,num+1):
        fib_list.append(fib_list[-1]+fib_list[-2])
        
    
    if num == 1:
        return 1
    elif num == 2:
        return 1
    elif num >= 3:
        return fib_list[-1]


def less_than_fib():
    i = 1
    fib1 = 0
    sum1 = 0
    while fib1 < (4 * 10**9):
        fib1 = fibonacci(i)
        i+=1
        if fib1 % 2 == 0:
           sum1 += fib1
    return sum1

print less_than_fib()
