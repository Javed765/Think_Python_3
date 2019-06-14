###############################################################################
### Chapter 8. String
###############################################################################

# The len function
fruit  = 'banana'
len(fruit)


# 8.3 Traversal with a for loop
for letter in fruit:
    print(letter)

index = 0
while index < len(fruit):
    print(fruit[index])
    index += 1

# printing in reverse order
index = len(fruit) - 1
while index >= 0:
    print(fruit[index])
    index -= 1

# Concatenation - string addition
'''
The following example shows how to use concatenation (string addition) and a 
for loop to generate an abecedarian series (that is, in alphabetical order). 
In Robert McCloskey’s book MakeWay for Ducklings, the names of the ducklings 
are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. This loop outputs 
these names in order
'''
prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter + 'u' + suffix)
    else: 
        print(letter + suffix)

# 8.4 String slices
s = 'Monty Python'
s[0:5]
s[6:12]

s[:]

# 8.6 Searching
'''
Searching the index position of a string
'''
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        else:
            index += 1
    return -1
    
find('Monty Python', 'P')

def find_2(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        else:
            index += 1
    return -1

find_2('Monty Python', 'P', 5)


# 8.7 Looping and counting
def count_letter(word, letter):
    count = 0
    for i in word:
        if i == letter:
            count = count + 1
    print(count)

count_letter('Monty Python', 'o')


# 8.8 String methods
word = 'banana'
new_word = word.upper()
index = word.find('a')
word.find('na',3)


def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1
    
    while j >= 0:
        print(i, j)
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
    return True

is_reverse('pots', 'stop')


word = 'banana'
word.capitalize()
word.casefold()


### 8.13 Exercises
# 8.2
word = 'banana'
word.count('a')

# 8.3 
def is_palindrome(word):
    if word[:] == word[::-1]:
        return True
    return False

is_palindrome('noon')

# 8.4
'''
any_lowercase1(s) - only checks the first character in the string

'''
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
    
any_lowercase1('BoB')

'''
any_lowercase2 -only checks if the string 'c' is lower case and ignores the
the string s
'''
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

any_lowercase2('d')

'''
any_lowercase3 - will only return the last the case of the last character
'''
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

any_lowercase3('ooP')

'''
any_lowercase4 - works
'''
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
        print(flag)
    return flag

any_lowercase4('BbBB')

'''
any_lowercase4 - having the key word not implies the function is checking for
not True which equals Flase, i.e., the function is checking for uppercases
'''
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return True
    return False

any_lowercase5('bb')


# Exercise 8.5
def rotate_letter(letter, n):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter
    
    c = ord(letter) - start
    i = (c + n) % 26 + start
    
    return chr(i)
    
    
def rotate_word(word, n):
    result = ''
    for letter in word:
        result += rotate_letter(letter, n)
    return result
    
