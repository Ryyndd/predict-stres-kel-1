import streamlit as st

st.Page("streamlit_app.py", title="DASHBOARD")
# Set page configuration
st.set_page_config(page_title="DASHBOARD")

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
