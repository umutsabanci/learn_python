ogrenci1 = ["Umut", "Sabancı", 95, 100]
ogrenci2 = ["Batu", "Kochan", 10, 90]
ogrenci3 = ["Emir", "Besi", 100, 90]
ogrenci4 = ["Alp", "Besi", 90, 99]
ogrenci5 = ["Aziz", "Bektas", 15, 10]

ogrenciler = [ogrenci1, ogrenci2, ogrenci3, ogrenci4,ogrenci5]

for item in ogrenciler:
    if(item[2]+item[3])/2 < 50:
        print(f"{item[0]} {item[1]} --> Kaldı")
    else:
        print(f"{item[0]} {item[1]} --> Geçti")
