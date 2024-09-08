##y=float(input("введите число"))
##i=int(y*10)%10
##t=int(y*100)%10
##print(i+t)
##rx=int(input("сколько вам лет?"))
##if rx>13:
##    print("доступ разрешён")
##else:
##    print("доступ запрещён")
##xx=2>1
##print(True+True)
##health=int(input("какое у вас здоровье?"))
##if health<1:
##    print("0")
##else:
##    print("1")
##gt=int(input("введите число"))
##df=int(input("введите число"))
##wa=int(input("введите число"))
##wur=0
##if gt<0:
##    wur=wur+1
##if df<0:
##    wur=wur+1
##if wa<0:
##    wur=wur+1
##print(wur)
##sss=int(input("введите число"))
##if sss%2==0:
##    print("число чётное")
##else:
##    print("число не чётное")
##fd=int(input("введите число"))
##ds=int(input("введите число"))
##if fd>ds:
##    print(fd)
##else:
##    print(ds)
##fd=int(input("введите число"))
##ds=int(input("введите число"))
##if fd%2==0:
##    yt=str(fd)
##    gh=str(ds)
##    print(yt+gh)
##elif ds%2==0:
##    yt=str(fd)
##    gh=str(ds)
##    print(yt+gh)
##else:
##    print(fd+ds)

br=input("введите код")
ti=len(br)
k=br.isdigit()
if ti==4:
    if k==True:
        print("pin код правильный")
    else:
        print("pin код не правильный")
else:
    print("pin код не правильный")
    
    
