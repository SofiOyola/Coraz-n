# 🫀 Predictor de Problemas Cardiacos  

Aplicación desarrollada en **Streamlit** que permite predecir si un paciente sufrirá o no de problemas cardiacos a partir de dos variables:  
- **Edad** (entre 25 y 80 años)  
- **Colesterol** (entre 120 y 600 mg/dL)  

El modelo fue entrenado con un **Support Vector Classifier (SVC)** y los datos fueron normalizados usando **MinMaxScaler**. Ambos objetos fueron guardados en archivos `.jb` mediante **joblib**.  

---

## 🚀 Ejecución de la aplicación

1. Clonar este repositorio o descargar los archivos:  
   - `app.py`  
   - `svc_model.jb`  
   - `scaler.jb`  
   - `requirements.txt`

2. Instalar las dependencias necesarias:  
   ```bash
   pip install -r requirements.txt
