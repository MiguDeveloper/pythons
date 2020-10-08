# Funciones: se usan para eliminar codigo repetitivo
# funcion simple sin argumentos
def nombreDeLaFuncion():
    print('ejecución mi primera funcion');

# llamar a una funcion
nombreDeLaFuncion();

# funcion con argumento
def imprimirDato(dato1, dato2):
    print('dato1: ' + dato1 + ' dato2: ' + dato2)

imprimirDato('python','basic')

# argumentos variables: el argumento sera recibido como una tupla por lo tanto no
# podra ser modificado
def funcConArgumentosVariables(*args):
    print(args)
    print('primer elemento: ' + args[0])

funcConArgumentosVariables('miguel','mario','mateo','feliz')

# argumentos inicializados
def funcArgsInicializada(arg='miguel'):
    print(arg)

funcArgsInicializada()
funcArgsInicializada('Mateo')

def funcArgsLista(lista):
    for item in lista:
        print(item)

funcArgsLista(['miguel', 'mateo'])

# Recursividad
def recursion(numero):
    if numero<0:
        return
    print (numero)
    numero -= 1
    recursion(numero)

recursion(5)

# fibonacci
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
print ('fibonacci de orden 4')
print(fib(5))