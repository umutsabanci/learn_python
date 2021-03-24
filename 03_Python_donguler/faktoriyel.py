
i = 1
j = 1
sonuc = 1

sinir = int(input("Faktoriyelini hesaplamak istediğiniz sayıyı giriniz:"))

while i <= sinir:

    while j <= i:
        sonuc = sonuc*j
        j += 1

        print(f"{i}  {sonuc} ")
    i += 1        
    
"""
a = int(input("sayı: "))
i, fakt = 1, 1
while i < a:
    i += 1
    fakt *= i
print(f"{a}! = {fakt}")
"""

"""
i = 1
res = 1
while i <= 5:
    res *= i
    print(f"{i} sayısının faktöriyeli = {res}")
    i += 1
"""    
