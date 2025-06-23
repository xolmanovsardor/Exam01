cauntry = "Toshkent"
for i in range(10):
    quistion = input("O‘zbekiston poytaxti nima?")
    if quistion.capitalize() == cauntry:
        print("tug'ri javob! tabriklaymiz.")
        break
    else:
        print("notug'ri lavob, yana bir bor urunib kuring.")
