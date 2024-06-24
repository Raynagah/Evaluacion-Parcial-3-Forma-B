#Función modificar producto
coleccion=["arroz","fideos"];
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



                    



                    
