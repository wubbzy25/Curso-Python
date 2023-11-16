#Creando un conjunto con set

conjunto = set(['dato1', 'dato2'])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(['dato1', 'dato2'])
conjunto2 = {conjunto1, 'dato1'}

#Teoria de conjuntos

conjunto1 = {'1', '2', '3', '5'}
conjunto2 = {'1', '2'}

#Verificamos si es un subconjunto
resultado = conjunto1.issubset(conjunto2)

#Verificamos si es un superconjunto
resultado = conjunto1.issuperset(conjunto2)

#verificar si hay algun numero en comun
resultado = conjunto1.isdisjoint
print(resultado)