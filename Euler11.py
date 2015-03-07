import numpy as np

numbers = np.random.randint(100, size=(5,5))

def find_array_combinations_4_numbers(num_array):
    '''For some 1 x n array, finds all of the 4 number combinations'''
    combinations = []
    (width, length) = num_array.shape
    print num_array.shape
    #the elements that are 4 x 1
    for i in range(length - 3):
        for j in range(width): 
            combinations.append(num_array[j,i:i+4])
    #The elements that are 1 x 4
    for k in range(length):
        for l in range(width - 3):
            combinations.append(num_array[l:l+4,k:k+1].reshape(1,4))
    return combinations
    

def find_adjacent_numbers(numbers):
    combinations = []
    (length, width) = numbers.shape
    combinations.append(find_array_combinations_4_numbers(numbers))
    #The diagonal elements
    diagonal_nums = []
    diagonal_nums.append(np.array(numbers.diagonal()).reshape(1,len(numbers.diagonal())))
    for k in range(1,width):
        if len(numbers.diagonal(k)) >= 4:         
            diagonal_nums.append(np.array(numbers.diagonal(k)).reshape(1,len(numbers.diagonal(k))))
        if len(numbers.diagonal(-k)) >= 4:
            diagonal_nums.append(np.array(numbers.diagonal(-k)).reshape(1,len(numbers.diagonal(-k))))
    for nums in diagonal_nums:
        combinations.append(find_array_combinations_4_numbers(nums))
    return combinations
