fayllar_nomi = input()
if fayllar_nomi in fayllar_nomi:
    if fayllar_nomi.endswith(".pdf") or fayllar_nomi.endswith(".docx") or fayllar_nomi.endswith("txt"):
        print("tug'irfayl nomi")
    else:
        print("error")
else:
    print ("error")        