import time
print("hello world")
#暂停1s
time.sleep(1)

print("End")

#for-in 循环
#从0-9
for i in range(10):
    print("hello world")
    print(i)
    time.sleep(0)
#其他形式
for _ in range(5):
    print("你好世界")
    time.sleep(0)
#ctrl+c终止程序

#求和1-100偶数
Sum=0
for i in range(1,101):
    if i%2==0:
        Sum+=i
print(Sum)

Sum=0
#可以表示跨度为2
for i in range(2,101,2):
    Sum+=i
print(Sum)

#更简单的表示方法
print(sum(range(2,101,2)))

#while循环
total=0
i=1
while i<=100:
    total+=i
    i+=1
print(total)

#break和continue可用于进入下一轮循环和结束循环

#乘法口诀表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i*j,end="\t")
    print()


#随机数
import random

answer=random.randrange(1,10)
counter=0
while True:
    counter+=1
    num=int(input("请输入："))
    if num==answer:
        break
    else:
        if num>answer:
            print("大了")
        else:
            print("小了")
        continue
print(f"你一共猜了{counter}次")








