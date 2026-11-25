nombre = int(input("Entrez le nombre que vous voulez multiplier : "))

for i in range(1, 11):
    resulat = round(nombre * i, 1)
    print(f"{nombre} x {i} = {resulat}")