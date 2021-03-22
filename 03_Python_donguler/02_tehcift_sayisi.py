teklerinSayisi = 0
ciftlerinSayisi = 0
sayi = int(input("lütfen sayı giriniz, çıkmak için 0 yazın : "))
while sayi != 0:   #-1 olmadığı sürece döngüye devam et
    if sayi%2 == 1: 
        teklerinSayisi +=1
    else :
        ciftlerinSayisi += 1
    sayi = int(input("lütfen sayı giriniz, çıkmak için 0 yazın : "))
print(f"girdiğiniz sayıların tek olanları  {teklerinSayisi}")
print(f"girdiğiniz sayıların çift olanları {ciftlerinSayisi} ")
