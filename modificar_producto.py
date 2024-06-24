#Función modificar producto
coleccion=["arroz","fideos"];
def modificar_producto(coleccion):
    print("Seleccionó modificar un producto\n");
    bandera_menu_modificacion=True;
    print("Seleccione el producto que desea modificar ingresando el número que corresponda");
    for i in range(len(coleccion)):
        producto=coleccion[i];
        print(f"Producto {i+1}: {producto}");
    while bandera_menu_modificacion:
        try:
            opcion_modificacion=int(input("Ingrese el código del producto el cual desee modificar: "));
        except:
            if opcion_modificacion not in producto:
                print("El producto seleccionado no existe, intentelo nuevamente");
        else:
            
            for i in range(len(coleccion)):
                producto=coleccion[i];
                if opcion_modificacion == producto["codigo"]:
                    print("Modifique el producto");


                    
