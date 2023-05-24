import os
os.system("cls")
import json

def menu():
    os.system("cls")
    try:
        print("════════════════════════════════════════   MENU   ════════════════════════════════════════")
        print("")
        print("1-  Cargar datos del archivo (obligatorio)")
        print("2-  Mostrar marcas y insumos de cada una")
        print("3-  Mostrar para cada marca el nombre y el precio de los insumos")
        print("4-  Buscar por caracteristica")
        print("5-  Mostrar productos ordenados por marcas de forma ascendente")
        print("6-  Realizar Compras")
        print("7-  Guardar en JSON")
        print("8-  Leer desde JSON")
        print("9-  Actualizar Precios en 8.4%")
        print("10- Salir")
        opcion=int(input("Ingrese una opcion:"))
        return opcion

    except ValueError:
        print("----------------OPCION INVALIDA--------------------")
        os.system("pause")
        os.system("cls")

def csv_list_dic(nombre_archivo)->list:
    """
    Function: 
        Ingresa direccion del archivo a cargar, por ejemplo: 'carpeta//ejemplo.csv'.

    Args:
        nombre_archivo (str): Archivo a cargar

    Returns:
        Se carga el archivo en formato de lista de diccionarios y los muestra.
    """
    os.system("cls")
    separador = ","


    with open(nombre_archivo, encoding="utf-8") as archivo:
        lista_diccionario = []
        for linea in archivo:
            linea = linea.strip("\n").replace("$", "")                    # Saco el salto de linea y elimino $
            columnas = linea.split(separador)                              # Separo con , los datos

            id, nombre, marca, precio, caracteristica = columnas           # Asigno las columnas

            diccionarios = {
                "id": id,
                "nombre": nombre,
                "marca": marca,                                            # Creo los diccionarios
                "precio": precio,
                "caracteristica": caracteristica
            }                                           

            lista_diccionario.append(diccionarios)                                     # Los agrego a la lista_diccionario

        print("═══════════════════════════════════════════════════════════════════════ DATOS DEL ARCHIVO ═══════════════════════════════════════════════════════════════════════")
        for diccionario in lista_diccionario:
            print(diccionario)                                             # Muestro con un espacio entre cada diccionario
            print() 

        os.system("pause")
        os.system("cls")

        return lista_diccionario

def contar_en_lista_dic(lista_dic:list,key:str)->dict:
    """
    Function: Recibe una lista de diccionarios y una clave, agrega esos valores de la clave a una lista y luego recorre la lista agregandolos a un diccionario, si ya estaban, cuenta.
    Por ultimo muestra de forma prolija los valores con su contador de veces que estan.

    Args:
        lista_dic (list): Lista que recibe
        key (str): Clave que usara sus valores para contarlos
    
    Returns:
        diccionario (dict): Diccionario con los valores sin repetir y contados.

    """
    lista_aux=[]
    diccionario = {}

    for clave in lista_dic:                    # Agrego a una lista las claves
        lista_aux.append(clave[key])
    for elemento in lista_aux:
        if elemento in diccionario:
            diccionario[elemento] += 1         # Si el elemento ya existe en el diccionario, los voy contando.
        else:
            diccionario[elemento] = 1
    for elemento in diccionario:               # Muestro de forma prolija
        cantidad = diccionario[elemento]
        print(f"{elemento}: {cantidad}")

    os.system("pause")
    os.system("cls")
    return diccionario

def mostrar_tres_claves(lista_dic:list,key:str,key_2:str,key_3:str)->list:
    """
    Function: Recibe una lista de diccionarios y tres claves,termina reduciendo la lista original agregando las claves con diccionarios a una nueva lista.

    Args:
        lista_dic (list): Lista de diccionarios que recibe
        key (_type_): Clave nro 1
        key_2 (_type_): Clave nro 2
        key_3 (_type_): Clave nro 3

    Returns:
        lista_reducida (list): Lista de diccionarios reducida a tres diccionarios
    """
    lista_aux=[]
    diccionario={}
    lista_reducida=[]
    for clave in lista_dic:
        diccionario = {
                "marca": clave[key],
                "nombre": clave[key_2],
                "precio": clave[key_3],                                            # Creo los diccionarios
            } 
        lista_reducida.append(diccionario)
    print("═══════════════════════════════════════════════════════════════════════ CLAVES - VALORES ═══════════════════════════════════════════════════════════════════════")
    for diccionario in lista_reducida:
        print(diccionario)                                             # Muestro con un espacio entre cada diccionario
        print() 

    os.system("pause")
    os.system("cls")
    return lista_reducida

def buscar_por_caracteristica(lista_diccionarios,caracteristica_ingresada)->list:
    """
    Function: Busca por la caracteristica ingresada y muestra los diccionarios que coincidan

    Args:
        lista_diccionarios (list): Lista que recibe
        caracteristica_ingresada (str): Caracteristica que buscara coincidencias
    
    Returns:
        lista_diccionarios (dict): Lista que tiene los diccionarios que coinciden con la caracteristica

    """
    lista_caracteristica = []
    for diccionario in lista_diccionarios:
        for valor in diccionario.values():
            if caracteristica_ingresada in valor:
                lista_caracteristica.append(diccionario)
    print("═══════════════════════════════════════════════════════════════════════ FILTRADO CARACTERISTICA ═══════════════════════════════════════════════════════════════════════")
    for diccionario in lista_caracteristica:
        print(diccionario)                                             # Muestro con un espacio entre cada diccionario
        print() 
    os.system("pause")
    os.system("cls")
    return lista_caracteristica

