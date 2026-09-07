#定义函数
#def function(arg1,arg2):
#    return 'Something'

#阶乘函数
def fac(num):
    if num==0:
        return 1
    else:
        return num*fac(num-1)

num=5
print(fac(num))

#Python 标准库的math模块中，已经有一个名为factorial的函数实现了求阶乘的功能
#我们可以直接用import math导入math模块
#然后使用math.factorial来调用求阶乘的函数
#也可以通过from math import factorial直接导入factorial函数来使用它

import math
print(math.factorial(num))

from math import factorial as fac
#导入时可以改写函数名以便后续使用简便
print(fac(num))

#强制位置参数:调用函数时只能按照参数位置来接收参数值的参数
def judge_make1(a,b,c,/):
    return True

print(judge_make1(1,2,3))

#命名关键字:只能通过“参数名=参数值”的方式来传递和接收参数
def judge_make2(*,a,b,c):
    return True

print(judge_make2(a=1,b=2,c=3))

#默认值
def add(a=0,b=0,c=0):
    return a+b+c
#带默认值的参数必须放在不带默认值的参数之后

#可变参数
#以团队协作的方式开发商业项目时，很有可能要设计函数给其他人使用，但有的时候我们并不知道函数的调用者会向该函数传入多少个参数，这个时候可变参数就能派上用场


# 用星号表达式来表示args可以接收0个或任意多个参数
# 调用函数时传入的n个参数会组装成一个n元组赋给args
# 如果一个参数都没有传入，那么args会是一个空元组
def Sum(*args):
    total=0
    for enum in args:
        if type(enum) in (int,float):
            total+=enum
    return total

#如果我们希望通过“参数名=参数值”的形式传入若干个参数，
#具体有多少个参数也是不确定的，
#我们还可以给函数添加可变关键字参数
# 把传入的关键字参数组装到一个字典中

def foo(*args,**kwargs):
    print(args)
    print(kwargs)
print("1")
#参数传入形式
foo(1,2,3,'Python','1234',45,name='高',age=18,hobby='王者荣耀')

print("1")
#用模块管理函数
#通过import关键字导入指定的模块再使用完全限定名（模块名.函数名）的调用方式
#可以区分到底要使用的是哪个模块中的foo函数
"""
import 字典
#会直接把字典.py文件运行一遍

print(字典.foo(6))

import 集合
print(集合.foo(6))
"""

#也会把未在类和其他函数里面的部分跑一遍
from 字典 import foo
print(foo(6))

#标准库中的模板和函数
"""
abs
bin:把一个整数转换为'0b'开头的二进制字符串
bin(123)='0b1111011'

chr:把Unicode编码转换为对应的字符

hex	将一个整数转换成以'0x'开头的十六进制字符串，例如：hex(123)会返回'0x7b'。
input	从输入中读取一行，返回读到的字符串。
len	获取字符串、列表等的长度。
max	返回多个参数或一个可迭代对象中的最大值，例如：max(12, 95, 37)会返回95。
min	返回多个参数或一个可迭代对象中的最小值，例如：min(12, 95, 37)会返回12。
oct	把一个整数转换成以'0o'开头的八进制字符串，例如：oct(123)会返回'0o173'。
open	打开一个文件并返回文件对象。
ord	将字符转换成对应的Unicode编码，例如：ord('€')会返回8364。
pow	求幂运算，例如：pow(2, 3)会返回8；pow(2, 0.5)会返回1.4142135623730951。
print	打印输出。
range	构造一个范围序列，例如：range(100)会产生0到99的整数序列。
round	按照指定的精度对数值进行四舍五入，例如：round(1.23456, 4)会返回1.2346。
sum	对一个序列中的项从左到右进行求和运算，例如：sum(range(1, 101))会返回5050。
type	返回对象的类型，例如：type(10)会返回int；而 type('hello')会返回str。

"""


#数据统计
import random
Data=[]
for i in range(1,11):
    Data.append(random.randrange(1,101))
print(Data)

def sam_mean(*data):
    sum_sam=0
    for i in range(0,len(Data)):
        sum_sam+=Data[i]
    return sum_sam/len(Data)

def sam_variance(*data):
    sum_sam=0
    for i in range(0,len(data)):
        sum_sam+=(Data[i]-sam_mean(*data))**2
    return sum_sam/(len(data)-1)

def sam_standard(*data):
    return math.sqrt(sam_variance(*data))

def sam_coefficient(*data):
    return math.sqrt(sam_standard(*data)/sam_mean(*data))

def calc(init_value,op_fun,*args,**kwargs):
    items=list(args)+list(kwargs.values())
    result=init_value
    for item in items:
        if type(item) in (int,float):
            result=op_fun(result,item)
    return result

import operator
print(calc(0,operator.add,1,2,3,4,5,name='高心仪',age=19))


#sorted函数从功能上来讲跟列表的sort方法没有区别，
#但它会返回排序后的列表对象，而不是直接修改原来的列表,
#这一点我们称为函数的无副作用设计，
#也就是说调用函数除了产生返回值以外，不会对程序的状态或外部环境产生任何其他的影响。

old_strings=['bear','pear','grape','apple','banana']
new_strings=sorted(old_strings,key=len)
print(new_strings)

#Lambda函数
#lambda 函数只能有一行代码，
#代码中的表达式产生的运算结果就是这个匿名函数的返回值。

#阶乘函数
def fac(num):
    if num==0:
        return 1
    else:
        return num*fac(num-1)

import functools
import operator
#可以用Lambda函数替换
fac2=lambda n:functools.reduce(operator.mul,range(2,n+1),1)

#偏函数是指固定函数的某些参数，生成一个新的函数，这样就无需在每次调用函数时都传递相同的参数。
import functools
#二进制
int2=functools.partial(int,base=2)
#八进制
int8=functools.partial(int,base=8)
#十六进制
int16=functools.partial(int,base=16)

print(int('1001'))
print(int2('1001'))
print(int8('1001'))
print(int16('1001'))

#函数高级应用
#装饰器本身是一个函数，它的参数是被装饰的函数，
#它的返回值是一个带有装饰功能的函数。
#装饰器是一个高阶函数，它的参数和返回值都是函数

import time


def record_time(func):
    def wrapper(*args, **kwargs):
        # 在执行被装饰的函数之前记录开始时间
        start = time.time()
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        # 返回被装饰函数的返回值
        return result

    return wrapper


