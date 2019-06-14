###############################################################################
### Chapter 9. String
###############################################################################

fin = open('G:\My Drive\Studies\Data Science\Python\Books\Think Python 2nd editon\9. Chapter 9 - case study word play\words.txt')

fin.readline()

fin.readline()

line = fin.readline()
word = line.strip()
print(word)

w = 'dfjn'

w.c

for line in fin:
    word
    

### 9.2 Exerclses
# Exercise 9.1
'''
Write a program that reads words.txt and prints only the words with more than 20
characters (not counting whitespace).
'''
fin = open('G:\My Drive\Studies\Data Science\Python\Books\Think Python 2nd editon\9. Chapter 9 - case study word play\words.txt')

for word in fin:
    if len(word) > 20:
        print(word)

# Exercises 9.2
'''
In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that
does not contain the letter “e”. Since “e” is the most common letter in 
English, that’s not easy to do.

Write a function called has_no_e that returns True if the given word doesn’t 
have the letter “e” in it.

Modify your program from the previous section to print only the words that 
have no “e” and compute the percentage of the words in the list that have no “e”.
'''
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

fin = open('G:\My Drive\Studies\Data Science\Python\Books\Think Python 2nd editon\9. Chapter 9 - case study word play\words.txt')
count = 0
count_no_e = 0
for word in fin:
    count += 1
    if has_no_e(word) == True:
        count_no_e += 1
        print(word)
print('Percentage', count_no_e/count * 100)
        
# Exercise 9.3
'''
Write a function named avoids that takes a word and a string of forbidden 
letters, and that returns True if the word doesn’t use any of the forbidden 
letters.

Modify your program to prompt the user to enter a string of forbidden letters
and then print the number of words that don’t contain any of them. Can you find
a combination of 5 forbidden letters that excludes the smallest number of words?
'''
def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
                return False
    return True

avoids('Letter', 'eab')

fin = open('G:\My Drive\Studies\Data Science\Python\Books\Think Python 2nd editon\9. Chapter 9 - case study word play\words.txt')

forbidden = input('> Type a word')

for word in fin:
    count += 1
    if avoids(word, forbidden) == True:
        print(word)


# Exercise 9.4
'''
Write a function named uses_only that takes a word and a string of letters, and
that returns True if the word contains only letters in the list. Can you make 
a sentence using only the letters acefhlo? Other than “Hoe alfalfa?”
'''
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True


# Exercise 9.5 
'''Write a function named uses_all that takes a word and a string of required 
letters, and that returns True if the word uses all the required letters at 
least once. How many words are there that use all the vowels aeiou? 
How about aeiouy?
'''
def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True


uses_all('jved', 'javed')

'''
Exercise 9.6. Write a function called is_abecedarian that returns True if the 
letters in a word appear in alphabetical order (double letters are ok). 
How many abecedarian words are there?
'''
def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

is_abecedarian('cba')

### using recursion
def is_abecedarian_r(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian_r(word[1:])
    
### using while loop
def is_abecedarian_w(word):
    i = 0
    while i < len(word) - 1:
        if word[i + 1] < word[i]:
            return False
        i += 1
    return True

is_abecedarian_w('abcd')

'''
Exercise 9.7. This question is based on a Puzzler that was broadcast on the 
radio program Car Talk (http: // www. cartalk. com/ content/ puzzlers ):
Give me a word with three consecutive double letters. I’ll give you a couple 
of words that almost qualify, but don’t. For example, the word committee, 
c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ that sneaks in there. 
Or Mississippi: M-i-s-s-i-s-s-ip-p-i. If you could take out those i’s it would 
work. But there is a word that has three consecutive pairs of letters and to 
the best of my knowledge this may be the only word. Of course there are 
probably 500 more but I can only think of one. What is the word? 
Write a program to find it. 
Solution: http: // thinkpython2. com/ code/ cartalk1. py .
'''
def find_double(word):
    for i in range(0, len(word)):
        if word[i] == word[i+1]:
            return word[i] + word[i+1]
        
def is_three_double(word):
    for letter in word:
            for i in range(0, len(word)):
                if word[i] == word[i+1]:
                    return word[i] + word[i+1]
                
find_double('bookkeeper')














