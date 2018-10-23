# NIM/Nama  : 16518360/Ilham Syahid S
# Tanggal   : 22 Oktober 2018
# Deskripsi : Data Karyawan

import pandas as pd

df = pd.read_csv("stei-b-3.csv")

# 1. Banyaknya data
print(len(df))
#   9079

# 2. Data karyawan bernama Tuan Yon
print(df.loc[(df['nama'] == 'Tuan Yon')])
#             nama departemen  tahun_masuk  usia  golongan     gaji
#   2227  Tuan Yon  teknologi         2017    31        10  9939125

# 3. Banyaknya karyawan dengan usia kurang dari atau sama dengan 30
df3 = df.loc[(df['usia'] <= 30)]
print(len(df3))
#   1542

# 4. Banyaknya karyawan personalita dengan gaji di luar rentang 4-5 juta
df4 = df.loc[((df['gaji'] < 4000000) | (df['gaji'] > 5000000)) & ((df['departemen'] == 'personalia'))]
print(len(df4))
#   1122

# 5. Data karyawan produksi dengan gaji maksimum
df5 = df.loc[(df['departemen'] == 'produksi')]
df5 = df5.loc[(df5['gaji'] == df5['gaji'].max())]
print(df5)
#	                               nama departemen  tahun_masuk  usia  golongan     gaji
#	5047                Ario Nuswantoro   produksi         2014    36         3  9995982

# 6. Data 10 karyawan teknologi dengan gaji terbanyak. Jika ada gaji yang sama banyak, urutkan dari usia yang termuda
df6 = df.loc[(df['departemen'] == 'teknologi')]
df6 = df6.sort_values(['gaji', 'usia'], ascending=[0, 1])
print(df6[:10])
#	                         nama departemen  tahun_masuk  usia  golongan     gaji
#	3282   Jawahir Asy Mahdy Maro  teknologi         2015    26         1  9996959
#	8971         Vania Avviantari  teknologi         2015    35         1  9994946
#	4972               Brian Luas  teknologi         2014    26         1  9989154
#	6127       Tiara Fahiramadyan  teknologi         2014    46         1  9987370
#	6260               Vivi Novia  teknologi         2014    26         1  9986306
#	3739            Nana Restiana  teknologi         2016    37         1  9982168
#	8275  Rizkiyani Nadifa Puteri  teknologi         2015    26         1  9956570
#	3365         Zaki Abdurrasyid  teknologi         2013    50         1  9951235
#	7410     Made Santihayu Sukma  teknologi         2015    35         1  9944009
#	8194          Naufal Arifandy  teknologi         2013    42         1  9941846

# 7. Tabel frekuensi banyaknya karyawan tiap golongan
df7 = df['golongan'].value_counts()
print(df7)
#	9     945
#	6     927
#	5     925
#	2     913
#	8     908
#	7     905
#	1     903
#	3     902
#	4     876
#	10    875

# 8. Tabel frekuensi banyaknya karyawan tiap departemen yang masuk sebelum tahun 2015
df8 = df.loc[(df['tahun_masuk'] < 2015)]
df8 = df8['departemen'].value_counts()
print(df8)
#	keuangan       546
#	marketing      544
#	produksi       530
#	teknologi      522
#	kreatif        501
#	personalia     480
#	operasional    476

# 9. Rata-rata gaji seluruh karyawan
df9 = df['gaji'].mean()
print(df9)
#   5476321.027756361

# 10. Standar deviasi usia karyawan operasional 
df10 = df.loc[(df['departemen'] == 'operasional')]
df10 = df10[('usia')].std()
print(df10)
#   10.436347593016766

# 11. Dengan apakah gaji berkorelasi? Usia, tahun masuk, atau golongan? Tuliskan koefisien korelasinya
usia = df['gaji'].corr(df['usia'])
tahun_masuk = df['gaji'].corr(df['tahun_masuk'])
golongan = df['gaji'].corr(df['golongan'])

nilai_korelasi = [usia, tahun_masuk, golongan]
nama = ["usia.", "tahun masuk.", "golongan."]

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
    
print("Gaji lebih berkorelasi(terbalik/lurus) dengan " + nama[id]) # Cetak dengan apa(usia, tahun masuk, golongan) berkorelasi
print("Dengan nilai " + str(maks)) # dan cetak nilainya
#   Gaji lebih berkorelasi(terbalik/lurus) dengan golongan.
#   Dengan nilai -0.8708577012378015