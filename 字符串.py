#所谓字符串，就是由零个或多个字符组成的有限序列
#字符串中的字符可以是特殊符号、英文字母、中文字符、日文的平假名或片假名、希腊字母、Emoji 字符
#from 变量 import s3

#原始字符串:以r或R开头
print(r'hello\n')
print('hello\n')
print('hello')

#\n 换行符
#\t 制表符
#\r 回车符

#\141 八进制--表示字母a
#\x61 十六进制--表示字母a

s1='\141\142\143\x61\x62\x63'#字母
s2='\u9a86\u660a'#中文
print(s1)
print(s2)

#字符串运算
#拼接和重复
#比较运算
#成员运算
#获取字符串长度
#索引和切片
#字符的遍历

#大小写相关操作
s3="hello world"

#字符串首字母大写
print(s3)
s4=s3.capitalize()
#s3不会直接发生变换，只会返回相应变换后的结果
print(s3)
print(s4)

#每个单词首字母大写
s5=s3.title()
print(s3)
print(s5)

#字符串变大写
s6=s3.upper()
print(s3)
print(s6)

#字符串变小写
s7=s3.lower()
print(s3)
print(s7)

#查找操作
#在一个字符串中从前往后查有没有另一个字符串

print(s3.find('hello'))
#表示不必从索引为0开始查起
print(s3.find('world',4))
#返回第一次出现所在的位置
print(s3.find('hello',4))
#未找到返回-1

#index同理
#逆向 查找为rfind和rindex

#判断开头
print(s3.startswith('he'))

#判断结尾
print(s3.endswith('ld'))

print(s3[3])
print(s3.find(' '))
a=s3.find(' ')
print(a)
#s3[int(a)]='a'
#由于字符串是不可变类型，不可通过索引运算修改字符串中的字符
#判断是否完全由数字构成
print(s3.isdigit())
#判断是否由数字和字母构成
print(s3.isalnum())
#判断是否完全由字母构成
print(s3.isalpha())


#格式化
#字符串类型可以通过center、ljust、rjust方法做居中、左对齐和右对齐的处理。
#如果要在字符串的左侧补零，也可以使用zfill方法。
s='hello,world'
print(s.center(20,'*'))
print(s.rjust(20,'#'))
print(s.ljust(20,'@'))
print('33'.zfill(5))
print('-33'.zfill(5))

#字符串格式化输出
a=123
b=321
print('%d * %d = %d'%(a,b,a*b))

print('{0} * {1} = {2}'.format(a,b,a*b))

print(f'{a} * {b} = {a*b}')

#占位符：
#{:.2f}
#{:+.2f}
#{:.0f}
#{:0>10d}
#{:x<10d}
#{:>10d}
#{:,}
#{:.2%}
#{:.2e}

c=3.14159
print(f'{c:.2f}')
print(f'{c:.0f}')
print(f'{c:2e}')
print(f'{int(c):x>10d}')
print(f'{c:.2%}')
print(f'{c:,}')




#strip将用户输入时不小心键入的头尾空格等去掉
#strip方法还有lstrip和rstrip两个版本

s8='  abc def '
print(s8)
print(s8.strip())
#去掉左边的空格
#空格为默认，可以自己设置
print(s8.lstrip(' '))
print(s8.rstrip(' '))

#替换操作
print(s3.replace(' ','a'))
print(s3.replace('o','a',2))
print(s3.replace('l','a',2))
print(s3)

#拆分与合并
print(s3.split(' '))
print(s3.split('l'))
print('-'.join(word for word in s3))
print('-'.join(word for word in s3.split()))

#编码和解码
a='高心仪'
b=a.encode('utf-8')
c=a.encode('gbk')

print(b)
print(c)

print(b.decode('utf-8'))
print(c.decode('gbk'))