#集合并不支持索引运算
#集合的互异性决定了集合中不能有重复元素
#集合类型必然是支持in和not in成员运算的，这样就可以确定一个元素是否属于集合
#集合的成员运算在性能上要优于列表的成员运算
#集合底层使用了哈希存储（散列存储）

#创建集合
set1={1,2,3,4,5,6}

set2={'a','b','c','d'}

#利用set函数进行创建，并自动去重
set3=set('hello')

set4=set([1,2,2,3,4,5])

set5={num for num in range(0,20) if num%3==0}

print(set1)
print(set2)
print(set3)
print(set4)
print(set5)

# 集合中的元素必须是hashable类型
# 所谓hashable类型指的是能够计算出哈希码的数据类型
# 通常不可变类型都是hashable类型
# 如整数（int）、浮点小数（float）、布尔值（bool）、字符串（str）、元组（tuple）等
# 可变类型都不是hashable类型
# 因为可变类型无法计算出确定的哈希码，所以它们不能放到集合中。
# 例如：我们不能将列表作为集合中的元素；
# 同理，由于集合本身也是可变类型，所以集合也不能作为集合中的元素。
# 我们可以创建出嵌套列表（列表的元素也是列表），但是我们不能创建出嵌套的集合

#元素遍历
#集合运算
#成员运算

#二元运算
set1={1,2,3,4,5,6}
set2={2,6,7,8,9,0}

#交集
print(set1&set2)
print(set1.union(set2))

#并集
print(set1 | set2)
print(set1.intersection(set2))

#差集
print(set1-set2)
print(set1.difference(set2))

#对称差
#并集-交集
print(set1^set2)
print(set1.symmetric_difference(set2))

#集合的方法
set1={1,2,3,4,5,6}
#添加元素
set1.add(10)
print(set1)

#删除元素
set1.discard(3)
if 10 in set1:
    set1.remove(10)
print(set1)

#清空元素
set1.clear()
print(set1)

#isdisjoint判断有无相同元素

#不可变集合
#frozenset
#list跟tuple的区别
fset1 = frozenset({1, 3, 5, 7})
fset2 = frozenset(range(1, 6))
print(fset1)          # frozenset({1, 3, 5, 7})
print(fset2)          # frozenset({1, 2, 3, 4, 5})
print(fset1 & fset2)  # frozenset({1, 3, 5})
print(fset1 | fset2)  # frozenset({1, 2, 3, 4, 5, 7})
print(fset1 - fset2)  # frozenset({7})
print(fset1 < fset2)  # False

def foo(num):
    return num*2