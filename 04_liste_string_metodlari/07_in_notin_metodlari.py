# index -> bulunduğu index value error
# count("i")
# in not in

# region arama_in_ile
"""
meyveler = ["elma" , "armut" , "muz" , "ayva" , "üzüm" , "elma"]
arananMeyve = input("Lütfen aradığınız meyveyi giriniz.")
if arananMeyve in meyveler:
    print(f"{arananMeyve} liste elemanları içerisinde mevcut")
else:
    print(f"{arananMeyve} liste elemanları içerisinde mevcut değil")    
"""
# endregion

# region arama_index
"""
meyveler = ["elma" , "armut" , "muz" , "ayva" , "üzüm" , "elma"]
arananMeyve = input("Lütfen aradığınız meyveyi giriniz.")

print(meyveler.count(arananMeyve))
if meyveler.count(arananMeyve) != 0:
    print("Var")
else:
    print("Yok")    
"""


# endregion

meyveler = ["elma", "armut", "muz", "ayva", "üzüm", "elma"]
yeniListe = []

for i in meyveler:
    if i not in yeniListe:
        yeniListe.append(i)
        
print(yeniListe)    
