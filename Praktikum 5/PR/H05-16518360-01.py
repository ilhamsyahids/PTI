# NIM/Nama  : 16518360/Ilham Syahid S
# Tanggal   : 04 November 2018
# Deskripsi : Kendaraan Mahasiswa

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('stei-b-1.csv')


#1. Banyaknya data (poin 0)
print(len(df))
# 9312

#2. Pie chart banyaknya mahasiswa tiap kendaraan yang digunakan untuk berangkat ke kampus.
df2 = df['kendaraan'].value_counts()
df2.plot(kind='pie', title='Kendaraan')
plt.show()

#3. Pie chart banyaknya mahasiswa tiap tingkat yang berjalan kaki.
df3 = df.loc[(df['kendaraan'] == 'jalan kaki')]['tingkat'].value_counts()
#df3 = df3['tingkat']
#print(df3)
df3.plot(kind="pie", title='Mahasiswa Tiap Tingkat yang Berjalan Kaki')
plt.show()
#   df3.plot(kind='pie')
#plt.show()

#4. Histogram dengan tingkat sebagai sumbu x dan jumlah mahasiswa sebagai sumbu y
df[["tingkat"]].plot(kind="hist",title='Histogram Jumlah Mahasiswa Tiap Tingkat',rwidth=1)
plt.show()

#5. Berdasar plot sebelumnya, angkatan berapa yang jumlah mahasiswanya paling banyak?
#Angkatan yang jumlah mahasiswa paling banyak adalah 2016

#6. Stacked bar chart dengan tingkat sebagai sumbu x dan jumlah mahasiswa tiap kendaraan sebagai stacked sumbu y
df6 = df.groupby(["tingkat","kendaraan"])["nama"].size().unstack()
df6.plot(kind="bar",stacked=True,title='Jumlah Mahasiswa Pemakai Kendaraan Tiap Tingkat')
plt.show()


#7. Berdasar plot sebelumnya, sebutkan trend kendaraan transportasi tiap tingkat!
#Pada tingkat 2015, trend kendaraannya adalah motor
#Pada tingkat 2016, trend kendaraannya adalah motor
#Pada tingkat 2017, trend kendaraannya adalah angkot
#Pada tingkat 2018, trend kendaraannya adalah jalan kaki

#8. Line chart dengan tingkat sebagai sumbu x dan jumlah mahasiswa sebagai sumbu y
df.groupby(["tingkat"])['nama'].size().plot(kind="line", title='Line Chart Jumlah Mahasiswa')
plt.show()


#9. Line chart seperti soal sebelumnya, namun terdapat 4 garis, masing-masing untuk tiap kendaraan
df6 = df.groupby(["tingkat","kendaraan"]).size().unstack()
df6.plot(kind="line")
plt.show()


#10. Berdasar plot sebelumnya, apa kendaraan yang penggemarnya terus bertambah?
#Berdasarkan plot sebelumnya kendraan yang penggemarnya terus bertambah adalah angkot

#11. Berdasar plot sebelumnya, apa kendaraan yang penggemarnya terus menurun?
#Berdasarkan plot sebelumnya kendraan yang penggemarnya terus menurun adalah motor

