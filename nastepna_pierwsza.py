import math as m

a = int(input("Podaj liczbe: "))

def pierwsza(x):
    a = True
    for i in range (2,int(m.sqrt(x)+1)):
        if x%i==0:
            a=False
            break
    return a

def nastepna_pierwsza(n):
    while(True):
        if pierwsza(n):
            print(n)
            break
        else:
            n += 1
    return n
        
def zmierz(f,n=100):
    t0=t.time()
    w=f(n)
    t1=t.time()
    return t1-t0

print(zmierz(a))
