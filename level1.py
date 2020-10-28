'''Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.'''

# solution 1
# a = []
# for i in range(2000, 3201):
#     if i % 7 == 0 and i % 5 != 0:
#         a.append(str(i))
# print(','.join(a))

'''Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320'''


# n = int(input())
# # solution 1
#
#
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
#
#
# print(factorial(n))
#
# # solution 2
# s = 1
# for i in range(1, n+1):
#     s = s * i
# print(s)


'''With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an 
integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}'''

# solution
# n = int(input())
# d = dict()
# for i in range(1, n+1):
#     d[i] = i * i
# print(d)

'''Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')'''
# solution
# n = input()
# l = n.split(',')
# print(l)
# print(tuple(l))

'''Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.'''
# solution


# class TestString():
#     def __init__(self):
#         self.s = ""
#
#     def get_string(self):
#         self.s = input()
#
#     def print_string(self):
#         print(self.s.upper())
#
# strobject = TestString()
# strobject.get_string()
# strobject.print_string()