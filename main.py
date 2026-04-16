from src.logica import cargar_datos, limpiar_datos


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

if __name__ == "__main__":
    main()


