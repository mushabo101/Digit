def digitAwal(x,y):
    hasil = x**y #menghitung pangkat
    while hasil >= 10: #perulangan untuk menentukan digit awal
        hasil = hasil/10
    return int(hasil)

def digitAkhir(x,y):
    hasil = x**y
    hasil = str(hasil) 
    return int(hasil[len(hasil)-1]) #ambil digit akhir pada string lalu di integerkan

print(digitAwal(10,8))
print(digitAwal(2,3))
print(digitAwal(6,3))
print('------------------')
print(digitAkhir(10,8))
print(digitAkhir(2,3))
print(digitAkhir(6,3))