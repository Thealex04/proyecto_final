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


