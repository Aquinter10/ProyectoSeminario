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


st.write("""
         En este grafico de barras se evidencia la distribucion de clientes por cada tipo de seguros. Sin embargo, para el modo en que se tomaron los datos la compania uso una fuente de datos diferente a la original.
         
         Por lo tanto, se decide revisar estos datos y compararlos con los datos fuente.

         Desde el Dataframe usado para la grafica se pueden encontrar algunas inconsistencias, como el caso de datos duplicados.
         
         """)

st.dataframe(dpf)


st.write("---")


st.title('Comparación de DataFrames')
col1, col2 = st.columns(2)
with col1:
    st.header("DataFrame de Clientes mas reciente")
    st.dataframe(counts)
with col2:
    st.header("DataFrame Original Clientes")
    st.dataframe(conteo_tipos_seguro)


st.write("Dada la inconsistencia de ambos datos se determina que hubo error a la hora de la migracion de datos. Puntualmente hubo una neglicencia en transferir datos generales de clientes para determinar la proporcion de seguros y hacerlo manualmente. De haber sido el caso, esto explicaria los datos duplicados.")

st.write()