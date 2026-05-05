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
    # Limpiamos el formato
    df['tiempo'] = df['tiempo'].astype(str).str.strip()

    #Convertimos el formato de h:mm a horas
    df['tiempo_horas'] = pd.to_timedelta(df['tiempo'] + ":00").dt.total_seconds() /3600

    #Elimina datos inválidos
    df = df.dropna(subset=['tiempo_horas'])
    df = df[df['tiempo_horas'] > 0]

    df['velocidad'] = df['distancia'] / df['tiempo_horas']

    return df


def estadisticas(df):
    distancia_total = df['distancia'].sum()
    distancia_media = df['distancia'].mean()
    tiempo_total = df['tiempo_horas'].sum()

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
    # aseguramos el formato de fecha que queremos
    df['fecha'] = pd.to_datetime(df['fecha'], dayfirst=True)

    # ordenamos por fecha
    df = df.sort_values('fecha')

    # lo dividimos en inicio vs actual
    primeras = df.head(5)
    ultimas = df.tail(5)

    # calculamos las medias
    velocidad_inicio = primeras['velocidad'].mean()
    velocidad_fin = ultimas['velocidad'].mean()

    distancia_inicio = primeras['distancia'].mean()
    distancia_fin = ultimas['distancia'].mean()

    desnivel_inicio = primeras['desnivel'].mean()
    desnivel_fin = ultimas['desnivel'].mean()

    #evitar divisiones por 0
    mejora_velocidad = 0 if velocidad_inicio == 0 else ((velocidad_fin - velocidad_inicio) /velocidad_inicio) * 100
    mejora_distancia = 0 if distancia_inicio == 0 else ((distancia_fin - distancia_inicio) /distancia_inicio) * 100
    mejora_desnivel = 0 if desnivel_inicio == 0 else ((desnivel_fin - desnivel_inicio) / desnivel_inicio) * 100

    #indice global
    indice = (mejora_velocidad * 0.5) + (mejora_distancia * 0.3) + (mejora_desnivel * 0.2)

    return {
        "mejora_velocidad_%": round(mejora_velocidad, 2),
        "mejora_distancia_%": round(mejora_distancia, 2),
        "mejora_desnivel_%": round(mejora_desnivel, 2),
        "indice_progreso": round(indice, 2)
    }



