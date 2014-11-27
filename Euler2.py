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
    last_fib_number = 0
    sum1 = 0
    while last_fib_number < (4 * 10**6):
        last_fib_number = fibonacci(i)
        i+=1
        if last_fib_number % 2 == 0:
           sum1 += last_fib_number
    return sum1



print less_than_fib()
#4613732
