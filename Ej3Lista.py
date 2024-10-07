##Imagina un sistema de nombres donde queremos identificar el nombre más común. Para ello
##primero pide al usuario que inserte nombres. Utiliza la estructura do-while
##Introduce los nombres... (-1 para terminar)
##carmen,julia,juan,carmen,carmen,julia carmen: 3,julia: 2,juan: 1
nombres = []

while True:
    canNom = str(input("Inserte su nombre o escriba -1 para frenar:"))
    if canNom != "-1":
        nombres.append(canNom)
    else:
        break
    
print= str(nombres)
