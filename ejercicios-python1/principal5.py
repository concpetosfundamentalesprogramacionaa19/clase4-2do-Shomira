"""
    @reroes
    Manejo de estructuras
"""

diccionario = {"nombre": "René", "apellidos": "Elizalde"}

diccionario2 = {"nombre": "Luis", "apellidos": "Alvares"}
#Asignacion de los dos diccionarios en una lista
lista = [diccionario , diccionario2]

print("Imprimir diccionario")
for l in  lista:
	midiccionario = l 
	print("Mi nombre es: %s y mi apellido es: %s " % \
		(midiccionario["nombre"],midiccionario["apellidos"]))


