
def generar_recomendacion(progreso):
    '''
    Genera una recomendación basada en el progreso
    que está teniendo el ciclista
    '''
    indice = progreso.get("indice_progreso",0)

    if indice >= 15:
        return (
            "Excelente rendimiento."
            "Tu progreso es muy bueno y estás mejorando constantemente"
        )
    
    elif indice >=5:
        return (
            "Buen trabajo."
            "Tienes una mejora progresiva en tus entrenamientos"
        )
    
    elif indice >= 0:
        return (
            "Tu progreso es estable"
            "Intenta aumentar ligeramente la intensidad o frecuencia"
        )
    
    else:
        return (
            "Has tenido una bajada en tu rendimiento"
            "Necesitas revisar tu descanso y planificación."
        )
    

def recomendacion_velocidad(df):
    '''
    Analiza la velocidad media del ciclista
    '''
    velocidad_media = df["velocidad"].mean()

    if velocidad_media >= 30:
        return "Tu velocidad media es excelente."
    
    elif velocidad_media >= 24:
        return "Tu velocidad media es buena."
    
    else:
        return (
            "Tu velocidad media puede mejorar."
            "Prueba entrenamientos de resistencia."
        )
    

def recomendiacion_desnivel(df):
    '''
    Analiza la capacidad en rutas con desnivel
    '''

    desnivel_medio = df["desnivel"].mean()

    if desnivel_medio >= 800:
        return "Tienes muy buen rendimiento en montaña. Eres todo un escalador."
    
    elif desnivel_medio >= 400:
        return "Tienes buen rendimiento en rutas con desnivel"
    
    else:
        return(
            "Podrías mejorar tu rendimiento en subida"
            "Haz rutas más exigentes"
        )
    

def recomendacion_frecuencia(df):
    '''
    Analiza la frecuenci de entrenamientos
    '''

    total_rutas = len(df)

    if total_rutas >= 20:
        return "Tu frecuencia de entrenamiento es excelente."
    
    elif total_rutas >= 10:
        return "Mantienes una buena regularidad"
    
    else:
        return  "Intenta entrenar con mayor frecuencia"
        

def informe_completo(df, progreso):
    '''
    Genera un informe completo con todas las
    recomendaciones
    '''

    recomendaciones = [
        generar_recomendacion(progreso),
        recomendacion_velocidad(df),
        recomendiacion_desnivel(df),
        recomendacion_frecuencia(df)
    ]

    return recomendaciones



