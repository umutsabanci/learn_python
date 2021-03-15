print("Yurtiçi uçuşlarda KDV %18 Dir 15kg üzerinde fiyat güncellenecektir.")

biletFiyat = int(input("Lütfen biyet fiyatını giriniz."))

bavulKilosu=20

if bavulKilosu > 15:
  eklenecek=(bavulKilosu-15)*5
  biletFiyat=eklenecek + biletFiyat

print(f"Yeni fiyat: {biletFiyat} ")
