# BAB 07 - Tuple: Data yang Tidak Berubah

titik = (3, 7)
warna = (255, 128, 0)

x, y = titik            # unpacking
print(f"x={x}, y={y}")
print(warna[0], len(warna))

# Tuple bersifat immutable, mengubah isinya menyebabkan TypeError.
# Dibungkus try-except agar program tidak berhenti.
try:
    titik[0] = 10
except TypeError as e:
    print(f"TypeError: {e}")
