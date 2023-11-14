frutas = ['banana', 'pera','uva','manzana']
juan = "Es gay"
numeros = [1,2,3,5,8]
#Evitando un elemento con la sentencia continue
for fruta in frutas:
    if fruta == 'banana':
        continue
    print(fruta)

#Evitando que el bucle siga ejecutandose con la sentencia break(el else tampoco se ejecuta)
for fruta in frutas:
    if fruta == 'uva':
        break
    print(fruta)
else:
    print('bucle terminado')

#Recorrer cadenas de texto

for letra in juan:
    print(letra)
    
#for en una sola linea
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)