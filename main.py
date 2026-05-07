from src.logica import cargar_datos, limpiar_datos, calcular_velocidad, estadisticas, calcular_progreso
from src.modelos import RutaMTB, RutaCarretera, RutaCiclocross, Ciclista
from src.visualizacion import grafico_distancia, grafico_velocidad, grafico_desnivel


def main():
    print("Proyecto ciclismo iniciado\n")
   
    # Carga y análisis de datos
    
    rutas = cargar_datos("data/rutas.csv")
    competiciones = cargar_datos("data/competiciones.csv")

    if rutas is not None:
        print(" Datos de las rutas:")
        rutas = limpiar_datos(rutas)
        rutas = calcular_velocidad(rutas)
        print(rutas, "\n")

        print(" --- ESTADÍSTICAS ---")
        estadisticas_rutas = estadisticas(rutas)

        for clave, valor in estadisticas_rutas.items():
            print(f"{clave}: {valor}")

        print("\n --- Progreso del ciclista ---")
        progreso = calcular_progreso(rutas)

        for clave, valor in progreso.items():
            print(f"{clave}: {valor}")

    if competiciones is not None:
        print("\n Datos de las competiciones:")
        competiciones = limpiar_datos(competiciones)
        print(competiciones.head(), "\n")

    df = cargar_datos("data/rutas.csv")
    grafico_distancia(df)
    grafico_velocidad(df)
    grafico_desnivel(df)

    print("Gráficos generados correctamente")
    
    # Preubas de POO

    print("\n --- PRUEBA DE CLASES (POO) ---\n")

    ruta1 = RutaMTB("2025-05-05", 25, 60, 600, "MTB")
    ruta2 = RutaCarretera("2025-07-05", 45, 90, 200, "Carretera")
    ruta3 = RutaCiclocross("2025-08-05", 35, 80, 400, "Ciclocross")

    ciclista1 = Ciclista("Sandro", 21, 93, 1.87)
    ciclista2 = Ciclista("Andres", 18, 65, 1.82)
    ciclista3 = Ciclista("Hugo", 19, 71, 1.70)

    ciclista1.agregar_ruta(ruta1)
    ciclista1.agregar_ruta(ruta3)

    ciclista2.agregar_ruta(ruta3)
    ciclista2.agregar_ruta(ruta2)

    ciclista3.agregar_ruta(ruta1)
    ciclista3.agregar_ruta(ruta3)

    print(ciclista1.resumen(), "\n")
    print(ciclista2.resumen(), "\n")
    print(ciclista3.resumen(), "\n")

    print(" --- INFORMACIÓN DE RUTAS ---")
    print(ruta1.terreno())
    print(ruta1.dificultad())
    print(ruta3.porteo())
    print(ruta2.terreno())


if __name__ == "__main__":
    main()
