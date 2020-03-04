import math as m

n = int(input("Podaj liczbe: "))

def pierwsza(x):
    a = True
    for i in range (2,int(m.sqrt(x)+1)):
        if x%i==0:
            a=False
            break
    return a

while(True):
    if pierwsza(n):
        print(n)
        break
    else:
        n += 1
