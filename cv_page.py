import streamlit as st

def show():
    st.title("Curriculum Vitae")
    
    st.header("Qui suis-je ?")
    st.write("""
    Bonjour, je suis Louise Lavergne , une étudiante à l'Efrei dans le domaine de la Data et de l'IA 🤖. Voici un aperçu de mon parcours professionnel :
    """)
    
    st.subheader("Expériences professionnelles 💼")
    st.write("""
    - **DataScientest** (nov 2024 - mars 2025) : Data Scientist Stagiaire, description des tâches 📊.
    - **Iconcept** (jan 2023) : Commercial stagiaire, description des tâches 🗣️.
    """)
    
    st.subheader("Compétences 💪")
    st.write("""
    - Organisée 🗂️
    - Rigoureuse 📋
    - Curieuse 🔍
    """)
    
    st.subheader("Formation 🎓")
    st.write("""
    - **Diplôme d'ingénieur Efrei** - Efrei Paris, 2021-2026 🎓.
    - **Baccalauréat Général option Mathématiques Physique-Chimie section européenne** - Lycée Jean Giraudoux, 2021 🏅.
    """)
