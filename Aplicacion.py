import pandas as pd
import streamlit as st
import numpy as np
from modulos import Banda, Difraccion, Energia, fotoelectrico, Interferencia, Maxwell, Polarizacion, Reflexion, Refraccion, Rendija
st.set_page_config(page_title="Óptica Cuántica")

Titulo_concurso = '<p style="text-align:center";"font-family:Courier; color:Blue; font-size: 20px;">Hackaton-Quantum Apps</p>'
st.markdown(Titulo_concurso, unsafe_allow_html=True)


Titulo_principal = '<p style="font-family:TimesNewRoman; color:DarkBlue; font-size: 42px;">Óptica Cuántica</p>'
st.markdown(Titulo_principal, unsafe_allow_html=True)

st.caption('Esta aplicacón fue hecha con el propósito de introducir hacia los fenómenos cuánticos, especificamente dentro de la rama de la óptica cuántica, que ha sido de dificil comprensión para la cual nuestro objetivo es demostrar tales fenómenos con ejemplos visuales y prácticos de entender')

title_to_app = {
    
    t("Efecto Fotoeléctrico"): fotoelectrico.fotoelectrico_page,
    t("Ancho de Banda"): Banda.Banda_page,
    t("Ecuaciones de Maxwell"): Maxwell.Maxwell_page,
    t("Energia transportada"): Energia.Energia_page,
    t("Polarizacion de la luz"): Polarizacion.Polarizacion_page,
    t("Interferencia"): Interferencia.Interferencia_page,
    t("Experimento de la doble rendija"): Rendija.Rendija_page,
    t("Difraccion"): Difraccion.Difraccion_page,
    t("Reflexion"): Reflexion.Reflexion_page,
    t("Refraccion"): Refraccion.Refraccion_page, 
    } 

query_params = st.experimental_get_query_params()
if "page" in query_params:
    page_url = query_params["page"][0]
    if page_url in title_to_app.keys():
        st.session_state["page_selector"] = page_url

with st.sidebar:
    add_header = st.header(
        "Temas")  

st.subheader('Introducción')
st.markdown('**¿Qué es la luz?**')
st.markdown('Una pregunta que los seres humanos han tratado de responder durante siglos.')

col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.image("newton.png", width=600, caption='Figura No.1 Newton y el estudio de la luz')

with col3:
    st.write("")

st.markdown('Newton, principal aportador de la teoria de la luz estipulaba que las partículas de luz provenian de una fuente luminosa que estimulaba la vista.')
st.markdown('Esta idea le permitió justificar las bases de la refracción y reflexión')
st.markdown('Durante su vida sostuvó que la luz podría seguir un movimiento ondulatorio lo cual fue demostrado por Thomas Young, que bajo condiciones de difracción los rayos de luz interfieren unos con otros al igual que con las ondas mecánicas')

col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.markdown("![Alt Text](http://blog.soton.ac.uk/soundwaves/files/2013/12/light1.gif)")

with col3:
    st.write("")

#("![Your Awsome GIF](https://media.giphy.com/media/3ohzdIuqJoo8QdKlnW/giphy.gif)") 

