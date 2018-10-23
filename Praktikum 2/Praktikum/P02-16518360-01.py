# NIM/Nama   : 16518360/Ilham Syahid S
# Tanggal    : 19 Sept 2018
# Deskripsi  : Jodoh

laki = int(input("Masukkan jumlah laki-laki: "))

l = [ 0 for i in range(laki)]
for i in range(laki):
	l[i]= input("Masukkan tingkat kegantengan " + str(i+1) + ": ")

perempuan = int(input("Masukkan jumlah perempuan: "))

p = [ 0 for i in range(perempuan)]
for i in range(perempuan):
	p[i]= input("Masukkan tingkat kegantengan " + str(i+1) + ": ")
	
x = int(input("Masukkan nilai X: "))

jodoh = 0 

for i in range(laki):
	for j in range(perempuan):
		if int(l[i])+int(p[j]) == x:
			jodoh += 1

	
print("Jumlah pasangan yang jodoh ada " + str(jodoh) + ".")
