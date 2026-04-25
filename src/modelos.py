
#Clase Ruta
class Ruta:
    def __init__(self, fecha, distancia, tiempo, desnivel, tipo):
        self.fecha = fecha
        self.distancia = distancia
        self.tiempo = tiempo 
        self.desnivel = desnivel
        self.tipo = tipo

    def velocidad_media(self):
        if self.tiempo > 0:
            return self.distancia / (self.tiempo /60)
        else:
            return 0

#Subclases de la clase Ruta (RutaMTB, RutaCarretera y RutaCiclocross)
class RutaMTB(Ruta):
    def terreno(self):
        return "Terreno de montaña"

    def dificultad(self):
        if self.desnivel > 500:
            return "Ruta dura"
        else:
            return "Ruta moderada"

    def acelerar(self):
        return "Aumenta la velocidad pedaleando más..."

    def frenar(self):
        return "Disminuye la velocidad dandole al freno..."

class RutaCarretera(Ruta):
    def terreno(self):
        return "Asfalto"

    def ajustar_desarrollo(self):
        return "Cambia de marcha para mantener cadencia"

class RutaCiclocross(Ruta):
    def terreno(self):
        return "Terreno mixto (barro, tierra, hierba...)"
    
    def porteo(self):
        return "Carga la bici al pasar por tramos de mucho barro..."
    

#Clase Ciclista
class Ciclista:
    def __init__(self, nombre, edad, peso, altura):
        self.nombre = nombre
        self.edad = edad 
        self.peso = peso
        self.altura = altura
        self.rutas =  []

    def agregar_ruta(self, ruta):
        self.rutas.append(ruta)

    def distancia_total(self):
       return sum(ruta.distancia for ruta in self.rutas)
    
    def velocidad_media_total(self):
        if len(self.rutas) == 0:
            return 0
        
        distancia_total = sum(ruta.distancia for ruta in self.rutas)
        tiempo_total = sum(ruta.tiempo for ruta in self.rutas)

        if tiempo_total == 0:
            return 0

        return distancia_total / (tiempo_total / 60)

    def resumen(self):
        return (
            f"Ciclista: {self.nombre}\n"
            f"Rutas realizadas: {len(self.rutas)}\n"
            f"Distancia total: {self.distancia_total()} km\n"
            f"Velocidad media: {round(self.velocidad_media_total(), 2)} km/h"
        )

    
