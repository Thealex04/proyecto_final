import matplotlib.pyplot as plt
import pandas as pd
import os

os.makedirs("static/graficos", exist_ok=True)

# Aplicamos un estilo visual predifinido a todos los graficos para que se vean más limpios y claros
plt.style.use("seaborn-v0_8")

def grafico_distancia(df):

    # Creamos la figura del gráfico (ancho,alto)
    plt.figure(figsize=(8,5))

    # Creamos un gráfico de líneas
    plt.plot(df["fecha"], df["distancia"], marker="o", color="blue", label="Distancia")

    plt.title("Evolución de distancia")
    plt.xlabel("Fecha")
    plt.ylabel("Distancia (km)")

    # Con grid(True) añadimos cuadrícula al gráfico
    plt.grid(True)

    # Legend muestra la leyenda del grafico
    plt.legend()

    # Con xticks se rota las etiquetas del eje X
    plt.xticks(rotation=45)

    # Tight_layout ajusta automáticamente los espacios
    plt.tight_layout()

    # Guarda el gráfico como imagen y con dpi le ponemos una buena calidad a la imagen
    plt.savefig("static/graficos/distancia.png", dpi=300)

    # Por último cerramos el gráfico
    plt.close()

def grafico_velocidad(df):

    plt.figure(figsize=(8,5))

    plt.plot(df["fecha"], df["velocidad_kmh"], marker="o", color="green", label="Velocidad")

    plt.title("Velocidad media")
    plt.xlabel("Fecha")
    plt.ylabel("Velocidad (km/h)")

    plt.grid(True)

    plt.legend()

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("static/graficos/velocidad.png", dpi=300)

    plt.close()

def grafico_desnivel(df):
    plt.figure(figsize=(8,5))

    # Creamos un gráfico de barras
    plt.bar(df["fecha"], df["desnivel"], color="orange", label="Desnivel")

    plt.title("Desnivel")
    plt.xlabel("Fecha")
    plt.ylabel("Metros")

    plt.grid(True)

    plt.legend()

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("static/graficos/desnivel.png", dpi=300)

    plt.close()

def grafico_tipos_ruta(df):

    tipos = df['tipo'].value_counts()

    plt.figure(figsize=(6,6))

    plt.pie(
        tipos,
        labels=tipos.index,
        autopct='%1.1f%%',
        startangle=90
    )

    plt.title("Tipos de rutas")

    plt.savefig("static/graficos/tipos_ruta.png", dpi=300)

    plt.close()

def grafico_paises_ganadores(df):

    paises = df["pais"].value_counts()

    plt.figure(figsize=(8,5))

    plt.bar(paises.index, paises.values, color="purple", label="Victorias")

    plt.title("Victorias por pais")
    plt.xlabel("Pais")
    plt.ylabel("Numero de victorias")

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.savefig("static/graficos/paises.png", dpi=300)

    plt.close()
