class Usuario:
    nombre = 'Miguel'
    apePat = ''
    apeMat = ''

usuario =  Usuario();

usuario2 = Usuario();
usuario2.nombre = 'Mario'
print(usuario.nombre, usuario2.nombre)

class User:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName
        self.adicional = ''
    
    def saludo(self):
        print('Hola mi nombre es: ' + self.name + ' ' + self.lastName)

user = User('Clorinda', 'Turner')
print(user.name)
user.saludo()

# eliminar propiedades de un objeto
del user.adicional
# eliminar un objeto completo
# del user

# Herencia
class Administrador(User):
    def superSaludo(self):
        print ('Hola me llamo ' + self.name + ' y soy el administrador')

userAdmin = Administrador('Cesar', 'Vallejo')
userAdmin.saludo()
userAdmin.superSaludo()

# Ejemplos
class Mascota:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola soy el ' + self.tipo + ' ' + self.nombre + ' y mi sonido es: ' + self.onomatopeya)

# dos formas de extender el metodo __init__ de la clase padre con NombreClase y con Super     
class Gato(Mascota):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya):
        Mascota.__init__(self, nombre, onomatopeya)
        print('Gato extendido')

class Perro(Mascota):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('instanciando a un perro extendido')

perro = Perro('Coda','Ladrido')
perro.saludo()

michigan = Gato('Michi', 'Maullido')
michigan.saludo()