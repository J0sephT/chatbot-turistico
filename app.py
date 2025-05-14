import streamlit as st
import json
from openai import OpenAI

# Cargar clave API desde secrets
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

# Cargar el dataset turístico
with open("dataset_turismo.json", encoding="utf-8") as f:
    dataset = json.load(f)

# Construir el contexto a partir del dataset
def construir_contexto():
    contexto = ""
    for entry in dataset:
        ciudad = entry.get("ciudad", "Sin nombre")
        descripcion = entry.get("descripcion", "Sin descripción")
        atracciones = ""
        for a in entry.get("atracciones", []):
            if isinstance(a, dict):
                nombre = a.get("nombre", "Sin nombre")
                desc = a.get("descripcion", "Sin descripción")
                atracciones += f"\n  - {nombre}: {desc}"
            else:
                atracciones += f"\n  - {str(a)}"
        mapa = entry.get("mapa", "No disponible")
        contexto += f"\n\nCiudad: {ciudad}\nDescripción: {descripcion}\nAtracciones:{atracciones}\nMapa: {mapa}"
    return contexto.strip()

# Contexto turístico general
contexto_turismo = construir_contexto()

# Interfaz
st.set_page_config(page_title="Asistente Turístico del Ecuador", page_icon="🧭")
st.title("Asistente Turístico del Ecuador")
st.markdown("""
Bienvenido. Soy tu guía turístico virtual especializado en Ecuador.  
Puedes preguntarme qué ver, qué visitar o qué hacer en las siguientes ciudades:

""")

# Mostrar las ciudades conocidas
ciudades_conocidas = [
    "Quito", "Guayaquil", "Cuenca", "Baños de Agua Santa", "Otavalo", "Mindo", "Montañita",
    "Puerto Ayora (Galápagos)", "Puerto Baquerizo Moreno (Galápagos)", "Puerto Villamil (Galápagos)",
    "Salinas", "Manta", "Puerto López", "Tena", "Puyo", "Riobamba", "Loja", "Vilcabamba", "Zaruma",
    "Papallacta", "Alausí", "Playas (General Villamil)", "Canoa", "Puerto Misahuallí"
]

st.markdown(f"""<div style='background-color:#f0f0f5; padding: 10px; border-radius: 5px;'>
<b>Cobertura actual:</b><br>
{", ".join(ciudades_conocidas)}
</div>""", unsafe_allow_html=True)

st.markdown("")

# Entrada del usuario
pregunta = st.text_input("¿Qué deseas saber sobre estas ciudades?")

# Generar respuesta si hay pregunta
if pregunta:
    with st.spinner("Consultando al asistente..."):
        try:
            respuesta = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "Eres un asistente turístico inteligente. Solo puedes responder preguntas basadas en el siguiente contexto sobre ciudades de Ecuador. Si no está en el contexto, responde: 'Lo siento, no tengo información sobre eso en este momento.' Sé claro, elocuente y detallado."
                    },
                    {
                        "role": "system",
                        "content": f"Contexto del dataset:\n{contexto_turismo}"
                    },
                    {
                        "role": "user",
                        "content": pregunta
                    }
                ],
                temperature=0.7,
                max_tokens=800
            )

            st.success(respuesta.choices[0].message.content)

        except Exception as e:
            st.error(f"Error al consultar la API: {e}")
