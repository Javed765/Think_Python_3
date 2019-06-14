###############################################################################
### Chapter 6
###############################################################################

### Boolean functions
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False
    
is_divisible(1, 2)

# more compact form
def is_divisible_2(x, y):
    return x % y == 0

print(is_divisible_2(2,5))

# use of boolean with condition statements
def is_divisible_3(x, y):
    if is_divisible_2(x, y):
        print(x, "is divisible by", y)

# is_between function
def is_between(x, y, z):
    '''
    The function returns True if x <= y <= z or
    False otherwise.
    '''
    if x <= y and y <= z:
        return True
    else:
        return False

is_between(1, 2, 3)


### Further recursion
# factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorial(4)

# fibonacci with recurssion
def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(6)

### Checking types
# factorial 2.0
def factorial_2(n):
    if not isinstance(n, int):
        print('Factorial only defined for integer')
        return None
    elif n < 0:
        print('Factorial only defined for positive ineteger')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial_2(n - 1)

factorial_2(10)


### Exercises
# 6.2: The Ackermann function
def ack(m, n):
    if m == 0: 
        return n + 1
    elif m > 0 and n == 0:
        return ack(m -1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))

ack(3, 3)

# 6.3: Palindrome Word
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]
    
middle('abc')

'''
6.3(1)
Calling middle with a two letter string returns an empty string, similarly with
an empty string
'''

def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

is_palindrome('bob')


# Exercise 6.4
def is_power(a, b):
    if round(a % b) != 0:
        return False
    elif a / b == 1:
        return True
    else:
        a = a / b
        return is_power(a, b)
    
is_power(6.25,2.5)

# Exercise 6.5
def gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        print('gcd of', b, '&', r, 'is',  gcd(b, r))
        return gcd(b, r)

gcd(16, 0)



