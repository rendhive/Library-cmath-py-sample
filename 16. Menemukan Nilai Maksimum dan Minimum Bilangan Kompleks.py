import cmath

z1 = complex(3, 4)
z2 = complex(1, 2)
max_value = max(z1, z2, key=abs)
min_value = min(z1, z2, key=abs)
print("Nilai maksimum dan minimum berdasarkan modulus:", max_value, min_value)
# Fungsi: Menemukan nilai maksimum dan minimum dari sekumpulan bilangan kompleks sesuai modulus.
# Kondisi: Ketika Anda melakukan analisis data numerik kompleks.
