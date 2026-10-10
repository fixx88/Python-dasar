# BAB 11 - Filter, Hitung & Cari Nilai Tertinggi
import csv
import os

FOLDER = os.path.dirname(os.path.abspath(__file__))
FILE_CSV = os.path.join(FOLDER, "nilai.csv")

data = []
with open(FILE_CSV, encoding="utf-8") as f:
    for baris in csv.DictReader(f):
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

nilai = [d["nilai"] for d in data]
rata = sum(nilai) / len(nilai)
print(f"Rata-rata: {rata:.1f}")

lulus = [d["nama"] for d in data
         if d["nilai"] >= 75]
print("Lulus:", lulus)

top = max(data, key=lambda d: d["nilai"])
print("Tertinggi:", top["nama"])
