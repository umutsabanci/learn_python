not1 = int(input("İlk notu giriniz."))
not2 = int(input("İkinci notu giriniz."))

ort = (not1+not2)/2

if ort>=85:
    print(f"Yıl sonu notu:  {ort} Pek iyi")
elif ort >= 70:
    print(f"Yıl sonu notu: {ort} İyi")
elif ort >= 55:
    print(f"Yıl sonu notu: {ort} Orta")    
elif ort >= 45:
    print(f"Yıl sonu notu: {ort} Geçer")  
else:
    print(f"Yıl sonu notunuz: {ort} Kalır")    