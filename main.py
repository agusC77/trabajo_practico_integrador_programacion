from edicion_archivo import *
from validaciones import *
from ver_informacion_paises import ver_informacion_pais
from filtrar_paises import *
import os

print("Directorio actual:", os.getcwd())
# ===========================================================================================================================


with open("paises.csv", "r", encoding="utf-8", newline="") as contenido:
    lista_paises = contenido.readlines()


# ===========================================================================================================================


# Menú principal
while True:
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
    print()

    match opcion:
        
        case "1":
            agregar_paises(lista_paises)

# ===========================================================================================================================

        case "2":
            if os.path.exists("informacion_pais.csv"):
                print("ingrese el nombre del pais a revisar o una parte de el: ")
                pais_revisar = validar_texto()
                ver_informacion_pais(pais_revisar)
            else:
                print("❌ El archivo no existe.")
# ===========================================================================================================================

        case "3":
            if os.path.exists("informacion_pais.csv"):
                # Menú para que el usuario elija como filtrar los países 
                opcion = ""
                while True:
                    print(" Mostrar país por")
                    print("  1) Continente")
                    print("  2) Poblacion")
                    print("  3) Superficie")
                    opcion = input(" Elija la opcino deseada: ")
                    print()

                    if not opcion in ["1", "2", "3"]:
                        print(f"Error, debes seleccionar una opción entre 1 y 3 ")
                        print()
                    else:
                        break

                match opcion:
                    case "1":
                        paises_continente()
                    case "2":
                        pass
                    case "3":
                        pass
            else:
                print("❌ El archivo no existe.")
# ===========================================================================================================================
        case "4":
            if os.path.exists("informacion_pais.csv"):
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
                                    # Mostrar los países de mayor a menor
                                    pass
                                case "2":
                                    # Mostrar los países de menor a mayor
                                    pass
                                case _:
                                    print(" Error, opción inválida debes ingresar 1 o 2")
                    case "3":
                        pass
            else:
                print("❌ El archivo no existe.")

# ===========================================================================================================================

        case "5":
            if os.path.exists("informacion_pais.csv"):
                # Aca debemos poner una función que nos permita ver UNICAMENTE las estadisticas de un pais en especifico
                pass
            else:
                print("❌ El archivo no existe.")

# ===========================================================================================================================

        case "6":
            if os.path.exists("informacion_pais.csv"):
                    while opcion not in ["1","2"]:
                        print("Ingrese el nombre del país a modificar")
                        pais_modificar = validar_texto()
                        modificar_archivo(pais_modificar)

                        # EL usuario elije si desea modificar o no otro país
                        opcion = ""
                        while not opcion in ["1", "2"]:
                            print()
                            print("¿Desea modificar otro archivo?")
                            print(" 1) Si")
                            print(" 2) No")
                            opcion = input("Esperando elección: ")
            else:
                print("❌ El archivo no existe.")
                print("Error, no hay ningun archivo con países, por favor agregue algún pais")

# ===========================================================================================================================

        case "7":
            if os.path.exists("informacion_pais.csv"):
                print("ingrese el pais que desea eliminar: ")
                pais_eliminar = validar_texto()
                eliminar_pais(pais_eliminar)
            else:
                print("❌ El archivo no existe.")

# ===========================================================================================================================

        case "8":
            # Opcion de salir del programa
            break

# ===========================================================================================================================

        case _:
            print("Error, valor inválido, por favor ingrese un número entre 1 y 8")