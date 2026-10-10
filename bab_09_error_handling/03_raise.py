# BAB 09 - raise: Memunculkan Error Sendiri

def set_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak valid")
    return umur

try:
    set_umur(-5)
except ValueError as e:
    print(f"Error: {e}")

# Membuat jenis error sendiri
class UmurTidakValid(Exception):
    pass

try:
    raise UmurTidakValid("Umur harus 0 atau lebih")
except UmurTidakValid as e:
    print(f"Error khusus: {e}")
