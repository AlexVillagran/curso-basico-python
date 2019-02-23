# String cadenas de caractes
#  2 String distintos
print ("Hola mundo")
print ("Hola Mundo")
print ('''Hola Mundo''')
print ("""Hola Mundo""")


#Mostrar el tipo de dato
print (type("Hola mundo"))

#Unir strings (esta operacion la llamamos concatenacion de string)
print ("Hola, Alex" + " Bienvenido")

#Dato tipo entero (int)
print (type(30))
print(30)

#Datos tipos decimal(float)
print (type(30.2))
print(30.2)

#Tipos de dato estado: activado-desactivado (Tipo de dato logico: Cierto, Falso - True,False)
print (type(True))
print (type(False))

#Lista de datos (Lista de enteros)
[10, 20, 30, 40, 55]
['Hola','Adios','Hasta pronto']
[10,'Hola', True, 10.1]
#Lista Vacia
[]

print (type([34, 'Hola']))

#Tuplas (se utiliza en datos que no cambian)
(10, 20, 30, 55)
print(type((23, 'Hola')))
#Tupla vacia
()
print(type(()))


#Dicccionarios
{
    "nombre":"Juan",
    "apellido":"Perez",
    "apodo":"torz"
}

print(type({
    "temperatura": 23,
    "altura": 1.45
}))

#Tipo de dato que no esta definido
print(type(None))