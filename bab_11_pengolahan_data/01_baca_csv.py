# BAB 11 - Membaca Data dari File CSV
import csv
import os

# Lokasi nilai.csv dicari relatif terhadap file ini,
# jadi aman dijalankan dari folder mana pun di VS Code.
FOLDER = os.path.dirname(os.path.abspath(__file__))
FILE_CSV = os.path.join(FOLDER, "nilai.csv")

data = []
with open(FILE_CSV, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for baris in reader:
        baris["nilai"] = int(baris["nilai"])   # isi file selalu teks
        data.append(baris)

print(len(data), "baris")
print(data[0])
