import streamlit as st
import numpy as np
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns
#from io import StringIO

st.sidebar.image("Imagen.jpg", width=100)

st.title("Especialización en Python  for Analytics ") 
opcionHome = st.sidebar.selectbox(
    "",
    [ "Home","Modulo 1", "Modulo 2"]
)          

if opcionHome=="Modulo 1":
    st.subheader("Trabajo Practico 2 de la Especialización en Python  for Analytics") 
    st.write("Crysbel Anccasi Ramos") 
    st.write("Módulo 2 - Especialización en Python  for Analytics") 
    st.write("2026") 
    st.write("Trabajo practico del curso de Especializacion en Python for Analytics, en donde se pone practica lo aprendido en el 2º Modulo") 
    st.write("Teconologìas usadas: Steamlit,NumPy,Pandas , matplotlib,seaborn y DataFrame ") 

if opcionHome=="Modulo 2":
    archivo=st.file_uploader("BankMarketing.csv",type=["csv"]) 

    if archivo is not None   :

        st.write("Archivo cargado") 
        df=pd.read_csv(archivo)


        st.subheader("Vista previa")
        st.write(df.head())
        
        st.write("Nº de columnas y columnas") 
        st.write(df.shape)
        
        st.subheader("Item 1: Información general del dataset")  
        buffer = io.StringIO()
        df.info(buf=buffer)
        info = buffer.getvalue()

        st.text(info)
        st.write("Tipos de datos") 
        st.write(df.dtypes)

        st.write("Conteo de valores nulos") 
        st.write(df.isnull().sum())

        st.subheader("Item 2: Clasifiaciòn de variables")  
        df["TotalCharges"] = pd.to_numeric(
            df["TotalCharges"],
            errors="coerce"
        ) 
        st.write("Datos Categoricos")  
        st.dataframe(df.select_dtypes(include="object"))

        st.write("Datos Numericos")  
        
        st.dataframe(df.select_dtypes(include="number"))
        
        st.write("Funcion Personalizada")
        def  prom_TotalCharges():

            prom_TotalCharges=df["TotalCharges"].mean()

            return prom_TotalCharges
        st.write("Promedio TotalCharges : " ,prom_TotalCharges())

        st.write("Mostrar resultados con conteo de Contract")
        conteo=df["Contract"].value_counts()
        conteo

        st.subheader("Item 3: Estadísticas descriptivas ")  
        resumen=df.describe()
        resumen
        st.write("Interpretación básica de medias, medianas y dispersión ")
        st.write("La media de Senior Citizen es: ", df["SeniorCitizen"].mean())
        st.write("La mediana de Senior Citizen es: ", df["SeniorCitizen"].median())
        st.write("La desviacion estandar de Senior Citizen es: ", df["SeniorCitizen"].std())

        st.subheader("Ítem 4: Análisis de valores faltantes ")  
        nulos=df.isnull().sum()
        st.write("Solo TotalCharges tiene valores nulos, estos son ",nulos[nulos > 0])

        st.subheader("Ítem 5:Distribución de variables numéricas ")

        variable = df.select_dtypes(include=np.number)
        variable.hist(
                figsize=(12,6),
                bins=30
        )

        st.pyplot()

        st.subheader("Ítem 6:Análisis de variables categóricas (Partner) ")
        
        plt.figure(figsize=(10,5))

        categ=df.select_dtypes(include="object" )
        conteo = categ["Partner"].value_counts()

        fig, ax = plt.subplots(figsize=(12,6))

        ax.bar(
            conteo.index,
            conteo.values
        )

        st.pyplot(fig)

        st.subheader("Ítem 7: Análisis bivariado (numérico vs categórico)") 

        bivariado = df[["Partner","tenure"]]
        fig, ax = plt.subplots(figsize=(10,5))
        sns.boxplot(
            x="Partner",
            y="tenure",
            data=df,
            ax=ax
        )

        plt.title("Tenure por Partner")
        st.pyplot(fig)

        st.subheader("Ítem 7: Análisis bivariado (categórico vs categórico)") 

        bivariado = df[["Partner","InternetService"]]
        fig, ax = plt.subplots(figsize=(10,5))
        sns.boxplot(
            x="Partner",
            y="InternetService",
            data=df,
            ax=ax
        )

        plt.title("Partner vs InternetService")
        st.pyplot(fig)








