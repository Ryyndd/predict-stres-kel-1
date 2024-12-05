import streamlit as st 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split

def show_dataset():
    # Load dataset
    data = pd.read_csv('pages/student_lifestyle_dataset.csv')

    st.title("STRESS LEVEL PREDICTION")
    st.header("Dataset Overview")
    
    # Display dataset
    num_rows = st.slider("Select number of rows to display:", 5, 2000, step=5)
    st.write("""
    Dataset ini mencakup data tentang gaya hidup siswa, termasuk waktu belajar, waktu tidur, aktivitas fisik, 
    kegiatan sosial, kegiatan ekstrakurikuler, tingkat stres, dan GPA (nilai akademik). Data ini membantu 
    menganalisis hubungan antara pola gaya hidup, tingkat stres, dan performa akademik siswa.
    """)
    st.dataframe(data.head(num_rows))

    # Encode Stress Level column
    if "Stress_Level" in data.columns:
        label_encoder = LabelEncoder()
        data["Stress_Level"] = label_encoder.fit_transform(data["Stress_Level"])

    # Split data into features (X) and target (y)
    features = [
        "Study_Hours_Per_Day", "Sleep_Hours_Per_Day", 
        "Physical_Activity_Hours_Per_Day", "GPA"
    ]
    X = data[features]
    y = data["Stress_Level"]

    # Normalize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Train RandomForestClassifier
    model = RandomForestClassifier(random_state=42, n_estimators=100)
    model.fit(X_train, y_train)

    # Predict on the test set
    y_pred = model.predict(X_test)
    
    col1, col2 = st.columns(2)
    
        # Menampilkan dataset pada dua kolom
    with col1:
        
        # Line chart for Study Hours
        st.write("### Grafik Jam Belajar (Study Hours)")
        st.write("""
        Grafik ini menunjukkan jumlah jam belajar siswa selama periode tertentu. Data ini menunjukkan fluktuasi 
        jumlah jam belajar dengan tren yang meningkat. Grafik ini membantu memahami pola belajar siswa 
        dan hubungannya dengan tingkat stres serta performa akademik.
        """)
        study_hours = pd.DataFrame(data, columns=["Study_Hours_Per_Day"])
        st.line_chart(study_hours.head(num_rows))

        # Line chart for Sleep Hours
        st.write("### Grafik Jam Tidur (Sleep Hours)")
        st.write("""
        Grafik ini menampilkan jumlah jam tidur siswa. Jam tidur cenderung menurun selama periode tertentu, 
        yang mungkin menunjukkan perubahan gaya hidup, tekanan akademik, atau faktor lainnya. 
        Pola tidur ini dapat berhubungan dengan tingkat stres dan performa akademik.
        """)
        sleep_hours = pd.DataFrame(data, columns=["Sleep_Hours_Per_Day"])
        st.line_chart(sleep_hours.head(num_rows))

        # Pie chart for Daily Activities
        st.subheader("Proporsi Kegiatan Harian")
        st.write("""
        Diagram ini memberikan visualisasi proporsi waktu yang dihabiskan siswa untuk berbagai aktivitas utama, 
        seperti belajar, tidur, aktivitas fisik, kegiatan ekstrakurikuler, dan kegiatan sosial. Diagram ini 
        membantu memahami bagaimana siswa membagi waktu untuk berbagai aspek kehidupan sehari-hari.
        """)
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
            st.error("Some activity columns are missing.")
            
        
        st.subheader("Confusion Matrix")
        st.write("""
        Confusion Matrix digunakan untuk memvisualisasikan kemampuan model RandomForestClassifier
        dalam memprediksi tingkat stres berdasarkan data pengujian. Matriks ini memiliki elemen diagonal 
        yang menunjukkan jumlah prediksi benar (True Positives dan True Negatives) untuk setiap kelas, sementara
        elemen di luar diagonal menunjukkan jumlah prediksi salah (False Positives dan False Negatives). Warna biru 
        pada matriks mencerminkan intensitas nilai, di mana warna yang lebih gelap menunjukkan jumlah prediksi yang 
        lebih besar. Visualisasi ini membantu dalam mengevaluasi akurasi dan ketepatan model untuk masing-masing kategori tingkat stres.
        """)
        cm = confusion_matrix(y_test, y_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=label_encoder.classes_)
        fig, ax = plt.subplots(figsize=(8, 6))
        disp.plot(cmap="Blues", ax=ax)
        plt.title("Confusion Matrix for RandomForestClassifier")
        st.pyplot(fig)

        

    with col2:
        
        # Line chart for Physical Activity Hours
        st.write("### Grafik Jam Aktivitas Fisik (Physical Hours)")
        st.write("""
        Grafik ini menggambarkan waktu yang dihabiskan untuk aktivitas fisik. Aktivitas fisik siswa 
        cenderung meningkat secara bertahap selama waktu tertentu, yang menunjukkan adanya upaya 
        untuk menjaga kebugaran fisik.
        """)
        physical_hours = pd.DataFrame(data, columns=["Physical_Activity_Hours_Per_Day"])
        st.line_chart(physical_hours.head(num_rows))

        # Line chart for GPA
        st.write("### Grafik GPA")
        st.write("""
        Grafik ini menampilkan nilai rata-rata poin kumulatif (GPA) siswa. Data menunjukkan fluktuasi dengan 
        tren peningkatan secara keseluruhan, yang merepresentasikan kemajuan akademik siswa.
        """)
        gpa_data = pd.DataFrame(data, columns=["GPA"])
        st.line_chart(gpa_data.head(num_rows))
        
        # Bar chart for GPA vs Stress Level
        st.subheader("GPA Berdasarkan Tingkat Stres")
        st.write("""
        Diagram ini membandingkan rata-rata GPA siswa pada berbagai tingkat stres. Dari data terlihat bahwa tingkat 
        stres yang lebih tinggi cenderung berkorelasi dengan penurunan GPA. Diagram ini membantu memvisualisasikan 
        dampak stres terhadap performa akademik.
        """)
        if "Stress_Level" in data.columns and "GPA" in data.columns:
            fig, ax = plt.subplots()
            sns.barplot(x="Stress_Level", y="GPA", data=data, ax=ax, palette="muted", ci="sd")
            ax.set_title("Rata-rata GPA Berdasarkan Tingkat Stres")
            ax.set_xlabel("Tingkat Stres")
            ax.set_ylabel("Rata-rata GPA")
            st.pyplot(fig)
        else:
            st.error("Columns 'Stress_Level' or 'GPA' not found in dataset.")
            
        
        # Distribusi Tingkat Stres
        st.subheader("Distribusi Tingkat Stres")
        st.write("""
        Distribusi Tingkat Stres merupakan visualisasi jumlah data
        pada setiap kategori tingkat stres (Low, Moderate, High). Grafik ini dibuat menggunakan
        countplot dari seaborn, yang menampilkan bar yang mewakili jumlah sampel pada setiap kelas.
        Distribusi ini penting untuk memahami keseimbangan data dalam dataset, karena ketidakseimbangan
        data dapat memengaruhi performa model. Dengan visualisasi ini, kita dapat melihat apakah jumlah data
        untuk kategori tertentu lebih dominan dibanding kategori lainnya, yang dapat memberikan insight tambahan tentang dataset tersebut.
        """)
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.countplot(x=data["Stress_Level"], palette="pastel", ax=ax)
        ax.set_title("Distribution of Stress Level in Dataset")
        ax.set_xlabel("Stress Level")
        ax.set_ylabel("Count")
        st.pyplot(fig)


