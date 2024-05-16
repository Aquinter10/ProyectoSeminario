import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Correccion de Informe de seguros.")
st.subheader("Proyecto de Seminario de Ingenieria de Sistemas")

st.image("insurace.webp")
st.write("---")

st.write("""
## Contexto
Durante el segundo trimestre de 2024, Seguros Alta Vida enfrentó importantes desafíos operativos y financieros. Se identificaron dos problemas principales que impactaron las operaciones: un error en la estimación del presupuesto y un desfase inusual en el número de reclamaciones reportadas.
""")


import pandas as pd

# Carga el archivo CSV
df = pd.read_csv('clientsdata.csv')

st.subheader("Tabla de datos de los clientes de la compania: ")

st.dataframe(df)

st.write("---")


conteo_tipos_seguro = df['Tipo de seguro'].value_counts()


fig1, ax1 = plt.subplots()
ax1.pie(conteo_tipos_seguro, labels=conteo_tipos_seguro.index, autopct='%1.1f%%', startangle=140)
ax1.axis('equal')  


st.write("""
         ### Gráfico de pastel por  'Tipo de seguro':
         """)
st.pyplot(fig1)

st.write("""
         ## Tabla de precios de los seguros.
         """)

df = pd.read_csv('precios.csv')

st.dataframe(df)

st.write("""La compania presento una grafica donde proyectaban las estimaciones de ganancia por cobro de seguro en el proximo mes con los clientes actuales.
         
         La grafica a continuacion:
         
         
         """)
dpf = pd.read_csv('datacobros.csv')

counts = dpf['Tipo de seguro'].value_counts()

# Crear una gráfica de barras
plt.figure(figsize=(10, 5))
plt.bar(counts.index, counts.values, color='blue')
plt.title('Cantidad de Personas por Tipo de Seguro')
plt.xlabel('Tipo de Seguro')
plt.ylabel('Cantidad de Personas')
plt.xticks(rotation=45)

# Mostrar la gráfica en Streamlit
st.title('Análisis de Tipos de Seguro')
st.pyplot(plt)