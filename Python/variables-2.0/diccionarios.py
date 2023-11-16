#creando diccionario con dict
diccionario = dict(nombre='carlos', apellido='salas')

#las tuplas si pueden ser claves,Las listas no pueden ser claves y usamos frozenset para meter conjuntos
#Tupla como clave
diccionario = {('hola'): 'como estas'}

#creando diccionarios con fromkeys() con valor None
diccionario = dict.fromkeys(['nombre', 'apellido'])

#Conjunto como clave
diccionario = {frozenset(['hola']): 'hi'}