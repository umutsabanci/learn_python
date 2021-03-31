# while döngüsü break satırı çalışmadan biterse, else içerisine GİRER
# while döngüsü break satırı çalışarak biterse, else içerisine GİRMEZ

# region while-else
"""
i = 1
while i <= 10:
    print(i)
    if i == 2:
        #break
        pass
    i += 1
else:
    print("Şu an else içerisine girdim.")
print("While döngüsü bitti.")
"""
# endregion

# region for-else

for i in range(10, 1, -1):
    print(i)
    if i == 9:
        #break
        pass
else:
    print("Şu an for elsedeyim.")
print("Burdayım")    


# endregion
