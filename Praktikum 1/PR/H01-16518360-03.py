# NIM/Nama  : 16518360/Ilham Syahid S
# Tanggal   : 9 September 2018
# Deskripsi : Asian Games 2 provinsi + Jakarta = 3 provinsi

ET = int(input("Masukkan perolehan emas Jawa Tengah: "))
PT = int(input("Masukkan perolehan perak Jawa Tengah: "))
PeT = int(input("Masukkan perolehan perunggu Jawa Tengah: "))

EB = int(input("Masukkan perolehan emas Jawa Barat: "))
PB = int(input("Masukkan perolehan perak Jawa Barat: "))
PeB = int(input("Masukkan perolehan perunggu Jawa Barat: "))

EJ = int(input("Masukkan perolehan emas DKI Jakarta: "))
PJ = int(input("Masukkan perolehan perak DKI Jakarta: "))
PeJ = int(input("Masukkan perolehan perunggu DKI Jakarta: "))

tengah = ET*3 + PT*2 + PeT*1
barat = EB*3 + PB*2 + PeB*1
jakarta = EJ*3 + PJ*2 + PeJ*1

Tengah = "Jawa Tengah."
Barat = "Jawa Barat."
Jakarta = "DKI Jakarta."

Menang = ""


if tengah == barat and barat == jakarta:
    if ET == EB and EB == EJ:
        if PT == PB:
            Menang = Jakarta
            
        elif PB == PJ:
            Menang = Tengah
            
        elif PJ == PT:
            Menang = Barat
            
        elif PT > PB:
            if PJ > PT:
                Menang = Jakarta
            else:
                Menang = Tengah
                
        else:
            if PJ > PB:
                Menang = Jakarta
            else:
                Menang = Barat
    
    elif EB == EJ:
        if ET > EB:
            Menang = Tengah
        else:
            if PB > PJ:
                Menang = Barat
            else:
                Menang = Jakarta
                
    elif ET == EB:
        if EJ > ET:
            Menang = Jakarta
        else:
            if PT > PB:
                Menang = Tengah
            else:
                Menang = Barat
                
    elif EJ == ET:
        if EB > EJ:
            Menang = Barat
        else:
            if PJ > PT:
                Menang = Jakarta
            else:
                Menang = Tengah
    elif ET > EB:
        if EJ > ET:
            Menang = Jakarta
        else:
            Menang = Tengah
            
    else:
        if EJ > EB:
            Menang = Jakarta
        else:
            Menang = Barat


elif barat == jakarta:
    if tengah > barat:
        Menang = Tengah
        
    elif EB == EJ:
        if PB > PJ:
            Menang = Barat
        else:
            Menang = Jakarta
            
    elif EB > EJ:
        Menang = Barat
        
    else:
        Menang = Jakarta
        
        
elif jakarta == tengah:
    if barat > jakarta:
        Menang = Barat
        
    elif EJ == ET:
        if PJ > PT:
            Menang = Jakarta
        else:
            Menang = Tengah
            
    elif EJ > ET:
        Menang = Jakarta
        
    else:
        Menang = Tengah
        
        
elif tengah == barat:
    if jakarta > tengah:
        Menang = Jakarta
        
    elif ET == EB:
        if PT > PB:
            Menang = Tengah
        else:
            Menang = Barat
            
    elif ET > EB:
        Menang = Tengah
        
    else:
        Menang = Barat
        
        
elif tengah > barat: 
    if jakarta > tengah:
        Menang = Jakarta
        
    else:
        Menang = Tengah
        
        
else:
    if jakarta > barat:
        Menang = Jakarta
        
    else:
        Menang = Barat


print("Pemenangnya adalah " + Menang)
