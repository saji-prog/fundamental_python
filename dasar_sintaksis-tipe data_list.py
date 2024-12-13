"""
data list
"""

daftar_buku = ['1 buku harian', '2 buku matematika', '3 buku sejarah', '4 buku mainan']
print('tampilkan variabel daftar_buku')
print(daftar_buku)

print('\nproses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\ntampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\ntampilan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'golkar', 'masakan enak']
print('\ntampilan dengan for in range,dimana tipe data tiap line berbeda-beda')
for i in  range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nkembalikan nilai awal dfatar buku')
daftar_buku = ['1 buku harian', '2 buku matematika', '3 buku sejarah', '4 buku mainan']
print('\ntambahkan 1 buku baru')
daftar_buku.append('5 dunia pelajaran sekolah')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nclear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

    print('\nganti elemn pertama')
daftar_buku = ['1 buku harian', '2 buku matematika', '3 buku sejarah', '4 buku mainan']
daftar_buku[0] = 'buku anak'
for i in  range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nbuku yang di ambil tadi')
print(buku)

print('\npop')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\npop -1')
daftar_buku = ['1 buku harian', '2 buku matematika', '3 buku sejarah', '4 buku mainan']
daftar_buku.pop(-4)
for i in  range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dg list coprehesion pertama')
daftar_buku = ['1 buku harian', '2 buku matematika', '3 buku sejarah', '4 buku mainan']
del daftar_buku[0:-2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dg list comprehesion stra,end,step')
daftar_buku = ['1 buku harian', '2 buku matematika', '3 buku sejarah', '4 buku mainan']
del daftar_buku[0::2]#star:end:step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nmembuat list baru')
daftar_buku = ['1 buku harian', '2 buku matematika', '3 buku sejarah', '4 buku mainan']
