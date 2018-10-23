# NIM/Nama  : 16518360/Ilham Syahid S
# Tanggal   : 7 Oktober 2018
# Deskripsi : KPK

def fpb(a, b): #Fungsi FPB
    c = a%b #Sisa pembagian a dibagi b
    if c == 0: #Jika sisa pembagian 0 maka itulah FPBnya
        return b
    else:
        while c != 0: #Jika tak sama (contoh 8%6 = 2)
            a = b #maka a menjadi b 
            b = c #dan b menjadi sisa pembagian awal 
            c = a%b # seperti contol awal menjadi 6%2 = 0
        return b # pada contoh, hasil FPBnya adalah 2

def kpk(a,b,c): #Fungsi KPK=a*b/FPB(a,b)
    p = a*b 
    q = fpb(a,b)
    x = p/q
    y = int(x*c/fpb(x, c)) #karena pembagian akan menghasilkan float, maka diubah ke bilangan bulat
    return y
    
#input
A = int(input("Masukkan bilangan A: "))
B = int(input("Masukkan bilangan B: "))
C = int(input("Masukkan bilangan C: "))

#output
hasil = kpk(A, B, C)
print('KPK dari ' + str(A) + ', ' + str(B) + ' dan ' + str(C) + ' adalah ' + str(hasil)) 