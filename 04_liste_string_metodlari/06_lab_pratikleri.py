# region siralama
"""
listem = [7, 9, 6, 1, 3]
siraliMi = False

while not siraliMi:
    print("heheheheh")
"""
# endregion

birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "almış", "yetmiş", "seksen", "doksan"]

girilen = int(input("Sayı giriniz."))

birlerBasamagı = girilen%10
onlarBasamagı = girilen//10

print(f"{onlar[onlarBasamagı]} {birler[birlerBasamagı]}")


