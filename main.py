import streamlit as st
import pandas as pd
import glob
import matplotlib.pyplot as plt


st.title('Dashboard Data Gempa 2015-2020')
st.write("Data gempa ini berisi informasi tentang gempa bumi yang terjadi di Asia selama periode 2015-2020. Data ini dikumpulkan dari Kemnaker dan mencakup kolom-kolom seperti Region, Tanggal, Magnitude, Lokasi, dan Kedalaman. Line chart yang ditampilkan menunjukkan frekuensi gempa di 5 region dengan frekuensi gempa tertinggi selama periode tersebut. Visualisasi ini bertujuan untuk menunjukkan region mana yang paling sering mengalami gempa bumi.")


def load_data():
    folder_path = 'data_gempa/'
    file_list = glob.glob(folder_path + '*.csv')
    df_list = []
    for file in file_list:
        df = pd.read_csv(file)
        df_list.append(df)
    df_gabungan = pd.concat(df_list, ignore_index=True)
    return df_gabungan


df_gempa = load_data()


frekuensi_gempa = df_gempa['Region'].value_counts()
frekuensi_gempa = frekuensi_gempa.head()

fig, ax = plt.subplots(figsize=(15, 5))
ax.plot(frekuensi_gempa.index, frekuensi_gempa.values)
ax.set_xlabel('Daerah')
ax.set_ylabel('Count')
ax.set_title('5 Daerah Yang Sering Terjadi Fenomena Gempa 2015 - 2020')


st.pyplot(fig)