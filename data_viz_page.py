import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import folium
from streamlit_folium import folium_static
from folium.plugins import HeatMap

def show():
    st.title("Visualisation de données")
    df = pd.read_csv("festivals.csv", delimiter=";")
    df.dropna(thresh=len(df.columns) - 20, inplace=True)
    df.drop_duplicates(inplace=True)
    df = df.drop(columns=['code_insee_epci_collage_en_valeur', 'complement_d_adresse_facultatif', 'sous_categorie_musique_cnm',
                          'sous_categorie_cinema_et_audiovisuel', 'sous_categorie_arts_visuels_et_arts_numeriques', 
                          'sous_categorie_livre_et_litterature', 'identifiant_agence_a', 'identifiant_cnm', 
                          'sous_categorie_spectacle_vivant', 'numero_de_voie', 'envergure_territoriale', 'sous_categorie_musique'])
    df_clean = df.dropna(subset=['geocodage_xy'])
    df_clean['geocodage_xy'] = df_clean['geocodage_xy'].astype(str)
    df_clean['latitude'] = df_clean['geocodage_xy'].str.split(',').str[0].astype(float)
    df_clean['longitude'] = df_clean['geocodage_xy'].str.split(',').str[1].astype(float)   

    st.write("Voici un aperçu des données :")
    st.write(df_clean.head())

    df_clean['annee_de_creation_du_festival'] = pd.to_numeric(df_clean['annee_de_creation_du_festival'], errors='coerce')

    df_clean['annee_de_creation_du_festival'] = pd.to_numeric(df_clean['annee_de_creation_du_festival'], errors='coerce')
    
    current_year = pd.Timestamp.now().year
    df_clean = df_clean[(df_clean['annee_de_creation_du_festival'] >= 1900) & 
                        (df_clean['annee_de_creation_du_festival'] <= current_year)]

    # Plotly - Distribution of festivals by year  
    st.write("Distribution des festivals selon l\'année de création")

    df_clean = df.dropna(subset=['annee_de_creation_du_festival'])
    df_clean['annee_de_creation_du_festival'] = pd.to_numeric(df_clean['annee_de_creation_du_festival'], errors='coerce')

    
    df_clean = df_clean[(df_clean['annee_de_creation_du_festival'] >= 1960) & (df_clean['annee_de_creation_du_festival'] <= 2024)]

    fig = px.histogram(df_clean, 
                        x='annee_de_creation_du_festival', 
                        nbins=13,  
                        labels={'annee_de_creation_du_festival': 'Année de création du festival'}
                        )

    fig.update_xaxes(dtick=5, tickangle=45)

    st.plotly_chart(fig)

