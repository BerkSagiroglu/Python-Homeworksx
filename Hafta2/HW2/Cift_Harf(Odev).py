arr=input("Kelimeyi Girin = ").lower()
d=[]
for c in arr :
    varmi = False
    for i in d:
        if c == i :
            varmi =True
            break
    if varmi == False:
        d.append(c)

print(''.join(d))
