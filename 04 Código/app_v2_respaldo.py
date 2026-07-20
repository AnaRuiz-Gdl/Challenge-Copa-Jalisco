import streamlit as st
import fitz

st.title("🤖 SIG-CJ AI")
st.write (
    "Bienvenida al Asistente Inteligente del Sistema Institucional de Gestión de la Copa Jalisco."
)    
pregunta = st.text_input(
    "¿Qué deseas buscar en el SIG-CJ?"
)
buscar = st.button("Buscar")
if buscar:
    ruta_pdf = "documentos/SIG-CJ.pdf"
    documento = fitz.open(ruta_pdf)
    texto_completo = ""
    for pagina in documento:
        texto_completo +=pagina.get_text()
    texto_minusculas = texto_completo.lower()
    pregunta_minusculas = pregunta.lower()

    resultados = []
    inicio_busqueda = 0

    while True:
        posicion = texto_minusculas.find(
            pregunta_minusculas,
            inicio_busqueda
        )

        if posicion == -1:
            break

        resultados.append(posicion)
        inicio_busqueda = posicion + len(pregunta_minusculas)

    if resultados:
        st.success(f"Se encontraron {len(resultados)} coincidencias.")

        for posicion in resultados:
            inicio = max(0, posicion -300)
            fin = min(len(texto_completo), posicion + 500)

            fragmento = texto_completo[inicio:fin]

            st.write(fragmento)
            st.divider()

    else:
        st.error("No encontré esa información.")

        

