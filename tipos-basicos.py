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

# acceder a elementos de una lista
print(listaCopia[0])

# eliminar elementos de una lista
# el ultimo elemento
listaCopia.pop()
print(listaCopia)

# un elemento especifico: le indicamos el valor del elemento y no el indice
listaCopia.remove(1)
print(listaCopia)

# voltear los elementos de una lista
listaCopia.reverse()
print(listaCopia)

# ordenar: para ordenar una lista los elementos tienen que ser del mismo tipo de dato
listaCopia.sort()
print(listaCopia)

# TUPLAS a diferencia de las listas:
# no se pueden modificar, si queremos modificar tenemos que pasarla a lista
# tiene muchos menos metodos
tupla = ('hola', 'miguel', 'developer', 'somos', 'tupla')
print(tupla)

print(tupla.count('miguel'))

# obtener el indice de un elemento
print(tupla.index('developer'))

# acceder a elementos de una tupla por ejemplo a 'somos'
print(tupla[tupla.index('somos')])

# proceso de modificacion de una tupla
listaDeTupla = list(tupla)
listaDeTupla.append('item agregado')
print(listaDeTupla)

# RANGOS
# solo admite como parémetros números enteros
# el tipo range es una lista inmutable(no se puede modificar) de números enteros en sucesión aritmética
# entiendase como sucesión a la diferencia entre dos elementos consecutivos siempre sera la misma
# el tipo range con un unico elemento 'range(n)' crea una lista inmutable de n números enteros consecutivos
# que comienza en 0 y termina en n-1, si 'n' fuera negativo se crea un range vacio
print(range(10))
# para ver los elementos del range es necesario convertirlo en una lista
lst = list(range(10))
print(lst)

# el tipo range con dos argumentos se escribe range(m,n) y genera elementos con números enteros
# consecutivos e inmutables desde m hasta n-1, si n es menor igual a m se crea un rango vacio
lst2 = list(range(5,15))
print(lst2)

# el range con tres parámetros se escribe range(m,n,p) crea una lista inmutable de numeros enteros
# consecutivos desde m hasta antes de superar o igualar a 'n' de 'p' en 'p' si 'p' fuese 
# negativo los valores van disminuyendo de '-p' en '-p'
lst3 = list(range(2,20,2))
print(lst3)

lst4 = list(range(25,0,-3))
print(lst4)

# DICCIONARIOS
# son similares a las listas pero usaremos como indices las claves basadas en strings

diccionario = {
    'nombre': 'miguel',
    'edad': 36,
    'cursos': ['java +8', 'amgular +2', 'node', 'javascript']
}
print(diccionario)

# para acceder a sus elemento debemos de usar los [clave] o tambien por el metodo get()
print(diccionario['edad'])
print(diccionario.get('nombre'))

# para modificar si tendremos que usar los corchetes
diccionario['nombre'] = 'Miguel Chinchay'
print(diccionario)

# tamaño del diccionario
print(len(diccionario))

# agregar elementos al diccionario
diccionario['nivel'] = 'avanzado'
print(diccionario)

# para eliminar una propiedad o elemento del diccionario
# o podemos usar el 'del' por ejemplo
# del diccionario['nivel']
diccionario.pop('nivel')
print(diccionario)

# si queremos eliminar el ultimo elemento agregado al diccionario usamos popitem
diccionario.popitem()
print(diccionario)

# generar copias del diccionario podemos usar 'copy' o 'dict'
# por ejemplo copiaDiccionario = dict(diccionario)
copiaDiccionario = diccionario.copy()
print(copiaDiccionario)

dicDeDic = {
    'miguel': {
        'nombre': 'Miguel',
        'profesion': 'Ingeniero',
        'edad': 36    
    },
    'mario': {
        'nombre': 'Mario',
        'profesion': 'Escritor',
        'edad': 36
    }
}

print(dicDeDic)

# Boolean
verdadero = True
falso =  False
print(verdadero, falso)