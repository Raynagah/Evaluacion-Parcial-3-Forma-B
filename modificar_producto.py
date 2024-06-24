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
                    nombre=input




                    bandera_menu_modificacion=False;
                    



                    
