# NIM/Nama  : 16518360/Ilham Syahid S
# Tanggal   : 9 September 2018
# Deskripsi : Warna

hue = int(input ("Masukkan nilai hue: "))

if hue >= 0 and hue <= 30:
 huae = "Red"
elif hue >= 31 and hue <= 90:
 huae = "Yellow"
elif hue >= 91 and hue <= 150:
 huae = "Green"
elif hue >= 151 and hue <= 210:
 huae = "Cyan"
elif hue >= 211 and hue <= 270:
 huae = "Blue"
elif hue >= 271 and hue <= 330:
 huae = "Magenta"
elif hue >= 331 and hue <= 360:
 huae = "Red"

print("Hue " + str(hue) + " merepresentasikan warna " + huae)