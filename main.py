from crud_db import connecter_db

conn = connecter_db()
print("Connexion réussie !")
conn.close()

from voiture import Voiture
from crud_db import ajouter_voiture

v1 = Voiture("bmw", "M3", 2020, 20000)
v2 = Voiture("Honda", "Civic", 2019, 18000)
v3 = Voiture("hyundai", "Elantra", 2019, 18000)

ajouter_voiture(v1)
ajouter_voiture(v2)
ajouter_voiture(v3)