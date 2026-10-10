# BAB 10 - Membuat Module & Package Sendiri
#
# proyek/
# ├── main.py
# └── utils/
#     ├── __init__.py
#     ├── hitung.py
#     └── teks.py
#
# Jalankan dari dalam folder 02_module_sendiri:  python main.py

from utils.hitung import rata_rata
from utils.teks import huruf_besar

nilai = [80, 90, 70]
print(rata_rata(nilai))
print(huruf_besar("python"))
