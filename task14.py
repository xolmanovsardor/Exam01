import os 

fayl_n = input("fayl nomini kiriting")
fayl_turi = os .path . splitext(fayl_n)[1].lower()

r = ['.pdf','dosc' , 'txt'] 
print(fayl_turi in r)