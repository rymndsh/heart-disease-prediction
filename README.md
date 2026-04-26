# Peningkatan Akurasi Prediksi Penyakit Jantung Melalui Optimasi Hyperparameter pada Model Extreme Gradient Boosting (XGBoost) 🫀

Repositori ini berisi implementasi model *machine learning* untuk memprediksi risiko penyakit jantung menggunakan algoritma XGBoost. Proyek ini mencakup mulai dari pembersihan data, optimasi *hyperparameter*, hingga penyebaran (*deployment*) menjadi aplikasi web interaktif menggunakan Streamlit.

🌐 **Akses Aplikasi Web:** [https://heart-disease-prediction-900.streamlit.app/](https://heart-disease-prediction-900.streamlit.app/)

---

## 📋 Deskripsi Proyek
Tujuan utama dari proyek ini adalah untuk membangun model klasifikasi yang mampu menentukan apakah seseorang memiliki risiko penyakit jantung berdasarkan fitur-fitur medis tertentu. Penggunaan XGBoost dipilih karena performanya yang unggul dalam menangani data tabular, ditambah dengan proses optimasi untuk mendapatkan akurasi terbaik.

## 🛠️ Panduan Instalasi (Lokal)

Ikuti langkah-langkah di bawah ini untuk menjalankan proyek ini di perangkat kamu sendiri:

### 1. Persiapan Lingkungan
Pastikan kamu sudah menginstal **Python 3.8+** dan **Git**.

### 2. Clone Repositori
Buka terminal (CMD/PowerShell/Bash) dan jalankan perintah berikut:
```bash
git clone [https://github.com/rymndsh/heart-disease-prediction](https://github.com/rymndsh/heart-disease-prediction)
cd heart-disease-prediction

### 3. Membuat Virtual Environment (Sangat Disarankan)
Langkah ini penting agar *library* proyek ini tidak bentrok dengan proyek Python lainnya di komputermu. Jalankan perintah berikut:
```bash
# Pengguna Windows
python -m venv venv
venv\Scripts\activate

# Pengguna Mac/Linux
python3 -m venv venv
source venv/bin/activate
