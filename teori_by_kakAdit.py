import streamlit as st
import Orange
import pickle

# ===============================
#  LOAD MODEL
# ===============================
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# ===============================
#  JUDUL APLIKASI
# ===============================
st.title("🌸 Prediksi Kategori Iris (Model Orange)")

st.write("Masukkan nilai fitur untuk memprediksi jenis bunga iris:")

# ===============================
#  INPUT FITUR
# ===============================
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, step=0.1)
sepal_width  = st.number_input("Sepal Width (cm)",  min_value=0.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, step=0.1)
petal_width  = st.number_input("Petal Width (cm)",  min_value=0.0, step=0.1)

# ===============================
#  PREDIKSI
# ===============================
if st.button("🔮 Prediksi"):
    # Buat instance data sesuai model Orange
    input_data = Orange.data.Instance(model.domain, [sepal_length, sepal_width, petal_length, petal_width])
    
    # Lakukan prediksi
    prediction = model(input_data)

    st.success(f"🌼 Jenis Iris yang diprediksi: **{prediction}**")

st.write("---")
st.caption("Dibuat dengan ❤️ menggunakan Streamlit & Orange3")
