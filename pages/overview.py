import streamlit as st

# st.set_page_config(page_title="OVERVIEW", layout="wide")

def show_overview():
    # Judul halaman

    tab1, tab2 = st.tabs(["✨ OVERVIEW", "📊 METHODE"])

    with tab1:
        
        st.title("✨ OVERVIEW")
        
        ove1, ove2 = st.columns(2)
        
        with ove1:
            # Gambar pendukung
            st.image("jj.png", width=500)
            
        with ove2:
            
            # Penjelasan umum
            st.markdown("""
            <div style="text-align: justify;">
            Website <strong>Prediksi Level Stres Berdasarkan Gaya Hidup 
            Mahasiswa</strong> dirancang untuk membantu mahasiswa memahami bagaimana gaya hidup mereka
            —seperti jam belajar, tidur, aktivitas fisik, dan waktu sosial—memengaruhi tingkat stres yang mereka alami.
            Website ini memanfaatkan teknologi machine learning untuk memprediksi tingkat stres dan memberikan wawasan yang 
            dapat membantu mahasiswa membuat keputusan yang lebih baik terkait kesejahteraan mereka.
            </div>
            """, unsafe_allow_html=True)

        
    with tab2:
        
        st.title("📊 METHODE")

        # Membuat dua kolom
        met1, met2 = st.columns(2)
        
        # Kolom pertama - Penjelasan singkat dan gambar
        with met1:
            # Ilustrasi pohon keputusan
            st.image("forest.png", caption="Ilustrasi Proses Random Forest")
        
        # Kolom kedua - Penjelasan singkat tentang Random Forest
        with met2:
            st.header("🌲 Penjelasan Random Forest")
            st.markdown("""
            <div style="text-align: justify;">
            Random Forest adalah algoritma pembelajaran mesin yang kuat dan fleksibel. Dengan memanfaatkan kumpulan 
            pohon keputusan, algoritma ini memberikan hasil yang akurat dan andal. Mari kita pelajari lebih lanjut!
            <br>
            </div>
            """, unsafe_allow_html=True)
            
            # Penjelasan Fungsi RandomForestClassifier
            with st.expander("Penjelasan Fungsi RandomForestClassifier"):
                st.write("""
                **RandomForestClassifier** adalah algoritma pembelajaran mesin berbasis ensemble yang digunakan untuk tugas klasifikasi.
                Algoritma ini bekerja dengan membangun beberapa pohon keputusan selama proses pelatihan, kemudian menggabungkan hasil 
                dari masing-masing pohon untuk memberikan prediksi akhir yang lebih akurat dan stabil.
                """)

            # Langkah Kerja dalam Proyek
            with st.expander("Langkah Kerja dalam Proyek Prediksi Tingkat Stres"):
                st.write("""
                1. **Mempersiapkan Data**:
                    - Menambah fitur baru: **Study_Sleep_Ratio** dihitung dengan membagi jam belajar per hari dengan (jam tidur per hari + 1).
                    - Memilih fitur utama seperti **Study_Hours_Per_Day**, **Sleep_Hours_Per_Day**, **Physical_Activity_Hours_Per_Day**, **GPA**, dan fitur tambahan **Study_Sleep_Ratio**.
                    - **Stress_Level** digunakan sebagai variabel target (y).
                
                2. **Encoding dan Normalisasi Data**:
                    - **Label encoding** digunakan untuk mengubah nilai target menjadi format numerik.
                    - Data dinormalisasi menggunakan **StandardScaler** agar setiap fitur memiliki distribusi yang sama.
                
                3. **Pembagian Dataset**:
                    - Data dibagi menjadi set **training (80%)** dan **testing (20%)** menggunakan **train_test_split**.
                
                4. **Pelatihan Model**:
                    - Model **RandomForestClassifier** dilatih menggunakan **100 pohon keputusan** untuk mengurangi overfitting.
                
                5. **Memprediksi dengan Data Baru**:
                    - Input data dari pengguna (jam belajar, jam tidur, aktivitas fisik, GPA) diambil melalui form dan diproses untuk prediksi.
                
                6. **Kelebihan RandomForestClassifier**:
                    - Mengurangi **overfitting**, fleksibilitas pada fitur numerik dan kategorikal, serta **skalabilitas** yang baik pada dataset besar.
                """)

            # Kelebihan Fitur
            with st.expander("Kelebihan RandomForestClassifier"):
                st.write("""
                - **Mengurangi Overfitting**: Dengan menggabungkan hasil dari banyak pohon keputusan, model lebih tahan terhadap outlier dan data noise.
                - **Fleksibilitas**: Algoritma ini mampu bekerja dengan baik pada data yang memiliki fitur numerik dan kategorikal.
                - **Skalabilitas**: Dengan paralelisasi, model dapat memproses dataset besar dengan lebih efisien.
                - **Interpretabilitas**: Model dapat memberikan informasi penting tentang pentingnya setiap fitur (feature importance) dalam menentukan prediksi.
                """)


        # Bagian 1: Gambaran Umum
        st.header("📚 Gambaran Umum")
        st.info("""
        - **Pembelajaran Terawasi:** Memanfaatkan data dengan label target.
        - **Fleksibilitas:** Cocok untuk regresi (prediksi nilai numerik) dan klasifikasi (mengelompokkan kategori).
        - **Metode Ensemble:** Menggabungkan banyak pohon keputusan untuk meningkatkan akurasi.
        """)

        # Bagian 2: Cara Kerja
        st.header("🔍 Cara Kerja Random Forest")
        st.markdown("""
        **Bayangkan Random Forest seperti sekumpulan ahli yang memberikan pendapat:**  
        - Setiap ahli adalah pohon keputusan yang bekerja berdasarkan subset data dan fitur acak.
        - Pohon-pohon tersebut memberikan prediksi, lalu suara terbanyak digunakan untuk menentukan hasil akhir.

        **Proses Prediksi:**  
        - Untuk *klasifikasi:* Menggunakan suara terbanyak.
        - Untuk *regresi:* Menggunakan rata-rata prediksi.
        """)

        # Bagian 4: Kesimpulan
        st.header("🏁 Kesimpulan")
        st.success("""
        Random Forest adalah pilihan yang sangat baik untuk tugas klasifikasi dan regresi. Dengan pendekatan kolektif
        yang melibatkan banyak pohon keputusan, algoritma ini memastikan hasil yang lebih akurat, andal, dan tahan 
        terhadap overfitting.Gunakan Random Forest untuk memecahkan berbagai masalah pembelajaran mesin!
        """)