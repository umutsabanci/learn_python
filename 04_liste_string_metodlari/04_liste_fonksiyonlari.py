"""
listeRakamlar = [2, 4, 5, 7, 1, 4, 5]
print(f"listenin en küçük değeri: {min(listeRakamlar)}")
print(f"listenin en büyük değeri: {max(listeRakamlar)}")

print(min(3, 9))
"""

# region ornek1

print("""Eklemek için -> 1
         Silmek için -> 2
         Listelemek için ->3
         Çıkmak için -> 4
""")

ogrenciListe = []
while True:
    secim = int(input("Seçiminiz: \t"))
    if secim == 4:
        break
    elif secim == 1:
        eklenecek = input("eklemek istediğiniz öğrencinin ismini giriniz.")
        ogrenciListe.append(eklenecek)

    elif secim == 2:
        silinecek = input("Silmek istediğiniz öğrencinin adını giriniz.")
        ogrenciListe.remove(silinecek)

    elif secim == 3:
        for i in ogrenciListe:
            print(f"Öğrenci Adı: {i}")

    else:
        print("Yanlış değer girdiniz.")


# endregion
