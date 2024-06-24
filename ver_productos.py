#Función para listar todos los productos


def ver_productos(coleccion):
    print("Seleccionó listar todos los productos");
    for i in range(len(coleccion)):
        producto=coleccion[i];
        print(f"{producto["codigo"]} | {producto["nombre"]} | {producto["cantidad"]} | {producto["precio"]} |");
