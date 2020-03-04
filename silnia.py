import time as t

n = int(input("Podaj liczbe: "))

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

t_p = t.time()
print(silnia_it(n))
t_k = t.time()
print("Czas wykonania silni iteracyjnie:", t_k-t_p)

t_p = t.time()
print(silnia_rek(n))
t_k=t.time()
print("Czas wykonania silni rekurencyjnie:", t_k-t_p)
