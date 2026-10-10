# BAB 11 - Mini Project: Rekap Nilai per Kelas
import csv
import os

FOLDER = os.path.dirname(os.path.abspath(__file__))
FILE_CSV = os.path.join(FOLDER, "nilai.csv")
KKM = 75

data = []
with open(FILE_CSV, encoding="utf-8") as f:
    for baris in csv.DictReader(f):
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

# Status lulus / remedial per siswa
for d in data:
    status = "Lulus" if d["nilai"] >= KKM else "Remedial"
    print(f"{d['nama']:<8}{d['nilai']:>4}  {status}")
print()

# Rekap per kelas
rekap = {}
for d in data:
    k = d["kelas"]
    rekap.setdefault(k, []).append(d["nilai"])

print(f"{'Kelas':<6}{'Jumlah':>8}{'Rata':>8}")
for k, v in sorted(rekap.items()):
    rata = sum(v) / len(v)
    print(f"{k:<6}{len(v):>8}{rata:>8.1f}")
