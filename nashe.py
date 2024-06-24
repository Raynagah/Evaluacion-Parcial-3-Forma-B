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

def eliminar_producto(coleccion):
    #Coleccion formato coleccion=[{}]
    #Mostrar lista de datos
    bandera_menu_eliminar=True;
    print("Seleccione el producto que desea modificar ingresando el número que corresponda");

    for i in range(len(coleccion)):
        producto=coleccion[i];
        print(f"Producto {i+1}: {producto}");
    
    
    productoEncontrado={}
    while bandera_menu_eliminar:
        try:
            codigo=int(input("Ingrese el código del producto el cual desee eliminar: "));
            
        except:
            for i in range(len(coleccion)):
                producto = coleccion[i]
                if codigo==producto["nombre"]:
                    productoEncontrado=producto
            if productoEncontrado not in coleccion:
                print("El producto seleccionado no existe, intentelo nuevamente");
        else:
            for i in range(len(coleccion)):
                producto=coleccion[i]
                if producto["codigo"]==codigo:
                    producto[i].pop(i)
                print(f"El producto con código {codigo} ha sido eliminado con éxito.")




