import streamlit as st
import cv_page
import data_viz_page
import os  

# Configuration de la page
st.set_page_config(page_title="FestivalViz", layout="wide")

# Ajout de HTML et CSS personnalisés pour la barre latérale

# Barre latérale avec photo et description
with st.sidebar:
    # Chargement de l'image avec st.image(), sans légende
    st.image("moi.jpg", width=200)
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
