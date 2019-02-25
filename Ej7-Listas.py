demo_lista = [1, 'Hola', 1.34, True , [1, 2, 3]]
colores = ['red', 'green', 'blue']
numbers_list = list((1, 2, 3, 4)) # Pasamos como argumento una tubla al metodo list
print (numbers_list)
print (type(numbers_list))


r = list(range(1,11)) #Formas de crear listas numericas
print(r)

print(type(colores))
#print(dir(colores)) #Muestra que metodos podemos ejecutar
print(len(colores))
print(len(demo_lista)) #La sublista cuenta como solo un elemento de la lista demo
print(colores[1])
print(colores[-1])
print('green' in colores)
print('yellow' in colores)

#Alterando los datos de una lista
print (colores)
colores[1]="yelow"
print (colores)

#Agragando valores
colores.append('violet')
print (colores)

#Pasar varios elemento

#colores.append(('blank','black'))
#print (colores)

colores.extend(['blank','black'])
print (colores)

colores.insert(1,'pink')
print(colores)

colores.insert(len(colores),'gray')
print(colores)

colores.pop() #quita el ultimo elemento
print(colores)
colores.pop() #quita el ultimo elemento
print(colores)

colores.remove('pink')
print(colores)

colores.pop(1)
print(colores)

##colores.clear()
##print(colores)

colores.sort()
print(colores)
colores.sort(reverse=True)
print(colores)


print(colores.index('red'))

colores2 = ['red', 'green', 'blue','red']
print(colores2.count('red'))#Cuenta el numero de veces que esta red