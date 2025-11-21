import cmath

z = complex(-1, 1)
polar = cmath.polar(z)
converted_back = cmath.rect(*polar)
print("Dari polar ke kompleks:", converted_back)
# Fungsi: Mengonversi bentuk polar kembali ke bilangan kompleks dan memverifikasi.
# Kondisi: Untuk memastikan konversi antara bentuk berbeda dilakukan dengan benar.
