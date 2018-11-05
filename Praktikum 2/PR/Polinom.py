# Fungsi f
f = int(input("Masukan derajat f : ")) # Input jumlah derajat terbesar f
a = [ 0 for i in range(f+1)] #Menetapkan nilai dari indeks a dari x^f sampai x^0
for i in range(f+1): #Mengganti setiap nilai indeks menjadi yang diinginkan
    a[i] = int(input("Masukan koefisien x^" + str(f - i) + ": "))

# Fungsi g
# Menetapkan fungsi g seperti fungsi f
g = int(input("Masukan derajat g : ")) 
b = [ 0 for i in range(g+1)]
for i in range(g+1):
    b[i] = int(input("Masukan koefisien x^" + str(g - i) + ": "))

# Memproses nilai
hasil = [ 0 for i in range(f+g+1)]
for j in range(f+1):
    for k in range(g+1):
        hasil[j+k] += a[j]*b[k]

# Output
print("Hasil perkalian polinom:")
out = ""
for i in range(f+g+1): 
    if i == 0: # Derajat terbesar
        if hasil[i] >= 0: # Jika derajat terbesar positif
            out += str(hasil[0]) + "x^" + str(f+g) # Seperti 6x^3
        else: # Jika derajat terbesar negatif
            hasil[i] *= -1 # Membuatnya menjadi positif
            out += "- " # Menambah penanda sebagai negatif
            out += str(hasil[0]) + "x^" + str(f+g)
    else: # Selain derajat terbesar
        if hasil[i] >= 0: # Jika positif
            out += " + "
        else: # Jika negatif
            hasil[i] *= -1
            out += " - "
        out += str(hasil[i]) + "x^" + str(f+g-i)
    
print(out)