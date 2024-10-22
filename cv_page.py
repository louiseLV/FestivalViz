import streamlit as st
import matplotlib.pyplot as plt

def show():
    st.title("Mon portfolio 📚")
    
    st.header("Qui suis-je ?")
    st.write("""
    Bonjour, je suis Louise Lavergne , une étudiante à l'Efrei dans le domaine de la Data et de l'IA 🤖. Voici un aperçu de mon parcours professionnel :
    """)
    
    st.subheader("Expériences professionnelles 💼")
    st.write("""
    - **DataScientest** (nov 2024 - mars 2025) : Data Scientist Stagiaire, 📊.
    - **Iconcept** (jan 2023) : Commercial stagiaire, 🗣️.
    """)
    
    
    st.subheader("Formation 🎓")
    st.write("""
    - **Diplôme d'ingénieur Efrei** - Efrei Paris, 2021-2026 🎓.
    - **Baccalauréat Général option Mathématiques Physique-Chimie section européenne** - Lycée Jean Giraudoux, 2021 🏅.
    """)

    st.subheader("Répartition des Compétences 📊")
    competencies = ['Analyse de données', 'Machine Learning', 'Communication', 'Travail en équipe', 'Programmation']
    levels = [4, 3, 4, 5, 3]  

    plt.figure(figsize=(8, 4))
    plt.barh(competencies, levels, color='skyblue')
    plt.xlabel('Niveau de compétence')
    plt.title('Répartition des compétences')
    plt.xlim(0, 5)
    st.pyplot(plt)
    plt.clf() 


    st.subheader("Mes Passions en dehors de l'école 🎶")

    passions = ["IA", "Voyages", "Cuisine", "Musique"]
    intensities = [7, 8, 7, 9]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.pie(intensities, labels=passions, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
    ax.axis('equal')  
    st.pyplot(fig)