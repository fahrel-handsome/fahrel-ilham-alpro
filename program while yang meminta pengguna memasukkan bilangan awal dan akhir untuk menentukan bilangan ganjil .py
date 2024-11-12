# Program untuk menentukan bilangan ganjil menggunakan while
print ("program untuk menentukan bilangan ganjil")
bilangan_awal = int(input("Masukkan bilangan awal: "))
bilangan_akhir = int(input("Masukkan bilangan akhir: "))

print("Bilangan ganjil dalam rentang tersebut adalah:")

while bilangan_awal <= bilangan_akhir:
    if bilangan_awal % 2 != 0:
        print(bilangan_awal)
    bilangan_awal += 1