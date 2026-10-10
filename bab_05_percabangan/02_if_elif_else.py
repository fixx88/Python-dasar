# BAB 05 - if - elif - else: Banyak Kondisi
# Dicek dari atas ke bawah, berhenti di kondisi True pertama.

nilai = 78

if nilai >= 85:
    grade = "A"
elif nilai >= 70:
    grade = "B"
elif nilai >= 55:
    grade = "C"
else:
    grade = "D"

print(f"Nilai {nilai} → grade {grade}")
