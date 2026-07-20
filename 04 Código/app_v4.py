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
if "fragmentos" not in st.session_state:
    st.session_state.fragmentos = []

if "total_resultados" not in st.session_state:
    st.session_state.total_resultados = 0

if buscar:
    ruta_pdf = "documentos/SIG-CJ.pdf"
    documento = fitz.open(ruta_pdf)
    texto_completo = ""
    for pagina in documento:
        texto_completo +=pagina.get_text()
    texto_minusculas = texto_completo.lower()
    pregunta_minusculas = pregunta.lower()
    palabras_vacias = {
    "el", "la", "los", "las",
    "un", "una", "unos", "unas",
    "de", "del", "al", "en",
    "y", "o", "que", "qué",
    "cual", "cuál", "cuales", "cuáles",
    "como", "cómo", "quien", "quién",
    "es", "son", "se", "para", "por"
}
    palabras_pregunta = pregunta_minusculas.split()
    palabras_clave = []

    for palabra in palabras_pregunta:
        palabra_limpia = palabra.strip("¿?¡!.,;:")

        if palabra_limpia not in palabras_vacias:
            palabras_clave.append(palabra_limpia)

    if not palabras_clave:
        st.warning("Escribe una pregunta con palabras más específicas.")
        st.stop()   

    fragmentos_documento = []

    tamano_fragmento = 900
    avance = 450

    for inicio in range(0, len(texto_completo), avance):
        fin = inicio + tamano_fragmento
        fragmento = texto_completo[inicio:fin]

        puntuacion = 0

        for palabra_clave in palabras_clave:
            if palabra_clave in fragmento.lower():
                puntuacion += 1

        if puntuacion > 0:
            fragmentos_documento.append(
                {
                    "fragmento": fragmento,
                    "puntuacion": puntuacion
                }
            )

    fragmentos_documento.sort(
    key=lambda resultado: resultado["puntuacion"],
    reverse=True
    )

    resultados = fragmentos_documento[:20]    
    if resultados:

        fragmentos = []

        for resultado in resultados:
            fragmentos.append(resultado["fragmento"])

        st.session_state.fragmentos = fragmentos
        st.session_state.total_resultados = len(resultados)

    else:

        st.session_state.fragmentos = []
        st.session_state.total_resultados = 0
if st.session_state.fragmentos:

    st.success(
        f"Se encontraron {st.session_state.total_resultados} coincidencias."
    )

    opciones = [
        f"Resultado {numero + 1}"
        for numero in range(len(st.session_state.fragmentos))
    ]

    seleccion = st.selectbox(
        "Selecciona el resultado que deseas consultar:",
        opciones
    )

    indice_seleccionado = opciones.index(seleccion)

    st.write(
        st.session_state.fragmentos[indice_seleccionado]
    )   
   
