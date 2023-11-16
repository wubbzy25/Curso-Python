#Con clases se usa pascalcase(todas las primeras letras van en mayuscula)

#Clase con atributos estaticos
class Celular():
    marca = 'Samsung'
    modelo = 'S23'
    camara = '48MP'
    
#creamos un objeto con la clase Celular instaciar
celular1 = Celular()
#Podemos modificar los valores estaticos 
celular1.camara = "500MP"

print(celular1.camara)
    
#Clase con atributos dinamicos
class Carro:
    def __init__(self, marca, modelo, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = kilometraje

#Creamos el objeto con sus atributos
carro1 = Carro('Porsche', 'GT4', '20.000KM')
#Creamos otros objetos con otros atributos
carro2 = Carro('Mazda', 'Mazda 3', '50.000KM')

print(carro2.marca)
