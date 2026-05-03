import streamlit as st
import numpy as np

import pandas as pd

from datetime import datetime  



 
#st.sidebar.selectbox("Hola") 
st.sidebar.image("Imagen.jpg", width=100)

st.title("TRABAJO PRACTICO  ") 
opcionHome = st.sidebar.selectbox(
    "",
    [ "Home","Ejercicio 1", "Ejercicio 2",
     "Ejercicio 3","Ejercicio 4"]
)             # Importa 'datetime' para obtener fecha y hora actual y registrar movimientos.

if opcionHome=="Home": 
    
    st.write("Crysbel Anccasi Ramos") 
    st.write("Módulo 1 - Python Fundamentals") 
    st.write("2026") 
    st.write("Trabajo practico del curso en donde se pone practica lo aprendido en el primer Modulo de curso de Python") 
    st.write("Teconologìas usadas: Steamlit,NumPy, arrays y DataFrame ") 

if opcionHome=="Ejercicio 1":  
    st.title("💵 Movimientos Bancarios") 

    class Movimiento:                               # Define una clase 'Cuenta' (POO) que modela una cuenta bancaria con saldo.
        def __init__(self, Ingreso, saldo=0):   # Método constructor: se ejecuta al crear una instancia; recibe titular y saldo inicial.
            self.titular, self.saldo = Ingreso, saldo  # Asigna a la instancia (self) el nombre del titular y el saldo actual.
        def ingresar(self, m): self.saldo += m        # Método de negocio: suma 'm' al saldo; NO valida negativo (se controla en la UI).
        def gastar(self, m):                          # Método de negocio: intenta retirar 'm' del saldo actual.
            if m <= self.saldo: self.saldo -= m  



        
    c = st.session_state.setdefault("c", Movimiento("Ingreso", 100)) 

    h = st.session_state.setdefault("h", [])                     # En 'h' guardamos el historial: si no existe, crea una lista vacía.

    m = st.number_input("Monto", 0, 1000, 100)   

    i = st.session_state.setdefault("i",[])  
    g = st.session_state.setdefault("g", [])  

    opcion = st.selectbox(
        "Tipo movimiento:",
        ["Tipo Movimiento","Ingresar", "Gastar"]
    )


    if opcion=="Ingresar":                                   
        c.ingresar(m)                                           
        h.append(f"{datetime.now():%Y-%m-%d %H:%M:%S} · Ingreso · ${m} ")  
        i.append(f"{datetime.now():%Y-%m-%d %H:%M:%S} · Ingreso · ${m} ")
                                                                
    if opcion=="Gastar":                                    
        saldo_prev = c.saldo                                    
        c.gastar(m)                                             
        if c.saldo < saldo_prev:                                 
            h.append(f"{datetime.now():%Y-%m-%d %H:%M:%S} · Gasto   · ${m} ")  
            g.append(f"{datetime.now():%Y-%m-%d %H:%M:%S} · Gasto · ${m} ")                                                 
        else:                                                   
            st.warning("Fondos insuficientes.")   



    st.write(f" {c.titular} — Saldo: ${c.saldo}") 


    st.subheader(" Historial")                                  # Subtítulo para la sección de historial.
    st.text("\n".join(reversed(h)) if h else "Aún sin movimientos.") 

    st.subheader("Ingresos")  
    st.text("\n".join(reversed(i)) if h else "No hay ingreso") 

    st.subheader(" Gastos")  
    st.text("\n".join(reversed(g)) if h else "No hay gastos") 

    st.subheader("Saldo Final")  
    st.write(c.saldo)

    st.subheader("Flujo de caja") 
    if c.saldo>0:
        st.write("A favor")
    else:
        st.write("En contra")


if opcionHome=="Ejercicio 2":
    class Producto:
        def __init__(self, nombre_producto, precio):
            self.nombre_producto = nombre_producto
            self.precio = precio

    class Venta(Producto):
        def __init__(self, nombre_producto, precio):
            super().__init__(nombre_producto, precio)
            self.cantidad = 0

        def agregar_cantidad(self, cantidad):
            #self.cantidad.append(cantidad)
            self.cantidad=cantidad
        def total(self):
            return sum(self.cantidad)/len(self.precio) if self.cantidad else 0

    # ==== Interfaz Streamlit ====
    nombre_prod = st.text_input("Nombre del producto")
    precio = st.number_input("Precio", 0.0, 1000.0)

    if "ventas" not in st.session_state:
        st.session_state.ventas = []

    if st.button("Registrar producto"):
        prod = Venta(nombre_prod, precio)
        st.session_state.ventas.append(prod)
        st.success(f"✅ Producto {nombre_prod} registrado correctamente.")

    st.subheader("📚 Agregar Venta")
    if st.session_state.ventas:
        seleccionado = st.selectbox("Selecciona producto", [e.nombre_producto for e in st.session_state.ventas])
        cantidad = st.number_input("Cantidad", min_value=1, max_value=1000)
        if st.button("Agregar venta"):
            for e in st.session_state.ventas:
                if e.nombre_producto == seleccionado:
                    e.agregar_cantidad(cantidad)
                    st.success(f"Venta de {cantidad}unidades registrada del producto  {e.nombre_producto}")

        dataVentas = [{"Producto": e.nombre_producto, "Precio": e.precio,"Cantidad":e.cantidad,"Total": e.precio*e.cantidad} for e in st.session_state.ventas]
        st.dataframe(pd.DataFrame(dataVentas))
