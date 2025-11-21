import cmath

def dft(signal):
    N = len(signal)
    return [sum(signal[n] * cmath.exp(-2j * cmath.pi * k * n / N) for n in range(N)) for k in range(N)]

signal = [1, 2, 3, 4]
dft_result = dft(signal)
print("Transformasi Fourier Discrete dari sinyal:", dft_result)
# Fungsi: Menerapkan DFT pada sinyal digital dengan bilangan kompleks.
# Kondisi: Ketika Anda menganalisis frekuensi dari sinyal listrik atau gelombang.
