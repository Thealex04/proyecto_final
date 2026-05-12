from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from config import Config
from src.logica import cargar_datos, limpiar_datos, calcular_velocidad, estadisticas, calcular_progreso
from src.models_db import db, Usuario

app = Flask(__name__)
app.config.from_object(Config)

# Inicializamos la base de datos
db.init_app(app)

# Configuramos el login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route("/registro", methods=["GET","POST"])
def register():
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        password = request.form["password"]

        #Verificamos si el email ya existe
        usuario_existente = Usuario.query.filter_by(email=email).first()

        if usuario_existente:
            return "Ya existe un usuario con ese email."
        
        # Sino creamos un nuevo usuario
        nuevo_usuario = Usuario(
            nombre = nombre, 
            email = email, 
            password_hash = generate_password_hash(password)
        )

        db.session.add(nuevo_usuario)
        db.session.commit()

        return redirect(url_for("inicio"))
    
    return render_template("registro.html")


@app.route("/login", methods=["GET","POST"])
def login():
    if request.methods == "POST":
        email = request.form["email"]
        password = request.form["password"]

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and check_password_hash(usuario.password_hash, password):
            login_user(usuario)
            return redirect(url_for("dashboard"))
        else:
            flash("Email o contraseña incorrectos")

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("inicio"))

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/")
def inicio(): 
    return render_template("index.html")

@app.route("/rutas")
def rutas():
    rutas_df = cargar_datos("data/rutas.csv")

    if rutas_df is not None:
        rutas_df = limpiar_datos(rutas_df)
        rutas_df = calcular_velocidad(rutas_df)

        stats = estadisticas(rutas_df)

        return render_template("rutas.html", estadisticas=stats)
    
    return render_template("rutas.html", estadisticas=None)

@app.route("/competiciones")
def competiciones():
    return render_template("competiciones.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)