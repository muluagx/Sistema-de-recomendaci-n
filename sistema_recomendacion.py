# -*- coding: utf-8 -*-
"""SISTEMA_RECOMENDACION.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XiibZ-bimWNjIeS81nbgR-rgUAgRyABS
"""

!pip install streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile pp.py
# import streamlit as st
# import pandas as pd
# from nltk.corpus import stopwords
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.neighbors import NearestNeighbors
# from PyPDF2 import PdfReader
# import nltk
# 
# # Descargar stopwords en español
# nltk.download('stopwords')
# stop_words_spanish = stopwords.words('spanish')
# 
# # Funciones de procesamiento de texto
# def cargar_texto_pdf(file):
#     paginas_texto = []
#     pdf = PdfReader(file)
#     for i, pagina in enumerate(pdf.pages):
#         texto_pagina = pagina.extract_text()
#         if texto_pagina:
#             paginas_texto.append((i + 1, texto_pagina))
#     return paginas_texto
# 
# def preprocesar_y_vectorizar(textos):
#     vectorizer = TfidfVectorizer(stop_words=stop_words_spanish)
#     vectores = vectorizer.fit_transform(textos)
#     return vectores, vectorizer
# 
# def entrenar_recomendador(vectorizer, vectores):
#     knn = NearestNeighbors(n_neighbors=1, metric='cosine')
#     knn.fit(vectores)
#     return knn
# 
# def clasificar_noticia(noticia, vectorizer, knn, categorias):
#     vector_noticia = vectorizer.transform([noticia])
#     distancia, indice = knn.kneighbors(vector_noticia)
#     return categorias[indice[0][0]], distancia[0][0]
# 
# def clasificar_varias_noticias(file, vectorizer, knn, categorias, palabras_clave):
#     paginas_texto = cargar_texto_pdf(file)
#     resultados = []
# 
#     for pagina, texto_noticia in paginas_texto:
#         facultad_recomendada, distancia = clasificar_noticia(texto_noticia, vectorizer, knn, categorias)
# 
#         relevancia_clave = sum(1 for palabra in palabras_clave if palabra in texto_noticia.lower())
# 
#         resultados.append({
#             "Página": pagina,
#             "Facultad": facultad_recomendada,
#             #"Distancia": distancia,
#             "Relevancia Palabras Clave": relevancia_clave,
#             "Texto": texto_noticia[:100] + '...'
#         })
# 
#     tabla_resultados = pd.DataFrame(resultados)
#     tabla_resultados = tabla_resultados.sort_values(by=["Relevancia Palabras Clave", "Distancia"], ascending=[False, True])
# 
#     return tabla_resultados
# 
# # Interfaz con Streamlit
# st.title("Sistema de Recomendación de Noticias")
# 
# # Cargar archivo
# uploaded_file = st.file_uploader("Selecciona un archivo PDF de noticias", type="pdf")
# 
# # Entrada de palabras clave
# palabras_clave_input = st.text_input("Ingresa palabras clave (separadas por coma):")
# 
# # Ejecutar análisis
# if st.button("Ejecutar Clasificación"):
#     if uploaded_file is None:
#         st.error("Por favor, sube un archivo PDF.")
#     else:
#         # Procesar palabras clave
#         palabras_clave = [palabra.strip().lower() for palabra in palabras_clave_input.split(",")]
# 
#         # Ejemplo de datos de categorías
#         textos_categorias = {
#             "ingeniería": "texto de ejemplos de noticias o artículos sobre ingeniería...",
#             "medicina": "texto de ejemplos de noticias o artículos sobre medicina...",
#             "economía": "texto de ejemplos de noticias o artículos sobre economía...",
#             "sistemas": "texto de ejemplos de noticias o artículos sobre sistemas..."
#         }
#         textos = list(textos_categorias.values())
#         categorias = list(textos_categorias.keys())
# 
#         # Entrenamiento del modelo
#         vectores, vectorizer = preprocesar_y_vectorizar(textos)
#         knn = entrenar_recomendador(vectorizer, vectores)
# 
#         # Clasificación de noticias
#         tabla_resultados = clasificar_varias_noticias(uploaded_file, vectorizer, knn, categorias, palabras_clave)
# 
#         st.success("Análisis completado.")
#         st.write(tabla_resultados)
# 
#         # Opción de descargar el archivo CSV
#         csv = tabla_resultados.to_csv(index=False).encode('utf-8')
#         st.download_button("Descargar resultados como CSV", data=csv, file_name="resultados.csv", mime="text/csv")
# 
#

!nohup streamlit run pp.py &

!pip install pyngrok #Install pyngrok using pip
from pyngrok import ngrok

# Configuración automática de ngrok para el acceso público
ngrok.set_auth_token("2oJtCBdkmzT5O3fVNMUYwxKgZg8_5Q3JtqZWgDUjikBjXAku6")  # Coloca tu token aquí

# Conectar ngrok a la aplicación de Streamlit
public_url = ngrok.connect("8501")
print(f"Access your Streamlit app here: {public_url}")

#!ps aux

#!kill 38852

#!pkill streamlit