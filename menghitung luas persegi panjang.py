#menemukan luas persegi panjang
def luas_persegi_panjang (Panjang, Lebar):
    return Panjang * Lebar
Panjang = float(input("Masukkan Panjang: "))
Lebar = float(input("Masukkan Lebar: "))

area = luas_persegi_panjang (Panjang,Lebar)

print(f"Luas persegi Panjang adalah: {area} ")