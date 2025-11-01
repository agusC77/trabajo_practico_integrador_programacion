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

# Función para elmiminar un país del archivo
def eliminar_pais(eliminar):
    # Variable para seber si el país que se desea eliminar esta o no en la lista
    esta = False
    # Abre el archivo en modo lectura y almacena sus lineas como listas en una lista que almacenara todas las demas
    with open("informacion_pais.csv", "r",encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo)
        lista_paises = list(lector)
        # Rvisa en el primer elemento de cada lista el país a eliminar 
        for pais in lista_paises:
            if pais[0] == eliminar:
                esta = True
                break
    # Si lo encuentra, se sobreescribira el archivo, si no lo encuentra le dira al usuario que
    # el país que esta buscando no se encuentra en el archivo
    if esta:
        # Sobreescribe el archivo linea por linea
        with open("informacion_pais.csv", "w",encoding="utf-8", newline="") as archivo:
            # Accede al primer índice de todas las listas para verificar que el país que desee eliminar se encuentre em la lista
            # En caso de encontrar el país lo elimina si no lo encuentra no hace nada
            for pais in lista_paises:
                if pais[0] == eliminar:
                    continue
                else:
                    escritor = csv.writer(archivo)
                    escritor.writerow(pais)
        print(f"El país {eliminar.title()} fue eliminado del archivo.")
        print()
    else:
        print(f"El país {eliminar.title()} no se puede eliminar debido a que no se encuentra en la lista.")
        print()

# ===========================================================================================================================

# Función para modificar la población o superficie de un país a elecón del usuario
def modificar_archivo(pais_modificar):
    encabezado = ["País","Continente","Población","Superficie"]
    poblacion = ""
    superficie = ""
    elceccion = ""

    # Esto nos permite almacenar las lineas del archivo para poder modificar algún valor o para sobreescribir el archivo
    with open("informacion_pais.csv", "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        lista_paises = list(lector)

    while not elceccion in ["1", "2", "3"]:
        print("------------------------------")
        print("¿ Qué datos deseas modificar?")
        print(" 1) Población")
        print(" 2) Superficie")
        print(" 3) Población y superficie")
        elceccion = input("Esperando elección: ")
        print("------------------------------")

    
    match elceccion:
        case "1":
            # El usuario ingresa la población del país
            while True:
                print(f"Ingrese la población de {pais_modificar.title()}")
                poblacion = numero_positivo()
                print()
                # Esto permite verificar que el usuario ingrese un entero positivo
                if not poblacion.isdigit():
                    print("Error, valor inválido, por favor ingrese un número entero positivo.")
                    print()
                    continue
                else:
                    break
            # Modifica el valor de la población
            for diccionario in lista_paises:
                if diccionario["País"] == pais_modificar:
                    diccionario["Población"] = poblacion

        case "2":
            print(f"Ingrese la superficie de {pais_modificar.title()}:")
            superficie = numero_positivo()
                        # Modifica el valor de la población
            for diccionario in lista_paises:
                if diccionario["País"] == pais_modificar:
                    diccionario["Superficie"] = superficie
            
        case "3":
            # El usuario ingresa la población del país
            while True:
                print(f"Ingrese la población de {pais_modificar.title()}")
                poblacion = numero_positivo()
                print()
                # Esto permite verificar que el usuario ingrese un entero positivo
                if not poblacion.isdigit():
                    print("Error, valor inválido, por favor ingrese un número entero positivo.")
                    print()
                    continue
                else:
                    break
            
            # Modifica el valor de la población
            for diccionario in lista_paises:
                if diccionario["País"] == pais_modificar:
                    diccionario["Población"] = poblacion
            print(f"Ingrese la superficie de {pais_modificar.title()}:")
            superficie = numero_positivo()
                        # Modifica el valor de la población
            for diccionario in lista_paises:
                if diccionario["País"] == pais_modificar:
                    diccionario["Superficie"] = superficie

    with open("informacion_pais.csv", "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames= encabezado)
        # Vuelve a escribir el encabezado
        escritor.writeheader()
        # Vuelve a escribir la lineas de código pero con los valores modificados
        escritor.writerows(lista_paises)