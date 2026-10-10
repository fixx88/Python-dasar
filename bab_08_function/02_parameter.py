# BAB 08 - Jenis Parameter & Argumen

def sapa(nama, salam="Halo"):
    return f"{salam}, {nama}!"

print(sapa("Ani"))
print(sapa(salam="Hai", nama="Budi"))

# *args: banyak argumen -> tuple
def total(*angka):
    return sum(angka)

print(total(1, 2, 3, 4))

# **kwargs: banyak key=value -> dict
def profil(**data):
    return data

print(profil(nama="Ani", umur=20))
