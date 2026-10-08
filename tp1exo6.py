total_minutes=int(input("merci de saisir la valeure"))

jour=total_minutes//(24*60)
reste_minutes=total_minutes%(24*60)

heure=reste_minutes//60
minutes=reste_minutes%60
print(f"date associe : jour{jour}, {heure}h{minutes}m")