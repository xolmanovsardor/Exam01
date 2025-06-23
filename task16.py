chipta = 100 
yosh = int(input("yoshingizni kiriting ->>"))
if yosh < 7:
  chipta *= 0.5
  print("sizga 50% chegirma taqdim etildi")
if 7 < yosh < 17:
  chipta *= 0.8
  print("sizga 20% chegirma taqdim etildi")
if yosh < 60:
  chipta *= 0.7
  print("sizga 30% chegirma taqdim etildi")

