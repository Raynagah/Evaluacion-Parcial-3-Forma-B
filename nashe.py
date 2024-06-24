#agregar, visualizar, actualizar y eliminar productos del inventario,
#así como guardar y cargar la información de los productos desde un archivo .txt o .csv



#Guardar colección en un archivo.


def guardar_archivo(coleccion, nombreArchivo):
    #Coleccion formato coleccion=[{}]
    
    datos="Codigo,Nombre,Cantidad,Precio\n"
    for i in range(len(coleccion)):
        producto=coleccion[i]
        datos=f"{datos}{producto["codigo"]},{producto["nombre"]},{producto["cantidad"]},{producto["precio"]}"

    archivoN = nombreArchivo+".txt"
    with open(archivoN,"w") as archivo:
        archivo.write(datos)

def eliminar_producto(coleccion,codigo):
    #Coleccion formato coleccion=[{}]
    #
    for i in range(len(coleccion)):
        producto=coleccion[i]
        if producto["codigo"]==codigo:
            producto[i].pop(i)
        print(f"El producto con código {codigo} ha sido eliminado con éxito.")
        