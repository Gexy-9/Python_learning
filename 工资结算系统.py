#抽象类
from abc import ABCMeta,abstractmethod

class Employee(metaclass=ABCMeta):
    def __init__(self,name):
        self.namae=name

    @abstractmethod
    def get_salary(self):
        pass
    #这里暂且没办法实现

class Manager(Employee):
    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    def __init__(self,name,working_hours):
        super().__init__(name)
        self.working_hours=working_hours

    def get_salary(self):
        return 200*self.working_hours

class Salesman(Employee):
    def __init__(self,name,sales=0):
        super().__init__(name)
        self.sales=sales

    def get_salary(self):
        return 1800+self.sales*0.05

#isinstance函数：
#判断出一个对象是不是某个继承结构下的子类型，你可以简单的理解为type函数是对对象类型的精准匹配，而isinstance函数是对对象类型的模糊匹配。
somebodies=[Manager('刘备'),Programmer('诸葛亮',8),Salesman('司马懿',40)]
for somebody in somebodies:
    if isinstance(somebody,Programmer):
        print(somebody.working_hours)
