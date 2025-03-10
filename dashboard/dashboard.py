import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
import os

sns.set(style='dark')

# create_polutan_daily_df() digunakan untuk menyiapkan polutan_daily_df 
def create_polutan_daily_df(df, polutan):
    polutan_daily_df = df.resample(rule='D', on='datetime').agg({
        polutan: "sum"   # Menghitung jumlah nilai unik pada polutan yang dipilih
    })
    polutan_daily_df = polutan_daily_df.reset_index()
    return polutan_daily_df

# create_byseason_df() digunakan untuk menyiapkan byseason_df 
def create_byseason_df(df, polutan):
    byseason_df = df.groupby(by="season")[polutan].sum().reset_index()
    return byseason_df


# create_bytime_df() digunakan untuk menyiapkan bytime_df 
def create_bytime_df(df, polutan):
    bytime_df = df.groupby(by="time")[polutan].sum().reset_index()
    return bytime_df 


# create_bywd_df() digunakan untuk menyiapkan bywd_df 
def create_bywd_df(df, polutan):
    bywd_df = df.groupby(by="wd")[polutan].sum().reset_index()
    return bywd_df   

# Fungsi untuk mencari warna berdasarkan nilai terbesar
def highlight_max(data):
    colors = ["#90CAF9"] * len(data)
    max_index = data.idxmax()
    colors[max_index] = "#1E88E5"  # Warna biru terang untuk nilai tertinggi
    return colors

# Load berkas
file_path = os.path.join("dashboard", "main_data.csv")
all_df = pd.read_csv(file_path)

# Membuat kolom datetime dari year, month, day, hour
all_df["datetime"] = pd.to_datetime(all_df[['year', 'month', 'day']])

# Sidebar untuk filter
min_date = all_df["datetime"].min()
max_date = all_df["datetime"].max()

with st.sidebar:
    st.image("LOGO.png")

    # Widget filter polutan
    polutan_list = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
    selected_polutan = st.selectbox("Pilih Polutan:", polutan_list)

    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Pilih Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )


# Filter data berdasakan tanggal dan disimpan di variabel main_df
main_df = all_df[
    (all_df["datetime"] >= str(start_date)) & 
    (all_df["datetime"] <= str(end_date))
]

# Filter data berdasakan polutan dan disimpan di variabel polutan_df
polutan_df = main_df[["datetime", selected_polutan]]

# Memanggil helper function yang telah dibuat sebelumnya dan memberikan argument dari hasil filter tanggal dan polutan
polutan_daily_df = create_polutan_daily_df(main_df, selected_polutan)
byseason_df = create_byseason_df(main_df, selected_polutan)
bytime_df = create_bytime_df(main_df, selected_polutan)
bywd_df = create_bywd_df(main_df, selected_polutan)

# VISUALISASI DATA
# Judul Dashboard 
st.header('Air Quality in Tiantan Dashboard :sparkles:')

# subjudul dashboard
st.write(f"### Data Polutan '{selected_polutan}' dari {start_date} hingga {end_date}")
result_df = create_polutan_daily_df(main_df, selected_polutan) # Menampilkan hasil berdasarkan filter

# Menampilkan total konsentrasi polutan terpilih
total_polutan = polutan_df[selected_polutan].sum()
st.metric("Total Konsentrasi Polutan", value=total_polutan)
 
# Visualisasi daily polutan 
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    polutan_daily_df["datetime"],  #x: Waktu
    polutan_daily_df[selected_polutan],  #y: Polutan yang dipilih
    marker="o",
    linewidth=2,
    color="#1E88E5",
    alpha=0.8,
    label=f"Konsentrasi {selected_polutan}"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

# Visualisasi data polutan berdasarkan musim
colors = highlight_max(byseason_df[selected_polutan])
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
    y=selected_polutan, 
    x="season",
    data= byseason_df,
    palette=colors,
    ax=ax
)
ax.set_title(f"Konsentrasi {selected_polutan} Berdasarkan Musim", fontsize=22)
ax.set_xlabel("Musim", fontsize=18)
ax.set_ylabel("Konsentrasi", fontsize=18)
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)
st.pyplot(fig)

# Visualisasi data polutan berdasarkan waktu
colors = highlight_max(bytime_df[selected_polutan])
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
    y=selected_polutan, 
    x="time",
    data= bytime_df,
    palette=colors,
    ax=ax
)
ax.set_title(f"Konsentrasi {selected_polutan} Berdasarkan Waktu", fontsize=22)
ax.set_xlabel("Waktu", fontsize=18)
ax.set_ylabel("Konsentrasi", fontsize=18)
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)
st.pyplot(fig)

# Visualisasi data polutan berdasarkan arah angin
colors = highlight_max(bywd_df[selected_polutan])
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
    y=selected_polutan, 
    x="wd",
    data= bywd_df,
    palette=colors,
    ax=ax
)
ax.set_title(f"Konsentrasi {selected_polutan} Berdasarkan Arah Angin", fontsize=22)
ax.set_xlabel("Arah Angin", fontsize=18)
ax.set_ylabel("Konsentrasi", fontsize=18)
ax.tick_params(axis='x', labelsize=16, rotation=45)
ax.tick_params(axis='y', labelsize=16)
st.pyplot(fig)
