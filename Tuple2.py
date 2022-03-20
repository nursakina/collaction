#membuat tuple dan mengisi value/nilai ke dalamnya
benda = ('tas','buku','pulpen','penggaris','kunci')

#menampilkan tuple menggunakan perulangan
for i in benda :
    print(i)

b = 0
while b < len(benda) :
    print(benda[b])
    b += 1

#mengupdate salah satu nilai/value dalam tuple
b = list (benda)
b [2] = 'kipas'
benda = tuple (b)
print(benda)

#menghapus salah satu / nilai dalam tuple
# remove
# del
# pop

b = list (benda)
b.remove ('buku')
benda = tuple (b)
print(benda)

b = list(benda)
del b [1]
benda = tuple (b)
print(benda)


b = list (benda)
b.pop ()
benda = tuple (b)
print(benda)


# menambahkan salah satu nilai/value kedalam tuple
# append
# insert

b = list(benda)
b.append ('sapu')
benda = tuple (b)
print(benda)

b = list (benda)
b.insert (1,'gelas')
benda = tuple (b)
print(benda)