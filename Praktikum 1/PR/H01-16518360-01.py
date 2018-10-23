# NIM/Nama  : 16518360/Ilham Syahid S
# Tanggal   : 9 September 2018
# Deskripsi : Warung Indomie

bayar = 0

print ("Menu makanan:") 
print ("1. Indomie Single") 
print ("2. Indomie Double") 
print ("3. Indomie Telor") 
makanan = int(input("Masukkan nomor menu makanan: "))

print ("Menu minuman:") 
print ("1. Air Putih") 
print ("2. Teh Manis") 
print ("3. Kopi") 
minuman = int(input("Masukkan nomor menu minuman: "))

if (makanan == 1):
	bayar += 4000
elif (makanan == 2):
	bayar += 8000
elif (makanan == 3):
	bayar += 7000

if (minuman == 1):
	bayar += 0
elif (minuman == 2):
	bayar += 2000
elif (minuman == 3):
	bayar += 4000
	
print ("Biaya yang harus dibayarkan: " + str(bayar))
