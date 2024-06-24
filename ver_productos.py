#Función para listar todos los productos
coleccion=["a"]
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
