with open("paises.txt","r") as contenido:
    listar_paises = contenido.readlines()
    for pais in listar_paises:
        print(pais)
# Menú principal
enunciado = True
while enunciado == True:
    print("==============================")
    print("            MENU")
    print(" 1) Agregar paises")
    print(" 2) Buscar pais por nombre")
    print(" 3) Filtrar paises")
    print(" 4) Ordenar paises")
    print(" 5) Mostrar Estadistica")
    print(" 6) Editar paises")
    print(" 7) eliminar pais de la lista")
    print(" 8) Salir del menu")
    print("==============================")
    opcion = input(" Elija la opción deseada: ")

    match opcion:
        
        case "1":
            # Aca debemos poner una función que nos permita añadir países por nombre
            pass
        case "2":
            # Menú para que el usuario elija como filtrar los países osea si elije la opción 2 mostrara 
            # le mostrara los países con mayor ploblación, menor población, promedio de poblacón, a elección 
            # y con la misma metodolgía con las otras opciones
            print(" 1) Filtrar paises de un continente")
            print(" 2) filtrar paises por rango de poblacion")
            print(" 3) Filtrar paises por rango de superficie")
            opcion = input(" Elija la opcino deseada: ")
            match opcion:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
        case "3":
            # Menu para que el usuario vea todos los países ordenados por nombre, población y superficie
            print(" 1) Ordenar en orden alfabético")
            print(" 2) Ordenar países por rango de población")
            print(" 3) Ordenar países por rango de superficie")
            opcion = input(" Elija la opción deseada: ")
            match opcion:
                case "1":
                    # Función que ordena países por orden alfabético
                    pass
                case "2":
                    # Permite elejir al usuario si quiere ver todos los paíse ordenados del que tiene menos población 
                    # al que tiene mayor población y vicebersa
                    while True:
                        print(" 1) De Menor a mayor")
                        print(" 2) Mayor a menor")
                        opcion = input(" Elija la opción deseada: ")
                        match opcion:
                            case "1":
                                # Mosrar lospaíses de mayor a menor
                                pass
                            case "2":
                                # Mostrar los países de menor a mayor
                                pass
                            case _:
                                print(" Error, opción inválida debes ingresar 1 o 2")
                case "3":
                    pass
        case "4":
            pass
        case "5":
            # Aca debemos poner una función que nos permita añadir países por nombre
            pass
        case "6":
            #aca hay que agregar la opcion de editar el codigo
            pass
        case "7":
            #aca agregamos una opcion para eliminar un pais de la lista
            pass
        case "8":
            #opcion de salir del programa
            pass
        case _:
            print("error, ingrese un valor valido del 1 al 8")