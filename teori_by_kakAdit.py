import streamlit as st
import pickle
import numpy as np

# Judul Aplikasi
st.title("🌸 Prediksi Kategori Bunga Iris")
st.write("Masukkan nilai fitur di bawah ini untuk memprediksi jenis bunga Iris.")

# --- Load model ---
with open('Tugas_by_kak_adit.pkcls', 'rb') as file:   # ganti nama file sesuai punyamu
    model = pickle.load(file)

# --- Input data dari user ---
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)

# --- Tombol Prediksi ---
if st.button("Prediksi"):
    # Menyiapkan data input
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    
    # Prediksi menggunakan model
    prediction = model.predict(features)[0]

   
    label_map = {
        0: "Iris-setosa",
        1: "Iris-versicolor",
        2: "Iris-virginica"
    }

    # Kadang hasil prediksi bisa float (misal 0.0), jadi ubah ke int dulu
    prediction_label = label_map.get(int(prediction), "Tidak diketahui")

    # Menampilkan hasil prediksi
    st.success(f"🌼 Hasil Prediksi: **{prediction_label}**")

# --- Info tambahan ---
st.write("---")
st.caption("Dibuat dengan ❤️ menggunakan Streamlit & model Machine Learning Iris")

