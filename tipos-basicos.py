# tipos de datos string con comillas simples o dobles
frase = 'hola miguel'
frase2 = "hola migu"

# tipo de dato numerico : entero, decimal(float) y complejos
entero = 20
decimalFloat = 20.55
complejo = 1j

print (frase, entero, decimalFloat, complejo)

# listas
lista = [1,2,3]
lista2 = [1,2,3]

# metodos de listas:
# append(agregar un unico elemento)
lista.append(4);

# clear(limpiamos la lista)
lista2.clear()

# copy(generar una copia de una lista) no es por referencia ojo
listaCopia = lista.copy()

# extend: lst.extend([2,3..])
# se queremos agregar otra coleccion de elementos
# para extender la lista por múltiples valores de cualquier tipo de iterable, 
# ya sea otra lista o cualquier otra cosa que proporcione una secuencia de valores.
listaCopia.extend([5,4,6, 'miguel']);

print (lista)
print (lista2)
print (listaCopia)

# count: contar elementos repetidos lst.count()
print ('El numero 4 se repite: ' + str(listaCopia.count(4)))

# len: obtener el numero de elementos de una lista len(lst)
print('tamaño de la listaCopia es: ' + str(len(listaCopia)))
