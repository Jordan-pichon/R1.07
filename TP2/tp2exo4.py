Base=4
fromage=800.0
eau=2
ail=2
pain=400.0
nb_convives=int(input("Entrez le nombre de personne(s) convivées à la fondue : "))
fromage=fromage*nb_convives/Base
eau=eau*nb_convives/Base
ail=ail*nb_convives/Base
pain=pain*nb_convives/Base
print(f"Pour faire une fondue fribourgeoise pour 3 personnes, il vous faut :")
print(f"{fromage} gr formage")
print(f"{eau} dl d'eau")
print(f"{ail} gousse(s) d'ail")
print(f"{pain} gr de pain")