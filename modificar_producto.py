#Función modificar producto
coleccion=["arroz","fideos"];
def modificar_producto(coleccion):
    print("Seleccionó modificar un producto\n");
    bandera_menu_modificacion=True;
    print("Seleccione el producto que desea modificar ingresando el número que corresponda");
    #For para mostrar los productos y sus respectivos códigos.
    for i in range(len(coleccion)):
        producto=coleccion[i];
        print(f"Producto {i+1}: {producto}");
    while bandera_menu_modificacion:
        #Validamos el código ingresado por el usuario.
        try:
            opcion_modificacion=int(input("Ingrese el código del producto el cual desee modificar: "));
        except:
            if opcion_modificacion not in coleccion["codigo"]:
                print("El producto seleccionado no existe, intentelo nuevamente");
        else:
            #
            for i in range(len(coleccion)):
                producto=coleccion[i];
                if opcion_modificacion == producto["codigo"]:
                    print("Ya puede modificar el producto");
                    bandera_menu_modificacion=False;
                    



                    
