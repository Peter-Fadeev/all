import turtle
def move(x,y):
    i.up()
    i.goto(x,y)
    i.down()
def no(x,y):
    i.up()
    i.goto(x,y)
    i.down()
    i.circle(150)
def kr(pp,nn):
    i.up()
    i.goto(pp,nn)
    i.down()
    i.goto(pp-250,nn+250)

    i.up()
    i.goto(pp,nn+250)
    i.down()
    i.goto(pp-250,nn) 
def krall(num):
    if num==1:
        kr(-175,175)
    if num==2:
        kr(125,175)
    if num==3:
        kr(425,175)
    if num==4:
        kr(-175,-125) 
    if num==5:
        kr(125,-125)
    if num==6:
        kr(425,-125)
    if num==7:
        kr(-175,-425)
    if num==8:
        kr(125,-425)
    if num==9:
        kr(425,-425)
def noall(num):
    if num==1:
        no(-300,150) 
    if num==2:
        no(0,150)
    if num==3:
        no(300,150)
    if num==4:
        no(-300,-150)
    if num==5:
        no(0,-150)   
    if num==6:
        no(300,-150)
    if num==7:
        no(-300,-450)
    if num==8:
        no(0,-450)
    if num==9:
        no(300,-450)        
o=turtle.Screen()
o.bgcolor("black")
o.setup(900,900)
i=turtle.Turtle()
i.speed(10)
i.color("white")
i.width(10)

move(-150,450)
i.goto(-150,-450)

move(150,-450)
i.goto(150,450)

move(-450,150)
i.goto(450,150)

move(-450,-150)
i.goto(450,-150)

n=1
while n<=9:
    if n%2==1:
        print("ходят крестики")
    else:
        print("ходят нолики")
    num=int(input("номер клетки"))
    if n%2==1:
        krall(num)
    else:
        noall(num)
       
           
    n=n+1










input()