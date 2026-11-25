nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []
for i in range(nombreEtudiants):
    note = float(input(f"Note etudiant {i} : "))
    if note < 0 or note > 20:
        print("Erreur : La note doit etre comprise entre 0 et 20")
    else:
        notes.append(note)
        moyenne += note

moyenne = moyenne / nombreEtudiants
print(f"Moyenne de classe : {moyenne}")

print(f"Numero de l'etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    print(f"Numero de l'etudiant {i} | note : {notes[i]} | ecart a la moyenne : {notes[i]-moyenne}")