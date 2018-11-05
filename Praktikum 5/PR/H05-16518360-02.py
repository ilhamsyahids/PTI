# NIM/Nama  : 16518360/Ilham Syahid S
# Tanggal   : 05 November 2018
# Deskripsi : Kesehatan Mahasiswa

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('stei-b-2.csv')

#1. Banyaknya data (poin 0)
print(len(df))
# 9023

#2. Pie chart banyaknya mahasiswa tiap gender.
df['gender'].value_counts().plot(kind='pie', title='Gender')
plt.show()

#3. Berdasarkan plot sebelumnya, gender mana yang lebih mayoritas?
# Gender yang lebih mayoritas adalah M(male)

#4. Bar chart dengan fakultas sebagai sumbu x dan jumlah mahasiswa dengan tinggi di atas 160 sebagai sumbu y.
df4 = df.loc[(df['tinggi'] > 160)]
df4.groupby(["fakultas"])["nama"].size().plot(kind='bar', title='Bar Chart Fakultas dan Jumlah Mahasiswa dengan Tinggi diatas 160')
plt.show()

#5. Histogram dengan tinggi sebagai sumbu x dan jumlah mahasiswa laki-laki sebagai sumbu y.
df5 = df.loc[(df['gender'] == 'M')]
df5['tinggi'].plot(kind='hist',rwidth=1, title='Histogram Tinggi dan Jumlah Mahasiswa Laki-Laki')
plt.show()

#6. Stacked bar chart dengan fakultas sebagai sumbu x dan jumlah mahasiswa tiap gender sebagai stacked sumbu y.
df6 = df.groupby(["fakultas","gender"])["nama"].size().unstack()
df6.plot(kind="bar",stacked=True,title='Jumlah Mahasiswa Tiap Gender Dengan Fakultas')
plt.show()

#7. Berdasar plot sebelumnya, fakultas mana yang rasio mahasiswa perempuannya paling banyak dibanding fakultas lain?
# Fakultas yang rasio perempuannya paling banyak dibandingkan fakultas lain adalah SITHR

#8. Line chart dengan berat badan sebagai sumbu x dan jumlah mahasiswa sebagai sumbu y.
df.groupby(["berat"])['nama'].size().plot(kind="line", title='Line Chart Berat Badan')
plt.show()

#9. Line chart seperti soal sebelumnya, namun terdapat 2 garis, masing-masing untuk tiap gender.
df.groupby(["berat", 'gender'])['nama'].size().unstack().plot(kind="line", title='Line Chart Berat Badan Tiap Gender')
plt.show()

#10. Berdasar plot sebelumnya, gender manakah yang cenderung memiliki berat lebih ringan?
# Gender yang cenderung memiliki berat lebih ringan adalah F(Female)

#11. Scatter plot dengan berat badan sebagai sumbu x dan tinggi badan sebagai sumbu y
df.plot.scatter(x='berat',y='tinggi', title='Scatter Plot Berat Badan dan Tinggi Badan')
plt.show()
