# NIM/Nama  : 16518360/Ilham Syahid S
# Tanggal   : 21 Oktober 2018
# Deskripsi : Data Mahasiswa

import pandas as pd

df = pd.read_csv("stei-b-1.csv")

# 1. Banyaknya data
print(len(df))
#   9628

# 2. Nilai matematika, fisika dan kimia dari mahasiswa bernama Tuan Yon
print(df.loc[df['nama'] == 'Tuan Yon'])
#             nama fakultas  nilai_mat  nilai_fis  nilai_kim
#   8404  Tuan Yon     STEI         91         83         63

# 3. Banyaknya mahasiswa yang mendapat nilai matematika di atas 80
df3 = (df.loc[df['nilai_mat'] > 80])
print(len(df3))
#   2789

# 4. Banyaknya mahasiswa yang mendapat nilai kurang dari 40 di matkul apapun
df4 = (df.loc[(df['nilai_mat'] < 40) | (df['nilai_fis'] < 40) | (df['nilai_kim'] < 40)])
print(len(df4))
#   4351

# 5. Banyaknya mahasiswa yang mendapat nilai terendah di fisika
df5 = df.loc[df['nilai_fis'] == df['nilai_fis'].min()]
print(len(df5))
#   126

# 6. Data 10 besar peserta peraih nilai tertinggi di fisika. Jika ada yang nilainya sama, ambil mahasiswa dengan nama lebih kecil
df6 = df.sort_values(['nilai_fis',"nama"], ascending=[0, 1])
print(df6[:10])
#                           nama fakultas  nilai_mat  nilai_fis  nilai_kim
#   1905           Abdillah Aziz     FTMD         59         99         23
#   3489  Agatha Nabilla Lestari     STEI         33         99         81
#   5087    Ahmad Zahi Ulul Azmi     FTMD         41         99         81
#   2822          Aidah Fithriah     FTMD         85         99         81
#   1431                  Albert     FTMD         80         99         25
#   5317        Alexander Sukono     FTMD         54         99         81
#   6169            Alfred Andry     STEI         94         99         81
#   7403    Alief Rizky Ramadhan    SITHR         90         99         81
#   3046   Alwidya Angga Safitri     FTSL         40         99         81
#   7060  Alyssa Nadhira Windari     FTMD         46         99         81

# 7. Tabel Frekuensi masing-masing fakultas
print(df["fakultas"].value_counts())
#   FTSL     2475
#   STEI     2416
#   SITHR    2376
#   FTMD     2361

# 8. Rata-rata dari nilai matematika semua mahasiswa
print(df['nilai_mat'].mean())
#   65.24293726630661

# 9. Standar deviasi dari nilai fisika semua mahasiswa
print(df['nilai_fis'].std())
#   25.7295023400875

# 10. Rata-rata dari nilai kimia STEI
df10 = df.loc[(df['fakultas'] == "STEI")]
print(df10['nilai_kim'].mean())
#   50.226407284768214

# 11. Dengan nilai manakah (matematika / kimia) nilai fisika berkorelasi? Berapa koefisien korelasinya?
# Membuat masing-masing nilai korelasi
matematika = (df["nilai_mat"].corr(df["nilai_fis"]))
kimia = (df["nilai_kim"].corr(df["nilai_fis"]))
nilai_korelasi = [matematika, kimia]
matkul = ["matematika.", "kimia."]

# Menentukan nilai korelasi dan namanya
isTrue = False # Inisiasi awal untuk masuk looping
while not isTrue:
    maks = -1 # Tetapkan nilai maks -1, karena tidak akan kurang dari -1
    id = 0 # Misal awal letak nilai maks
    for i in range(len(nilai_korelasi)): # Looping sebanyak jumlah nilai_korelasi
        if abs(nilai_korelasi[i]) >= maks: # Jika lebih dari atau sama dengan nilai maks 
            maks = nilai_korelasi[i] # tetapkan nilai baru maks
            id = i # ingat juga dimana letak nilai maks nya
    isTrue = True

print("Nilai fisika lebih berkorelasi(terbalik/lurus) dengan " + matkul[id]) # Cetak matkul apa
print("Dengan nilai " + str(maks)) # dan cetak nilainya
# Nilai fisika lebih berkorelasi(terbalik/lurus) dengan kimia.
# Dengan nilai 0.8246142287210513