# NIM/Nama  : 16518360/Ilham Syahid S
# Tanggal   : 7 Oktober 2018
# Deskripsi : Pasangan Prima

def Prima(n): #Fungsi apakah n adalah prima
    isTrue = True
    for j in range(2, n): #Jika bilangan itu ada yang habis dibagi, maka bukan bil. prima
        if n%j == 0:
            isTrue = False 
    if n == 1: #1 tidak termasuk bil. prima 
        isTrue = False
    if isTrue:
        return isTrue # mengembalikan nilai jika prima
    
def PasPrim(a, b): #Fungsi apakah pasangan prima. Contoh: 1, 5
    c = int(str(a)+str(b)) # c bil. ab yang di satukan. Contoh: 15
    if Prima(a) and Prima(b) and Prima(c): # jika a, b, c lulus fungsi prima
        return True # maka dinyatakan pasangan prima

#input
a = int(input("Masukkan A: "))      
b = int(input("Masukkan B: "))      

#output
print("Pasangan bilangan prima:")
for i in range(a, b+1): # Cek bil. dari a hingga b  
    for j in range(a, b+1):
        if PasPrim(i,j): # Cek bil. tersebut pasangan komposit dan yang pertama harus lebih kecil dari yang kedua 
            print(i, j) #print