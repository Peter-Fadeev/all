# for io in range(1,101):
#     print("привет")
#     print(io)
# a=int(input("введите число"))
# b=int(input("введите число"))
# for t in range(a,b+1):
#     if t%2==0:
#         print(t)

# wo="привет"
# ow=len(wo)
# for ww in range(0,ow):
#     print(wo[ww])

# for g in "привет":
#     print("пока",g)

def len2(pm):
    tx=0
    for ff in pm:
        tx=tx+1
    return tx
# y=len2("мама")
# l=len("мама")
# print(y,l)

def count2(text,s):
    kl=0
    for cc in text:
        if cc==s:
            kl=kl+1
    return kl
# lk=count2("машина","а")
# print(lk)
# def ind(text,s):
#     kl=0
#     for cc in text:
#         if cc==s:
#             return kl
#         else:
#             kl=kl+1
# lk=ind("бочкак","к")
# print(lk)

# def probels(txt):
#     kl=0
#     for pr in txt:
#         if pr==" ":
#             kl=kl+1
#     return kl
# kk=probels("привет, как дела?")
# print(kk)

# def g(dnk):
#     aa=count2(dnk,"A")
#     tt=count2(dnk,"T")
#     cc=count2(dnk,"C")
#     gg=count2(dnk,"G")
#     sad=str(aa)+" "+str(tt)+" "+str(cc)+" "+str(gg)
#     return sad
# ff=g("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
# print(ff)

# def f(text,q,e):
#     ii=ind(text,q)
#     i=ind(text,e)
#     i3=text[ii+1:i]
#     return i3
# oo=f('Сегодня {очень} хороший день',"х","й")
# print(oo)

def cg(dnk):
    cc=count2(dnk,"C")
    gg=count2(dnk,"G")
    gdf=len2(dnk)
    yer=(cc+gg)/gdf*100
    return yer
gc=cg("ACTAGCGTCAGCTAGCTCGGTCAATTCGCTATGCGATCGCGCTTTAAC")
print(gc)