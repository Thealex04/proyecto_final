
def victorias_por_pais(df):
    return df["pais"].value_counts()

def victorias_por_equipo(df):
    return df["equipo"].value_counts()

def victorias_por_corredor(df):
    return df["ganador"].value_counts()

def victorias_por_competicion(df):
    return df["carrera"].value_counts()

def filtrar_por_año(df, año):
    return df[df["año"] == año]

def ciclistas_con_mas_victorias(df):
    return df["ganador"].value_counts().idxmax()

def top_ciclistas(df, n=5):
    return df["ganador"].value_counts().head(n)