import streamlit as st
import cv_page
import data_viz_page
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

st.set_page_config(page_title="FestivalViz", layout="wide")

st.markdown(
    """
    <style>
    .profile-pic-container {
        border-radius: 50%; /* Arrondir le conteneur */
        overflow: hidden; /* S'assurer que l'image est contenue */
        width: 200px; /* Largeur du conteneur */
        height: 200px; /* Hauteur du conteneur */
    }
    .profile-pic {
        width: 100%; /* L'image remplit le conteneur */
        height: auto; /* Conserver les proportions */
    }
    </style>
    """,
    unsafe_allow_html=True
)

image_path = "moi.jpg" 

with st.sidebar:
    image_base64 = get_base64_image(image_path)
    st.markdown(
        f"""
        <div class="profile-pic-container">
            <img src="data:image/png;base64,{image_base64}" class="profile-pic">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("""
    ## Louise LAVERGNE 🌼
    Hello ! Je suis Louise, passionnée par les données et les analyses 📊. 
             
    """)
    st.write("""Contacts :
             
    - 📧  louiselavergne87@gmail.com 
             
    - 📱 0618217195

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

    page = st.selectbox(
        "Choisissez une page",
        ("Portfolio", "Visualisation des données")
    )

if page == "Portfolio":
    cv_page.show() 
elif page == "Visualisation des données":
    data_viz_page.show() 
