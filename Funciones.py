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