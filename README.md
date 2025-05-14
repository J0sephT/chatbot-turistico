
# Chatbot Turístico del Ecuador

Este proyecto implementa un asistente conversacional inteligente desarrollado con Streamlit y la API de OpenAI. Está diseñado exclusivamente para responder preguntas relacionadas con el turismo en las principales ciudades del Ecuador, utilizando un dataset personalizado con información recopilada de fuentes confiables como TripAdvisor y Wikipedia.

## Descripción

El chatbot puede responder a preguntas como:

- "¿Qué lugares puedo visitar en Otavalo?"
- "Recomiéndame sitios turísticos en Quito"
- "¿Qué atractivos turísticos hay en Cuenca?"

Su funcionamiento se basa en un archivo JSON que contiene datos estructurados de cada ciudad, incluyendo descripciones y principales atracciones. El modelo no inventa información: solo responde lo que está presente en el dataset.

## Instalación local

1. Clona este repositorio:

```bash
git clone https://github.com/tu-usuario/Chatbot-turismo.git
cd Chatbot-turismo
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Crea un archivo `secrets.toml` dentro de la carpeta `.streamlit/` con tu clave API de OpenAI:

```
.streamlit/secrets.toml
```

Contenido:

```toml
OPENAI_API_KEY = "tu-clave-api"
```

4. Ejecuta la aplicación:

```bash
streamlit run app.py
```

## Despliegue en Streamlit Cloud

1. Sube el repositorio a GitHub (puede ser público o privado).
2. Accede a https://streamlit.io/cloud e inicia sesión con tu cuenta de GitHub.
3. Crea una nueva aplicación seleccionando este repositorio.
4. En la sección "Secrets" del panel de configuración de la app, añade tu clave de API:

```toml
OPENAI_API_KEY = "tu-clave-api"
```

5. Haz clic en "Deploy" para poner en línea la aplicación.

## Estructura del proyecto

```
chatbot-turismo/
├── app.py
├── dataset_turismo.json
├── requirements.txt
├── .gitignore
└── .streamlit/
    └── secrets.toml (solo localmente, no se sube a GitHub)
```

## Tecnologías utilizadas

- Python
- Streamlit
- OpenAI API

## Fuentes de información

- TripAdvisor Ecuador
- Wikipedia
- Wikivoyage
- Sitios turísticos oficiales del Ecuador
