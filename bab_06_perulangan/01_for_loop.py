# BAB 06 - for: Mengulang Setiap Item

for i in range(1, 4):
    print(f"Putaran ke-{i}")

buah = ["apel", "jeruk", "mangga"]
for b in buah:
    print(b.upper())

# Variasi range()
print(list(range(5)))          # 0,1,2,3,4
print(list(range(1, 6)))       # 1..5 (batas akhir tidak ikut)
print(list(range(0, 10, 2)))   # langkah 2
