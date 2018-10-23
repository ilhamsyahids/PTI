# NIM/Nama  : 16518360/Ilham Syahid S  
# Tanggal   : 17 Okto 2018
# Deskripsi : STEI-B data

import pandas as pd

df = pd.read_csv ("stei-b.csv")

# 1. Banyaknya data
print(len(df))
# 10000

print()

# 2. Transaksi yang dilakukan oleh Tuan Yon
print(df.loc[4393, "tipe_barang"])
#elektronik

print()

# 3. Banyaknya transaksi dengan profit di atas 150.000
c = df.loc[(df["profit"] > 150000)]
print(len(c))
#2656

print()

# 4. Banyaknya transaksi di bulan Oktober 2014 dengan quantitiy kurang dari 10
a = df.loc [(df["tahun"] == 2014) & (df["qty"] > 10)]
print(len(a))
#598

print()

# 5. Banyaknya transaksi makanan dengan profit minimum
b = df.loc [(df["tipe_barang"] == "makanan") & (df["profit"] == df["profit"].min())]
print(len(b))
#1260

# 6. Data 10 transaksi alat makan dengan profit terbesar di tahun 2017
d = df.loc [(df["tipe_barang"] == "alat makan") & (df["profit"] == df["profit"].min()) & (df["tahun"] == 2017)]
print(d[:10])

# 7. Tabel frekuensi masing-masing tahun
print(df["tahun"].value_counts())

# 8. Rata-rata profit di bulan Desember 2016
#rata2016 = df.loc [df["profit"].mean() & df["tahun"] == 2016] 
print(df["profit"].mean())

# 11. Koefisien korelasi dari quantity dengan profit
print(df["quantity"].corr["profit"])