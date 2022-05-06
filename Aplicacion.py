import pandas as pd
import streamlit as st
import numpy as np
streamlit_style = "dd""
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Roboto', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)
Titulo_concurso = '<p style="text-align:center";"font-family:Courier; color:Blue; font-size: 20px;">Hackaton-Quantum Apps</p>'
st.markdown(Titulo_concurso, unsafe_allow_html=True)


Titulo_principal = '<p style="font-family:TimesNewRoman; color:DarkBlue; font-size: 42px;">Óptica Cuántica</p>'
st.markdown(Titulo_principal, unsafe_allow_html=True)

with st.sidebar:
    add_header = st.header(
        "Temas"
        
    )

st.subheader('Introduccion')