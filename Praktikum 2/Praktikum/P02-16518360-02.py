# NIM/Nama   : 16518360/Ilham Syahid S
# Tanggal    : 19 Sept 2018
# Deskripsi  : Bilangan Prima


a = int(input("Masukkan A: "))
b = int(input("Masukkan B: "))

print("Bilangan prima dari A hingga B:")

for i in range(a, b+1):
	p= True
	for j in range(2, i):
		if i%j ==0:
			p=False
	if p:
		print(i)
