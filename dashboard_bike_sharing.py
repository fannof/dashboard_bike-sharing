# -*- coding: utf-8 -*-
"""dashboard_bike-sharing.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u110mQuKdNch6-9uCR0E-D8ZIzMXB3_j
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

# Membaca dataset
data = pd.read_csv('hari_data.csv')

# Mengubah kolom 'dteday' menjadi tipe data datetime
data['dteday'] = pd.to_datetime(data['dteday'])

# Menambahkan kolom bulan dan tahun untuk analisis per bulan dan per tahun
data['bulan'] = data['dteday'].dt.month
data['tahun'] = data['dteday'].dt.year

# Mengubah kolom 'dteday' menjadi tipe data datetime
data['dteday'] = pd.to_datetime(data['dteday'])

# Menambahkan kolom bulan dan tahun untuk analisis per bulan dan per tahun
data['bulan'] = data['dteday'].dt.month
data['tahun'] = data['dteday'].dt.year

# Sidebar untuk pemilihan analisis
analisis_option = st.sidebar.selectbox(
    'Pilih Analisis:',
    ['Peminjaman per Bulan', 'Peminjaman per Tahun', 'Pengaruh Cuaca']
)

# Analisis peminjaman per bulan
if analisis_option == 'Peminjaman per Bulan':
    st.title('Dashboard Peminjaman Sepeda per Bulan')

    # Menghitung total peminjaman sepeda per bulan
    total_peminjaman_per_bulan = data.groupby(data['bulan'])['cnt'].sum()

    # Visualisasi peminjaman per bulan
    plt.figure(figsize=(12, 6))
    sns.barplot(x=total_peminjaman_per_bulan.index, y=total_peminjaman_per_bulan.values, color='skyblue')
    plt.xlabel('Bulan')
    plt.ylabel('Total Peminjaman Sepeda')
    st.pyplot()

# Analisis peminjaman per tahun
elif analisis_option == 'Peminjaman per Tahun':
    st.title('Dashboard Peminjaman Sepeda per Tahun')

    # Menghitung total peminjaman sepeda per tahun
    total_peminjaman_per_tahun = data.groupby(data['tahun'])['cnt'].sum()

    # Visualisasi peminjaman per tahun
    plt.figure(figsize=(10, 5))
    sns.barplot(x=total_peminjaman_per_tahun.index, y=total_peminjaman_per_tahun.values, color='green')
    plt.xlabel('Tahun')
    plt.ylabel('Total Peminjaman Sepeda')
    st.pyplot()

# Analisis pengaruh cuaca
elif analisis_option == 'Pengaruh Cuaca':
    st.title('Pengaruh Cuaca Terhadap Peminjaman Sepeda')

    # Menghitung rata-rata peminjaman sepeda untuk setiap jenis cuaca
    avg_peminjaman_per_cuaca = data.groupby('weathersit')['cnt'].mean()

    # Visualisasi pengaruh cuaca
    plt.figure(figsize=(8, 5))
    sns.barplot(x=avg_peminjaman_per_cuaca.index, y=avg_peminjaman_per_cuaca.values, palette='coolwarm')
    plt.xlabel('Jenis Cuaca')
    plt.ylabel('Rata-rata Peminjaman Sepeda')
    plt.title('Pengaruh Cuaca Terhadap Peminjaman Sepeda')
    st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)
st.caption('Copyright (c) Dicoding 2023')
