
coleccion=[{"codigo":1234,"nombre":"carlos","cantidad":0,"precio":1234}]
datos="Codigo,Nombre,Cantidad,Precio\n"
nombreArchivo="juli"
for i in range(len(coleccion)):
    producto=coleccion[i]
    datos=f"{datos}{producto["codigo"]},{producto["nombre"]},{producto["cantidad"]},{producto["precio"]}"




archivoN = nombreArchivo+".txt"
with open(archivoN,"w") as archivo:
    archivo.write(datos)