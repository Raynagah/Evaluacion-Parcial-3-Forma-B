def funcion_agregar(lista):
    
    flag = True
    flag1 = True
    flag2 = True

    print("\nUsted selecciono la opcion de agregar productos\n")

    while flag == True:
        try:
            codigo = int(input("Ingrese el codigo del producto: "))
        except:
            print("\nEl codigo debe ser númerico. Vuelva a intentarlo...\n") 
        else:
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

    producto = {"codigo": codigo, "nombre": nombre, "cantidad": cantidad, "precio": precio }
    lista.append(producto)
