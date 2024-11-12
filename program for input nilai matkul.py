jumlah_mahasiswa = int(input("banyak mahasiswa: "))
for i in range(jumlah_mahasiswa):
    
    print(f"\nMahasiswa ke-{i + 1}:")
    
    # Meminta pengguna untuk memasukkan banyak mata kuliah
    jumlah_mata_kuliah = int(input("banyak mata kuliah yang diambil: "))
    
    total_nilai = 0  # Inisialisasi total nilai
    
    # Menggunakan loop untuk setiap mata kuliah
    for j in range(jumlah_mata_kuliah):
        nilai = float(input(f"input nilai mata kuliah ke-{j + 1}: "))
        total_nilai += nilai  # Menambahkan nilai ke total
    
    # Menghitung rata-rata
    rata_rata = total_nilai / jumlah_mata_kuliah
    
    # Menampilkan hasil
    print(f"Rata-rata nilai mahasiswa ke-{i + 1}: {rata_rata:.2f}")