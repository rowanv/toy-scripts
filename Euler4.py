#Project Euler Problem 4

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers


#Reverses a number

def reverse(num1):
  '''int -> int
  reverses a number
  >>> reverse(1245)
  5421
  >>> reverse(6724)
  4276
  '''
  num1 = str(num1)
  num1 = num1[::-1]
  return(int(num1))

def is_palindrome(num1):
  '''int -> bool
  tests if a number is a palindrome, returns
  True or False
  >>> is_palindrome(1245)
  False
  >>> is_palindrome(456654)
  True
  '''
  flipnum = reverse(num1)
  return(flipnum == num1)

digit_3_num = range(900, 999)

#Create the list of multiples that we will be testing

multiples1 = []
for i in digit_3_num:
  for j in digit_3_num:
    multiples1.append(i*j)

print(multiples1)

#Descending order
multiples1.sort(reverse = True)

#Testing the multiples to see if they are palindromes
for i in multiples1:
  if is_palindrome(i) == True:
    print(i)

#Answer is 906609
