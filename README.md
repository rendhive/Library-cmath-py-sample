# Library-cmath-py-sample

📘 Operasi Bilangan Kompleks dengan Python cmath

Modul cmath di Python memungkinkan Anda melakukan berbagai operasi pada bilangan kompleks, seperti penjumlahan, pengurangan, perkalian, pembagian, hingga perhitungan modulus, fase (angle), dan transformasi Fourier.
cmath adalah bagian dari Python Standard Library, sehingga dapat digunakan tanpa instalasi tambahan.


---

📑 Daftar Isi

Instalasi

Penggunaan

Dasar-dasar Bilangan Kompleks

Operasi Aritmetika

Fungsi Lain


Kondisi Penggunaan

Referensi



---

🛠 Instalasi

Tidak perlu instalasi tambahan karena cmath sudah termasuk dalam Python Standard Library.
Pastikan menggunakan Python 3.x.


---

🚀 Penggunaan

🔹 Dasar-dasar Bilangan Kompleks

Untuk membuat bilangan kompleks di Python, gunakan fungsi complex(real, imaginary):

import cmath

z = complex(2, 3)  # Bilangan kompleks 2 + 3j
print(z)


---

🔹 Operasi Aritmetika

Anda dapat melakukan operasi seperti penjumlahan, pengurangan, perkalian, dan pembagian:

z1 = complex(1, 2)
z2 = complex(3, 4)

tambah = z1 + z2
kurang = z1 - z2
kali   = z1 * z2
bagi   = z1 / z2

print("Tambah:", tambah)
print("Kurang:", kurang)
print("Kali:", kali)
print("Bagi:", bagi)


---

🔹 Fungsi Lain

Modul cmath menyediakan banyak fungsi penting:

Fungsi	Deskripsi

abs(z)	Menghitung modulus (magnitudo) bilangan kompleks
cmath.phase(z)	Mendapatkan sudut/phase dari bilangan kompleks
cmath.polar(z)	Mengonversi bilangan kompleks ke bentuk polar (r, φ)
cmath.rect(r, φ)	Mengonversi bilangan kompleks dari bentuk polar ke kartesian


Contoh:

z = complex(3, 4)

print("Modulus :", abs(z))
print("Phase   :", cmath.phase(z))
print("Polar   :", cmath.polar(z))

r, phi = cmath.polar(z)
print("Rect    :", cmath.rect(r, phi))


---

📌 Kondisi Penggunaan

Modul cmath sangat cocok digunakan ketika:

Anda bekerja dengan bilangan kompleks dalam komputasi matematis.

Membutuhkan perhitungan FFT/DFT (bersama cmath.exp()).

Membutuhkan operasi presisi tinggi pada domain kompleks.

Membuat simulasi sains dan engineering seperti:

sinyal digital

analisis frekuensi

fisika (gelombang, resonansi)

algoritma matematika lanjutan




---

📚 Referensi

Dokumentasi resmi Python: https://docs.python.org/3/library/cmath.html
