# NIM/Nama  : 16518360/Ilham Syahid S
# Tanggal   : 7 Oktober 2018
# Deskripsi : Pasangan Komposit

'''
    Tuan Yon baru tahu mengenai bilangan komposit. Sesuai namanya, bilangan komposit adalah bilangan yang
    dapat dibuat dengan mengalikan dua bilangan lain selain 1 dan bilangan itu sendiri. Secara singkat, kita
    dapat menyebut bilangan komposit sebagai bilangan bukan prima, namun ingat juga kalau 1 bukan bilangan
    komposit.
    
    Tuan Yon memiliki dua bilangan A dan B. Kini ia ingin mencari PrimaPrima. Pasangan bilangan komposit adalah
    bilangan x dan y sehingga A ≤ x, y ≤ B dan x + y merupakan bilangan komposit. Perhatikan contoh berikut:
    
    • 6 dan 9 merupakan bilangan komposit dan 6 + 9 = 15 juga merupakan bilangan komposit, maka 6 dan 9
    adalah pasangan bilangan komposit
    • 4 dan 15 merupakan bilangan komposit namun 4 + 15 = 19 bukan bilangan komposit, maka 4 dan 15
    bukan pasangan bilangan komposit
    • 2 dan 7 bukan bilangan komposit, jadi meskipun 2 + 7 = 9 merupakan bilangan komposit, 2 dan 7 tetap
    bukan pasangan bilangan komposit
'''
def Komposit(x): #Fungsi apakah x adalah komposit
    isTrue = False
    i = 2
    while x > i and not isTrue: # Pertama akan masuk while
        if x % i == 0: # Jika ada yang sisa bagi 0, maka itu adalah komposit, jika bersisa hingga x-1 maka bil. itu adalah prima
            isTrue = True # Jika diketahui bil. komposit maka setelah putaran selanjutnya tidak akan masuk while
        i += 1 
    return isTrue

def PasanganKom(a, b): #Fungsi apakah pasangan komposit
    if Komposit(a) and Komposit(b) and Komposit(a+b): # jika a, b, a+b lulus fungsi Komposit
        return True # maka dinyatakan pasangan komposit

#input
a = int(input("Masukkan A: "))      
b = int(input("Masukkan B: "))      

#output
print("Pasangan bilangan komposit:")
for i in range(a, b+1): # Cek bil. dari a hingga b  
    for j in range(a, b+1):
        if PasanganKom(i,j) and i < j: # Cek bil. tersebut pasangan komposit dan yang pertama harus lebih kecil dari yang kedua 
            print(i, j) #print