import pandas as pd
import streamlit as st
import numpy as np

Titulo_concurso = '<p style="text-align:center";"font-family:Courier; color:Blue; font-size: 20px;">Hackaton-Quantum Apps</p>'
st.markdown(Titulo_concurso, unsafe_allow_html=True)


Titulo_principal = '<p style="font-family:TimesNewRoman; color:DarkBlue; font-size: 42px;">Óptica Cuántica</p>'
st.markdown(Titulo_principal, unsafe_allow_html=True)

st.caption('Esta aplicacón fue hecha con el propósito de introducir hacia los fenómenos cuánticos, especificamente dentro de la rama de la óptica cuántica, que ha sido de dificil comprensión para la cual nuestro objetivo es demostrar tales fenómenos con ejemplos visuales y prácticos de entender')

with st.sidebar:
    add_header = st.header(
        "Temas")

st.subheader('Introducción')
st.markdown('**¿Qué es la luz?**')
st.markdown('Una pregunta que los seres humanos han tratado de responder durante siglos.')
from imagenes import newton.png
st.image("newton.png")