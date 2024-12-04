import streamlit as st
import pages.prediction as prediction

# Set page configuration
st.set_page_config(page_title="HOME", layout="wide")

def show_home():
    # Title
    st.markdown(""" 
    <div style="text-align: center; font-size: 38px; font-weight: bold;">
        PREDIKSI LEVEL <span style=" color: #ff004c;">STRES </span> BERDASARKAN <br> GAYA HIDUP MAHASISWA
    </div>
    """, unsafe_allow_html=True)



    col1, col2 = st.columns(2)
    
        # Menampilkan dataset pada dua kolom
    with col1:
        st.image("ss.png")
        
    with col2:
    
        st.markdown(
            """
            <div style="text-align: center; margin-top: 100px;">
                <h1 style="color: #ff004c; font-size: 2.5em;">
                    😌 Stres? Jangan Panik!
                </h1>
                <p style="font-size: 1.2em;  margin-top: 10px;">
                    Bosan sama tugas kuliah? Capek ngadepin dosen?<br>
                    Tenang, kamu nggak sendirian! Yuk, cari tahu seberapa <strong>stres</strong> kamu sebenarnya
                    dan dapatkan tips jitu untuk menghadapinya. 💡
                </p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        
        
        if st.button("CEK LEVEL STRESSMU", icon="🤣",use_container_width=True , type="primary") :
            prediction.show_prediction()
            
    # Footer
    st.markdown("""
        <div style="text-align: center; margin-top: 50px; color: ">
        Made with Love <br>
        &copy; 2024 Kelompok 1
        </div>
        """, unsafe_allow_html=True)
    