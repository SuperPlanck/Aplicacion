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

col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.image("newton.png", width=600, caption='Figura No.1 Newton y el estudio de la luz')

with col3:
    st.write("")

st.markdown('Newton, principal aportador de la teoria de la luz estipulaba que las partículas de luz provenian de una fuente luminosa que estimulaba la vista.')
st.markdown('Esta idea le permitió justificar las bases nitrogenadas de la refracción y reflexión')