

import pandas as pd
import streamlit as st
import numpy as np
st.set_page_config(page_title="Óptica Cuántica",page_icon="🎇")


Titulo_concurso = '<p style="text-align:center";"font-family:Courier; color:Blue; font-size: 20px;">Hackaton-Quantum Apps</p>'
st.markdown(Titulo_concurso, unsafe_allow_html=True)


Titulo_principal = '<p style="font-family:TimesNewRoman; color:DarkBlue; font-size: 42px;">Óptica Cuántica</p>'
st.markdown(Titulo_principal, unsafe_allow_html=True)

st.caption('Esta aplicacón fue hecha con el propósito de introducir hacia los fenómenos cuánticos, especificamente dentro de la rama de la óptica cuántica, que ha sido de dificil comprensión para la cual nuestro objetivo es demostrar tales fenómenos con ejemplos visuales y prácticos de entender')

page_names = ['Introducción', 'Efecto Fotoeléctrico', 'Ecuaciones de Maxwell', 'Polarización','Interferencia','Experimento de la doble rendija','Difracción','Reflexión','Refracción']

Temas = st.sidebar.radio("Escoge el tema",page_names)      


if Temas == 'Introducción':
    
    st.header('Introducción')
    st.subheader('**¿Qué es la luz?**')
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

    st.markdown('Ahora se sabe que la luz actúa como una onda y una particula, que es a lo que llamamos la naturaleza dual de la luz; la luz sigue principios de electromagnetismo, por lo que decimos que son ondas electromagnéticas.')
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.image("onda.png", width=450, caption='Onda electromangnética')

    with col3:
        st.write("")

    st.markdown("Las ondas electromagnéticas pueden ser clasificadas por su longitud de onda o su frecuencia; esta clasificación se llama **Espectro electromagnético**")
    st.image("https://cdn.kastatic.org/ka-perseus-images/01f944ab4471010d09766560f4d1c6da4846d97d.png", caption='Espectro electromagnético')
    st.markdown("Dentro del espectro electromagnético se encuentra la luz visible, esta es una pequeña parte de todo el espectro que en seres humanos es la única visualizable; arrastra el punto para ver que color se obtiene a diferentes longitudes")
    longitud = st.slider('Longitud de onda visible en nm',380,750,380)
    if longitud < 450:
        st.markdown('Color Morado')
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Morado.png/250px-Morado.png",width=200)
    if 450 < longitud < 495:
        st.markdown('Color Azul')
        st.image("https://upload.wikimedia.org/wikipedia/commons/5/52/Tipos_de_azules.png",width=200)
    if 495 < longitud < 570:
        st.markdown('Color Verde')
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Tipos_de_verde.png/250px-Tipos_de_verde.png",width=200)
    if 570 < longitud < 590:
        st.markdown('Color Amarillo')
        st.image("https://upload.wikimedia.org/wikipedia/commons/5/5b/Amarillos.png",width=200)
    if 590 < longitud < 620:
        st.markdown('Color Naranja')
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Shades_of_orange.png/250px-Shades_of_orange.png",width=200)
    if 620 < longitud < 750:
        st.markdown('Color Rojo')
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Rojos.png/250px-Rojos.png",width=200)

    st.markdown("No se entendía muy bien el concepto de luz hasta 1900, cuando el físico Max Planck empezó a estudiar cuerpos negros (Objetos teóricos que absorven la energía radiante totalmente), estos se calentaban y empezaban a brillar.")
    st.image("http://nuclear-power.com/wp-content/uploads/blackbody-radiation-chart-min.png",width=700)
    st.markdown("Planck descubrió que la radiación electromagnética emitida por estos cuerpos no podia ser explicada por la física clásica; que postulaba que la energía podía ser emitida y absorbida por la materia en cualquier cantidad")
    st.markdown("Un cuerpo negro absorbe energía en modo de calor y emite luz, la física clásica postulaba que el cuerpo tiene la capacidad de absorber la energía hasta emitir ondas electromagnéticas por encima de la luz visible, emitiendo ondas de alta energía como las UV,  de rayos x y gamma")
    st.markdown("![Alt Text](https://steemitimages.com/DQmSXqSXPGdcPQiP3EfaZZQhipbZJg2RsAZmVTpUJvcGetZ/output_final_radiation.gif)")
    st.markdown("A esto se le llamó la catástrofe ultravioleta")
    st.image("https://slideplayer.es/slide/5497387/17/images/12/LEY+DE+RAYLEIGH-JEANS+Cat%C3%A1strofe+ultravioleta.jpg")
    st.markdown("Planck observó que la materia absorbía o emitía la energia en multiplos enteros del valor de la constante de Planck, pequeños paquetes conocidos como cuántos, por lo que Einstein propuso su teoría del efecto fotoeléctrico")
    st.latex('h=6.626^{-34}J')
    st.caption('El efecto fotoeléctrico nos dice que si un electrón absorbe la energía de un fotón y este tiene más energía que la función del trabajo el electrón es arrancado del material, explicando porque los materiales no absorben energia hasta emitir ondas de alta energía')
    st.markdown("Los fotones pueden ser emitidos o absorbidos por los átomos, se absorben por completo y al momento de que el átomo pierde energía se emiten, cargando con la energía exacta que se perdió la cual es directamente proporcional a su frecuencia.")
    st.markdown("Eso demostró que la luz se comporta también como una partícula")
    st.markdown("Esta relación es descrita por la famosa **Ecuación de Planck**:")
    st.latex('E=hf')
    st.caption("*Las frecuencias más altas nos hacen más daño, porque significan más energía")

