# NIM/Nama  : 16518360/Ilham Syahid S
# Tanggal   : 5 September 2018
# Deskripsi : Kuadran

x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))

letak = 0

if x != 0 and y == 0:
	letak = "sumbu x"
	
elif x > 0:
	if y > 0:
		letak = "kuadran 1"
	else:
		letak = "kuadran 4"

elif x < 0:
	if y > 0:
		letak = "kuadran 2"
	else:
		letak = "kuadran 3"

elif x == 0:
	if y == 0:
		letak = "titik pusat"
	else:
		letak = "sumbu y"
		
print("(" + str(x) + "," + str(y) + ") ada di " + letak + ".")
