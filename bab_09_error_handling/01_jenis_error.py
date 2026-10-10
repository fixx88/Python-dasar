# BAB 09 - Jenis Error yang Sering Muncul
# Semua error dipicu SENGAJA di dalam try-except supaya program tetap jalan.

def coba(nama, fungsi):
    try:
        fungsi()
    except Exception as e:
        print(f"{nama:<18}-> {type(e).__name__}: {e}")

# SyntaxError: penulisan kode tidak sesuai aturan -> print("hai"
coba("SyntaxError", lambda: compile('print("hai"', "<contoh>", "exec"))

# IndentationError: indentasi blok tidak konsisten
coba("IndentationError", lambda: compile("if x:\nprint(x)", "<contoh>", "exec"))

# NameError: variabel belum pernah dibuat
coba("NameError", lambda: print(skor_x))  # noqa: F821

# TypeError: operasi pada tipe data yang salah
coba("TypeError", lambda: "5" + 3)

# ValueError: tipe benar, tetapi nilainya tidak valid
coba("ValueError", lambda: int("abc"))

# ZeroDivisionError: membagi angka dengan nol
coba("ZeroDivisionError", lambda: 10 / 0)

# IndexError: indeks di luar panjang list
coba("IndexError", lambda: [1, 2][5])

# KeyError: key tidak ada di dictionary
coba("KeyError", lambda: {"a": 1}["b"])

# Tips: baca pesan error dari baris paling bawah.
