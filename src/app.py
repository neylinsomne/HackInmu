import streamlit as st
import pandas as pd
from controllers.Real_State_Controllers  import get_property , get_study_property
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium

# Obtener propiedades
locals_sales = get_property()
locals_study = get_study_property()

df = pd.DataFrame(locals_sales).head()

# Convertir latitud y longitud a tipo numérico
df['latitud'] = pd.to_numeric(df['latitud'], errors='coerce')
df['longitud'] = pd.to_numeric(df['longitud'], errors='coerce')

# Eliminar filas con valores NaN en latitud y longitud
df = df.dropna(subset=['latitud', 'longitud'])

# Mapa interactivo usando Streamlit-Folium
st.subheader("INMU")

if not df.empty:
    # Crear un mapa base
    map_center = [df['latitud'].mean(), df['longitud'].mean()]  # Centro del mapa
    folium_map = folium.Map(location=map_center, zoom_start=12)

    # Añadir marcadores al mapa
    for index, row in df.iterrows():
        folium.Marker(
            location=[row['latitud'], row['longitud']],
            popup=f"<strong>Ubicación:</strong> {row['ubicacion']}<br>"
                  f"<strong>Descripción:</strong> {row['descripcion']}<br>"
                  f"<strong>Inmobiliaria:</strong> {row['inmobiliaria']}<br>"
                  f"<strong>Precio:</strong> {row['codigo_fr']}",
            icon=folium.Icon(color='blue')
        ).add_to(folium_map)

    # Mostrar el mapa en Streamlit
    st_folium(folium_map, width=725)

    # Mostrar la tabla de propiedades
    st.subheader("Tabla de Propiedades")
    st.dataframe(df[['ubicacion', 'descripcion', 'inmobiliaria', 'codigo_fr', 'Estrato']])  # Ajusta las columnas según lo necesites
else:
    st.write("No hay propiedades para mostrar en el mapa.")

# Gráfica de cantidad de propiedades por estrato
estrato_counts = df['Estrato'].value_counts()

# Crear una gráfica
plt.figure(figsize=(10, 5))
estrato_counts.plot(kind='bar', color='skyblue')
plt.title('Cantidad de Propiedades por Estrato')
plt.xlabel('Estrato')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar la gráfica en Streamlit
st.pyplot(plt)

# Mostrar el título de la app
st.title('Filtrar Propiedades por Estrato')

# Filtrar por estrato
estrato = st.selectbox('Seleccionar estrato:', ['Todos'] + df['Estrato'].unique().tolist())
if estrato != 'Todos':
    df = df[df['Estrato'] == estrato]

# Mostrar resultados
if df.empty:
    st.write("No se encontraron propiedades.")
else:
    for index, row in df.iterrows():
        st.subheader(f"Propiedad {index + 1}")
        st.image(row['image'], width=300)
        st.write(f"**Ubicación:** {row['ubicacion']}")
        st.write(f"**Descripción:** {row['descripcion']}")
        st.write(f"**Inmobiliaria:** {row['inmobiliaria']}")
        st.write(f"**Precio:** {row['codigo_fr']}")
        st.write(f"**Área Construida:** {row['Área Construida']}")
        st.write(f"**Baños:** {row['Baños']}")
        st.write(f"**Habitaciones:** {row['Habitaciones']}")
        st.write(f"**Fecha:** {row['fecha']}")
        st.write("**Características:**")
        for caracteristica in row['caracteristicas']:
            st.write(f"- {caracteristica}")
