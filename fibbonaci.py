import time as t

n = int(input("Podaj liczbe: "))

def fib_it(x):
  a = 1
  b = 1
  for i in range (2,x+1):
    tmp = a
    a = b
    b = b + tmp
  return b
  
def fib_rek(x):
  if x<=2:
    return 1
  else:
    return fib_rek(x-1) + fib_rek(x-2)

t_p = t.time()
print(fib_it(n))
t_k = t.time()
print("Czas dzialania funkcji iteracyjnie:", t_k-t_p)


t_p = t.time()
print(fib_rek(n))
t_k = t.time()
print("Czas dzialania funkcji rekurencyjnie:", t_k-t_p)
