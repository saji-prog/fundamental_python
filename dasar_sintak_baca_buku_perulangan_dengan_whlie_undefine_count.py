"""
program perulangan membaca buku dengan while sampai paham
"""
jumlah_buku = 10
print('ibu berkata,"baca semua bukumu"')
total_jumlah_baca = 0

jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
print(f'jumlah buku yang sudah di baca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == 9:
        print(f"buku ke{jumlah_buku_yang_sudah_dibaca_dan_dipahami} belum paham")
    else:
        jumlah_buku_yang_sudah_dibaca_dan_dipahami = jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1
        print(f"buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah di baca dan dipahami")

print(f'jumlah buku yang sudah di baca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')
if jumlah_buku_yang_sudah_dibaca_dan_dipahami == jumlah_buku
    print(f'bu,semua buku sudah di baca dan dipahami')
else:
    print(f'"bu, tidak semua buku bisa dipahami.'
          f' budi hanya bisa memamahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami} buku)

