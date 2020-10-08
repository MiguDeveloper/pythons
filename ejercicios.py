dato = input('Ingrese el dato: ')
lista = ['hola', 'miguel', 'chanchito', 'feliz', 'dragones', 'chanchito']

if lista.count(dato) == 1:
    print('Correcto coincide con un termino')
elif lista.count(dato)>1:
    print('mas de una coincidencia!')
else:
    print('no se encontro coincidencia')

# calculadora con las cuatro operaciones
operaciones = ['suma','resta','multiplicacion', 'division']

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multipliacion(a,b):
    return a*b

def division(a,b):
    if b==0:
        print ('division entre cero indefinida')
        return 0
    else:
        return a/b

def calcular (operacion, a,b):
    calculadora = {
        'suma': suma(a,b),
        'resta': resta(a,b),
        'multiplicacion': multipliacion(a,b),
        'division': division(a,b)
    }
    return calculadora[operacion]

operador = input('ingrese la operacion: suma, resta, division, multiplicacion: ')
if operaciones.count(operador) == 1:
    try:
        item1 =  float(input('ingrese el primer elemento: '))
        item2 =  float(input('ingrese el segundo elemento: '))
        print('resultado: ' + str(calcular(operador,item1, item2)))
    except:
        print('debe ingresar numeros')
else:
    print('el tipo de operación no esta soportada')

