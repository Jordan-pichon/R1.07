import random
x = random.randint(0, 100)
t = 0
n = -1

while n != x:
    n = int(input("Nombre ? "))
    t += 1

    if n < x:
        print("plus grand")
    elif n > x:
        print("plus petit")

print("Bravo ! Trouve en", t, "essais.")