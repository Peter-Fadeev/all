import random
num=random.randint(1,10)
print(num)

p=3
while p>0:
    first=int(input("угадайте число"))
    if num==first:
        print("вы угадали")
        p=p-3
    elif num>first:
        print("ваше число меньше")
    elif num<first:
        print("ваше число больше")
    p=p-1
if not num==first:
    print("вы проиграли, загаданное число было "+str(num))