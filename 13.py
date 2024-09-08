# ms={1:"январь", 2:"февраль"}
# print(ms[3])
# ms[2]="март"
# print(ms)

# def dna(sd):
#     tt=""
#     tr={"A":"T","T":"A","C":"G","G":"C"}
#     for vv in sd:
#         d=tr[vv]
#         tt=tt+d
#     return ttACTA
# ii=dna("GCGTCAGCTAGCTCGGTCAATTCGCTATGCGATCGCGCTTTAAC")   
# print(ii)

# k=1 
# sl={} 
# while k>0:      
#     print("1 - показать перевод слова  2 - добавить новое слово 3 - показать словарь 4 - выйти из программы")
#     p=int(input("какое действие хотите выполнить? "))
#     if p==1:
#         o=input("введите слово для перевода ")
#         if o in sl:
#             print(sl[o])
#         else:
#             print("такого слова нет в словаре")
#     if p==2:
#         z=input("введите слово на русском языке ")
#         x=input("введите его перевод на английском ")
#         sl[z]=x
#     if p==3:
#         for u in sl:
#             print(u,sl[u])
#     if p==4:
#         k=k-1

def zp(t):
    ui=""
    for gg in t:
        if gg not in ",.!?;-":        
            ui=ui+gg
    return ui
def ind(text,s):
    kl=0
    for cc in text:
        if cc==s:
            return kl
        else:
            kl=kl+1
def hg(txt):
    io=[]
    txt=zp(txt)
    while  " "  in txt:
        pp=ind(txt," ")
        ll=txt[0:pp]
        io.append(ll)
        txt=txt[pp+1:]
    io.append(txt)
    return io

def count2(text,s):
    kl=0
    for cc in text:
        if cc==s:
            kl=kl+1
    return kl
def yt(x):
    q={}
    x=hg(x)
    for r in x:
        ii=count2(x,r)
        q[r]=ii
    return q
tr=yt("сегодня хороший, хороший день")
print(tr)