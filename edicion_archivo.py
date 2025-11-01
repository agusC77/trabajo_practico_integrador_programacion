from validaciones import *
import csv

# ===========================================================================================================================

# Funcion para crear un archivo que almacenara los paises con los que trabajaremos
def agregar_paises(paises):
    nombre_pais = ""
    poblacion = 0
    superficie = 0
    salir = ""
    continente = ""
    existe = False
    encabezado = ["País","Continente","Población","Superficie"]
    pais_agregar = {"País": "", "Continente": "", "Poblacion": "", "Superficie": ""}

    while True:
        try:
            # abrimos el archivo en modo lectura solo para verificar que exista, en caso de que no exista va 
            # hasta el execp y crea el archivo con el encabezado
            with open("informacion_pais.csv", "r",encoding="utf-8", newline="") as archivo:
                lector = csv.DictReader(archivo)

            with open("informacion_pais.csv", "a",encoding="utf-8", newline="") as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=encabezado)
                # El usuario ingresa el nombre del país a agregar
                while True:
                    print("Ingrese el país a agregar:")
                    nombre_pais = validar_texto()
                    print()

                    # Verifica que el país no se haya ingresado antes
                    if verificar_pais_archivo(nombre_pais):
                        # Si ya está en el archivo, mostramos error y pedimos otro
                        print(f"Error, el país {nombre_pais} ya se encuentra en el archivo.")
                        print()
                        continue

                    # Verifica si el país existe
                    existe = False
                    for info_pais in paises:
                        lista = info_pais.split(",")
                        if lista[0] == nombre_pais:
                            existe = True
                            continente = lista[1].strip()
                            break
                    # En caso de que el país no exista, se le avisa al usuario y se vuelve a pedir que ingrese un país
                    if not existe:
                        print(f"Error, el país {nombre_pais} no existe, por favor ingrese otro")
                        print()
                        continue 
                    else:
                        break

                # El usuario ingresa la población del país
                while True:
                    print(f"Ingrese la población de {nombre_pais.title()}")
                    poblacion = numero_positivo()
                    print()
                    # Esto permite verificar que el usuario ingrese un entero positivo
                    if not poblacion.isdigit():
                        print("Error, valor inválido, por favor ingrese un número entero positivo.")
                        print()
                        continue
                    else:
                        break

                # El usuario ingresa la superficie del país
                print(f"Ingrese la superficie de {nombre_pais.title()}:")
                superficie = numero_positivo()
                print()

                # Se ingresa estos valores como una nueva linea del archivo
                pais_agregar = {"País": nombre_pais, "Continente": continente, "Población": poblacion, "Superficie": superficie}
                escritor.writerow(pais_agregar)

            # El usuario decide si agregar más paises o no
            salir = ""
            while salir not in ["1", "2"]:
                print("¿Desea agregar más países?")
                print(" 1) Si")
                print(" 2) No")
                salir = input("Esperando elección: ")
                print()
            if salir == "2":
                break

        # En caso de que el archivo no exista, lo crea, agrega el encabezado y luego vuelve a repetir el bucle, debido a que 
        # al crearse el archivo en la proxima iteración cuando intente leerlo no generara error y podremos agregar paises
        # de esta forma podemos reutilizar código 
        except FileNotFoundError:
            print("El archivo no existe")
            print("Creando archivo....")
            print()
            with open("informacion_pais.csv", "w",encoding="utf-8", newline="") as archivo:
                escritor = csv.writer(archivo)
                # Encabezado
                escritor.writerow(["País","Continente","Población","Superficie"])


# ===========================================================================================================================


def eliminar_pais(eliminar):
    with open("informacion_pais.csv", "r",encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo)
        lista_paises = list(lector)
    with open("informacion_pais.csv", "w",encoding="utf-8", newline="") as archivo:
        for pais in lista_paises:
            if pais[0] == eliminar:
                continue
            else:
                escritor = csv.writer(archivo)
                escritor.writerow(pais)


# ===========================================================================================================================

# Función para modificar la población o superficie de un país a elecón del usuario
def modificar_archivo(pais_modificar):
    eleccion = ""

    with open("informacion_pais.csv", "r",encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo)
        lista_paises = list(lector)

    while True:
        # El usuario indicara lo que quiere modificar
        while eleccion not in ["1", "2", "3"]:
            print("¿Qué deseas modificar?")
            print(" 1) Población")
            print(" 2) Superficie")
            print(" 3) Todas la anteriores")
            eleccion = input("Esperando elección: ")
            print()
            if eleccion not in ["1", "2", "3"]:
                print("Error, valor inválido, por favor ingrese un número entre 1 y 3")
        
        # Sobreescribe el archivo con los nuevos datos
        with open("informacion_pais.csv", "w",encoding="utf-8", newline="") as archivo:
            escritor = csv.writer(archivo)
            # Reescribira todas las lineas del archivo, en el caso de que se encuentre el país que se desea modificar
            # modificara su población o superficie, si no lo encuentra dejara la linea como estaba
            for informacion_pais in lista_paises:
                if informacion_pais[0] == pais_modificar:
                    match eleccion:
                        case "1":
                            # Se modifica la población del país
                            print(f"Ingrese cuánta población tiene {informacion_pais[0]}")
                            informacion_pais[2] = numero_positivo()
                            escritor.writerow([informacion_pais])
                            break
                        case "2":
                            # Se modifica la superficie del país
                            print(f"Ingrese la superficie de {informacion_pais[0]}")
                            informacion_pais[3] = numero_positivo()
                            escritor.writerow([informacion_pais])
                            break
                        case "3":
                            # Se modifica la población del país
                            print(f"Ingrese cuánta población tiene {informacion_pais[0]}")
                            informacion_pais[2] = numero_positivo()
                            # Se modifica la superficie del país
                            print(f"Ingrese la superficie de {informacion_pais[0]}")
                            informacion_pais[3] = numero_positivo()
                            escritor.writerow([informacion_pais])
                            break
                else:
                    escritor.writerow(informacion_pais)
            break