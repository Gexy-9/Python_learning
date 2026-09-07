#键值对
person1={
    'name':'高心仪',
    'age':18,
    'height':160,
    'addr':'四川',
    'number':'18784438619'
}
print(person1)

# dict函数(构造器)中的每一组参数就是字典中的一组键值对
person2=dict(name='小王',age=19,height=170,addr='沈阳',number='13568257576')
print(person2)

# 可以通过Python内置函数zip压缩两个序列并创建字典
items1=dict(zip('Chinese','math'))#前后互相对应形成键值对
print(items1)

items2=dict(zip(items1,range(1,10)))
print(items2)

#遍历字典
for key in person1:
    print(key)


person3 = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': ['成都市武侯区科华北路62号1栋101', '北京市西城区百万庄大街1号'],
    'car': {
        'brand': 'BMW X7',
        'maxSpeed': '250',
        'length': 5170,
        'width': 2000,
        'height': 1835,
        'displacement': 3.0
    }
}
print(person3)

print(person3['name'])
person3['age']=18
print(person3)

for key in person3:
    print(f'{key}:\t{person3[key]}')

print(person3.get('name'))

print(person3.keys())

print(person3.values())

print(person3.items())

for key,value in person3.items():
    print(f'{key}\t{value}')

#合并操作
person1.update(person3)
#若有相同的键，对应的值会被person3中的值更新
person1 |= person3
#其他表达方式
print(person1)

#可以通过pop或popitem方法从字典中删除元素
#前者会返回（获得）键对应的值
#但是如果字典中不存在指定的键，会引发KeyError错误
#后者在删除元素时，会返回（获得）键和值组成的二元组
#字典的clear方法会清空字典中所有的键值对
print(person1.pop('age'))
#把最后一个删了
print(person1.popitem())
print(person1)

del person1['addr']
print(person1)

#字典是一种非常有利于数据检索的数据类型
#但是字典中的键必须是不可变类型
#列表、集合、字典等类型的数据都不能作为字典的键

def foo(num):
    return num*3