def ordenar_lista(lista_diccionarios: list, clave_principal: str, clave_auxiliar: str):
    """
    Function: Ordena la lista segun el abecedario de forma ascendente segun la clave que pongas.

    Args:
        lista_diccionarios (list): Lista que toma de base.
        clave (str): Clave que comparara y ordenara de forma ascendente.

    Returns:
        lista_diccionarios: Lista ordenada de forma ascendente.
    """

    tam = len(lista_diccionarios)
    
    for i in range(tam - 1):
        for j in range(0, tam): 
            if lista_diccionarios[i][clave_principal] < lista_diccionarios[j][clave_principal] or (lista_diccionarios[i][clave_principal] == lista_diccionarios[j][clave_principal] and lista_diccionarios[i][clave_auxiliar] > lista_diccionarios[j][clave_auxiliar]):
                aux=None
                aux=lista_diccionarios[i]
                lista_diccionarios[i]=lista_diccionarios[j]
                lista_diccionarios[j]= aux

    print("═══════════════════════════════════════════════════════════════════════ DATOS ORDENADOS ═══════════════════════════════════════════════════════════════════════")
    for diccionario in lista_diccionarios:
        print(diccionario)  # Muestro con un espacio entre cada diccionario
        print() 
    
    os.system("pause")
    os.system("cls")
    
    return lista_diccionarios

def seguir_salir():
    """
    Function: 
        Nos pregunta si deseamos continuar o finalizar un programa
    Returns:
        Nos retorna una respuesta, si es "S" continua, si no, finaliza el programa
    """
    continuar_salir=input("Desea continuar? s/n: ")
    while continuar_salir != "s" and continuar_salir != "n":
        continuar_salir=input("ERROR, desea continuar? s/n: ")
    if continuar_salir =="n":
        quit("----------------------------FIN DEL PROGRAMA-------------------------------")

def comprar(lista_diccionarios, caracteristica_ingresada):
    lista_caracteristica = []
    
    for diccionario in lista_diccionarios:
        if caracteristica_ingresada in diccionario.values():
            lista_caracteristica.append(diccionario)
    
    for diccionario in lista_caracteristica:
        print(diccionario)
        print()
    
    carrito = []
    
    while True:
        producto_id = input("Ingrese el ID del producto que desea comprar (0 para finalizar): ")
        
        if producto_id == "0":
            if carrito == []:  # Verificar si el carrito está vacío
                print("El carrito está vacío. Por favor, seleccione al menos un producto.")
                continue
            else:
                break
        
        cantidad = int(input("Ingrese la cantidad: "))
        
        producto_seleccionado = None
        for diccionario in lista_caracteristica:
            if producto_id == diccionario['id']:
                producto_seleccionado = diccionario
                break
        
        if producto_seleccionado != None:
            producto_seleccionado['cantidad'] = cantidad
            carrito.append(producto_seleccionado)
            print("Producto agregado al carrito.")
        else:
            print("ID de producto inválido. Intente nuevamente.")
        print()
        respuesta = input("¿Desea seguir comprando? (s/n): ")
        if respuesta.lower() != "s":
            break

    print("════════════ CARRITO:")
    for producto in carrito:
        print(producto)
    
    os.system("pause")
    os.system("cls")
    return carrito

def generar_archivo_txt(carrito, nombre_archivo:str):
    try:
        with open(nombre_archivo, 'w') as archivo:
            total = 0.0 
            
            for producto in carrito:
                archivo.write(str(producto) + '\n')
                precio = float(producto['precio'])
                cantidad = int(producto['cantidad'])
                total += precio * cantidad              # Calcular el total
                
            archivo.write(f"Total: ${total}\n")         # Escribir el total en el archivo
            
        print(f"El archivo {nombre_archivo} se ha generado correctamente.")
        os.system("pause")
        os.system("cls")
    except IOError:
        print("Se produjo un error al generar el archivo.")
        os.system("pause")
        os.system("cls")

def guardar_JSON(lista_de_productos,path):
    lista_filtrada=[]
    for producto in lista_de_productos:
        if ("Alimento" in producto['nombre']):
            lista_filtrada.append(producto)
    with open (path,"w") as file:
        json.dump(lista_filtrada,file,indent=4)

def leer_JSON(path):
    lista_leida=[]
    with open(path) as file:
        lista_leida=json.load(file)
    return lista_leida

def aumentar_precio(diccionario):
    precio = diccionario["precio"]
    precio = precio.strip("$")
    precio.replace(".","").replace(",",".")
    precio = float(precio)
    precio_aumentado = precio + (precio * 0.084)
    precio_aumentado = round(precio,2)
    diccionario["precio"]= precio_aumentado
    diccionario["precio"] = str(precio_aumentado)
    return diccionario

def csv_momento(diccionario):
    with open("C:\\Users\\Matias\\Desktop\\insumos2.csv","w",encoding="utf-8") as file:
        renglon = 0
        for i in diccionario:
            linea= f'{i["ID"]},{i["NOMBRE"]},{i["MARCA"]},${i["PRECIO"]},{i["CARACTERISTICA"]}'
            file.writelines("\n")
            file.writelines(linea)
            renglon+=1