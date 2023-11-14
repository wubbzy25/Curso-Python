cadena1 = "Hola soy carlos"
cadena2 = "Hola crack"

# Mostrar todo los metodos que tienen los string ocualquier tipo de dato
dir = dir(cadena1)

#Convertir todo a mayuscula
upper = cadena1.upper()

#Convertir todo a minusucla
lower = cadena1.lower()

#Convertir Primera letra en mayuscula
capitalize = cadena1.capitalize()

#Buscamos una cadena en otra cadena y nos devuelve la posicion en la que se encuentra, si no hay coincidencia devuelve -1
find = cadena1.find("a")

#Buscamos una cadena en otr cadena y si no hay coincidencia da un error
index = cadena1.index("H")

#Si es numerico devuelve true, si no devuelve false(aunque este dentro de un string si hay solo numero devolvera true)

es_numerico = cadena1.isnumeric()

#Si es alfanumerico devuelve true, si no devuelve false

es_alfanumerico = cadena1.isalpha()

#contamos las coincidencia de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("a")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#Verificamos si una cadena empienza con una letra o oracion si es asi devuelve true
empieza_con = cadena1.startswith('H')

#Verificamos si una cadena finalize con una letra o oracion si es asi devuelve true
terminar_con = cadena1.endswith('s')

#Reemplaza un valor de una cadena replace(parametro que quiere reemplazarte, parametro por el que se quiere reemplazar)
cadena_nueva = cadena1.replace('la', 'lu')

#separar cadena con la cadena que le pasemos
cadena_separada = cadena1.split(',')

print(cadena_separada)