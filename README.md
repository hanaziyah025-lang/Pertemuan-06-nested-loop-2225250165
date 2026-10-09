
# Pertemuan 06 - Nested Loop Python

**Nama:** Hana Karimah Ghoziyah  
**NIM:** 2225250165  
**Kelas:** 3B

## Tujuan

Menggunakan nested loop, pola, akumulasi, dan pencacahan.

## Cara Menjalankan

Jalankan program melalui terminal VS Code dengan perintah:

```bash
python tugas/tabel_perkalian_dan_statistik.py
```

## Algoritma Tugas 3

1. **Loop luar:** Mengatur baris tabel perkalian dari 1 sampai n.
2. **Loop dalam:** Menghitung hasil perkalian setiap baris dengan angka 1 sampai n.
3. **Akumulator:** `total_baris` menghitung jumlah hasil perkalian pada setiap baris, sedangkan `total_semua` menghitung jumlah seluruh hasil perkalian.
4. **Counter:** `count_genap` menghitung banyaknya hasil perkalian yang merupakan bilangan genap.
5. **Validasi:** Perulangan `while` memastikan nilai n harus lebih besar dari 0.

## Hasil Pengujian

| Input n | Hasil yang Diharapkan | Keluaran Aktual | Status |
|---|---|---|---|
| 1 | Total = 1, genap = 0 | Total = 1, genap = 0 | Berhasil |
| 2 | Total = 9, genap = 3 | Total = 9, genap = 3 | Berhasil |
| 3 | Total = 36, genap = 5 | Total = 36, genap = 5 | Berhasil |
| 0 | Program meminta input positif | Program meminta input positif | Berhasil |

## Analisis Efisiensi

Untuk input n, badan loop dalam berjalan sebanyak n × n atau n² kali karena setiap perulangan luar menjalankan loop dalam sebanyak n kali. Jadi, kompleksitas waktunya adalah O(n²).

## Refleksi

Kesalahan yang dapat terjadi adalah menginisialisasi `total_baris` di luar loop luar sehingga jumlah dari baris sebelumnya ikut terhitung. Cara memperbaikinya adalah menginisialisasi `total_baris = 0` di dalam loop luar agar jumlah setiap baris dihitung secara terpisah.