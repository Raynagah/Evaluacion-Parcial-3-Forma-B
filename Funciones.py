#Archivo dedicado a las funciones

#Creacion de la funcion que agrega productos
def funcion_agregar(lista):
    
    #Asignacion de banderas en True
    flag = True
    flag1 = True
    flag2 = True    
    flag3=True
    print("\nUsted selecciono la opcion de agregar productos\n")
    prodEncontrado={}
    #Pedir datos al usuario con 3 Ciclos WHILE que contienen (TRY, EXCEPT) para corregir que el usuario ingrese datos numericos
    while flag == True:
        try:
            codigo = int(input("Ingrese el codigo del producto: "))
        except:
            print("\nEl codigo debe ser númerico. Vuelva a intentarlo...\n") 
        else:

            while flag3==True:
                for i in range(len(lista)):
                    prod=lista[i]
                    if prod["codigo"]==codigo:
                        prodEncontrado=prod

                if prodEncontrado in lista:
                    print("El codigo ingresado ya existe, vuelva a intentarlo...")
                    codigo=int(input("Ingrese el codigo del producto"))
                else:
                    flag3=False
                

            
            flag = False

    nombre = input("Ingrese el nombre del producto: ")

    while flag1 == True:
        try:
            cantidad = int(input("Ingrese la cantidad de productos: "))
        except:
            print("\nLa cantidad ingresada debe ser en números. Vuelva a intentarlo...\n")
        else:
            flag1 = False

    while flag2 == True:
        try:
            precio = int(input("Ingrese el precio del producto: "))
        except:
            print("\nERROR. El precio ingresado deben ser números...\n")
        else:
            flag2 = False

    #Guardar datos ingresados en un diccionario y agregarlos a una lista
    producto = {"codigo": codigo, "nombre": nombre, "cantidad": cantidad, "precio": precio }
    lista.append(producto)
    print(f"El producto {producto["nombre"]} ha sido agregado con éxito.")
#Función modificar producto
def modificar_producto(coleccion):
    flag1 = True
    flag2 = True
    print("Seleccionó modificar un producto\n");
    bandera_menu_modificacion=True;
    print("Seleccione el producto que desea modificar ingresando el número que corresponda");
    #For para mostrar los productos y sus respectivos códigos.
    for i in range(len(coleccion)):
        producto=coleccion[i];
        print(f"Producto {i+1}: {producto}");
    productoEncontrado={}
    while bandera_menu_modificacion:
        #Validamos el código ingresado por el usuario.
        try:
            codigo=int(input("Ingrese el código del producto el cual desee modificar: "));
        except:
            for i in range(len(coleccion)):
                producto = coleccion[i]
                if codigo==producto["nombre"]:
                    productoEncontrado=producto
            if productoEncontrado not in coleccion:
                print("El producto seleccionado no existe, intentelo nuevamente");
        else:
            #
            for i in range(len(coleccion)):
                producto=coleccion[i];
                if codigo == producto["codigo"]:
                    print("Ya puede modificar el producto");
                    nombre = input("Ingrese el nombre del producto: ")
                    while flag1 == True:
                            try:
                                cantidad = int(input("Ingrese la cantidad de productos: "))
                            except:
                                print("\nLa cantidad ingresada debe ser en números. Vuelva a intentarlo...\n")
                            else:
                                flag1 = False

                    while flag2 == True:
                        try:
                            precio = int(input("Ingrese el precio del producto: "))
                        except:
                            print("\nERROR. El precio ingresado deben ser números...\n")
                        else:
                            flag2 = False
                        
                    #Actualizar
                    coleccion[i]={"codigo":producto["codigo"],"nombre":nombre,"cantidad":cantidad,"precio":precio}
                    bandera_menu_modificacion=False;



#Función para listar todos los productos
def ver_productos(coleccion):
    #Generamos la tabla que se mostrará al usuario
    print("Seleccionó listar todos los productos\n");
    print("------------------------------------------------------------------------");
    print("|     CODIGO     |     NOMBRE     |     CANTIDAD     |      PRECIO     |");
    print("------------------------------------------------------------------------");
    #Ciclo For para mostrar todos los productos existentes.
    for i in range(len(coleccion)):
        producto=coleccion[i];
        print(f"{producto["codigo"]} | {producto["nombre"]} | {producto["cantidad"]} | {producto["precio"]} |");



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



                    
