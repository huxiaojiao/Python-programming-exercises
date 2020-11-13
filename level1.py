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


'''Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books.
 But Python has a built-in document function for every built-in functions.
Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
And add document for your own function'''

# solution
# print(abs.__doc__)
# print(int.__doc__)
#print(input.__doc__)


# def new_add(x, y):
#     '''calculate the sum of two integers'''
#     return x + y
#
#
# print(new_add.__doc__)

'''Define a class, which have a class parameter and have a same instance parameter'''
# solution


# class People():
#     legs = 2
#
#     def __init__(self, legs=None):
#         self.legs = legs
#
#
# bob = People(1)
# print('bob has %s leg' % bob.legs)
#
# print(People.legs)

'''Define a function that can accept two strings as input and print the string with maximum length in console.
 If two strings have the same length, then the function should print al l strings line by line.
'''
# solution
# def print_line():
#     line1 = input()
#     line2 = input()
#     if len(line1) > len(line2):
#         print(line1)
#     elif len(line1) < len(line2):
#         print(line2)
#     else:
#         print(line1)
#         print(line2)
#
# print_line()

'''Define a function that can accept an integer number as input and print the 
"It is an even number" if the number is even, otherwise print "It is an odd number".
'''
# solution
# def even_or_odd(n):
#     if n % 2 == 0:
#         print('It is an even number')
#     else:
#         print('It is an odd number')
#
#
# even_or_odd(-9)

'''Define a function which can print a dictionary where the keys are numbers between 1 and 3 
(both included) and the values are square of keys.
'''
# solution
# def dic():
#     d = {}
#     for i in range(4):
#         d[i] = i ** 2
#     return d
# print(dic())

'''Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
 and the values are square of keys. The function should just print the values only.
'''

# solution
# def dic():
#     d = dict()
#     for i in range(21):
#         d[i] = i ** 2
#     for k,v in d.items():
#         print(v)
# dic()

'''Define a function which can generate and print a list where the values are square of numbers between 1 
and 20 (both included).
'''

# solution
# def generate_list():
#     l = [i ** 2 for i in range(21)]
#     print(l)
#
# generate_list()

'''With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line 
and the last half values in one line. 
'''
# solution
# t = (1,2,3,4,5,6,7,8,9,10)
# print(t[:5])
# print(t[5:])

'''Write a program to generate and print another tuple whose values are even numbers in the given 
tuple (1,2,3,4,5,6,7,8,9,10). 
'''
# solution
# t = (1,2,3,4,5,6,7,8,9,10)
# l = [i for i in t if i % 2 == 0]
# print(tuple(l))

'''Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes",
 otherwise print "No".'''
# solution
# s = input()
# if s in (['Yes','yes','YES']):
#     print('Yes')
# else:
#     print('No')

'''Write a program which can filter even numbers in a list by using filter function. 
The list is: [1,2,3,4,5,6,7,8,9,10].'''
# solution1
# def check_even(n):
#     return n % 2 == 0
# l = filter(check_even,[1,2,3,4,5,6,7,8,9,10])
# print(list(l))

# solution2
# li = [1,2,3,4,5,6,7,8,9,10]
# l = filter(lambda x: x % 2 == 0, li)
# print(list(l))

'''Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].'''
# li = [1,2,3,4,5,6,7,8,9,10]
# l = map(lambda x:x ** 2, li)
# print(list(l))

'''Write a program which can map() and filter() to make a list whose elements are square of even number 
in [1,2,3,4,5,6,7,8,9,10].
'''
# solution 先过滤，再map
# li = [1,2,3,4,5,6,7,8,9,10]
# l1 = list(filter(lambda x :x % 2 == 0,li))
# l = map(lambda x :x ** 2,l1)
# print(list(l))

'''Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).'''
# solution
# l = filter(lambda x: x % 2 == 0, range(1, 21)) # 为什么可以直接代表列表？
# print(list(l))

'''Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).'''
# solution
# l = map(lambda x: x ** 2, range(1, 21))
# print(list(l))

'''Please write assert statements to verify that every number in the list [2,4,6,8] is even.'''
# for i in [2, 4, 6, 8]:
#     assert i % 2 == 0


'''Please write a program which accepts basic mathematic expression from console and print the evaluation result.
Example:
If the following string is given as input to the program:  35+3
Then, the output of the program should be:  38
'''
# expression = input()
# print(eval(expression))


'''Please write a binary search function which searches an item in a sorted list. The function should return the index 
of element to be searched in the list.'''


# def f(l, k):
#     left = 0
#     right = (len(l) - 1)
#
#     while left <= right:
#         mid = (left + right) // 2   # 确定中间元素索引
#         if l[mid] > k:    # 如果要搜索的值位于中间元素的左侧，说明最右侧的元素范围缩小了
#             right = mid - 1  # 至少比中间元素值小于1
#         elif l[mid] < k:  # 如果要搜索的值位于中间元素的右侧，说明最左侧的元素范围缩小了
#             left = mid + 1  # 至少比中间元素值大于1
#         else:
#             return mid
#     return -1
#
# li = [2, 4, 6, 8, 19]
# print(f(li, 0))


'''Please generate a random float where the value is between 10 and 100 .'''
# import random
# s = random.random() * 100  # random.random()代表随机返回0到1之间的浮点数
# print(s)

'''Please generate a random float where the value is between 5 and 95 .'''
# import random
# s = random.random()
# print(s * 100 - 5)

'''Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.'''
# import random
# s = random.choice([x for x in range(11) if x % 2 == 0])
# print(s)