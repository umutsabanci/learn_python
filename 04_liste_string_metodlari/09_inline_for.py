# inline for
"""
liste = [i for i in range(1,9)]
print(liste)
"""

haftanınGunleri = ["", "Pazartesi", "Salı", "Çarşamba",
                   "Perşembe", "Cuma", "Cuamrtesi", "Pazar"]

liste = [f"Haftanın {i}. günü {haftanınGunleri[i]} dir " for i in range(1, 8) if i<3]
print(liste)
