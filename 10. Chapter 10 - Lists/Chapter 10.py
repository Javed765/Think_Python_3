###############################################################################
### Chapter 9. Sets
###############################################################################

### 10.1 List is a sequence
cheese = ['Cheddar', 'Edam', 'Gouda']
for cheeses in cheese:
    print(cheeses)

number = [42, 123]
for i in range(len(number)):
    number[i] = number[i] * 2

number

# 10.4 List operation
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b

d = [0] * 4
d

[1, 2, 3] * 3

# 10.5 List Slices
t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3]
t[:4]
t[3:]

t[1:3] = ['x', 'y']
t[:]


# List methods
t = ['a', 'b', 'c']
t.append('d')
t = t[:3]
t.append('d')
t

''' extends takes a list as arguemnet '''
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
t2

t = ['d', 'c', 'e', 'b', 'a']

t.sort()

# 10.7 Map, filter and reduce
t = [1, 2, 3]
sum(t)

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

capitalize_all(t)

t = ['A', 'b', 'C', 'd', 'e', 'F']

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s.capitalize())
    return res

only_upper(t)

# 10.8 Deleting elements
# using pop
t = ['a', 'b', 'c']

x = t.pop(1)
x

# using del
t = ['a', 'b', 'c']

del t[1]
t

# using remove
t = ['a', 'b', 'c']

t.remove('a')
t

# deleting multiple elements
t = ['a', 'b', 'c', 'd', 'e', 'f']

del t[1:5]
t

#  10.9 Lists and strings
s = 'spam'

t = list (s)
t

s = 'pining for the fjords'
t = s.split()
t

s = 'spam-spam-spam'
delimiter = '-'

t = s.split('-')
t

t = ['pinning', 'for', 'the' ,'fjords']

delimeter = ' '
s = delimeter.join(t)
s

# 10.11 Aliasing
a = [1, 2, 3]
b = a

# then changes in either a or b will affect the other

b[0] = 42
a

# 10.13 Debugging

t = [1, 2, 3, 4]

t.extend(1)
t

t.pop()
t

t.append(5)
t

t.extend([10,100])
t

t.remove(10)

del t[len(t)-1]
t

### 10.15 Exercises

'''
Exercise 10.1. Write a function called nested_sum that takes a list of lists of
integers and adds up the elements from all of the nested lists. For example:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
'''
def nested_sum(t):
    accu = 0
    for i in range (len(t)):
        accu += sum(t[i])
    return accu

t = [[1, 2], [3], [4, 5, 6]]

def nested_sum_2(t):
    total = 0
    for nested in t:
        total += sum(nested)
    return total

t = [[1, 2], [3], [4, 5, 6]]
nested_sum_2(t)

'''
Exercise 10.2. Write a function called cumsum that takes a list of numbers and 
returns the cumulative sum; that is, a new list where the ith element is the 
sum of the first i + 1 elements from the original list. For example:
>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
'''
def cumsum(t):
    accu = 0
    s = []
    for i in range (len(t)):
        accu += t[i]
        s.append(accu)
    return s 

t = [1, 2, 3, 4, 5]
cumsum(t)

'''
Exercise 10.3. Write a function called middle that takes a list and returns a 
new list that contains all but the first and last elements. For example:
>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]
'''
def middle(t):
    return t[1:-1]
        
s = middle(t)
s

'''
Exercise 10.4. Write a function called chop that takes a list, modifies it by removing the first and
last elements, and returns None. For example:
>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]
'''
def chop(t):
    del t[0]
    del t[-1]
    
t = [1, 2, 3, 4, 5]
chop(t)
t


'''
Exercise 10.5. Write a function called is_sorted that takes a list as a
parameter and returns True 
if the list is sorted in ascending order and False otherwise. For example:
>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False
'''
def is_sorted(t):
    return t == sorted(t)

t = [1, 2, 2]
is_sorted(t)

'''
Two words are anagrams if you can rearrange the letters from one to spell the 
other. Write a function called is_anagram that takes two strings and returns 
True if they are anagrams.
'''
def is_anagram(word1,word2):
    return sorted(word1) == sorted(word2)

t = 'abcb'
s = 'dcba'

is_anagram(t,s)


'''
Exercise 10.7. Write a function called has_duplicates that takes a list and 
returns True if there is any element that appears more than once. It should not
modify the original list.
'''

def has_duplicates(t):
    s = sorted(t)
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            return True
        
t = [1, 2, 2]
has_duplicates(t)
    

def middle(t):
    return t[1:len(t)-1]

t = [1, 2, 3, 4]
middle(t)



























