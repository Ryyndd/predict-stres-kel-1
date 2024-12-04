import streamlit as st

# st.set_page_config(page_title="OVERVIEW", layout="wide")

def show_overview():
    # Judul halaman

    
    # Membagi tampilan menjadi dua kolom
    col1, col2 = st.columns(2)

    with col1:
        
        st.title("✨ OVERVIEW")
        # Gambar pendukung
        st.image("jj.png")

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

        
    with col2:
        
        st.title("💫 METHODE")
        # Ilustrasi pohon keputusan
        st.image("forest.png", caption="Ilustrasi Proses Random Forest")
        
        st.title("🌲 Penjelasan Random Forest")
        st.markdown("""
        <div style="text-align: justify;">
        Random Forest adalah algoritma pembelajaran mesin yang kuat dan fleksibel. Dengan memanfaatkan kumpulan 
        pohon keputusan, algoritma ini memberikan hasil yang akurat dan andal. Mari kita pelajari lebih lanjut!
        </div>
        """, unsafe_allow_html=True)

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
        # st.image("random_forest_process.png", caption="Ilustrasi Proses Random Forest", use_column_width=True)

        # Bagian 3: Keunggulan
        st.header("🌟 Keunggulan Random Forest")
        st.success("""
        - **Tahan terhadap Overfitting:** Dengan menggabungkan banyak pohon, hasil lebih stabil.
        - **Fleksibilitas Fitur:** Dapat digunakan dengan data berskala besar maupun kecil.
        - **Akurasi Tinggi:** Menggunakan pendekatan kolektif untuk meningkatkan keandalan.
        """)

        # Bagian 4: Diagram Confusion Matrix
        st.header("📊 Confusion Matrix dalam Klasifikasi")
        st.markdown("""
        Berikut adalah *confusion matrix* untuk dua kelas, yang digunakan untuk mengevaluasi kinerja model:
        """)
        # st.image("confusion_matrix_example.png", caption="Contoh Confusion Matrix", use_column_width=True)

        # Bagian 5: Kesimpulan
        st.header("🏁 Kesimpulan")
        st.markdown("""
        Random Forest adalah pilihan yang sangat baik untuk tugas klasifikasi dan regresi. Dengan pendekatan kolektif
        yang melibatkan banyak pohon keputusan, algoritma ini memastikan hasil yang lebih akurat, andal, dan tahan 
        terhadap overfitting.  
        Gunakan Random Forest untuk memecahkan berbagai masalah pembelajaran mesin!
        """)
