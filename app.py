from flask import Flask, render_template
from src.logica import cargar_datos, limpiar_datos, calcular_velocidad, estadisticas, calcular_progreso

app = Flask(__name__)

@app.route("/")
def inicio(): 
    return render_template("index.html")

@app.route("/rutas")
def rutas():
    return render_template("rutas.html")

@app.route("/competiciones")
def competiciones():
    return render_template("competiciones.html")

if __name__ == "__main__":
    app.run(debug=True)