import streamlit as st

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
    home.show_home()
if selected == "Dataset":
    dataset.show_dataset()
if selected == "Overview":
    overview.show_overview()
if selected == "Prediction":
    prediction.show_prediction()
    
