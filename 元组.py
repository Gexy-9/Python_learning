#元组也是多个元素按照一定顺序构成的序列。
# 元组和列表的不同之处在于，元组是不可变类型
# 这就意味着元组类型的变量一旦定义，其中的元素不能再添加或删除
# 元素的值也不能修改

#tuple
#定义一个三元组
t1=(12,23,34)
#定义一个四元组
t2=('高心仪','18',True,'四川')

#class 'tuple'类型
print(type(t1))
print(type(t2))

#查看元组中元素数量
print(len(t1))

#索引运算
print(t2[3])
print(t2[-1])

#切片运算
print(t2[1:2:1])

#循环遍历
for elem in t2:
    print(elem)

#成员运算:判断True or False
print('高心仪' in t2)
print('18' in t2)

#拼接运算
t3=t1+t2
print(t3)

#比较运算

#n个元素表示n元组
#()表示空元组
#(元素一,)表示一元组，逗号不能少

t4=('hello')
print(type(t4))

t5=('hello',)
print(type(t5))

#打包和解包操作

#打包操作
#当我们把多个用逗号分隔的值赋给一个变量时，多个值会打包成一个元组类型
a=1,10,100
print(type(a))
print(a)

#解包操作
#当我们把一个元组赋值给多个变量时，元组会解包成多个值然后分别赋给对应的变量，如下面的代码所示。
i,j,k=a
print(i,j,k)
#若元素个数不对应就会出现异常
#为解决此问题，引入*号，当解决变量个数小于元素个数时，多余的元素打包给待*号的变量
a=1,10,100,1000,10000
i,j,*k=a
print(i,j,k)

i,*j,k=a
print(i,j,k)

#交换变量的值
a=1
b=2
c=3
#交换a,b
print(a,b)
a,b=b,a
print(a,b)

#交换a,b,c
print(a,b,c)
a,b,c=b,c,a
#让左侧等于右侧
print(a,b,c)





"""
元组是不可变类型，不可变类型更适合多线程环境，
因为它降低了并发访问变量的同步化开销。
关于这一点，我们会在后面讲解并发编程的时候跟大家一起探讨。

元组是不可变类型，
通常不可变类型在创建时间上优于对应的可变类型。
我们可以使用timeit模块的timeit函数来看看创建保存相同元素的元组和列表各自花费的时间，
timeit函数的number参数表示代码执行的次数。
下面的代码中，我们分别创建了保存1到9的整数的列表和元组，
每个操作执行10000000次，统计运行时间。
import timeit

print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))
"""
import timeit

print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))

#将元组转换为列表
infos=t1
print(list(infos))
t6=list(infos)

#将列表转换为元组
Frts=t6
print(tuple(Frts))