import streamlit as st
<<<<<<< HEAD
import os
import pages.home as home
import pages.dataset as dataset
import pages.overview as overview
import pages.prediction as prediction
from streamlit_option_menu import option_menu

st.set_page_config(page_title="STRES LEVEL", layout="wide", initial_sidebar_state="collapsed")

# Tambahkan CSS untuk menyesuaikan tampilan
st.markdown(
    """
    <style>
    .css-1y0tads {
        margin-left: 0 !important; /* Navbar mentok ke kiri */
        margin-right: 0 !important; /* Navbar mentok ke kanan */
    }
    .nav-item {
        width: 100%; /* Menyesuaikan lebar setiap item */
        text-align: center; /* Memusatkan teks dalam menu */
    }
    section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
        
    .css-1y0tads .nav-link {
        font-size: 18px; /* Adjust font size if necessary */
    }
    </style>
    """,
    unsafe_allow_html=True
)

selected =  option_menu(
    menu_title=None,
    options=["Home", "Dataset",  "Prediction", "Overview"],
    icons=["bi bi-house-door-fill","bi bi-file-earmark-bar-graph-fill","bi bi-code-slash","bi bi-file-earmark-fill"],
    orientation="horizontal",
    menu_icon="cast",
    default_index=0
)

if selected == "Home":
    # Home = importlib.import_module("home")
    home.show_home()
if selected == "Dataset":
    # Data = importlib.import_module("data")
    dataset.show_dataset()
if selected == "Overview":
    # Visualization = importlib.import_module("visualisasi")
    overview.show_overview()
if selected == "Prediction":
    # About = importlib.import_module("about")
    prediction.show_prediction()
    
=======

st.Page("streamlit_app.py", title="DASHBOARD")
# Set page configuration
st.set_page_config(page_title="DASHBOARD")
st.Page("streamlit_app.py", title="DASHBOARD")

# Title
st.markdown(""" 
<div style="text-align: center; font-size: 38px; font-weight: bold;">
    PREDIKSI LEVEL <span style=" color: #ff004c;">STRES </span> BERDASARKAN GAYA HIDUP MAHASISWA
</div>
""", unsafe_allow_html=True)

st.image("ss.png", width=450 )

# Justified text description
st.markdown("""
<div style="text-align: justify; font-size: 16px; line-height: 1.6; ">
Stres adalah sebuah kondisi yang dirasakan saat seseorang menghadapi tantangan, 
atau berada dalam situasi yang mengharuskan kita menyesuaikan diri secara cepat 
dengan sebuah perubahan. Ketika stres membuat kita menjadi lebih terpacu dan termotivasi, 
stres ini dinamakan eustress atau stress yang positif. Eustress bermanfaat dalam memacu kreativitas,
menimbulkan inspirasi dan rasa bahagia, serta menyehatkan tubuh. Eustress diperlukan, 
misalnya untuk membantu kita menyelesaikan pekerjaan sebelum tenggat waktu yang diberikan,
mengejar prestasi atau pencapaian dan lain sebagainya. 
</div>
""", unsafe_allow_html=True)

# Additional information
st.markdown("""
<div style="text-align: justify; font-size: 16px; line-height: 1.6;">
Apa penyebab stres ?

Pengalaman menghadapi stres pada anak tidak selalu sama dengan orang dewasa. Di kalangan orang dewasa, stres terkait pekerjaan sangat umum terjadi. Namun, bagi anak, stres terjadi ketika mereka tidak bisa menghadapi situasi yang mengandung ancaman, situasi sulit, atau situasi yang menyakitkan, antara lain:

- Pikiran atau perasaan negatif tentang diri sendiri,
- Perubahan fisik, misalnya permulaan pubertas,
- Beban belajar, misalnya ulangan atau bertambahnya pekerjaan rumah seiring waktu,
- Masalah dengan teman di sekolah atau lingkungan sosial,
- Perubahan besar, seperti pindah rumah, pindah sekolah, atau perpisahan orang tua,
- Penyakit kronis, masalah keuangan di keluarga, atau kematian orang terdekat,
- Situasi rumah atau lingkungan sekitar yang tidak aman.
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 50px; color: ">
Made with Love <br>
&copy; 2024 Kelompok 1
</div>
""", unsafe_allow_html=True)
>>>>>>> 917033165f4a1c81a317a4221eab39d2d9684bd2
