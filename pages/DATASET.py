import pickle
import streamlit as st 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.linear_model import LinearRegression
from joblib import dump
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data = pd.read_csv('pages/student_lifestyle_dataset.csv')

# Load the trained model
model = pickle.load(open('pages/model.sav', 'rb'))
print(type(model))  # Check the model type (should be LinearRegression)

st.title("STRESS LEVEL PREDICT")

st.header("DATASET")
num_rows = st.slider("Pilih jumlah baris yang ingin ditampilkan:", min_value=5, max_value=2000, step=5)
st.dataframe(data.head(num_rows))
# st.dataframe(data)

# Mengonversi kolom 'Stress_Level' menjadi numerik jika kolom tersebut ada
if "Stress_Level" in data.columns:
    label_encoder = LabelEncoder()
    data["Stress_Level"] = label_encoder.fit_transform(data["Stress_Level"])


# Display charts for each feature
st.write("Grafik Study Hours")
chart_study_hours= pd.DataFrame(data, columns=["Study_Hours_Per_Day"])
st.line_chart(chart_study_hours.head(num_rows))

st.write("Grafik Sleep Hours")
chart_sleep_hours = pd.DataFrame(data, columns=["Sleep_Hours_Per_Day"])
st.line_chart(chart_sleep_hours.head(num_rows))

st.write("Grafik Physical Hours")
chart_physical_hours = pd.DataFrame(data, columns=["Physical_Activity_Hours_Per_Day"])
st.line_chart(chart_physical_hours.head(num_rows))

st.write("Grafik GPA")
chart_gpa = pd.DataFrame(data, columns=["GPA"])
st.line_chart(chart_gpa.head(num_rows))

# 3. Proporsi Kegiatan Harian
st.subheader("Proporsi Kegiatan Harian")
activity_columns = ["Study_Hours_Per_Day", "Sleep_Hours_Per_Day", "Social_Hours_Per_Day",
                    "Extracurricular_Hours_Per_Day", "Physical_Activity_Hours_Per_Day"]
if all(col in data.columns for col in activity_columns):
    mean_activities = data[activity_columns].mean()
    fig, ax = plt.subplots()
    mean_activities.plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax, colors=sns.color_palette("pastel"))
    ax.set_title("Proporsi Kegiatan Harian")
    ax.set_ylabel("")
    st.pyplot(fig)
else:
    st.error("Beberapa kolom aktivitas tidak ditemukan dalam dataset.")

# 4. GPA Berdasarkan Tingkat Stres
st.subheader("GPA Berdasarkan Tingkat Stres")
if "Stress_Level" in data.columns and "GPA" in data.columns:
    fig, ax = plt.subplots()
    sns.barplot(x="Stress_Level", y="GPA", data=data, ax=ax, palette="muted", ci="sd")
    ax.set_title("Rata-rata GPA Berdasarkan Tingkat Stres")
    ax.set_xlabel("Tingkat Stres")
    ax.set_ylabel("Rata-rata GPA")
    st.pyplot(fig)
else:
    st.error("Kolom 'Stress_Level' atau 'GPA' tidak ditemukan dalam dataset.")
