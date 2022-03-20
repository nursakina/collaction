#membuat list dan mengisi value/nilai 
warna = ['biru','merah','putih','coklat','hitam']

#Meanmapilkan list dengan perulangan 
for i in warna :
    print(i)

w = 0
while w < len(warna) :
    print(warna[w])
    w +=1 

#mengupdate salah satu nilai/value dalam list
warna [1] = 'hijau'
print(warna)

#menghapus salah satu nilai/value dalam list
#del
#pop
#remove

del warna [2]
print(warna)

warna.pop ()
print(warna)

warna.remove ('biru')
print(warna)

#menambahkan salah satu nilai/value kedalam list
#extend
#append
#insert

warna.extend (['orange'])
print(warna)

warna.append ('jingga')
print(warna)

warna.insert(1,'ungu')
print(warna)
