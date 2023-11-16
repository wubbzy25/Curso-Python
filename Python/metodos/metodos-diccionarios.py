diccionario = {
    'nombre': 'Carlos',
    'Vacante': 'Backend Developer',
    'Salario': '4M',
    'Estado': 'Contratado'
}

#Nos devuelve los keys
key = diccionario.keys()

#Sirve para Obtener el value pasandole como parametro una key

get = diccionario.get('Salario') #Si no lo encuentra devuelve none
print(diccionario)

#Eliminar todo del diccionario
clear = diccionario.clear()

#Eliminar un elemento del diccionario
pop = diccionario.pop('Salario') 

#Obtener un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario)