# 🤖 SIG-CJ AI

> **Asistente inteligente para consultar el Sistema Institucional de Gestión de la Copa Jalisco (SIG-CJ)**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?logo=streamlit&logoColor=white)
![Versión](https://img.shields.io/badge/versión-0.5-success)
![Estado](https://img.shields.io/badge/estado-funcional-brightgreen)

Proyecto desarrollado como parte del **Challenge ONE — Oracle Next Education (Alura Latam)**.

---

## 📌 Descripción

**SIG-CJ AI** es una aplicación web desarrollada en Python y Streamlit para consultar información contenida en el Documento Maestro del **Sistema Institucional de Gestión de la Copa Jalisco**.

La versión 0.5 procesa el documento PDF, identifica las palabras clave de la consulta, clasifica los fragmentos encontrados mediante un sistema de puntuación y presenta de forma jerarquizada el resultado documental con mayor relevancia, acompañado de coincidencias relacionadas y la referencia de la fuente utilizada.

Su propósito es reducir el tiempo necesario para localizar información institucional y facilitar la consulta de funciones, responsabilidades, actores y principios del Programa Institucional Copa Jalisco.

---

## 🎯 Objetivo del proyecto

Desarrollar un asistente documental funcional capaz de:

- leer y procesar un documento institucional en formato PDF;
- recibir consultas formuladas por el usuario;
- identificar palabras clave relevantes;
- localizar fragmentos relacionados dentro del documento;
- clasificar coincidencias por puntuación;
- presentar el resultado principal y otras coincidencias;
- mantener visible la referencia documental utilizada.

---

## ✨ Funcionalidades

- Lectura automática del Documento Maestro SIG-CJ.
- Extracción de texto mediante **PyMuPDF**.
- Normalización de consultas y eliminación de palabras vacías.
- Fragmentación del contenido con superposición.
- Búsqueda por palabras clave.
- Clasificación de coincidencias mediante puntuación.
- Presentación automática del fragmento documental con mayor puntuación.
- Consulta de resultados complementarios.
- Referencia permanente a la fuente documental.
- Interfaz web desarrollada con Streamlit.

---

## 🏗️ Arquitectura de la solución

```text
Usuario
  │
  ▼
Interfaz web (Streamlit)
  │
  ▼
Captura y normalización de la consulta
  │
  ▼
Identificación de palabras clave
  │
  ▼
Lectura y procesamiento del PDF
  │
  ▼
Fragmentación del contenido
  │
  ▼
Clasificación de coincidencias
  │
  ▼
Presentación del resultado principal
y de coincidencias relacionadas
```

---

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **Streamlit**
- **PyMuPDF (fitz)**
- **Git**
- **GitHub**
- **Visual Studio Code**
- **Markdown**

---

## 📂 Estructura del repositorio

```text
Challenge-Copa-Jalisco/
│
├── 04 Código/
│   ├── assets/
│   │   ├── 01_interfaz_principal.png
│   │   ├── 02_direccion_deporte_municipal.png
│   │   ├── 03_empresa_operadora.png
│   │   └── 04_empresa_tecnica_deportiva.png
│   │
│   ├── documentos/
│   │   └── SIG-CJ.pdf
│   │
│   ├── src/
│   │   └── app_v5.py
│   │
│   ├── app.py
│   ├── app_v2_respaldo.py
│   ├── app_v4.py
│   ├── image.png
│   ├── README.md
│   └── requirements.txt
│
└── README.md
```

> El README técnico con la explicación detallada del desarrollo se encuentra en [`04 Código/README.md`](04%20Código/README.md).

---

## ▶️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone git@github.com:AnaRuiz-Gdl/Challenge-Copa-Jalisco.git
cd Challenge-Copa-Jalisco
```

### 2. Entrar a la carpeta de código

```bash
cd "04 Código"
```

### 3. Crear un entorno virtual

```bash
python -m venv .venv
```

### 4. Activar el entorno virtual

**Windows**

```bash
.venv\Scripts\activate
```

**Linux o macOS**

```bash
source .venv/bin/activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 6. Ejecutar la aplicación

```bash
streamlit run src/app_v5.py
```

La aplicación estará disponible localmente en:

```text
http://localhost:8501
```

---

## 💬 Casos de uso validados en la versión 0.5

### Dirección de Deporte Municipal

Consulta utilizada:

> Dirección de Deporte Municipal

![Consulta sobre Dirección de Deporte Municipal](04%20Código/assets/02_direccion_deporte_municipal.png)

### Empresa Operadora

Consulta utilizada:

> ¿Cuáles son las obligaciones de la Empresa Operadora?

![Consulta sobre Empresa Operadora](04%20Código/assets/03_empresa_operadora.png)

### Empresa Técnico-Deportiva

Consulta utilizada:

> Empresa Técnico-Deportiva y sus funciones

![Consulta sobre Empresa Técnico-Deportiva](04%20Código/assets/04_empresa_tecnica_deportiva.png)

---

## 🖥️ Interfaz principal

La siguiente captura muestra la aplicación en funcionamiento, incluyendo la consulta, el número de coincidencias, la respuesta encontrada y la referencia documental.

![Interfaz principal de SIG-CJ AI](04%20Código/assets/01_interfaz_principal.png)

---

## 📈 Evolución del proyecto

| Versión | Descripción |
|---|---|
| **0.1** | Lectura inicial del documento PDF y extracción del contenido. |
| **0.2** | Implementación de búsqueda básica por palabras clave. |
| **0.3** | Incorporación de múltiples coincidencias y selección de resultados. |
| **0.4** | Clasificación de fragmentos mediante un sistema de puntuación por relevancia. |
| **0.5** | Presentación jerarquizada del resultado principal, coincidencias complementarias y referencia documental. |

---

## 🚀 Estado actual

**Versión vigente: 0.5**

La aplicación es funcional y cumple con el objetivo central del Challenge: responder consultas basadas en un documento PDF mediante una interfaz web disponible para el usuario.

La versión actual utiliza recuperación por palabras clave. Por ello, la calidad de la respuesta depende de la relación entre los términos de la consulta y el contenido literal del documento.

---

## 🔮 Próxima evolución: versión 0.6

La versión 0.6 estará orientada a mejorar la precisión y pertinencia de las respuestas mediante:

- mayor peso para coincidencias en encabezados y frases institucionales;
- identificación más precisa de la intención de la consulta;
- reducción de fragmentos relacionados pero no directamente pertinentes;
- delimitación más limpia de las respuestas;
- identificación de la página de origen;
- evaluación de búsqueda semántica mediante embeddings;
- generación de respuestas sintetizadas con referencia documental.

---

## 📚 Aprendizajes obtenidos

Durante el desarrollo se aplicaron conocimientos relacionados con:

- procesamiento de documentos PDF;
- desarrollo de interfaces web con Streamlit;
- organización del código fuente;
- construcción de motores de búsqueda por palabras clave;
- clasificación de resultados mediante puntuación;
- control de versiones con Git;
- publicación y documentación de proyectos en GitHub;
- elaboración de documentación técnica en Markdown.

---

## 👩‍💻 Autora

**Ana Ruiz**

Proyecto desarrollado como parte del **Challenge ONE — Oracle Next Education (Alura Latam)**.

---

## 📄 Documentación técnica

Para consultar la arquitectura detallada, las instrucciones completas de instalación, los ejemplos de respuestas y el historial técnico del proyecto, revisa:

➡️ [`04 Código/README.md`](04%20Código/README.md)
