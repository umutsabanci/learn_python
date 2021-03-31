# break --> Döngüyü sonlandırır.
# continue --> Tepeye geri döner.
"""
i = 1
while i < 11:
    if i == 5:
        break
    print(f"{i}. döngüdeyim.")
    i += 1
"""
"""
i = 1
while i < 100:
    if i % 7 == 0:
        i += 1
        continue
    elif i % 15 == 0:
        break
    print(f"{i}. döngüdeyim.")
    i += 1
"""
eb = 0
while True:
    sayi = int(input("Lütfen Sayı Giriniz. Çıkmak için -1 \t"))
    if sayi == -1:
        break
    if sayi > eb:
        eb = sayi
print(f"En büyük sayı: {eb}")    
