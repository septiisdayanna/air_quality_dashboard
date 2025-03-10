# Air Quality Dashboard ✨

Dashboard ini merupakan aplikasi berbasis Streamlit untuk menganalisis kualitas udara di Stasiun Tiantan berdasarkan data polutan seperti PM2.5, PM10, SO2, NO2, CO, dan O3. Dashboard ini memungkinkan pengguna untuk memfilter data berdasarkan rentang waktu dan menampilkan visualisasi data polutan berdasarkan waktu, musim, dan arah angin.

## Setup Environment - Anaconda
```
conda create --name air-quality-dashboard python=3.12
conda activate air-quality-dashboard
pip install -r requirements.txt
```


## Setup Environment - Shell/Terminal
```
mkdir air_quality_dashboard
cd air_quality_dashboard
pipenv install
pipenv shell
pip install -r requirements.txt
```


## Jalankan Aplikasi Streamlit
```
streamlit run dashboard.py
```


## Struktur Data
- *Datetime*: Waktu pengukuran polutan
- *PM2.5, PM10, SO2, NO2, CO, O3*: Konsentrasi masing-masing polutan
- *Season*: Musim saat data diambil
- *Time*: Waktu dalam format jam
- *Wind Direction (wd)*: Arah angin saat pengambilan data

## Fitur Dashboard
- *Visualisasi Konsentrasi Harian*: Grafik garis untuk melihat tren harian polutan yang dipilih
- *Analisis Berdasarkan Musim*: Grafik batang yang menunjukkan konsentrasi polutan per musim
- *Analisis Berdasarkan Waktu*: Grafik batang yang menunjukkan konsentrasi polutan berdasarkan jam
- *Analisis Berdasarkan Arah Angin*: Grafik batang untuk melihat hubungan arah angin dengan konsentrasi polutan

## Dependencies
Pastikan dependencies berikut telah terinstal:
```
pandas
matplotlib
seaborn
streamlit
babel
```
