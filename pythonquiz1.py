print("=== Program Gaji Harian ===")

# TODO: Ambil input nama pegawai
nama = input("Masukkan nama pegawai: ")

# TODO: Ambil jumlah hari kerja yang direncanakan
total_hari = int(input("Masukkan jumlah hari kerja yang direncanakan: "))

print(f"Selamat datang, {nama.upper()}!")
print("Masukkan gaji harian selama bekerja.\nMasukkan 0 jika ingin berhenti lebih awal.\n")

# Inisialisasi hari dan total gaji
hari_ke = 1
total_gaji = 0

# TODO: Gunakan perulangan while untuk iterasi setiap hari


print()
print()

# Debuging
# Rekap Gaji Mingguan Pegawai Shift

# Deskripsi
# Program ini bertujuan untuk:
# 1. Meminta input nama pegawai, jumlah hari kerja, dan tarif per jam.
# 2. Untuk setiap hari, meminta input jumlah jam kerja.
# 3. Jika jam kerja == 0, hari dianggap libur → continue
# 4. Jika jam kerja > 12, program dihentikan karena overload → break
# 5. Jika jam kerja > 8 tapi ≤ 12, dianggap lembur, kelebihan jam dikali tarif 1.5×
# 6. Total gaji dihitung dan ditampilkan di akhir program

print("=== PROGRAM REKAP GAJI MINGGUAN v3 ===")

nama = input("Masukkan nama pegawai: ")
# Konversi input hari_kerja ke integer
hari_kerja = int(input("Jumlah hari kerja minggu ini: "))
# Konversi input tarif_per_jam ke integer
tarif_per_jam = int(input("Tarif per jam (contoh: 20000): "))

gaji_total = 0
hari = 1

# Pastikan perulangan berjalan sesuai jumlah hari kerja yang diinput
while hari <= hari_kerja:
    print(f"Hari ke-{hari}:") # Gunakan f-string untuk formatting yang lebih baik
    jam_kerja = int(input("Masukkan jumlah jam kerja: "))

    # Perbaikan: Perbandingan dengan integer 0, bukan string "0"
    if jam_kerja == 0:
        print("Hari libur. Lanjut ke hari berikutnya.\n")
        hari += 1 # Tambahkan hari agar tidak terjadi infinite loop jika hari libur
        continue

    if jam_kerja > 12:
        print("Jam kerja melebihi batas maksimum! Program dihentikan.\n")
        break

    if jam_kerja > 8:
        # Perbaikan: Hitung jam lembur yang sebenarnya
        jam_normal = 8
        jam_lembur = jam_kerja - jam_normal
        gaji_harian = (tarif_per_jam * jam_normal) + (tarif_per_jam * 1.5 * jam_lembur)
    else:
        gaji_harian = tarif_per_jam * jam_kerja

    # Perbaikan: Tambahkan gaji harian ke gaji_total, bukan menimpa
    gaji_total += gaji_harian
    hari += 1 # Pindahkan increment hari_ke di luar if/else agar selalu bertambah

# Perbaikan: Akses atribut .upper() pada string nama
print(f"Total gaji minggu ini untuk {nama.upper()} adalah Rp{gaji_total}")
print()