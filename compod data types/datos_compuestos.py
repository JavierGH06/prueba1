#lista normal
lista = [1,2,3,4,5]
print(lista[0])


#las listas [] si se pueden modificar los datos
lista2 = ["javier", "gonzalez",True,23]
print(lista2[1])

#esto es valido
lista2[0] = "antoni"
print(lista2[0])


#las tuplas () no se pueden modificar los datos
tupla = ("javier", "gonzalez",True,23)
print(tupla[2])

#esto no se puede
#tupla[0] = "antoni"
#print(tupla[0])

#creando un conjunto (set)

conjunto = {"nombre","curso","edad",15,24}

print(conjunto)