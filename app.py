import streamlit as st
import joblib
import numpy as np

# Cargar el modelo y el scaler
scaler = joblib.load("scaler.jb")
modelo = joblib.load("svc_model.jb")

# Título y subtítulo
st.title("Predictor de problemas cardiacos")
st.subheader("Elaborado por ® Unab 2025")

# Sliders de entrada
edad = st.slider(
    "Seleccione la edad:",
    min_value=25,
    max_value=80,
    value=55,
    step=1
)

colesterol = st.slider(
    "Seleccione el nivel de colesterol:",
    min_value=120,
    max_value=600,
    value=242,
    step=2
)

# Botón para predecir
if st.button("Predecir"):
    # Transformar los datos
    entrada = np.array([[edad, colesterol]])
    entrada_norm = scaler.transform(entrada)

    # Predicción
    prediccion = modelo.predict(entrada_norm)[0]

    # Mostrar resultado con imagen
    if prediccion == 0:
        st.success("✅ El paciente NO sufrirá del corazón")
        st.image("https://e00-expansion.uecdn.es/assets/multimedia/imagenes/2016/03/20/14584973664622.jpg", width=400)
    else:
        st.error("⚠️ El paciente SÍ sufrirá del corazón")
        st.image("https://www.shutterstock.com/image-vector/unwell-man-feel-sick-suffer-600nw-2145831019.jpg", width=400)
