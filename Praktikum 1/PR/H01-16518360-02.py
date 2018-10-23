# NIM/Nama  : 16518360/Ilham Syahid S
# Tanggal   : 9 September 2018
# Deskripsi : Alarm

print("Masukkan waktu sekarang!")

JA = int(input("Jam   : "))
MA = int(input("Menit : "))
DA = int(input("Detik : "))

print("Masukkan waktu alarm!")

JS = int(input("Jam   : "))
MS = int(input("Menit : "))
DS = int(input("Detik : "))

Jam = JS - JA
Menit = MS - MA
Detik = DS - DA

if Detik < 0:
	Detik %= 60
	Menit -= 1

if Menit < 0:
	Menit %= 60
	Jam -= 1

if Jam < 0:
	Jam %= 24

print ("Alarm akan berbunyi dalam " + str(Jam) + " jam " + str(Menit) + " menit " + str(Detik) + " detik lagi.")
