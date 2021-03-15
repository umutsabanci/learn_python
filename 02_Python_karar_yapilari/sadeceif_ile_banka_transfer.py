
bakiye = 5000


bankaKodu = int(input("Banka kodu giriniz."))
transferUcret = float(input("transfer etmek istediğiniz ücreti giriniz."))
kesinti = 0

if bankaKodu != 101:
    kesinti = (transferUcret*5)/100
    
print(f"Güncel bakiye:  {bakiye-transferUcret-kesinti}")



