# NIM/Nama  : 16518360/Ilham Syahid S
# Tanggal   : 22 Sept 2018
# Deskripsi : Stik

# Input jumlah stik Tuan Yon
Y = int(input("Masukkan banyaknya stik Tuan Yon : ")) 
a = [ 0 for i in range(Y)] #Menetapkan nilai dari setiap indeks a sejumlah stik Tuan Yon
print("Masukkan panjang stik Tuan Yon: ")
for i in range(Y): #Mengganti setiap nilai indeks menjadi yang diinginkan
    a[i] = int(input())

# Input jumlah stik Nyai Rin
R = int(input("Masukkan banyaknya stik Nyai Rin : ")) 
b = [ 0 for i in range(R)] #Menetapkan nilai dari setiap indeks b sejumlah stik Nyai Rin
print("Masukkan panjang stik Tuan Yon: ")
for i in range(R): #Mengganti setiap nilai indeks menjadi yang diinginkan
    b[i] = int(input())

# Input jumlah stik Tuan Mi
M = int(input("Masukkan banyaknya stik Tuan Mi : ")) 
c = [ 0 for i in range(M)] #Menetapkan nilai dari setiap indeks b sejumlah stik Nyai Rin
print("Masukkan panjang stik Tuan Mi: ")
for i in range(M): #Mengganti setiap nilai indeks menjadi yang diinginkan
    c[i] = int(input())

#Output
print("Daftar segitiga yang dapat dibuat:")
for i in a:
    for j in b:
        for k in c:
            if i + j > k and i + k > j and j + k > i: # Keadaan dimana a+b>c, a+c>b, b+c>a
                print(str(i) + " " + str(j) + " " + str(k)) # Print output