import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from joblib import dump, load
import streamlit as st
from openai import OpenAI

# st.set_page_config(page_title="PREDIKSI TINGKAT STRES", layout="wide")

def show_prediction():
    # Load dataset
    data = pd.read_csv('pages/student_lifestyle_dataset.csv')

    # Menambah fitur Study-Sleep Ratio (menghindari pembagian dengan nol)
    data['Study_Sleep_Ratio'] = data['Study_Hours_Per_Day'] / (data['Sleep_Hours_Per_Day'] + 1)

    # Fitur dan target
    X = data[['Study_Hours_Per_Day', 'Sleep_Hours_Per_Day', 
            'Physical_Activity_Hours_Per_Day', 'GPA', 'Study_Sleep_Ratio']]
    y = data['Stress_Level']

    # Encode target
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    # Normalisasi data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split data untuk training dan testing
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

    # Training model dengan RandomForestClassifier
    model = RandomForestClassifier(random_state=42, n_estimators=100)
    model.fit(X_train, y_train)

    # Menyimpan model dan scaler
    dump(model, 'modelku_rf.sav')
    dump(scaler, 'scaler_rf.sav')
    dump(label_encoder, 'label_encoder_rf.sav')

    # Load kembali model, scaler, dan label encoder
    model = load('modelku_rf.sav')
    scaler = load('scaler_rf.sav')
    label_encoder = load('label_encoder_rf.sav')

    # Judul aplikasi
    st.title("🎯 Prediksi Tingkat Stres Berdasarkan Gaya Hidup")

    # Membuat dua kolom
    col1, col2 = st.columns([2, 1])

    with col1:
        # Form input pengguna
        keluhan = st.text_area("Masukkan Keluhan Anda")
        jam_belajar = st.number_input('Jam Belajar per Hari', min_value=0.0, max_value=24.0, step=0.1)
        jam_tidur = st.number_input('Jam Tidur per Hari', min_value=0.0, max_value=24.0, step=0.1)
        aktivitas_fisik = st.number_input('Jam Aktivitas Fisik per Hari', min_value=0.0, max_value=24.0, step=0.1)
        nilai_gpa = st.slider('Nilai GPA', 0.0, 4.0, step=0.01)

        if st.button('Prediksi'):
            # Menghitung rasio belajar dan tidur
            study_sleep_ratio = jam_belajar / (jam_tidur + 1)

            # Menyiapkan data untuk prediksi
            input_data = [[jam_belajar, jam_tidur, aktivitas_fisik, nilai_gpa, study_sleep_ratio]]
            input_data_scaled = scaler.transform(input_data)

            # Melakukan prediksi
            prediction_encoded = model.predict(input_data_scaled)
            prediction_label = label_encoder.inverse_transform(prediction_encoded)

            # Menampilkan hasil prediksi
            st.success(f"✨ Tingkat Stres Anda: **{prediction_label[0].upper()}**")
            st.markdown("**Keterangan Tingkat Stres:**\n- **High**: Tinggi\n- **Moderate**: Sedang\n- **Low**: Rendah")

            # Konsultasi menggunakan OpenAI
            if "messages" not in st.session_state:
                st.session_state["messages"] = [{"role": "system", "content": "Saya adalah seorang ahli kesehatan mental."}]

            user_prompt = (
                f"Pengguna mengeluhkan '{keluhan}'. Dengan {jam_belajar} jam belajar, "
                f"{jam_tidur} jam tidur, dan nilai GPA {nilai_gpa}, kemungkinan stres pengguna adalah {prediction_label[0]}."
                " Berikan saran untuk membuat gaya hidup sesuai dan ideal"
            )
            st.session_state.messages.append({"role": "user", "content": user_prompt})

            client = OpenAI(base_url="https://api.electronhub.top/v1/", api_key="ek-SnjqmE0dzQ4A3nesT9hV4kddgC4bwXGHH3Q9iiFHIhIRodeSpk")
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages
            )
            ai_response = response.choices[0].message.content
            st.session_state.messages.append({"role": "system", "content": ai_response})
            st.chat_message("system").write(ai_response)

    with col2:
        st.markdown("""<div style="margin-top: 50px;"> </div>""", unsafe_allow_html=True)
        st.image("oo.png", caption="Ilustrasi Tingkat Stres")
        st.info("""
        ✨ **Petunjuk Penggunaan:**  
        1. Masukkan *keluhan Anda* di kotak teks.  
        2. Isi jumlah *jam belajar, **jam tidur, dan **aktivitas fisik per hari* di kolom angka.  
        3. Pilih *GPA* Anda dengan menggeser slider.  
        4. Klik tombol **"Predict"** untuk melihat hasil prediksi tingkat stres.  
        5. Lihat hasil prediksi dan saran yang diberikan oleh AI untuk mengelola stres Anda.  

        💡 Selamat mencoba dan semoga bermanfaat!
        """)

