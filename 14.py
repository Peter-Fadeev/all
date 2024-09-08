# class Cars:
#     def __init__(self,col):
#         self.color=col
#     def signal(self):
#         print("бип-бип",self)
# r=Cars("red")
# y=Cars("green")
# print(r)
# print(y)
# y.signal()
# r.signal()
# print(r.color)
# print(y.color)
# class Rectangle:
#     def __init__(self,s,w):
#         self.shirina=s
#         self.vysota=w
#     def information(self):
#         print("ширина = ",self.shirina,"высота = ",self.vysota)
#     def p(self):
#         u=self.shirina*self.vysota
#         return u
#     def uv(self,num):
#         self.shirina=self.shirina*num
#         self.vysota=self.vysota*num
# k=Rectangle(12,34)
# l=Rectangle(53,47)
# k.information()
# l.information()
# kp=k.p()
# print(kp)
# l.uv(2)
# l.information()

# class Human:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
#     def sl(self):
#         print("Привет,я человек")
# g=Human("Kirill","25")
# f=Human("Vanya","41")
# g.sl()
# f.sl()
# print(g.name)
# print(g.age)
# print(f.name)
# print(f.age)
# def nod(yu,uy):
#     while yu!=uy:
#         if yu>uy:
#             yu=yu-uy
#         else:
#             uy=uy-yu
#     return yu
# j=nod(32,12)
# print(j)
# def nok(tr,rt):
#     tt=tr*rt
#     hi=nod(tr,rt)
#     ti=tt/hi
#     return ti

# class Fraction:
#     def __init__(self,ch,zn):
#         self.chislitel=ch
#         self.znamenatel=zn
#     def vv(self):
#         print(str(self.chislitel)+"/"+str(self.znamenatel))
#     def um(self,num):
#         self.chislitel=self.chislitel*num
#     def sk(self):
#         don=nod(self.chislitel,self.znamenatel)
#         self.chislitel=self.chislitel//don
#         self.znamenatel=self.znamenatel//don
# h=Fraction(3,6)
# p=Fraction(4,11)
# h.vv()
# p.vv()
# h.sk()
# h.vv()

class Item:
    def __init__(self,n,am):
        self.name=n
        self.amount=am
    def set_amount(self,am):
        if am>0:
            self.amount=self.amount+am
        else:
            print("отрицательное количество не принимается")
    def decrease_amount(self,num):
        if num<=self.amount:
            self.amount=self.amount-num
        else:
            raise ValueError("нет такого количества")
    def increase_amount(self,unm):
        if unm>0:
            self.amount=self.amount+unm
        else:
            print("нельзя прибавить отрицательное число")
    def information(self):
        return self.name+"--"+str(self.amount)
g=Item("grechka",3)
h=Item("mylo",8)
g.increase_amount(2)
g.information()

class Shop:
    def __init__(self):
        self.stock=[g,h]
    def list_items(self):
        rt=0
        yu=1
        for jj in self.stock:
            po=jj.information()
            print(yu,po)
            yu=yu+1
            rt=rt+jj.amount
        print("общее количество = ",rt)
    def buy(self,nm,kol):
        hy=0
        for kk in self.stock:
            if nm==kk.name:
                print("товар найден") 
                kk.decrease_amount(kol)
                hy=hy+1
        if hy==0:
            print("товар не найден")
    def sell(self,na,ko):
        op=0
        for ll in self.stock:
            if na==ll.name:
                ll.increase_amount(ko)
                op=op+1
        if op==0:
            i=Item(na,ko)
            self.stock.append(i)



                

                

        
            
ui=Shop()
ui.list_items()
ui.buy("grechka",5)
ui.sell("tort",6)
ui.sell("maslo",1)
ui.list_items()
