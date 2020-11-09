'''Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24'''
# solution
# import math
# C = 50
# H = 30
# values = input().split(',')
# l = list()
# for i in values:
#     q = (2 * C * int(i)) / H
#     root = int(math.sqrt(q))
#     l.append(str(root))
# print(','.join(l))

'''Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] '''

# solution
# values = input().split(',')
# out_l = list()
# inner_l = list()
# for i in range(int(values[0])):
#     for j in range(int(values[1])):
#         inner_l.append(i * j)
#     out_l.append(inner_l)
#     inner_l = []
# print(out_l)

'''Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated 
sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''

# solution1
# values = input().split(',')
# sort_value = sorted(values)
# print(','.join(sort_value))

# solution2
# values = input().split(',')
# values.sort()
# print(','.join(values))

'''Write a program that accepts sequence of lines as input and prints the lines after making all characters in 
the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''
# solution
# l = []
# while True:
#     words = input()
#     if words:
#         l.append(words.upper())
#     else:
#         break
#
# for line in l:
#     print(line)

'''Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing 
all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world'''

# solution1 ：先去重，再排序
# values = input().split(' ')
# l = []
# for i in values:
#     if i not in l:
#         l.append(i)
# l.sort()
# print(' '.join(l))

# solution2
# s = input()
# words = [word for word in s.split(' ')]
# print(' '.join(sorted(set(words))))

'''Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check 
whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010'''

# solution
# values = input().split(',')
# l = [x for x in values if int(x, 2) % 5 == 0]
# print(','.join(l))

'''Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the
 number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.'''


# solution 2
# l = []
# for i in range(1000, 3001):
#     if int(str(i)[0]) % 2 == 0 and int(str(i)[1]) % 2 == 0 and int(str(i)[2]) % 2 == 0 and int(str(i)[3]) % 2 == 0:
#         l.append(str(i))
#
# print(','.join(l))

'''Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''

# solution
# d = {'Letters': 0, 'DIGITS': 0}
# value = input()
# for i in value:
#     if i.isalpha():
#         d['Letters'] += 1
#     elif i.isdigit():
#         d['DIGITS'] += 1
#     else:
#         pass
#
# print('LETTERS ' + str(d['Letters']))
# print('DIGITS ' + str(d['DIGITS']))

'''Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9'''

# solution
# value = input()
# d = {'UPPER CASE': 0 , 'LOWER CASE': 0}
# for i in value:
#     if i.isupper():
#         d['UPPER CASE'] += 1
#     elif i.islower():
#         d['LOWER CASE'] += 1
#     else:
#         pass
# print('UPPER CASE ', d['UPPER CASE'])
# print('LOWER CASE ', d['LOWER CASE'])

'''Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''
# solution
# value = input()
# total = int(value) + int(value * 2) + int(value * 3) + int(value * 4)
# print(total)

'''Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9'''

# solution
# values = input().split(',')
# l = [x for x in values if int(x) % 2 != 0]
# print(','.join(l))

'''Write a program that computes the net amount of a bank account based a transaction log from console input.
 The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500'''

# solution
# d = {'d': 0, 'w': 0}
# while True:
#     s = input()
#     if s:
#         num = int(s.split(' ')[1])
#         if 'D' in s:
#             d['d'] += num
#         elif 'W' in s:
#             d['w'] += num
#     else:
#         break
#
# print(d['d'] - d['w'])

'''A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1'''

# solution
# import re
# # re = re.match('[a-z]+[A-Z]+[0-9]+[$#@]+{6,19}')
# values = input().split(',')
# l = []
# for value in values:
#     if len(value) < 6 or len(value) > 12:
#         continue
#     else:
#         if not re.split('[a-z]', value):
#             continue
#         elif not re.search('[A-Z]', value):
#             continue
#         elif not re.search('[0-9]', value):
#             continue
#         elif not re.search('[$@#]', value):
#             pass
#         else:
#             l.append(value)
#
# print(','.join(l))

'''You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, 
age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]'''

# solution
# from operator import itemgetter
#
# l = []
# while True:
#     s = input()
#     if s:
#         l.append(tuple(s.split(',')))
#     else:
#         break
# print(sorted(l, key=itemgetter(0, 1, 2)))

'''Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.'''

# def putnumbers(n):
#     i = 0
#     while i<n:
#         j=i
#         i=i+1
#         if j%7==0:
#             yield j
#
#
# for i in putnumbers(100):
#     print(i)
