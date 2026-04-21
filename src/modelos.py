class Ruta:
    def __init__(self, fecha, distancia, tiempo, desnivel):
        self.fecha = fecha
        self.distancia = distancia
        self.tiempo = tiempo 
        self.desnivel = desnivel

    def velocidad_media(self):
        return self.distancia / (self.tiempo /60)

class Ruta_MTB(Ruta):
    def __init__(self, fecha, distancia, tiempo, desnivel):
        super().__init__(fecha, distancia, tiempo, desnivel)

class Ruta_carretera(Ruta):
    def __init__(self, fecha, distancia, tiempo, desnivel):
        super().__init__(fecha, distancia, tiempo, desnivel)

class Ruta_gravel(Ruta):
    def __init__(self, fecha, distancia, tiempo, desnivel):
        super().__init__(fecha, distancia, tiempo, desnivel)


class Ciclista:
    def __init__(self, nombre, edad, peso, altura):
        self.nombre = nombre
        self.edad = edad 
        self.peso = peso
        self.altura = altura
        self.rutas =  []

    def agregar_ruta(self, ruta):
        self.rutas.append(ruta)

    
