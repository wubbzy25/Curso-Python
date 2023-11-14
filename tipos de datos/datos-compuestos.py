#Lista(Se pueden modificar los datos dentro de la lista)
lista = ["Carlos","Wuubzi",False,1.85]
print(lista)

#tupla(No se pueden modificar los datos dentro de la lista)
tupla = ('Carlos', 'Wuubzi', False, 1.85)
print(tupla)

#Conjunto set(no tienen un orden fijo elemento desordenados y se puede modificar el conjuntos pero no los datos dentro de la lista, no almacena duplicados )

conjuntos = {'Carlos', 'Wuubzi', True, 1.85}



#No se pueden acceder a los elementos de forma especifica
#print(conjuntos[1])

#Se accede de forma general a la lista
print(conjuntos)



#Diccionario (dict)
#equivalente a json en javascript

diccionario = {
   'nombre': 'Carlos',
   'Pseudonimo': 'Wuubzi',
   'Le gusta programar?': False,
   'Cuanto Mide': 1.85   
}

print(diccionario['nombre'])
