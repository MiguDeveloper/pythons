# Loops
# while, 
# brear: si queremos cortar la ejecucion
# continue: se salta la ejecucion de una porcion de codigo

print('Break: ')
i=0
while i < 5:
    i += 1
    if i == 3:
        break
    print (i)

print('Continue: ')

i=0
while i < 5:
    i += 1
    if i == 3:
        continue
    print (i)

# Forloop los usaremos para recorrer un arreglo o diccionarios, tambien podemos
# iterar dobre strings
usuarios = ['miguel', 'mario', 'jose', 'mateo']
for usuario in usuarios:
    print(usuario)

nombre = 'mi'
for letra in nombre:
    print (letra)

for x in range(6,18,2):
    print(x)