#membuat set dan mengisi value/nilai ke dalamnya
data = {'mangga','apel','pir','True','2'}

#menampilkan set menggunakan perulangan
for i in data :
    print(i)


#mengupdate salah satu nilai/value dalam set

#menghapus salah satu / nilai dalam set
# remove
#pop
# clear
#discard

data.remove ('pir')
print(data)

data.pop ()
print(data)


# menambahkan salah satu nilai/value kedalam set
#add
#update

data.add ('meja')
print(data)

data.update ({'kursai','5'})
print(data)