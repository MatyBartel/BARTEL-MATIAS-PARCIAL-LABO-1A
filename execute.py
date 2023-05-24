
from functions import *
import os

while True:
    os.system("cls")
    match(menu()):
        case 1:
            try:
                lista_diccionario =  csv_list_dic(nombre_archivo=input("-Ingrese direccion del archivo a usar 'carpeta//ejemplo.csv' :"))      # Parcial//insumos.csv
            except FileNotFoundError:
                print("ERROR: El archivo que ingreso no existe, ingrese la direccion correctamente.")
        case 2:
            try: 
                contador_lista_dic = contar_en_lista_dic(lista_diccionario,"marca")
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")

        case 3:            
            try: 
                diccionario_filtrado=mostrar_tres_claves(lista_diccionario,"marca","nombre","precio")
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")

        case 4:
            try: 
                lista_filtrada=buscar_por_caracteristica(lista_diccionario,caracteristica_ingresada=input("Ingrese caracteristica:"))
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")

        case 5:
            try: 
                lista_ordenada = ordenar_lista(lista_diccionario,"marca","precio")
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")

        case 6:
            try: 
                carrito = comprar(lista_diccionario,caracteristica_ingresada=input("Ingrese marca :"))
                archivo_texto = generar_archivo_txt(carrito,"carrito.txt")
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")

        case 7:
            try:
                guardar_JSON(lista_diccionario,"./lista_filtrada.json")
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1,6)")

        case 8:
            lista_filtrada=leer_JSON("./lista_filtrada.json")
            print(lista_filtrada)

        case 9:
            diccionario = lista_diccionario
            resultado=list(map(aumentar_precio,diccionario))

        case 10:
            seguir_salir()

        case _:
            print("Ingrese opcion valida")
