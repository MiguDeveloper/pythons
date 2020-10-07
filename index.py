# Para comentar lineas usaremos el simbolo de comentario
if 5>3: # esto es otro comentario: condicion
    print('5 es mayor a 3')
if 5<3:
    print('esto no se imprime ya que no cumple condicion')

# Uso de variables
sumando1 = 5
sumando2 = 7
suma = sumando1+sumando2
print ('La suma de x,y es: ' + str(suma));

# multiple declaracion de variables
a,b,c = 'Miguel','Jolu','Mateo'
print(a,b,c)

# multiple variables con un mismo valor
usuario1 = usuario2= usuario3 = 'role_user'
print(usuario1, usuario2, usuario3)

# concatenacion de palabras
saludo = 'hola'
print(saludo + ' ' + usuario1);
