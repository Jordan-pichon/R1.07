import random
x = random.randint(0, 100)
t = 0
n = -1

while n != x:
    n = int(input("Nombre ? "))
    t += 1
    print("Plus grand" if n < x else "Plus petit" if n > x else "Gagné en", t)