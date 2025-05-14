import streamlit as st
import openai

st.title("📝 Corrector gramatical en español")
st.write("Esta app **solo corrige errores gramaticales** en textos en español. No hace otras tareas.")

# Entrada para la API key
api_key = st.text_input("🔑 Ingresa tu clave API de OpenAI:", type="password")

# Entrada del texto a corregir
user_input = st.text_area("✍️ Introduce el texto que deseas corregir:")

# Botón de corrección
if st.button("Corregir texto"):
    if not api_key:
        st.warning("Por favor ingresa tu clave API.")
    elif not user_input.strip():
        st.warning("Por favor introduce un texto.")
    else:
        try:
            openai.api_key = api_key  # Establecer la clave API

            prompt = f"""
Eres un asistente que solo corrige errores gramaticales en textos escritos en español. 
No debes traducir, resumir ni responder preguntas. Si se te pide otra cosa, responde:
"Lo siento, solo puedo corregir errores gramaticales en textos escritos en español."

Texto original:
{user_input}

Texto corregido:
"""

            # ✅ Llamada correcta a la API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=300
            )

            correccion = response.choices[0].message.content
            st.success("Texto corregido:")
            st.write(correccion)

        except Exception as e:
            st.error(f"Error al llamar a la API: {e}")
