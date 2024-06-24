"""
El menú debe tener las siguientes opciones:
o Agregar un producto.
o Ver todos los productos.
o Modificar un producto.
o Eliminar un producto.
o Guardar colección en un archivo.
o Salir del programa
"""
import time;
import ver_productos as funcion;
bandera_menu = True;
bandera_opcion = True;
print("¡Bienvenido a nuestra Tienda!\n");

while bandera_menu:
    print("Seleccione una de las siguientes opciones:\n");
    print("1.Agregar un producto");
    print("2.Ver todos los productos");
    print("3.Modificar un producto");
    print("4.Eliminar un producto");
    print("5.Guardar colección en un archivo");
    print("6.Salir del programa");
    try:
        opcion=int(input("Elija una opción: "));
    except:
        print("La opción ingresada no es válida, intentelo nuevamente\n");
    else:
        if opcion==1:
                print();
        elif opcion==2:
                funcion.ver_productos();
                print("\n");
        elif opcion==3:
                print();
        elif opcion==4:
                print();
        elif opcion==5:
                print();
        elif opcion==6:
            print("Saliendo del programa...");
            time.sleep(1);
            bandera_menu=False;
            bandera_opcion=False;
        else:
            print("La opción ingresada no está disponible, intentelo nuevamente\n");
