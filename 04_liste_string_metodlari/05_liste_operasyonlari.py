# region yer_degistirme
"""
listem = [1, 2, 3, 4, 5]

temp = listem[2]
listem[2] = listem[3]
listem[3] = temp


listem[2] , listem[3] = listem[3] i listem[2]

print(listem)
"""
# endregion

# region slice
"""
listem = ["a1","a2","a3","a4"]
print("www.umutsabanci.com"[-3:])
print(listem[1:4])
print(listem[-2:])
"""

# endregion

# region slice_ornek

url = input("Lütfen bir site adı giriniz.")
if url[-3:] != "com" or url[0:3] != "www":
    print("Lütfen url formatına dikkat ediniz.")
else:
    print(f"Internet adresi : {url}")


# endregion
