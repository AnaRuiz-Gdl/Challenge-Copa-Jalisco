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
    st.subheader("📄 Respuesta encontrada en el documento")
    st.caption("Fuente documental:")
    st.caption("Sistema Institucional de Gestión de la Copa Jalisco (SIG-CJ)")
    st.caption("Documento Maestro • Versión 1.0")
    respuesta_principal = st.session_state.fragmentos[0]

    inicio = 0

    frases_importantes = [
        "Responsable principal",
        "Dirección de Deporte Municipal",
        "Dirección de Copa Jalisco",
        "Coordinación de Deporte Municipal",
        "Coordinadores REgionales",
        "Sistema Institucional de Gestión",
        "Empresa Técnico-Deportiva",
        "Empresa Operadora",
        "Comité de Honor y Justicia",
        "Presidente Municipal",
        "El Municipio",
        "La Copa Jalisco"
    ]
    posiciones_encontradas =[]

    for frase in frases_importantes:
        posicion = respuesta_principal.find(frase)

        if posicion != -1:
            posiciones_encontradas.append(posicion)
            
    if posiciones_encontradas:
        inicio =min(posiciones_encontradas)
        respuesta_limpia = respuesta_principal[inicio:]
    else:
        respuesta_limpia = respuesta_principal

    ultimo_punto = respuesta_limpia.rfind(".")
    if ultimo_punto != -1:
        respuesta_limpia = respuesta_limpia[:ultimo_punto + 1]

    st.write(respuesta_limpia)
    st.divider()
    st.write("Otras coincidencias encontradas:")

    opciones = [
        f"Resultado {numero + 2}"
        for numero in range(len(st.session_state.fragmentos) - 1)
    ]

    seleccion = st.selectbox(
        "Selecciona el resultado que deseas consultar:",
        opciones
    )

    indice_seleccionado = opciones.index(seleccion) + 1

    st.write(
        st.session_state.fragmentos[indice_seleccionado]
    )   
   
