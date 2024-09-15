import streamlit as st
import cv_page
import data_viz_page

# Configuration de la page
st.set_page_config(page_title="FestivalViz", layout="wide")

# Ajout de HTML et CSS personnalisés pour la barre latérale
st.markdown("""
    <style>
    .sidebar .sidebar-content img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 50%;
        width: 150px;  /* Ajustez la taille selon vos besoins */
        height: 150px; /* Maintenir les proportions rondes */
        object-fit: cover; /* Assure que l'image est bien cadrée */
    }
    </style>
""", unsafe_allow_html=True)

# Barre latérale avec photo et description
with st.sidebar:
    # Chargement de l'image avec st.image(), sans légende
    st.image("moi.jpg", use_column_width=False, width=150)
    
    st.write("""
    ## Louise LAVERGNE 🌼
    Hello ! Je suis Louise, passionnée par les données et les analyses 📊. Ravi de vous rencontrer ! 👋
    """)

    st.write("""
    💻 Étudiante en ingénierie informatique
    """)
    st.write("""
    📌 Paris, France
    """)
    st.write("""
    📚 M1 Data and AI à Efrei Paris
    """)

    # Menu de navigation
    page = st.selectbox(
        "Choisissez une page",
        ("Curriculum Vitae", "Visualisation des données")
    )

# Navigation vers les différentes pages
if page == "Curriculum Vitae":
    cv_page.show()  # Page CV
elif page == "Visualisation des données":
    data_viz_page.show()  # Page Data Viz
