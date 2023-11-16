diccionario = {
    'nombre': 'Carlos',
    'Vacante': 'Backend Developer',
    'Salario': '4M',
    'Estado': 'Contratado'
}

#Recorriendo un diccionario (Solo me devuelve la clave)
for key in diccionario:
    print(key)

#Recorriendo un diccionario con el meto items() para obtener la key y el valor
for datos in diccionario.items():
    key = datos[0]
    valor = datos[1]
    print(f'La clave es {key}, y el valor es {valor}')
