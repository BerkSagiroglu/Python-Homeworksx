x = input("Kelimeyi Gir :")
a = input("Birinci Sayıyı Gir : ")
a = int(a) - 1
b = input("İkinci Sayıyı Gir :")
b = int(b)
y = x[b:]
x = x[:a]
print(x,y)