if Temas == 'Efecto Fotoeléctrico':
    st.header('Efecto Fotoeléctrico')
    st.write("Cuando la luz brilla en un metal,los electrones pueden ser expulsados de la superficie del metal en un fenómeno conocido como el efecto fotoeléctrico.")
    st.write("Debido al efecto fotoeléctrico fue prueba que la luz tiene una dualidad, es decir, se puede comportar como partícula y como onda.")
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.image("FOTO.png")


    with col3:
        st.write("")
    st.subheader("Modelo propuesto por Einstein")
    st.write("Con base en el modelo ondulatorio de la luz, los físicos predijeron que el aumento de la amplitud de la luz incrementaría la energía cinética de los fotoelectrones emitidos, mientras que el aumento de la frecuencia incrementaría la corriente medida. Contrario a las predicciones, los experimentos mostraron que el aumento en la frecuencia incrementaba la energía cinética de los fotoelectrones, mientras que el aumento en la amplitud de la luz incrementaba la corriente.")
    st.write("Con base en estos descubrimientos, Einstein propuso que la luz se comportaba como una corriente de partículas llamadas fotones con una energía de:")
    st.latex("E= hv")
    st. write("La energía de un fotón es proporcional a la frecuencia de la luz (f) por lo que la amplitud de la luz (h) es proporcional al número de fotones con una frecuencia dada.")
    
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.markdown("![Alt Text](https://upload.wikimedia.org/wikipedia/commons/6/6e/EFECTOFOTOELECTRICOpeq.gif)")

    with col3:
        st.write("")
    
    st.subheader("Bandgap")
    st.write("El bandgap o tambien conocido como banda prohibida es la energía mínima necesaria para excitar un electrón desde su estado ligado a un estado libre que le permita participar en la conducción, dentro de una celda solar. Lo importante a resaltar aqui es el intervalo de banda es la cantidad mínima de energía necesaria para un electrón de liberarse de su estado de enlace. Cuando se cumple la energía de banda prohibida, el electrón es excitado a un estado libre, y por lo tanto puede participar en la conducción.La brecha de banda determina la cantidad de energía que se necesita del sol para la conducción, así como la cantidad de energía que se genera.Un agujero se crea donde el electrón estaba obligado anteriormente. Este agujero también participa en la conducción.")
    
    if st.button("Ver tabla"):
        col1, col2, col3 = st.columns([1,6,1])
        with col1:
            st.write("")

        with col2:
            st.write("")
            st.write("Anchos de Banda",pd.DataFrame({
            'Material':["PbSe","PbTe","PbS","InN","Ge","GaSb","Si","InP","GaAs", "CdTe", "AlSb","CdSe","AlAs","ZnTe","GaP","CdS","AlP","ZnSe","SiC","GaN","ZnS","Diamante","AlN"],
            'Banda Prohibida en eV':[0.27,0.29,0.37,0.67,0.67,0.7,1.11,1.35,1.43,1.58,1.6,1.73,2.16,2.25,2.26,2.42,2.45,2.7,2.86,3.4,3.6,5.5,6.2],
            }))
        with col3:
            st.write("")
        
    else:
        st.write("")    
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")

    with col2:
        st.image("Banda.png", width=550)
    with col3:
        st.write("")
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.markdown("![Alt Text](https://upload.wikimedia.org/wikipedia/commons/1/1f/Bulkbandstructure.gif)")

    with col3:
        st.write("")
    st.write("Ese “agujero” que participa en la conducción, su movimiento es análogo al movimiento de una burbuja en un líquido. A pesar de que en realidad es el líquido que se mueve, es más fácil para describir el movimiento de la burbuja que va en la dirección opuesta.")
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.markdown("![Alt Text](https://i.pinimg.com/originals/c1/4f/b5/c14fb5f3ad4a890f9296c2f842068463.gif)")

    with col3:
        st.write("")    

       
if Temas == 'Ecuaciones de Maxwell':
    st.header("Ecuaciones de Maxwell")

if Temas == 'Polarización':
    st.header("Polarización")

if Temas == 'Interferencia':
    st.header('Interferencia')
    st.markdown('La luz, como las ondas mecánicas puede presentar interferencia; existen dos tipos: la **Interferencia Constructiva** y la **Interferencia Destructiva**')
    st.markdown('En la interferencia constructiva la amplitud de la onda resultante es mayor que una u otra onda individual, mientras que en la interferencia destructiva la amplitud resultante es menor que la onda mas grande.')
    

if Temas == 'Experimento de la doble rendija':
    st.write("Mateme")

if Temas == 'Difracción':
    st.write("Porfavor")

if Temas == 'Reflexión':
    st.write(":,,")

if Temas == 'Refracción':
    st.write("refraccion")
