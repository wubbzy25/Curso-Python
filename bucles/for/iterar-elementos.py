animales = ['Loro', 'Perro', 'Cocodrilo', 'Elefante', 'Jirafa']
numeros = [10,12,32,43,12,43]
#Recorriendo la lista animales
for animal in animales:
    print(animal)   
    
#Recorriendo la lista de numero
for numero in numeros:
    resultado = numero * 2
    print(resultado)
    
#Recorrer dos o mas lista a la vez (solo funciona si las listas tienen el mismo numero de elementos)
for animal,numero in zip(animales,numeros):
    print(f'Lista 1: {animal}')
    print(f'Lista 2: {numero}')


#Forma no optima de recorrer una lista con su indice (no funciona con los conjuntos)
for num in range(len(numeros)):
    print(numeros[num])

#Forma optima de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es {indice}, y el valor es {valor}')
    
#Usando el else

for numero in numeros:
    print('a')
else:
    print('bucle termino')


#Todo lo anterior funciona igual con las tuplas y conjuntos