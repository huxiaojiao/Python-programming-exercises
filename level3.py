'''A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT
with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a
sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2'''

# solution
# import math
#
# point = [0, 0]
# while True:
#     trace = input()
#     if not trace:
#         break
#     trace_list = trace.split(' ')
#     operation = trace_list[0]
#     movement = int(trace_list[1])
#     if operation == 'UP':
#         point[1] += movement
#     elif operation == 'DOWN':
#         point[1] -= movement
#     elif operation == 'LEFT':
#         point[0] -= movement
#     elif operation == 'RIGHT':
#         point[0] += movement
#     else:
#         pass
# distance = round(math.sqrt(point[0] ** 2 + point[1]) ** 2)
# print(distance)

'''Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1'''

# solution 1
# d = dict()
# s = input().split(' ')
# for word in s:
#     if word not in d:
#         d[word] = 1
#     elif word in d:
#         d[word] += 1
#     else:
#         pass
# key = sorted(list(d.keys()))
# for k in key:
#     print(k + ':' + str(d[k]))

# solution 2
# d = {}
# s = input()
# for i in s.split():
#     d[i] = d.get(i, 0) + 1  # 返回键的值，如果键没有就返回默认值为键的值
#
# key = list(d.keys()) # 获取键列表
# key.sort() # 原地更改该列表的排序
#
# for k in key:
#     print('%s:%d' % (k, d[k]))

'''Define a class named American which has a static method called printNationality.'''
# class American():
#     @staticmethod
#     def printNationality():
#         print('American')
#
# a = American()
# a.printNationality()
# American.printNationality()

'''Define a class named American and its subclass NewYorker'''
# class American():
#     pass
# class NewYorker(American):
#     pass
#
# anAmerican = American()
# anNewYorker = NewYorker()
# print(anAmerican)
# print(anNewYorker)

'''Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.'''
# class Circle():
#     def __init__(self,r):
#         self.r = r
#
#     def area(self):
#         return self.r ** 2 * 3.14
#
# a = Circle(4)
# print(a.area())

'''Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.'''
# class Rectangle():
#     def __init__(self, length, width):
#         self.l = length
#         self.w = width
#
#     def area(self):
#         return self.l * self.w
#
# a = Rectangle(5, 9)
# print(a.area())

'''Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.'''
# class Shape():
#      def __init__(self):
#          pass
#      def area(self):
#          return 0
#
# class Square(Shape):
#     def __init__(self,l):
#         Shape.__init__(self)
#         self.length = l
#
#     def area(self):
#         return self.length * self.length
#
# b = Square(8)
# print(b.area())

'''Write a function to compute 5/0 and use try/except to catch the exceptions'''
# def f():
#     return 5 / 0
#
# try:
#     f()
# except ZeroDivisionError as e:
#     print('error:' + str(e))
# finally:
#     print('finished')

'''Define a custom exception class which takes a string message as attribute.'''
# class Exception_test():
#     def __init__(self, s):
#         self.message = s
#
# e = Exception_test('wrong type')
# print(e.message)

'''Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print 
the user name of a given email address. Both user names and company names are composed of letters only.'''
# solution1
# import re
# email = input()
# pat = r'^(\w+)@(\w+)$'
# r = re.match(pat, email)
# print(r.group(1))

# solution2
# s = input()
# e = s.split('@')[0]
# print(e)

'''Assuming that we have some email addresses in the "username@companyname.com" format, please write program to 
print the company name of a given email address. Both user names and company names are composed of letters only.'''
# import re
# s = input()
# pat = r'(\w+)@(\w+)(\.com)$'
# r = re.match(pat, s)
# print(r.group(2))

'''Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.'''
# 使用re.split()切割字符串, + 号表示至少1个，？ 号表示0个或1个，{n}表示n个，{n,m}表示n到m个，* 表示任意个
# solution1
# import re
# s = input()
# s1 = re.split(r'\s+', s)
# l = [i for i in s1 if re.match(r'\d', i)]
# print(l)

# solution2
# import re
# s = input()
# l = re.findall(r'\d+', s)
# print(l)

'''Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).'''
# solution 递归的特点:1.必须有一个明确的结束条件 2.每次进入更深一层递归时，计算量相比上一次递归应有所减少
# 3.递归次数过多会导致栈溢出

# def f(n):
#     if n == 1:
#         return float(n) / float(n+1)
#     s = float(n) / float(n+1) + f(n-1)
#     return round(s, 2)
# print(f(5))

# solution2
# s = input()
# sum = 0
# for i in range(int(s)+1):
#     sum += (float(i)/float(i+1))
# print(round(sum, 2))

'''Write a program to compute:f(n)=f(n-1)+100 when n>0 and f(0)=1 with a given n input by console (n>0).
Example:If the following n is given as input to the program:5. Then, the output of the program should be:501'''
# def f(n):
#     if n == 0:
#         return 1
#     return f(n-1) + 100
# s = input()
# print(f(int(s)))

'''The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.'''
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n > 1:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(7))

'''The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
Example:
If the following n is given as input to the program:7
Then, the output of the program should be:
0,1,1,2,3,5,8,13'''
# def fi(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return fi(n-1) + fi(n-2)
#
#
# s = input()
# l = [str(fi(i)) for i in range(int(s)+1)]
# print(','.join(l))

'''Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:   10
Then, the output of the program should be:  0,2,4,6,8,10'''
# 生成器：是一个可迭代对象，通常用for循环来迭代。


# def even(n):
#     i = 0
#     while i <= n:
#         if i % 2 == 0:
#             yield i
#         i += 1
#
#
# s = int(input())
# l = [str(i) for i in even(s)]
# print(','.join(l))

'''Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma 
separated form while n is input by console.
Example:
If the following n is given as input to the program:  100
Then, the output of the program should be:  0,35,70
'''
# def f(n):
#     i = 0
#     while i <=n:
#         if i % 5 == 0 and i % 7 == 0:
#             yield i
#         i += 1
#
#
# s = int(input())
# l = [str(x) for x in f(s)]
# print(','.join(l))

'''Please write a program which count and print the numbers of each character in a string input by console.
Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1'''

# s = input()
# d = {}
# for i in s:
#     d[i] = d.setdefault(i, 0) + 1
#
# for k, v in d.items():
#     print(k + ',' + str(v))



