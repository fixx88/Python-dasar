# BAB 05 - Nested if & Ternary

# NESTED IF - if di dalam if
umur, ktp = 20, True
if umur >= 17:
    if ktp:
        print("Boleh memilih")
    else:
        print("Buat KTP dulu")

# TERNARY - if dalam satu baris
umur = 16
s = "dewasa" if umur >= 17 else "anak"
print(s)   # anak
