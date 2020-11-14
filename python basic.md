提纲：random模块，map, filter,递归，generator,sorted,regex,sort,set
### python基础
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

3.dict.setdefault(key, default=None):跟上面的get方法类似，区别是当键不存在字典中时，会将键添加并将值设为defalut.

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

  ### 函数的高级特性

  * 生成器(generator):本质上一个可迭代对象，本身保留的是一种算法，可以通过for循环进行遍历

    1.创建一个生成器: 可以将列表生成式的 `[]`改为 `()`， 然后通过调用 `next` 函数进行遍历

  ```bash
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

  2. 

  