import random

#1表示胜利

guest_win=0
host_win=0
counter=0
first=0
sum_money=1000
give_money=0
while sum_money>0:
    counter+=1

    guest_win=0
    host_win=0

    give_money=int(input("请您输入本局下注金额："))
    num1=random.randrange(1,7)
    num2=random.randrange(1,7)
    Sum=num1+num2
    print(f"您摇出的点数为{num1}和{num2}")
    if counter==1:
        first=Sum
        if Sum==7 or Sum==11:
            guest_win=1
        elif Sum==2 or Sum==12 or Sum==3:
            host_win=1
    else:
        if Sum==first:
            guest_win=1
        elif Sum==7:
            host_win=1
    if guest_win==1:
        sum_money+=give_money
        print(f"玩家胜利，您剩余金额为{sum_money}")
    elif host_win==1:
        sum_money-=give_money
        print(f"庄家胜利，您剩余金额为{sum_money}")
    else:
        print("游戏继续")

print("您已破产，游戏结束！")

