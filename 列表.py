#列表,可以含重复元素
from Python311.Lib.random import Random

items1=[12,23,34,34,56,67]
#字符串列表
items2=['Chinese','math','English']
#混合列表
items3=[100,12.3,'Python',True]

#打印列表
print(items1)
print(items2)
print(items3)

#list类型
print(type(items1))
print(type(items2))
print(type(items3))

#list列表
items4=list(range(2,11))
items5=list('hello')
print(items4)
print(items5)

#list拼接
print(items4+items5)
#list倍乘
print(items5*3)

#list判断元素是否在列表中
print('h' in items5)
print('a' in items5)

items6=list(range(0,11))
print(items6[0],end='\t')
print(items6[-11])
print(items6[1],end='\t')
print(items6[-10])
print(items6[2],end='\t')
print(items6[-9])

#访问一定范围内的所有元素[start:end:stride]
#易混：其中，stride是指访问的元素之间位置间隔为stride
print(items5[0:5:1])
print(items5[-1:-5:-1])

#如果start=0，则可以省略
#如果end=N，也可以省略
#如果stride=1，也可以省略
#但是，两个冒号不能省略
print(items5[::2])

#修改元素操作
items5[1:2]=['a']
print(items5)

#列表之间还可以进行比较
#比较相不相同
#从头开始直到有不一样的

#列表的遍历
for index in range(len(items5)):
    print(items5[index])

for item in range(len(items3)):
    print(items3[item])

#方法二
for item in items3:
    print(item)

print()
for thing in items3:
    print(thing)


#添加和删除元素
#追加：append
#插入：insert
languages=['Python','C++','Java','Go','C#']
print(languages)

languages.append('JavaScript')
languages.append('C')
print(f'插入了两个元素：{languages}')
print()

languages.insert(2,'语言3')
print(f'在第三个位置（index为2）插入了语言3：{languages}')
print()

languages.remove('Python')
print(f'去掉了“Python”这个元素：{languages}')
print()

#pop可用于删除指定位置的元素（默认为末尾元素），并返回该元素
print(languages.pop())
print(languages)

#del关键字
del items5[4]
print(items5)


#查找元素位置
print(items5.index('a'))

#查找元素频次
print(items5.count('l'))

#元素排序
print(languages)
languages.sort()
print(languages)

#元素反转
languages.reverse()
print(languages)

#创建列表
items=[]

for i in range(1,12):
    items.append(i)
print(items)

nums1=[1,2,3,4,5]
nums2=[]

#**是幂次
for num in nums1:
    nums2.append(num**2)
print(nums2)

nums3=[num**2 for num in nums1]
print(nums3)

nums4=[num for num in nums1 if num>2]
print(nums4)

#嵌套列表
scores=[[90,90,90],[80,80,80],[70,70,70]]
print(scores)
print(scores[0])
print(scores[0][0])

"""
#列表的应用：彩票
import random
print("请您按照提示依次输入7个数")
guess=[]
for num in range(0,6):
    guess.append(int(input(f'请输入红球第{num+1}个数:')))
    while guess[num]<=0 or guess[num]>33:
        print("您输入的数字无效，请重新输入")
        guess[num]=int(input(f'请输入红球第{num+1}个数:'))

guess.sort()
guess.append(int(input('请输入篮球数字:')))
while guess[6] <= 0 or guess[6] > 33:
    print("您输入的数字无效，请重新输入")
    guess[6] = int(input('请输入蓝球数字:'))

result=[]
for num in range(0,6):
    result.append(random.randrange(1,34))

result.sort()
result.append(random.randrange(1,7))

flag=0
for num in range(0,7):
    if result[num]!=guess[num]:
        flag=1
if flag==0:
    print("恭喜中奖")
else:
    print("未中奖")
"""
#第三方库：rich
#作用：用最简单的方式产生最漂亮的输出
import random

from rich.console import Console
from rich.table import Table
#from prettytable import PrettyTable

#创建控制台
console=Console()


#创建表格
import random
#带表头
table=Table(show_header=True)

for Head_name in ('序号','红球','蓝球'):
    table.add_column(Head_name,justify='center')
    #表头内容居中对齐

n=int(input("生成几注号码："))

#分别生成数字列表
red_balls=[i for i in range(1,34)]
blue_balls=[i for i in range(1,17)]

print(type(red_balls))


for i in range(n):
    #从数字列表中随机挑选6个数字
    selected_balls=random.sample(red_balls,6)
    selected_balls.sort()
    blue_ball=random.choice(blue_balls)

    #向表格中添加行
    table.add_row(
        str(i+1),
        f'[red]{" ".join(f"{ball:0>2d}" for ball in selected_balls)}[/red]',
        f'[blue]{f"{blue_ball:0>2d}"}[/blue]'
    )

console.print(table)




"""
日志（Log）
日志处理器（Logging Handler）
Emoji 表情
表格（Tables）
进度条（Progress Bars）
状态动画（Status）
树（Tree）
列（Columns）
Markdown
语法高亮（Syntax Highlighting）
栈回溯信息（Tracebacks）
"""






