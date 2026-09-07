#if else elif
s=25
if 20<=s<30:
    print(s)
else:
    print("No")
bmi=10
#bmi=int(input("身高（cm）:"))
if 160<bmi<=180:
    print("您的身高达标")
elif bmi>180:
    print("您的身高高于180cm")
else:
    print("您的身高低于160cm")

description=0
status=0
#status=int(input("响应码状态："))
if status==400:
    description="Bad Request"
elif status==401:
    description="Unauthorized"
elif status==403:
    description="Forbidden"
elif status==404:
    description="Not Found"
else:
    print("未列举")

if description!=0:
    print("状态码描述：",description)

status2=int(input("响应状态码："))
print(status2)
match status2:
    case 400:description="Bad Request"
    case 405:description="Method Not Allowed"
    case 418:description="I'm a teapot"
    case 429:description="Too many requests"
    case _:description="Unknown Status Code"

print("状态码描述：",description)

#case 400|405:  表示合并

