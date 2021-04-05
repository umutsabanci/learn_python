# region append_eleman ekler_listenin_sonuna
"""
meyveler = ["elma","armut","muz","üzüm"]
print(f"listemizin ilk hali {meyveler}")
meyveler.append("karpuz")
print(f"listemizin son hali {meyveler}")
"""
# endregion

# region insert_eleman ekler_istediğimiz_yere
"""
meyveler = ["elma","armut","muz","üzüm"]
print(f"listemizin ilk hali {meyveler}")
meyveler.insert(2, "karpuz")
print(f"listemizin son hali {meyveler}")
"""
# endregion


# region remove_listeden_siler
"""
meyveler = ["elma","armut","muz","üzüm"]
print(f"listemizin ilk hali {meyveler}")
meyveler.remove("üzüm")
print(f"listemizin son hali {meyveler}")
"""
# endregion

# region pop_listeden_siler
"""
meyveler = ["elma","armut","muz","üzüm"]
print(f"listemizin ilk hali {meyveler}")
meyveler.pop(2)
print(f"listemizin son hali {meyveler}")
"""
# endregion

# region clear_listeyi_temizler
"""
meyveler = ["elma","armut","muz","üzüm"]
print(f"listemizin ilk hali {meyveler}")
meyveler.clear()
print(f"listemizin son hali {meyveler}")
"""
# endregion

# region copy_listemizi_yeni_bir_listeye_kopyalar
"""
meyveler = ["elma","armut","muz","üzüm"]
print(f"listemizin ilk hali {meyveler}")
meyveTabagı = meyveler.copy()
print(f"listemizin son hali {meyveTabagı}")
"""
# endregion

# region count
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"] 
arananMeyve = "muz"
elemanAdedi = meyveler.count("muz")
if elemanAdedi == 0:
    print(f"Aradığınız {arananMeyve} listede yer almamaktadır.")
else:
    print(f"aradığınız {arananMeyve} listede yer almaktadır.")
"""
# endregion

# region sort_reverse
"""
listeRakamlar = [5,3,8,9,3,6,7]
print(f"listemizin ilk hali: {listeRakamlar}")
listeRakamlar.sort()
print(f"listemizin son hali: {listeRakamlar}")
listeRakamlar.reverse()
print(f"listemizin son hali: {listeRakamlar}")
"""
# endregion
