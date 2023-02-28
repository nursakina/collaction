data = [0,1,2,2,3,3,4]
n = len (data)
jumlahData = 0

for i in data :
    jumlahData += i
 
print ("jumlah Data : ",jumlahData)
print ("n:",n)


#MEAN
mean = jumlahData / n
print ("mean:", mean)
print("--------------------------")


#MEDIAN
if n %2 == 0 :
    median = nim[int(RumusMedian)]
#ganjil
else :
     RumusMedian= (n +1)/2
#genap
     pass

print("data :", data)
print("nilai median terletak diurutan ke-  :", RumusMedian)
print("--------------------------")


#MODUS
data = [0,1,2,2,3,3,4]

counts = []
for i in data :
    counts.append(data.count(i))

max_count = max(counts)

mode = []
for i in data :
    if data.count (i) == max_count and i not in mode :
        mode.append(i)

if len (mode) == 1:
    print ("modus :", mode[0])
elif len(mode) > 1 :
    print ("modus :", mode)
else :
    print (" Tidak ada modus")

