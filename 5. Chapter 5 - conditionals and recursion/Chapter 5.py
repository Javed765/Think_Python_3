###############################################################################
### Chapter 5
###############################################################################

## Recursion
def countdown(n):
    if n <= 0:
        print('it is over')
    else:
        print(n)
        countdown(n-1)
countdown(3)


## Input 
n = input("Insert an integer please  \n")
print(n)


## Exercises
# 5.2(i)
import math
def power_of(x, n):
     return round(math.exp(n * math.log (x)))

def check_fermat(a, b, c, n):
    LHS = power_of(a, n) + power_of(b, n)
    RHS = power_of(c, n)
    if LHS != RHS:
        print('No, that doesn’t work.')
    else:
        print('Holy smokes, Fermat was wrong')
        
check_fermat(3, 4, 5, 3)

# 5.2(ii)
def check_fermat_2():
    a = int(input('Enter the value of a \n'))
    b = int(input('Enter the value of b \n'))
    c = int(input('Enter the value of c \n'))
    n = int(input('Enter the value of n \n'))
    check_fermat(a, b, c, n)
    
check_fermat_2()

# 5.3(i)
def is_triangle(a, b, c):
    if a > (b + c) or b > (a + c) or c > (a + b):
        print('No')
    elif a == (b + c) or b == (a + c) or c == (a + b):
        print('Degenerate triangle')
    else:
        print('Yes')

is_triangle(1,1,1)

# 5.3(ii)
def is_triangle_2():
    a = float(input('Enter the value of a \n'))
    b = float(input('Enter the value of b \n'))
    c = float(input('Enter the value of c \n'))
    is_triangle(a, b, c)

is_triangle_2()


# 5.4(i)
# output will be 6
def recurse(n, s):
    print(s)
    if n == 0:
        print('final s = ', s)
    else:
        recurse(n-1, n + s)

recurse(4, 10)

# with recurse(-1, 0), the function will be an infinite recursion

# docstring
'''
This function sum the positive integers upto n and adds s to it. 
'''















