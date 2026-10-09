
print("Tabel Perkalian dan Statistik")

n = int(input("n: "))

# Validasi n harus positif
while n <= 0:
    print("n harus positif.")
    n = int(input("n: "))

# Inisialisasi total keseluruhan dan counter genap
total_semua = 0
count_genap = 0

# Nested loop untuk membuat tabel perkalian
for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j

        print(f"{hasil:4}", end="")

        # Menghitung jumlah setiap baris
        total_baris += hasil

        # Menghitung total seluruh hasil
        total_semua += hasil

        # Menghitung banyak hasil genap
        if hasil % 2 == 0:
            count_genap += 1

    print(f"   | jumlah baris = {total_baris}")

# Menampilkan statistik
print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")