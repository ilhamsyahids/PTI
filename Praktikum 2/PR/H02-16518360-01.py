# NIM/Nama  : 16518360/Ilham Syahid S
# Tanggal   : 22 Sept 2018
# Deskripsi : Nilai FPB

# Input jumlah fakultas yang tersedia
jumlah = int(input("Masukkan jumlah fakultas : ")) 
a = [ 0 for i in range(jumlah)] #Menetapkan nilai dari indeks a sejumlah fakultas yang tersedia
for i in range(jumlah): #Mengganti setiap nilai indeks menjadi yang diinginkan
    a[i] = int(input("Jumlah mahasiswa dari fakultas " + str(i+1) + ": "))

#Misal nilai fpb pada indeks nol, bebas pilih, karena nilai FPB tidak akan lebih besar daripada nilai yang sudah ditetapkan
fpb = a[0]

#Menetapkan nilai isTrue
isTrue = True
for i in a: #Menetapkan i sebagai nilai di array a
    if i % fpb != 0: #Jika setiap nilai pada indeks tidak sama dengan 0 yang artinya adalah bilangan itu bukan FPB
        isTrue = False # Maka akan False, jika sama dengan nol untuk semua bilangan, maka itu adalah FPBnya

while not isTrue: # Masuk kondisi while jika (not) False
    fpb -= 1 # Mengurangi nilai FPB hingga menjadi nilai FPBnya
    isTrue = True # Menetapkan nilai semula isTrue
    for i in a:
        if i % fpb != 0: # Sama seperti kondisi diatas, jika untuk semua nilai pada array a modulo nya nol maka kondisi ini tidak akan terpenuhi, sehingga itu menjadi FPBnya
            isTrue = False #Jika masih tidak sama dengan nol kembali ke kondisi while hingga didapat nilai FPB

#Nilai output dan print nilai output
out = "Jumlah anggota tim terbanyak yang mungkin adalah " + str(fpb)
print(out)    