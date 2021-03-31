while True:
    secim = int(input("[1] km --> mil [2] mil --> km [3] Çıkış \n1"))

    if secim ==1:
        km = int(input("Lütfen km bilgisi giriniz."))
        mil = km * 0.62137
        print(f"{mil}")
        continue
    elif secim == 2:
        mil = int(input("Lütfen mil bilgisini giriniz."))
        km = mil / 0.62137
        print(f"{mil}")
        continue
    elif secim == 3:
        break       