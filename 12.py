# sn=["яблоко","груша","банан"]
# print(sn[0])
# sn.append("мандарин")
# print(sn)
# sn.pop(0)
# print(sn)
# o=len(sn)
# print(o)
# p=0
# while o>0:
#     print(str(p+1)+" "+sn[p])
#     p=p+1
#     o=o-1
# ee=[]
# o=5
# while o>0:
#     print("1 - добавить  2 - показать список, 3 - напечатать длину списка.. 4 -- удалить.  5 - выйти из программы")
#     k=int(input("какое действие хотите выполнить?"))
#     if k==5:
#         o=o-5
#     if k==1:
#         y=input("что хотите добавить?")
#         ee.append(y)
#     if k==2:
#         i=len(ee)
#         m=1
#         while i>0:
#             print(str(m)+" "+ee[m-1])
#             m=m+1
#             i=i-1
#     if k==3:
#         i=len(ee)
#         print("у вас "+str(i)+" дел")
#     if k==4:
#         d=int(input("какое дело хотите удалить?"))
#         ee.pop(d-1)

# ee=[]
# ar=int(input("введите число"))
# for kk in range (0,ar):
#     pp=int(input("введите число"))
#     ee.append(pp)
# print(ee)
# xx=0
# for ll in ee:
#     xx=xx+ll
# oo=len(ee)
# print(xx/oo)  

# def gh(l):
#     f=l[0]
#     for jj in l:
#         if f>jj:
#             f=jj
#     return f 
# def hg(ll):
#     k=[]
#     for vv in ll:
#         if vv%2==1:
#             k.append(vv)
#     return k
# def gg(iu):
#     mn=hg(iu)
#     if mn==[]:
#         return 0
#     else:
#         nm=gh(mn)
#         return nm
    
# print(gg([4,8,6,2,]))  

# def ty(l,k):
#     h=[]
#     for j in l:
#         if j in k:
#             h.append(j)
#     return h
# yt=ty([1,3,4],[5,9,1])
# print(yt)

# cc=[]
# yu=int(input("введите количество покупок"))
# while yu>0:
#     yo=(input("что хотите купить?"))
#     cc.append(yo)
#     yu=yu-1
# for bb in cc:
#     print(bb)

