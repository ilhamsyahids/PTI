# NIM/Nama  : 16518360/Ilham Syahid S
# Tanggal   : 5 September 2018
# Deskripsi : Asian Games

ET = int(input("Masukkan perolehan emas Jawa Tengah: "))
PT = int(input("Masukkan perolehan perak Jawa Tengah: "))
PeT = int(input("Masukkan perolehan perunggu Jawa Tengah: "))

EB = int(input("Masukkan perolehan emas Jawa Barat: "))
PB = int(input("Masukkan perolehan perak Jawa Barat: "))
PeB = int(input("Masukkan perolehan perunggu Jawa Barat: "))

tengah = ET*3 + PT*2 + PeT*1
barat = EB*3 + PB*2 + PeB*1

Tengah = "Pemenangnya adalah Jawa Tengah."
Barat = "Pemenangnya adalah Jawa Barat."
Imbang = "Jawa Tengah dan Jawa Barat masih imbang."

if tengah > barat:
	print(Tengah)
elif tengah < barat:
	print(Barat)
else:
	if ET > EB:
		print(Tengah)
	elif ET < EB:
		print(Barat)
	elif ET == EB:
		if PT > PB:
			print(Tengah)
		elif PT < PB:
			print(Barat)
		elif PT == PB:
			print(Imbang)
