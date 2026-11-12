x = float(input("Entrez un nombre decimal : "))

if ((-10 < x or x == -10) and (x < -2 or x == -2)) or (0 < x and (x < 1 or x == 1)) or ((2 < x or x == 2) and x < 3):
    print("x appartient a I")
else:
    print("x n'appartient pas a I")
