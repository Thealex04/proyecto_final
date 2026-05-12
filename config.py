import os

# Este archivo guardara la configuración principal
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Secret Key protege las sesiones y los formularios
    SECRET_KEY = "mi_clave_secreta"
    # Ruta al archivo de la base de datos
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "database", "ciclismo.db")
    # Desactivamos para evitar avisos innecesarios
    SQLALCHEMY_TRACK_MODIFICATIONS = False

