import mensajes
lista=[]
indice=0
palabra=" "
while len(lista) < 5:
    datos=input("Ingresa un dato: ")
    lista.append(datos)
for texto in range(0,len(lista)):
    if lista[texto] =="disco":
        palabra=lista[texto]
        indice=texto
if indice==0 and palabra=="":
    print(mensajes.error ("te haz equivocado el elememto no existe"))
else:
    print(mensajes.correcto(palabra,indice))