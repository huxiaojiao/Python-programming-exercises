提纲：random模块，map, filter,递归，generator,sorted,regex,sort,set

itertools.permutation,列表切片，timeit.Timer,zlib.compress,

1.python2有range和xrange,这两个有什么区别？

2.print(int('111',2))的结果是？7

3.在python中如何获取命令行参数？argv

4.test={{'name':'tom', 'salary':20000}, {'name':'jack', 'salary':15000}, {'name':'liming', 'salary':10000}}

根据salary由大到小排序

5.python中id,is,=,==分别是比较什么的？id函数用来获取对象的内存地址，is是内存地址是否相等的比较，==是值是否相等的比较

6.f.write('hello'),hello 是写进了文件还是只是存在内存当中？如何使写的内容主动存储到文件中？

7.流程控制当中：pass, continue,break ,exit分别是什么作用？

8.python当中的赋值，浅拷贝，深拷贝有什么区别？

9.python中的可变数据类型有哪些？为啥叫可变数据类型？

10.python中lambda,map,filter,reduce这些内置函数的作用？利用这些函数，找出1到100中所有的奇数



### python基础

* 切片

  1.列表的切片：方便获取指定索引范围内的列表片段。在列表中第一个数的索引值是0，最后一个数的索引值是-1.
  
  注：正向索引值 - 列表长度值 = 反向索引值

```bash
>>> l = list(range(100)) #创建一个列表
>>> l[:10] # 取前10个数字，如果第一个索引是0可省略。表示从索引0开始取，直到索引10为止，但不包括索引10
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l[-10:] # 取后10个数字，同样如果最后一个索引是-1也可省略。
[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> l[:10:2] # 前10个数，每2个取1个
[0, 2, 4, 6, 8]
>>> l[-90:-101:-1] # 前11个数，倒序排列，步长使用负数
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> l[:] # 复制一个列表，前后索引都可省略
[0, 1, 2, 3, ..., 99]
```

2. 元组的切片：规则同列表，只不过得到的结果还是元组

3. 字符串的切片：字符串也可以看成是一种list,每个元素就是一个字符。

```
>>> 'abcdefg'[:3]
'abc'
>>> 'abcdefg'[::2]
'aceg'
```

示例：利用切片操作，实现一个trim函数，可以去除字符串首尾的空格

```python
def trim(s):
    if len(s) == 0: #注意考虑异常情况
        return s
    while s[0] == ' ':
        s = s[1:]
    while s[-1] == ' ':
        s = s[:-1]
    return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
    
测试成功！
```



- 字典：实际上是builtins.py文件里的一个类dict
1. 生成空字典实例对象
`d = {}` 或  `d = dict()`

  2.dict.get(key, default=None):  该方法返回指定键的值，如果键不在字典则返回默认值。default是默认参数，值为 None，未传特定值时在交互模式下不会有结果。

```bash
>>> d = {}
>>> d.get('5',-1) 
>>> d
>>> -1
```

3.dict.setdefault(key, default=None):跟上面的get方法类似，区别是当键不存在字典中时，会将键添加并将值设为default.

```bash
>>> d = {}
>>> d.setdefault('t')
>>> d
{'t':None}
```

4.dict.keys():返回一个dict_keys()对象

```bash
>>> d = {'name':'anna', 'age':10, 'height':190}
>>> d.keys()
dict_keys(['name', 'age', 'height'])
>>> list(d.keys())
['name', 'age', 'height']

```

5.dict.values():返回一个dict_values()对象

```bash
>>> d = {'name':'anna', 'age':10, 'height':190}
>>> d.values()
dict_values(['anna', 10, 190])
>>> list(d.values())
['anna', 10, 190]
```

6.dict.items():返回一个dict_items()对象

```bash
>>> d = {'name':'anna', 'age':10, 'height':190}
>>> d.items()
dict_items([('name', 'anna'), ('age', 10), ('height', 190)])
>>> list(d.items())
[('name', 'anna'), ('age', 10), ('height', 190)]
```

