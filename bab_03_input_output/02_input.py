# BAB 03 - Membaca Input dari Pengguna
# Catatan: hasil input() selalu str, jadi umur dikonversi dengan int().
# Jika tidak dikonversi, "19" + 1 akan menyebabkan TypeError.

nama = input("Siapa namamu? ")
umur = int(input("Berapa umurmu? "))

tahun_depan = umur + 1
print(f"Halo {nama}!")
print(f"Tahun depan kamu {tahun_depan} tahun")
