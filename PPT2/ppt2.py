a = int(input("masukkan nilai a: "))
b = int(input("masukkan nilai b: "))
c = int(input("masukkan nilai c: "))

if(a > b) and (a > c):
    print('Nilai a paling besar, yaitu', a)
elif(b > a) and (b > c):
    print('Nilai b paling besar, yaitu', b)
else:
    print('Nilai c paling besar, yaitu', c)        