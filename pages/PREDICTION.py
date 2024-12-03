import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from joblib import dump, load
import streamlit as st
from openai import OpenAI

# Load the dataset
data = pd.read_csv('pages/student_lifestyle_dataset.csv')

# Add feature for Study-Sleep Ratio
data['Study_Sleep_Ratio'] = data['Study_Hours_Per_Day'] / (data['Sleep_Hours_Per_Day'] + 1)

# Features and target
X = data[['Study_Hours_Per_Day', 'Sleep_Hours_Per_Day', 'Physical_Activity_Hours_Per_Day', 'GPA', 'Study_Sleep_Ratio']]
y = data['Stress_Level']

# Encode target labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data for training and validation
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(random_state=42, n_estimators=100)
model.fit(X_train, y_train)

# Save model, scaler, and encoder
dump(model, 'modelku_rf.sav')
dump(scaler, 'scaler_rf.sav')
dump(label_encoder, 'label_encoder_rf.sav')

# Load model, scaler, and encoder for prediction
model = load('modelku_rf.sav')
scaler = load('scaler_rf.sav')
label_encoder = load('label_encoder_rf.sav')

# Streamlit application
st.title("PREDIKSI TINGKAT STRES BERDASARKAN GAYA HIDUP")

# OpenAI Client
client = OpenAI(base_url="https://api.electronhub.top/v1/", api_key="ek-SnjqmE0dzQ4A3nesT9hV4kddgC4bwXGHH3Q9iiFHIhIRodeSpk")

# Input fields
keluhan = st.text_area("Masukan Keluhan Anda...")
jam_belajar = st.number_input('Study Hours Per Day', min_value=0.0, max_value=24.0, step=0.1)
jam_tidur = st.number_input('Sleep Hours Per Day', min_value=0.0, max_value=24.0, step=0.1)
aktivitas_fisik = st.number_input('Physical Activity Hours Per Day', min_value=0.0, max_value=24.0, step=0.1)
nilai_gpa = st.slider('GPA', 0.0, 4.0, step=0.01)

if st.button('Predict'):
    # Add Study-Sleep Ratio
    study_sleep_ratio = jam_belajar / (jam_tidur + 1)

    input_data = [[jam_belajar, jam_tidur, aktivitas_fisik, nilai_gpa, study_sleep_ratio]]
    input_data_scaled = scaler.transform(input_data)

    prediction_encoded = model.predict(input_data_scaled)
    prediction_label = label_encoder.inverse_transform(prediction_encoded)

    # Display result
    st.success(f"TINGKAT STRES ANDA ADALAH : {prediction_label[0].upper()}")
    st.markdown(" Tingkat Level Stress adalah High : Tinggi, Moderate : Sedang, Low : Rendah")

    # Generate AI-based advice with context
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "system", "content": "Saya adalah seorang ahli kesehatan mental."}]

    # Contextual prompt with prediction and complaints
    user_prompt = (
        f"Pengguna mengeluhkan '{keluhan}'. Mengingat {jam_belajar} " 
        f"jam belajar dan {jam_tidur} jam tidur setiap hari, serta nilai GPA {nilai_gpa},"
        f"kemungkinan besar pengguna mengalami stres {prediction_label[0]}."
        f"Untuk mengelola stres ini, berikan saran yang bisa membantu mengurangi stress pengguna."
    )
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # Get response from OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages
    )
    ai_response = response.choices[0].message.content

    # Display AI-generated advice
    st.session_state.messages.append({"role": "system", "content": ai_response})
    st.chat_message("system").write(ai_response)