# Folium - Map visualization of festivals by year
    unique_years = df_clean['annee_de_creation_du_festival'].unique()
    min_year = int(df_clean['annee_de_creation_du_festival'].min())
    max_year = int(df_clean['annee_de_creation_du_festival'].max())

    year_slider = st.slider(
        "Sélectionnez l'année",
        min_value=min_year,
        max_value=max_year,
        value=min_year,  
        step=1
    )

    df_filtered = df_clean[df_clean['annee_de_creation_du_festival'] <= year_slider]
    df_filtered['latitude'] = df_clean['geocodage_xy'].str.split(',').str[0].astype(float)
    df_filtered['longitude'] = df_clean['geocodage_xy'].str.split(',').str[1].astype(float)
    df_filtered = df_filtered.dropna(subset=['latitude', 'longitude'])   
   # Vérifiez si les colonnes latitude et longitude existent
    
    if not df_filtered.empty:
        m = folium.Map(location=[46.603354, 1.888334], zoom_start=5, tiles='CartoDB positron')

        # Préparer les données pour la HeatMap
        heat_data = [[row['latitude'], row['longitude']] for index, row in df_filtered.iterrows()]

        # Ajouter la HeatMap
        HeatMap(heat_data, radius=15).add_to(m)  # Ajustez le rayon selon vos besoins

        st.write(f"Festivals jusqu'à l'année : {year_slider}")
        folium_static(m)

        # Graphique à barres du nombre de festivals par ville
        festivals_per_city = df_filtered['commune_principale_de_deroulement'].value_counts().reset_index()
        festivals_per_city.columns = ['Ville', 'Nombre de Festivals']

        # Création du graphique à barres
        fig = px.bar(
            festivals_per_city,
            x='Ville',
            y='Nombre de Festivals',
            title="Nombre de Festivals par Ville",
            labels={'Nombre de Festivals': 'Nombre de Festivals', 'Ville': 'Ville'},
            color='Nombre de Festivals',
            color_continuous_scale='Viridis'
        )

        st.plotly_chart(fig)
    else:
        st.write("Aucun festival trouvé pour l'année sélectionnée.")

    
 # Plotly - Distribution of festivals by discipline
    st.write("Répartition des disciplines dominantes")
    fig, ax = plt.subplots()
    df['discipline_dominante'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
    plt.ylabel('')  # Pour retirer le label de l'axe Y dans un pie chart
    plt.tight_layout()
    plt.show()
    st.pyplot(plt)

    discipline_choice = st.selectbox("Choisissez une discipline pour visualiser les festivals", df_clean['discipline_dominante'].unique())

    map_choice = st.radio("Choisissez le type de visualisation :", ("Carte Choropleth", "Carte avec points Plotly"))

    df_discipline = df_clean[df_clean['discipline_dominante'] == discipline_choice]

    df_discipline = df_discipline.dropna(subset=['annee_de_creation_du_festival', 'latitude', 'longitude'])

    if not df_discipline.empty:

        if map_choice == "Carte Choropleth":
            geojson_url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/regions.geojson"

            region_counts = df_discipline['region_principale_de_deroulement'].value_counts().reset_index()
            region_counts.columns = ['region', 'nombre_de_festivals']

            m = folium.Map(location=[46.603354, 1.888334], zoom_start=5, tiles='CartoDB positron')

            folium.Choropleth(
                geo_data=geojson_url,
                name="choropleth",
                data=region_counts,
                columns=["region", "nombre_de_festivals"],
                key_on="feature.properties.nom",
                fill_color='YlOrRd',
                fill_opacity=0.7,
                line_opacity=0.2,
                legend_name=f"Nombre de festivals pour {discipline_choice}",
            ).add_to(m)

            folium_static(m)

        elif map_choice == "Carte avec points Plotly":
            fig = px.scatter_mapbox(
                df_discipline,
                lat='latitude',
                lon='longitude',
                color='region_principale_de_deroulement',
                size='annee_de_creation_du_festival',
                size_max=5,
                hover_name='nom_du_festival',
                hover_data={'latitude': False, 'longitude': False},  # Ne pas afficher latitude et longitude
                mapbox_style="carto-positron",
                title=f"Répartition géographique des festivals - {discipline_choice}"
            )

            st.plotly_chart(fig)

    # Folium - Choropleth map of festivals by region

    # Créer un GeoDataFrame de la France par région
    region_counts = df_clean['region_principale_de_deroulement'].value_counts().reset_index()
    region_counts.columns = ['region', 'nombre_de_festivals']

    # Utiliser une carte GeoJSON pour les régions de France
    geojson_url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/regions.geojson"

    m = folium.Map(location=[46.603354, 1.888334], zoom_start=5, tiles='CartoDB positron')


    folium.Choropleth(
        geo_data=geojson_url,
        name="choropleth",
        data=region_counts,
        columns=["region", "nombre_de_festivals"],
        key_on="feature.properties.nom",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Nombre de festivals par région",
    ).add_to(m)

    folium_static(m)

    # Plotly - Choropleth map of festivals by region
    region_counts = df_clean['region_principale_de_deroulement'].value_counts().reset_index()
    region_counts.columns = ['region_principale_de_deroulement', 'nombre_de_festivals']

    
    geojson_url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/regions.geojson"

    fig = px.choropleth(
        region_counts,
        geojson=geojson_url,
        locations='region_principale_de_deroulement',
        featureidkey="properties.nom",  # Associe les noms des régions dans le GeoJSON
        color='nombre_de_festivals',
        color_continuous_scale="Blues",  # La couleur plus foncée indique plus de festivals
        hover_name='region_principale_de_deroulement',
        labels={'nombre_de_festivals': 'Nombre de festivals'},
        title="Nombre de festivals par région en France"
    )

    fig.update_geos(fitbounds="locations", visible=False)  # Ajuste le zoom de la carte
    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=False,
        ),
        coloraxis_colorbar=dict(
            title="Nombre de festivals",
            tickvals=[0, 10, 20, 30], 
        )
    )

    st.plotly_chart(fig)
        


    

    # Seaborn - Number of festivals per region
    st.write("Nombre de festivals par région")
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='region_principale_de_deroulement', palette='coolwarm', 
                  order=df['region_principale_de_deroulement'].value_counts().index)
    plt.xticks(rotation=90)
    st.pyplot(plt)

    # Plotly - Map visualization of festivals
    st.write("Distribution des festivals selon l\'année de création")

    df_clean = df.dropna(subset=['annee_de_creation_du_festival'])
    df_clean['annee_de_creation_du_festival'] = pd.to_numeric(df_clean['annee_de_creation_du_festival'], errors='coerce')

    # Filtrer les années entre 1960 et 2024
    df_clean = df_clean[(df_clean['annee_de_creation_du_festival'] >= 1960) & (df_clean['annee_de_creation_du_festival'] <= 2024)]

    fig = px.histogram(df_clean, 
                    x='annee_de_creation_du_festival', 
                    nbins=13,  
                    labels={'annee_de_creation_du_festival': 'Année de création du festival'}
                    )

    fig.update_xaxes(dtick=5, tickangle=45)

    st.plotly_chart(fig)
    