* 集合：是builtins.py文件里的一个类set，跟字典类似也是一组键的集合，并且键不能是可变对象，区别是它不存储键值，而且集合里不存在重复的键。

  1.要创建一个set，需要提供一个list作为输入集合

  ```bash
  >>> s = set([2,4,5,4,6,7])
  >>> s
  {2, 4, 5, 6, 7}
  ```

  2.接上面的交互，可以往集合中添加或移除元素，如果重复添加会自动过滤不会产生效果

  ```bash
  >>> s.add(8)
  >>> s
  {2, 4, 5, 6, 7, 8}
  >>> s.add(8)
  >>> s
  {2, 4, 5, 6, 7, 8}
  >>> s.remove(2)
  >>> s
  {4, 5, 6, 7, 8}
  ```

  3. 集合求交集和并集

  ```python
  >>> s1 = set([1,3,5,7])
  >> s2 = set([2,4,5,7])
  >> s1 & s2
  >> {5,7}
  >> s1 | s2
  >>> {1, 2, 3, 4, 5, 7}
  ```

  ### 函数的高级特性

  * 匿名函数：`lambda x:x *x`，等同于

    ```python
    def f(x):
    	return x * x
    ```

    冒号前的 `x` 表示函数参数，冒号后只能有一个表达式，不用写`return`，返回值就是该表达式的结果。使用匿名函数的好处是不必担心函数名冲突，因为匿名函数没有名字。

    

  * 列表生成式（list comprehension）：是python里面内置的简单却又强大的创建列表的生成式，基本格式是`[表达式 for 变量 in 列表 筛选条件]`

    1.if ... else在for 前面：for前面的部分都是表达式，如果有if就一定要有else，否则会会报错。这是因为必须根据这个表达式算出一个结果，如果没有else判断不出来

  ```python
    >>> [x if x % 2 == 0 else -x for x in range(1,11)]
  [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
    
  ```

    2.if在for后面：for后面的部分就是筛选条件，如果有if就不能带有else，因为条件只能给定一种情况
      
    ```python
    >>> [x for x in range(1,11) if x % 2 == 0]
  [2, 4, 6, 8, 10]
    ```

  

  * 生成器(generator):本质上是一个可迭代对象，本身保留的是一种算法

    1.创建一个生成器: 可以将列表生成式的 `[]`改为 `()`， 然后通过调用 `next` 函数进行遍历

  ```python
  >>> g = (x for x in range(3))
  >>> g
  <generator object <genexpr> at 0x0000019FA0750448>
  >>> next(g, 'no value')
  0
  >>> next(g, 'no value')
  1
  >>> next(g, 'no value')
  2
  >>> next(g, 'no value')
  'no value'
  ```

  2. 函数中包含yield关键字

     如， 以下是斐波那契数列函数

     ```python
     def fib(max):
         n, a, b = 0, 0 ,1
         while n < max:
             print(b)
             a , b = b, a + b
             n += 1
           
     ```

     将其改为生成器，然后通过for循环进行遍历

     ```python
     >>> def fib(max):
         ...    n, a, b = 0, 0, 1
         ...    while n < max:
         ...       yield b
         ...        a, b = b, a + b
         ...        n += 1
         ...
     ```

      ```python
     >>> fib(6)
     <generator object fib at 0x0000028B428B06C8>
     >>> for n in fib(6)
     ...    print(n)
     ...
     1
     1
     2
     3
     5
     8
     >>>
     
      ```

     通过上述例子，可以知道函数和生成器的区别：函数是顺序执行的，遇到return语句或者最后一行语句就返回，而变成生成器的函数在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
     
     

  ### 高级函数

  * sorted()函数：是python内置函数，可以对所有的可迭代序列进行排序，默认是按照ASCII的大小比较，升序排列，即有个参数`reverse`默认值是`False`。

  ```python
  >>> sorted([3,5,2,9])
  [2, 3, 5, 9]
  >>> sorted(['Bob','anna','cindy','Tina'])
  ['Bob', 'Tina', 'anna', 'cindy'] # 默认大写字母排在小写字母前面
  ```

  同时也可以接收一个`key`函数来实现自定义的排序，如

  ```python
  >>> sorted([36, 5, -12, 9, -21], key=abs) # 注意函数名后面不能有括号，否则就变成了调用
  [5, 9, -12, -21, 36] 
  >>> sorted(['Bob','anna','cindy','Tina'],key=str.lower)
  ['anna', 'Bob', 'cindy', 'Tina']
  ```

  对字典进行排序，如将下面的数据按照salary从大到小排序

  ```python
  test= [{'name':'tom', 'salary':20000}, {'name':'jack', 'salary':1500}, {'name':'liming', 'salary':10000}]
  
  def by_salary(d):
  	return d['salary']
  	
  print(sorted(test,key=by_salary,reverse=True)) # 倒序排列需要更改reverse参数值
  
  或
  print(sorted(test,lambda d: d['salary'],revers=True)) # 可以使用匿名函数
  ```

  输出：`[{'name': 'tom', 'salary': 20000}, {'name': 'liming', 'salary': 10000}, {'name': 'jack', 'salary': 1500}]`

  

  * filter(): 是python的內建函数，接收一个函数和一个序列，把传入的函数依次作用于每个元素，然后根据返回值是`True`还是`False`决定保留还是丢弃该元素。如

    ```python
    >>> l = list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6,7,8,9,10])) # 筛选偶数
    >>> l
    [2, 4, 6, 8, 10]
    ```

  

  * map(): 是python的內建函数，也接收一个函数和一个序列，把传入的函数依次作用于每个元素，返回一个`Iterator`，需要再通过`list()`函数把整个序列都计算出来并返回一个列表。如

    ```python
    >>> l = list(map(str,[1,2,3,4,5])) # 将每个元素转换为字符串
    >>>l
    ['1', '2', '3', '4', '5']
    ```


  ### 常用模块

  * random

    1. random.random(a,b): 返回一个范围内的随机数整数，不包括右区间值，如

       ```python
       >>> random.randrange(1,10) # 不包括10
       5
       >>> ramdom.randrange(1,10,2) # 第3个参数代表步长，代表只能返回该范围内特定的值
       4
       ```

    2. random.randint(a,b): 返回一个范围内的随机数整数，包括右区间值，如

       ```python
       >>> random.randint(10) # 包括10
       10
       ```

    3. random.random(): 返回[0,1)范围内随机浮点数，不包括1，如

       ```python
       >>> random.random()
       0.36106451823280206
       ```

    4. ramdom.sample(sequence, k): 从指定序列中获取指定长度的片段并随机排列，该函数不会改变原有序列， 如

       ```python
       >>> random.sample('i like you', 2)
       ['k', 'i']
       >>> random.sample([2,3,6,1,6,7,8], 4)
       [2, 1, 3, 6]
       >>> random.sample(list({'name':'hu', 'age':9, 'height':150}), 2)
       ['height', 'age']
       ```

    5. random.choice(sequence): 从序列中获取一个随机元素，如

       ```python
       >>> random.choice([2,4,5,6])
       2
       >>> random.choice('love')
       'o' 
       ```

       6.random.shuffle(sequence): 用于将一个列表中的元素打乱，即将列表内的元素随机排列。如

       ```python
       >>> l = [1,3,2,4,5,6,7,0]
       >>> random.shuffle(l)
       >>> l
       [3, 1, 7, 2, 4, 0, 6, 5]
       ```

       

