from src.logica import cargar_datos, limpiar_datos
from src.modelos import RutaMTB, RutaCarretera, RutaCiclocross, Ciclista


def main():
    print("Proyecto ciclismo iniciado\n")

    rutas = cargar_datos("data/rutas.csv")
    competiciones = cargar_datos("data/competiciones.csv")

    if rutas is not None:
        print("Datos de las rutas: ")
        rutas = limpiar_datos(rutas)
        print(rutas, "\n")

    if competiciones is not None:
        print("Datos de las competiciones: ")
        competiciones = limpiar_datos(competiciones)
        print(competiciones.head(), "\n")

    #Prueba clases POO

    ruta1 = RutaMTB("2025-05-05",25, 60, 600, "MTB")
    ruta2 = RutaCarretera("2025-07-05",45, 90, 200, "Carretera")
    ruta3 = RutaCiclocross("2025-08-05",35, 80, 400, "Ciclocross")

    ciclista1 = Ciclista("Sandro",21,93,1.87)
    ciclista2 = Ciclista("Andres",18,65,1.82)

    ciclista1.agregar_ruta(ruta1)
    ciclista1.agregar_ruta(ruta3)
    ciclista2.agregar_ruta(ruta3)
    ciclista2.agregar_ruta(ruta2)

    print(ciclista1.resumen())
    print("")
    print(ciclista2.resumen())
    print("")

    print(ruta1.terreno())
    print(ruta1.dificultad())
    print(ruta3.porteo())
    print(ruta2.terreno())


if __name__ == "__main__":
    main()

