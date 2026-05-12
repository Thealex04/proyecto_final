from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

# La tabla Usuario representa a cada ciclista que se registra
class Usuario(UserMixin, db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    rutas = db.relationship("RutaDB", backref="usuario", lazy=True)

    def __repr__(self):
        return f"<Usuario {self.nombre}>"
    
# La tabla Ruta representa cada ruta que hace el ciclista y la sube
class RutaDB(db.Model):
    __tablename__ = "rutas"

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(20), nullable=False)
    distancia = db.Column(db.Float, nullable=False)
    tiempo = db.Column(db.String(10), nullable=False)
    desnivel = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id"),
        nullable = False
    )

    def __repr__(self):
        return f"<Ruta {self.fecha} - {self.distancia} km"