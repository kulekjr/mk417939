import time as t

def silnia_it(x):
    wynik = 1
    for i in range (1,x+1):
        wynik *= i
    return wynik

def silnia_rek(x):
    if x == 1:
        return 1
    else:
        return x*silnia_rek(x-1)

def zmierz(f,n=100):
    t0=t.time()
    w=f(n)
    t1=t.time()
    return t1-t0

print("Czasz dzialania silni iteracyjnie:",zmierz(silnia_it,100))
print("Czasz dzialania silni rekurencyjnie:",zmierz(silnia_rek,100))
