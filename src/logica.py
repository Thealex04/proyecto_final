import pandas as pd 

#La función cargar_datos sirve para leer los datos desde el archivo CSV y los 
#convierte en un formato que Python pueda analizar
def cargar_datos(ruta_archivo):
    try:
        df = pd.read_csv(ruta_archivo)
        return df
    except Exception as error:
        print(f"Error al cargar datos:  {error}")
        return None
    
#La función limpiar_datos prepara los datos para que sean correctos y esten listos para analizarlos
def limpiar_datos(df):
    filas_antes = len(df)
    #La función dropna elimina filas que tienen valores vacíos
    df = df.dropna()
    filas_despues = len(df)

    print(f"Han sido eliminadas {filas_antes - filas_despues} filas")

    return df


def calcular_velocidad(df):
    # Convertimos todos los valores de la columna tiempo en string
    df['tiempo'] = df['tiempo'].astype(str)
    
    # Divide la columna tiempo en dos partes
    tiempo_split = df['tiempo'].str.split(":", expand=True)

    # Separamos las horas y los minutos y los convertimos a enteros
    df['horas'] = tiempo_split[0].astype(int)
    df['minutos'] = tiempo_split[1].astype(int)

    # Lo convertimos todo a minutos
    df['tiempo_min'] = df['horas'] * 60 + df['minutos']

    # Ya que tenemos el tiempo en minutos, calculamos la velocidad con la siguiente formula
    df['velocidad'] = df.eval('distancia / (tiempo_min/60)')
    return df


def estadisticas(df):
    distancia_total = df['distancia'].sum()
    distancia_media = df['distancia'].mean()
    tiempo_total = df['tiempo_min'].sum()

    if tiempo_total == 0:
        velocidad_media = 0
    else:
        velocidad_media = distancia_total / (tiempo_total/60)

    desnivel_total = df['desnivel'].sum()

    estadisticas = {
        "distancia_total": distancia_total,
        "distancia_media": distancia_media,
        "tiempo_total": tiempo_total,
        "velocidad_media": velocidad_media,
        "desnivel_total": desnivel_total

    }
    return estadisticas


def calcular_progreso(df):
    pass
    df.sort_values('fecha')
    



