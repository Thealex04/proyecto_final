from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from config import Config
from src.logica import cargar_datos, limpiar_datos, calcular_velocidad, estadisticas, calcular_progreso
from src.recomendaciones import informe_completo
from src.models_db import db, Usuario, RutaDB

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
def registro():
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
    if request.method == "POST":
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
    rutas_usuario = RutaDB.query.filter_by(usuario_id=current_user.id).all()

    # Si no tiene rutas todavía
    if not rutas_usuario:
        return render_template(
            "dashboard.html",
            estadisticas_rutas = None,
            progreso = None,
            recomendaciones = [],
            rutas = []
        )
    
    # Convertimos a DataFrame
    import pandas as pd

    datos = []
    for ruta in rutas_usuario:
        horas, minutos = map(int, ruta.tiempo.split(":"))
        tiempo_horas = horas + minutos / 60

        datos.append({
            "fecha": ruta.fecha,
            "distancia": ruta.distancia,
            "tiempo": ruta.tiempo,
            "tiempo_horas": tiempo_horas,
            "desnivel": ruta.desnivel,
            "velocidad": ruta.velocidad,
            "tipo": ruta.tipo
        })

    df = pd.DataFrame(datos)

    estadisticas_rutas = estadisticas(df)
    progreso = calcular_progreso(df)
    recomendaciones = informe_completo(df, progreso)

    return render_template(
        "dashboard.html",
        estadisticas_rutas = estadisticas_rutas,
        progreso = progreso,
        recomendaciones = recomendaciones,
        rutas = rutas_usuario
        )

@app.route("/")
def inicio(): 
    return render_template("index.html")

@app.route("/nueva_ruta", methods=["GET","POST"])
@login_required
def nueva_ruta():
    if request.method == "POST":
        fecha = request.form["fecha"]
        distancia = float(request.form["distancia"])
        tiempo = request.form["tiempo"]
        desnivel = int(request.form["desnivel"])
        tipo = request.form["tipo"]

        horas, minutos = map(int, tiempo.split(":"))
        tiempo_horas = horas + minutos / 60

        velocidad = distancia / tiempo_horas if tiempo_horas > 0 else 0

        ruta = RutaDB(
            fecha = fecha,
            distancia = distancia,
            tiempo = tiempo,
            desnivel = desnivel, 
            tipo = tipo,
            velocidad = velocidad,
            usuario_id = current_user.id
        )

        db.session.add(ruta)
        db.session.commit()

        flash("Ruta añadidad correctamente")
        return redirect(url_for("dashboard"))
    
    return render_template("nueva_ruta.html")


@app.route("/competiciones")
def competiciones():
    return render_template("competiciones.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)