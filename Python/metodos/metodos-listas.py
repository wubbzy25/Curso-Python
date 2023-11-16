
#creando una lista con list
lista = list([31,32,43])

#Cantidad de elementos de la lista
elementos = len(lista)

#Agregar elementos a la lista
lista.append(12)


#Agregar elementos a la lista a una posicion especifica
lista.insert(1, 23)

#Agregar varios elementos a la lista
lista.extend([False,20])

#Eliminar un elemento de la lista por su posicion
lista.pop(5) #-1 para eliminar el ultimo -2 para elimianr el antepenultimo y asi sucesivamente

#Eliminar un elemento de la lista por su valor
lista.remove(31)

#Eliminar todo los elemento de la lista
#lista.clear()

#Ordenar los elementos de menor a mayor, no funciona si tiene cadena de textos si usamos el parametro reverse=True 
# lo ordena en reversa de mayor a menor
lista.sort(reverse=True)

#Invierte los elementos de una lista
lista.reverse()
print(lista)
