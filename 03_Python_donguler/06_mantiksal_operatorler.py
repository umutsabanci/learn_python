# mantıksal operaötler -> logical operatörler

"""
ve    and
veya   or
değil  not

"""

# region and
"""
print(5 == 5 and 15 > 5)
print(5 == 4 and 10 > 2)
"""
# endregion

# region or
"""
print(5 == 5 or 15 > 5)
print(5 == 4 or 10 > 2)
print(5 == 4 or 10 < 2)
"""
# endregion

toplam = 0
while True:
    sayi = int(input("lütfen sayı giriniz. Çıkmak için 0 tuşuna basınız. \t"))
    if sayi == 0:
        break
    if sayi<0 or sayi %2 == 1:
        print("Negatif ve tek sayı giremezsin")
        continue
    toplam += sayi
print(toplam)

    
