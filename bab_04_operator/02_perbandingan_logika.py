# BAB 04 - Operator Perbandingan & Logika

print(5 == 5)    # Sama dengan          -> True
print(5 != 3)    # Tidak sama           -> True
print(7 > 9)     # Lebih besar          -> False
print(2 < 8)     # Lebih kecil          -> True
print(5 >= 5)    # Lebih besar / sama   -> True
print(4 <= 1)    # Lebih kecil / sama   -> False

print("--- Logika: and, or, not ---")
umur = 20
punya_ktp = True

print(umur >= 17 and punya_ktp)
print(umur < 13 or umur > 60)
print(not punya_ktp)
