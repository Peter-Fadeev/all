amd=int(input("введите число"))
opi=int(input("введите число"))
gtd=input("введите знак")
if gtd=="+":
    print(amd+opi)
elif gtd=="-":
    print(amd-opi)
elif gtd=="*":
    print(amd*opi)
elif gtd=="/":
    print(amd/opi)
else:
    print("такой операции не существует")

# k=int(input("введите число"))
# u=k**0.5
# if int(u)==u:
#     rt=u+1
#     sd=rt*rt
#     print(sd)
# else:
#     print(-1)