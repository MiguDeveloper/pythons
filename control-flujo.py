# control de flujo
# operadores validos ==, <=, <, >, >=, !=
if 2>5:
    print('2 es mayor')
elif 2<5:
    print('2 es menor que 5')
else:
    print('bloque esle')

if 'miguel'=='miguel':
    print('iguales')
else:
    print('distintos')

# if de una sola linea
if 2<5: print('un if de una linea')

# operador ternario
print('condicion evaluo true') if 2<5 else print('condicion evaluo false')

# operador and
if 2<5 and 3>2:
    print('cumplio condicion AND')

# operador or
if 2>5 or 2>1:
    print('cumplio condicion del OR')
