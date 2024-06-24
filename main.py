#Archivo main | Integrantes de la evaluación: Mayckol Mardones, Carlos Moil, Rodrigo Vargas.



#Importamos las funciones necesarias
import time;

import Funciones as funcion

coleccion=[]
#Definir variables
bandera_menu = True;
bandera_opcion = True;
print("¡Bienvenido a nuestra Tienda!\n");
#Realizamos un menú para que el usuario pueda utilizar las distintas funciones que hemos creado.
while bandera_menu:
    print("Seleccione una de las siguientes opciones:\n");
    print("1.Agregar un producto");
    print("2.Ver todos los productos");
    print("3.Modificar un producto");
    print("4.Eliminar un producto");
    print("5.Guardar colección en un archivo");
    print("6.Salir del programa");
    #Validamos que la opción ingresada por el usuario sea numérica.
    try:
        opcion=int(input("Elija una opción: "));
    except:
        print("La opción ingresada no es válida, intentelo nuevamente\n");
    else:
        #Utilizando la opción ingresada por el usuario, llamamos a la función correspondiente.
        if opcion==1:
                print();
                funcion.funcion_agregar(coleccion)
        elif opcion==2:
                print("\n");
                funcion.ver_productos(coleccion)
        elif opcion==3:
                print();
                funcion.modificar_producto(coleccion)
        elif opcion==4:
                print();
                funcion.eliminar_producto(coleccion)
        elif opcion==5:
                print();
                nombre=input("Ingrese el nombre que desea en el documento: ")
                funcion.guardar_archivo(coleccion,nombre)
        elif opcion==6:
            print("Saliendo del programa...");
            time.sleep(1);
            bandera_menu=False;
            bandera_opcion=False;
        else:
            print("La opción ingresada no está disponible, intentelo nuevamente\n");

