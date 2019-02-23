miCadena = "Hola Mundo"

#Palabra clave de Python : nos muestra los atributos y metodos que podemos usar para un String
#print (dir(miCadena))

print(miCadena.upper())
print(miCadena)
print(miCadena.lower())
print (miCadena.swapcase())
print (miCadena.capitalize())
print (miCadena.replace('Hola','Adios'))
print (miCadena.replace('Hola','Adios').upper()) #Metodos 
print (miCadena.count('o'))
print (miCadena.count(' '))
print (miCadena.startswith('hola')) #Pregunta si la cadena empieza con la cadena 'hola'
print (miCadena.startswith('Hola'))
print (miCadena.startswith('H'))
print (miCadena.endswith('H'))
print (miCadena.endswith('o'))


#Separar cadenas
print (miCadena.split()) #Separa el texto basado en un espacio

otraCadena = "Bienvenidos, al curso de Python"
print (otraCadena.split(',')) #La salida crea una lista de string

print (otraCadena.split('o'))

#Buscar caracteres

print (miCadena.find('o')) # Regresa la posicion del indice del caracter indicado

print (len(miCadena))
print (miCadena.index('l'))


print (miCadena.isnumeric())
print (miCadena.isalpha())
print (miCadena[5])
print (miCadena[6])
print (miCadena[-1]) #Orden inverso
print (miCadena[-2]) #Orden inverso


miNombre = "Alex"
print ("Mi nombre es :"+miNombre)
print ("Mi nombre es : "+miNombre) #con espacio despues de :

#print (f'Mi nombre es {miNombre}') solo para python >3.6
print ("Mi nombre es {0}".format(miNombre))