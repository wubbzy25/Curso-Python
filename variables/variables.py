#tipado dinamico(No es necesario declarar el tipo de variable)
#Definiendo Variables

nombre = 'Carlos'

entero = 10

float = 10.3

booleano = True

#Definiendo Variables con snake_case
nombre_completo = "Carlos Andres Salas Correa"


#Concatenar
nombre = 'Carlos'
bievenida = 'Hola ' + nombre + ' Como estas?' # Hola Carlos Como estas?

#fstring (Otra manera de concatenar)
nombre = 'Juan'
bienvenida = f'Hola {nombre} Como estas?'
print(bievenida) # Hola Juan Como estas?

#Eliminar variables el la memoria(palabra clave del)
del nombre

#Operadores de pertenencia (palabras claves in y not in)

print("Juan" in bienvenida) #true
print("Juan" not in bienvenida) #false
