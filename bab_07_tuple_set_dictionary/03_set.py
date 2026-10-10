# BAB 07 - Set: Kumpulan Nilai Unik

angka = {1, 2, 2, 3, 3, 3}
print(angka)

ipa = {"Ani", "Budi", "Citra"}
ips = {"Budi", "Dodi"}

print(ipa | ips)   # Union
print(ipa & ips)   # Intersection
print(ipa - ips)   # Difference

# Catatan: set tidak berurutan, jadi urutan tampilan bisa berbeda-beda.
# Set kosong dibuat dengan set(), bukan {}
kosong = set()
print(kosong, type(kosong))
