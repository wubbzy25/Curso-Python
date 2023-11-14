#si el modulo estuviera dentro de una carpeta en la misma ruta 
#import funciones_buenas.saludar as m_saludar

import sys
print(sys.path)

sys.path.append("C:\\Users\\wuubzi\\Desktop\\python\\modulos\\paquete")

import saludar as modulo_saludo

print(modulo_saludo.saludar("Dalto"))