###############################################################################
### Chapter 7
###############################################################################

# The while statement
def counter_down(n):
    while n > 0:
        print(n)
        n = n- 1
    print('Blastoff')
    
counter_down(5)

def sequence(n):
    
# printing a string times with while statement
def print_n(s, n):
    while n > 0:
        print(s)
        n = n - 1

print_n('a', 5)


# using the break command
while True:
    line = input('> ')
    if line == 'done':
        break
    print (line)
    
print('Done!')


# Newton's Method to find squart root
a = 144
x = 3
while True:
    print(x)
    y = (x + a/x) / 2
    if y == x:
        break
    x = y
    

while True:
    print(x)
    y = (x + a/x) / 2
    if abs (y - x) < epsilon:
        break
    x = y 

### Exercises
# Exercise 7.1
def mysqrt(a, x):
    epsilon = 0.0000000000000001
    while True:
        y = (x + a/x) / 2
        if abs (y - x) < epsilon:
            break
        x = y 
    return x

import math 

def test_square_root():
    print('a  ', 'mysqrt(a)        ', 'math.sqrt(a)       ', 'diff         '  )
    print('-  ', '-' * 9, ' ' * 7, '-' * 12, ' ' * 5, '-' * 4)    
    for a in range (1,11):
        d = abs(mysqrt(a, 1) - math.sqrt(a))
        print(a, ' ', "{0:.15f}".format((mysqrt(a, x))), "{0:.15f}".format((math.sqrt(a))), d  )

    
test_square_root()


# Exercise 7.2
def eval_loop():
    result = None
    while True:
        line = input('>')
        if line == 'done':
            print('Done!')
            return result
            break
        result = eval(line)
        print(result)

eval_loop()


# Exercise 7.3
def estimate_pi():
    k = 0
    pi_inverse = 0
    
    c = (2 * math.sqrt(2)) / 9801
    epsilon = 1e-15
    
    while True:
        nominator = math.factorial(4 * k) * (1103 + 26390 * k)
        demoninator = math.factorial(k) ** 4 * 396 ** (4 * k)
        term = nominator / demoninator
        
        pi_inverse = pi_inverse + term
        
        if abs(term) < epsilon:
            break
        
        k += 1
    return (1 / (c * pi_inverse))

estimate_pi()
 













