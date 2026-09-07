#面向对象编程：
#把一组数据和处理数据的方法组成对象，
#把行为相同的对象归纳为类，
#通过封装隐藏对象的内部细节，
#通过继承实现类的特化和泛化，
#通过多态实现基于对象类型的动态分派。

#定义类
class Student:

    #__init__
    #调用Student类的构造器创建对象时，
    #首先会在内存中获得保存学生对象所需的内存空间，
    #然后通过自动执行__init__方法，完成对内存的初始化操作,
    #也就是把数据放到内存空间中。
    #所以我们可以通过给Student类添加__init__方法的方式为学生对象指定属性，
    #同时完成对属性赋初始值的操作,
    #正因如此，__init__方法通常也被称为初始化方法。
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #行为定义
    def study(self,course_name):
        print(f'学生正在学习{course_name}')

    def play(self):
        print(f'学生正在玩游戏')

#创建和使用对象
#并且完成初始化
stu1=Student('高心仪',18)
stu2=Student('骆昊',44)
print(stu1)
print(hex(id(stu1)))#地址

#第一种方法：
#用类名进行调用
Student.study(stu1,'Python程序设计')

#第二种方法：
#用对象进行调用
stu1.study('C++课程设计')


#封装：
#隐藏一切可以隐藏的实现细节，只向外界暴露简单的调用接口
#ex:时钟

import time

class Clock:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second

    def run(self):

        self.second+=1
        if self.second==60:
            self.second=0
            self.minute+=1
            if self.minute==60:
                self.hour+=1
                self.minute=0
                if self.hour==24:
                    self.hour=0

    def show(self):
        return f'{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}'


clock=Clock()

while True:
    clock.run()
    time.sleep(1)
    print(clock.show())
    break

#可见性和属性装饰器
#private
#protected
#public
#__name:表示一个私有属性
#_name:表示一个受保护属性

class Stu:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def study(self,course_name):
        print(f'{self.__name}正在学习{course_name}')


stu=Stu('张三',24)
stu.study('Python')
#print(stu.__name)
#此行会报错，因为__开头表明name属性是私有的
#AttributeError（属性错误）异常

#print(stu._Stu__name)
#这个仍然是可以的

#动态属性
#C、C++ 等语言则不属于动态语言。
#Python中可以给类添加属性
stu.sex='男'

#如果不希望在使用对象时动态的为对象添加属性，
#可以使用 Python 语言中的__slots__魔法。
#对于Student类来说，可以在类中指定__slots__ = ('name', 'age')
#要在def __init__函数前面加 __slots__ = ('name','age')

#除了对象方法之外，类中还可以有静态方法和类方法
#静态方法和类方法就是发送给类对象的消息。
#在对象构造完成之前用某种方法先检验所要构造的对象是否符合要求
#这类方法称为静态方法或类方法

#ex:
class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    #静态方法
    #在对象构造之时调用，若返回False，则对象构造失败
    @staticmethod
    def is_valid(a,b,c):
        return a+b>c and b+c>a and a+c>b

    #类方法
    @classmethod
    #多了个cls
    def is_valid2(cls,a,b,c):
        return a+b>c and b+c>a and a+c>b

    #计算周长
    def perimeter(self):
        return self.a+self.b+self.c

    #计算面积
    def area(self):
        p=self.perimeter()
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5

if Triangle.is_valid(3,4,5):
    t=Triangle(3,4,5)
    print(f'周长：{t.perimeter()}')
    print(f'面积：{t.area()}')
else:
    print('无效的边长')

#可以直接使用类名.方法名的方式来调用静态方法和类方法，
#二者的区别在于，类方法的第一个参数是类对象本身，
#而静态方法则没有这个参数。
#简单的总结一下，
#对象方法、类方法、静态方法都可以通过“类名.方法名”的方式来调用，
#区别在于方法的第一个参数到底是普通对象还是类对象，
#还是没有接受消息的对象。
#静态方法通常也可以直接写成一个独立的函数,
#因为它并没有跟特定的对象绑定。

"""
这里做一个补充说明，我们可以给上面计算三角形周长和面积的方法添加一个property装饰器（Python 内置类型），这样三角形类的perimeter和area就变成了两个属性，不再通过调用方法的方式来访问，而是用对象访问属性的方式直接获得，修改后的代码如下所示。

class Triangle(object):
   

    def __init__(self, a, b, c):
       
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
       
        return a + b > c and b + c > a and a + c > b

    @property
    def perimeter(self):
      
        return self.a + self.b + self.c

    @property
    def area(self):
      
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


if Triangle.is_valid(3, 4, 5):
    t = Triangle(3, 4, 5)
    print(f'周长: {t.perimeter}')
    print(f'面积: {t.area}')
else:
    print('无效的边长!!!')
"""

#继承和多态
class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def eat(self):
        print(f'{self.__name}正在吃饭')

    def drink(self):
        print(f'{self.__name}正在喝水')

#继承
class Teacher(Person):
    def __init__(self,name,age,wage):
        #super函数是 Python 内置函数中专门为获取当前对象的父类对象而设计的
        #调用父类的初始化方法
        super().__init__(name,age)
        self.wage=wage

    def eat(self):
        print(f'教师{self.__name}正在吃饭')

person=Person('人',18)
teacher=Teacher('诸葛亮',22,2)

person.eat()
#teacher.eat()




