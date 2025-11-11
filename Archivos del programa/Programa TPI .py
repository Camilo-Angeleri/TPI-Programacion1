# Trabajo Práctico Integrador

import time #utilizaremos time para que el menu tenga un tiempo de aparicion y sea mas claro
import csv #Es un modulo nativo que descubrí que permite crear 2 objetos muy practicos para las funciones. csv.reader y csv.writer.

##### Funciones #####

def agregar_pais_a_base(pais_valor,poblacion_valor,superficie_valor,continente_valor):
    with open("base.csv","a") as base: #La funcion toma los inputs conseguidos anteriormente
        base.write("\n")               #Al Abrir base.csv, copia cada uno de los strings
        base.write(pais_valor+",")     #Y a todos les agrega una coma,excepto el final
        base.write(poblacion_valor+",")
        base.write(superficie_valor+",")
        base.write(continente_valor)   #Al saber que los datos estan bien, el resultado siempre es el esperado. En caso de que no, el bucle se reinicia por los else que hacen de filtro en la opcion
    return print("País agregado correctamente\n") 

def mostrar_menu(): #Funcion que llama la interfaz de opciones.
    print("*******************")
    print("Menú de operaciones\n\n---------\nIntroduce el numero de la operacion que desea realizar.\n---------\n")
    print("1- Agregar un país") #Solo se aceptan todos los datos. sin campos vacios
    print("2- Actualizar los datos de Poblacion de un país")
    print("3- Actualizar los datos de Superficie de un país")
    print("4- Buscar un país por nombre") #Coincidencia parcial o exacta
    print("5- Filtrar paises") #Continente, Rango de poblacion, rango de superficie, puedo hacerlo diferentes funciones
    print("6- Ordenar paises por paramentro") #Nombre (alfabetico), poblacion (Mayor o menor), superficie (Mayor o menor)
    print("7- Mostrar estadisticas") #Pais con mayor o menor poblacion, promedio de superficie, cantidad de paises por continente
    print("8- Salir")
    print("*******************")

def verificar_paises(): #Esta funcion es fundamental para saber si un nombre ya esta en base.csv. Al estar al principio de cada bucle, nos aseguramos que la lista siempre esta actualizada en conjunto a la base.
    with open("base.csv","r") as base: 
        base.readline() #evitamos el encabezado aca
        lineas=base.readlines() #Tomamos todo lo que no es el encabezado.
        paises=[] #lista paises
        
        for linea in lineas: #Se toma cada linea de todo el conjunto de lineas
            parte=linea.strip().split(",") #y de cada linea, sacamos una lista de sus partes
            paises+=[parte[0]] #tomamos la primer columna de todas las filas 
        lista_paises=paises #Llegado aqui, la lista resultante de todos los paises habiendo sido concatenados en una lista.
    return lista_paises#Como vemos, el resultado es silencioso para el user

def encontrar_poblacion(pais:str): #Funcion para buscar la poblacion de un pais
    with open("base.csv","r") as base:
        lineas=base.readlines() #incluso podemos tomar el encabezado, ya que se utiliza despues de pasar un filtro de si pais esta lista_paises
        for linea in lineas: #por cada linea
            parte=linea.split(",") #y cada elemento de la linea
            nombre_comparacion=parte[0] #la primera siempre sera el pais
            poblacion=parte[1] #con esto sacamos poblacion 
            if pais==nombre_comparacion: #si tiene el mismo nombre devuelve la poblacion de esa iteracion
                return poblacion

def encontrar_superficie(pais:str): #Funcion para buscar la superficie de un pais
    with open("base.csv","r") as base:
        lineas=base.readlines() #incluso podemos tomar el encabezado, ya que se utiliza despues de pasar un filtro de si pais esta lista_paises
        for linea in lineas: #por cada linea
            parte=linea.split(",") #y cada elemento de la linea
            nombre_comparacion=parte[0] #la primera siempre sera el pais
            superficie=parte[2] #con esto sacamos superficie
            if pais==nombre_comparacion: #si tiene el mismo nombre devuelve la superficie de esa iteracion
                return superficie

def encontrar_continente(pais:str):#Funcion que sirve para encontrar el continente de ese pais en especifico
    with open("base.csv","r") as base:
        lineas=base.readlines() #funcion basada en encontrar_poblacion y encontrar_superficie
        for linea in lineas: #por cada linea
            parte=linea.split(",") #y cada elemento de la linea
            nombre_comparacion=parte[0] #la primera siempre sera el pais
            continente=parte[3] #con esto sacamos 
            if pais==nombre_comparacion: #si tiene el mismo nombre devuelve el continente de esa iteracion
                return continente

def encontrar_nombre_pais_bool(pais:str): #funcion para buscar el nombre del pais con cierto margen de coincidencia, regresa un booleano pues esta pensada para un if statement
    lista_paises_temp=[]#Para ir tomando cada pais y comparar luego
    coincidencia=[] #utilizado para almacenar (o no), para un resultado booleano
    with open("base.csv","r") as base:
        lineas=base.readlines()
        for linea in lineas:
            parte=linea.split(",")
            nombre_comparacion=parte[0] #Siempre será el nombre del pais
            if nombre_comparacion==pais: #Si el nombre es igual, ya devuelve que si existe
                return True
            else: #sino, por cada loop se rellena la lista_paises_temp, que toma todos los paises que se almacenan en el nombre_comparacion
                pass
                lista_paises_temp+=[nombre_comparacion]
        for elemento in lista_paises_temp: #por cada elemento dentro de esta lista
            if pais in elemento: #si la string en pais, esta dentro (o parcialmente dentro) de elemento (otra string) #Entonces hay esa es la coincidencia mas cercana, y por lo tanto existe
                coincidencia=[elemento] #la lista coincidencia se rellena porque existe
        if coincidencia: #simple filtro, si hay algo en coincidencia, true e imprime el resultado mas cercano
            print(f"Coincidencia mas cercana: {elemento}\nProcediendo con {elemento}")
            return True
        else: #si es una lista vacia, false
            return False

def encontrar_nombre_pais_string(pais:str): #funcion para buscar el nombre del pais con cierto margen de coincidencia, regresa un string, esta pensado para remplazar el string pais original, por la coincidencia mas cercana
    lista_paises_temp=[]#Para ir tomando cada pais y comparar luego
    with open("base.csv","r") as base:
        lineas=base.readlines()
        for linea in lineas:
            parte=linea.split(",")
            nombre_comparacion=parte[0] #Siempre seran paises
            lista_paises_temp+=[nombre_comparacion] #Guardamos en una lista temporal los nombres de los paises
        for elemento in lista_paises_temp: #por cada elemento dentro de esta lista
            if pais in elemento: #si la string en pais, esta dentro (o parcialmente dentro) de elemento (otra string) 
                return elemento  #Entonces se regresa la coincidencia mas cercana.

def cambiar_poblacion(pais,nueva_poblacion):#funcion que cambia la poblacion de x pais en base.csv
    filas=[] #aqui guardaremos todo el archivo, aprovechando que no es muy grande
    #Reader
    with open("base.csv","r",newline="") as base: #investigando la funcion, se pueden colocar newline, que por cada linea pone el string asignado. aqui se utiliza para no aceptar input en blanco
        lector=csv.reader(base) #gracias al modulo, podemos usar al reader, el cual interpreta cada linea y la puede convertir en una lista, ahorrandonos bastante tiempo.
        encabezado=next(lector) #le decimos al lector que tome la primer linea, que seria nuestro encabezado y la guarde en tal variable.
        for fila in lector: #el lector a partir de aqui toma todo el archivo empezando por la linea despues del encabezado
            if fila[0]==pais: #si el indice 0 (paises) de esa fila listada es el pais que se introdujo, entra 
                fila[1]=nueva_poblacion #entonces indice 1 (poblacion) de esa fila es remplazada por la string nueva_poblacion, es decir, la cambiada
            filas.append(fila) #aprovechamos el bucle y vamos poniendo toda fila en la lista filas, para luego usarla.
    #Writer
    with open("base.csv","w",newline="") as base: #es cierto que el algoritmo principal con la cantidad de filtros de validacion, no necesita de newline, aunque implementarlo no hace ningun mal.
        escritor=csv.writer(base) #el objeto writer escribe las listas de las lineas a propiamente, lineas csv
        escritor.writerow(encabezado) #writerow escribe una sola linea, especificamos que sea la lista que guardamos en encabezado
        escritor.writerows(filas) #writerows (notese la s) escribe varias lineas. Al llamar la lista filas, que tiene todo el archivo a partir del siguiente del encabezado, el writer se encarga de escribir los elementos de la lista en el formato csv
    #Salida
    print(f"Poblacion de {pais} actualizada correctamente a {nueva_poblacion}.\n") #lo unico que ve el usuario

def cambiar_superficie(pais,nueva_superficie):#funcion que cambia la superficie de x pais en base.csv
    filas=[] #aqui guardaremos todo el archivo, aprovechando que no es muy grande
    #Reader
    with open("base.csv","r",newline="") as base: 
        lector=csv.reader(base) #gracias al modulo, podemos usar al reader, el cual interpreta cada linea y la puede convertir en una lista, ahorrandonos bastante tiempo.
        encabezado=next(lector) #le decimos al lector que tome la primer linea, que seria nuestro encabezado y la guarde en tal variable.
        for fila in lector: #el lector a partir de aqui toma todo el archivo empezando por la linea despues del encabezado
            if fila[0]==pais: #si el indice 0 (paises) de esa fila listada es el pais que se introdujo, entra 
                fila[2]=nueva_superficie #entonces indice 2 (superficie) de esa fila es remplazada por la string nueva_superficie, es decir, la cambiada
            filas.append(fila) #aprovechamos el bucle y vamos poniendo toda fila en la lista filas, para luego usarla.
    #Writer
    with open("base.csv","w",newline="") as base:
        escritor=csv.writer(base) #el objeto writer escribe las listas de las lineas a propiamente, lineas csv
        escritor.writerow(encabezado) #writerow escribe una sola linea, especificamos que sea la lista que guardamos en encabezado
        escritor.writerows(filas) #writerows (notese la s) escribe varias lineas. Al llamar la lista filas, que tiene todo el archivo a partir del siguiente del encabezado, el writer se encarga de escribir los elementos de la lista en el formato csv
    #Salida
    print(f"La superficie de {pais} actualizada correctamente a {nueva_superficie} km².\n") #lo unico que ve el usuario

def filtrar_por_rango_poblacion(rango_min,rango_max):#funcion que busca todos los paises dentro de un rango dado de poblacion
    #Reader
    with open("base.csv","r",newline="") as base: 
        lector=csv.reader(base) #gracias al modulo, podemos usar al reader, el cual interpreta cada linea y la puede convertir en una lista, ahorrandonos bastante tiempo.
        next(lector) #salteamos el encabezado
        print()
        for fila in lector: #el lector a partir de aqui toma todo el archivo empezando por la linea despues del encabezado
            if rango_min<=int(fila[1])<=rango_max: #si la poblacion esta entre el rango minimo y el maximo que se introdujo (vease que se transforma en int)
                existe=True #si almenos se entra una vez, se activa existe
                print(f"{fila[0]} tiene {fila[1]} habitantes\n")
        if existe==False: #solo puede dar false si nunca hubieron coincidencias
            print("No se encontraron resultados dentro del rango dado.")

def filtrar_por_rango_superficie(rango_min,rango_max):#funcion que busca todos los paises dentro de un rango dado de superficie
    #Reader
    with open("base.csv","r",newline="") as base: 
        lector=csv.reader(base) #gracias al modulo, podemos usar al reader, el cual interpreta cada linea y la puede convertir en una lista, ahorrandonos bastante tiempo.
        next(lector) #salteamos el encabezado
        print()
        for fila in lector: #el lector a partir de aqui toma todo el archivo empezando por la linea despues del encabezado
            if rango_min<=int(fila[2])<=rango_max: #si la superficie esta entre el rango minimo y el maximo que se introdujo (vease que se transforma en int)
                existe=True
                print(f"{fila[0]} abarca {fila[2]} km²\n")
        if existe==False:
            print("No se encontraron resultados dentro del rango.")

def filtrar_por_continente(continente): #funcion que busca todos los paises que sean de dado continente
    #Reader
    with open("base.csv","r",newline="") as base: 
        lector=csv.reader(base) #gracias al modulo, podemos usar al reader, el cual interpreta cada linea y la puede convertir en una lista, ahorrandonos bastante tiempo.
        next(lector) #salteamos el encabezado
        print()
        coincidencias_continente=[] #luego la usaremos para guardar o no las coincidencias
        for fila in lector: #el lector a partir de aqui toma todo el archivo empezando por la linea despues del encabezado
            if continente==fila[3]: #si el input coincide con el continente de la fila (indice 3)
                coincidencias_continente.append(fila[0]) #se agrega a la lista anterior el pais de esa fila (indice 0)
        if coincidencias_continente: #si la lista no esta vacia
            print(f"Los siguientes paises forman parte de {continente}:")
            for elemento in coincidencias_continente:
                print(elemento)
            print()
        else:
            print(f"No se encontraron paises registrados que se ubiquen en {continente}.\n")

def ordenar_paises(criterio_orden:str,modo:bool): #funcion que basada en un criterio de orden y un bool que marca si asciende o desciende, se muestra la lista de base.csv
    #Reader
    existe=False #para verificar que se logró, sirve luego
    with open("base.csv","r",newline="") as base: 
        lector=csv.reader(base) #gracias al modulo, podemos usar al reader, el cual interpreta cada linea y la puede convertir en una lista, ahorrandonos bastante tiempo.
        encabezado=next(lector) #salteamos el encabezado
        print()
        filas=list(lector) #tomamos todo el archivo luego del encabezado y queda en una lista

        if criterio_orden=="pais":
            existe=True #para dar el visto bueno a que se haga el sort
            indice=0 #la primer columna
            funcion_key= lambda fila: fila[indice] #variable llamada asi pues va a ser la key del .sort que usaremos luego
        elif criterio_orden=="poblacion": #usamos lambda, que sirve para crear funciones rapidas, utiles para situaciones como esta donde hay que poner pequeñas funciones de orden (funcion_key para el sort)
            existe=True
            indice=1 #la segunda 
            funcion_key= lambda fila: int(fila[indice]) #forzamos int para poder comparar
        elif criterio_orden=="superficie":
            existe=True
            indice=2 #la tercer columna
            funcion_key= lambda fila: int(fila[indice]) #la sintaxis es... lambda parametro: expresion
        #nuestro parametro es fila y su expresion la fila con su respectivo indice del criterio
        if existe: #si entro en el sistema y se logro reunir los recursos para la lista
            filas.sort(key=funcion_key, reverse=modo) #.sort ordena con la key de la funcion_key, con el reverse
            return [encabezado]+filas #el encabezado primero que se le suman a las filas

def mostrar_estadisticas():#Funcion que consigue sacar promedios de superficie, mayor y menores poblaciones y cantidad de paises registrado en ciertos continentes, sacando info de base.csv
    with open("base.csv","r") as archivo:
    #Reader
        lector=csv.reader(archivo)
        next(lector)#se salta el encabezado
        paises=[]

        for fila in lector:
            pais=fila[0]
            poblacion=int(fila[1]) #poblacion y superficie deben ser int
            superficie=int(fila[2])
            continente=fila[3]
            paises.append((pais, poblacion, superficie, continente))

    #bloque de estadistica, utilizamos lambda para hacer una funcion rapida
    pais_mayor_pob=max(paises, key=lambda x: x[1]) #sacamos el mayor
    pais_menor_pob=min(paises, key=lambda x: x[1]) #sacamos el menor

    promedio_poblacion = sum(p[1] for p in paises) / len(paises)
    promedio_superficie = sum(p[2] for p in paises) / len(paises)

    #cantidad continente
    continentes={} #aqui hacemos un diccionario, donde la key seria el nombre del continente
    for elemento in paises: #cada elemento en paises, que es una lista con toda la info de ese pais
        cont=elemento[3] #la el tercer indice siempre es el continente
        continentes[cont] = continentes.get(cont, 0)+1
    #Printeo de las estadisticas
    print("\nEstadisticas:\n")
    print(f"País con mayor población: {pais_mayor_pob[0]} ({pais_mayor_pob[1]})")
    print(f"País con menor población: {pais_menor_pob[0]} ({pais_menor_pob[1]})")
    print(f"\nPromedio de población: {promedio_poblacion}")
    print(f"Promedio de superficie: {promedio_superficie}")
    print("\nPaises por continente:")
    for cont, cant in continentes.items(): #al ser un diccionario, usamos dos iteradores, cont (la key, el nombre del continente)
        print(f"- {cont}:{cant}")          #y cant, cantidad (la value de ese continente)
    print()

#### Comienza el algoritmo en si ######

lista_continente=["America","Antartida","Asia","Africa","Europa","Oceania"]

print("\n-------------------------------------") #Mensaje inicial, solo aparece al iniciar el algoritmo
print("**Administrador de datos de Países**\n")
print("Este algoritmo permite el manejo de datos en relacion a los paises")
print("Se utiliza como encabezado el nombre del pais, su poblacion, su superficie en km² y el continente en el que se ubica.")
print("-------------------------------------\n")

while True: #Bucle while principal, solo se sale de el al tomar la opcion 9- Salir.

    #Funciones que iteran al inicio del bucle
    lista_paises=verificar_paises() #actualiza la lista de elementos con base.csv. sirve para verificar si un objeto esta en la base.
    mostrar_menu() #Muestra el menú

    opcion_listado=input(">> ").strip() #Input que lo sobrelleva el try.
    print()

    try: #Verificacion con try, intenta entrar en la estructura match
        match int(opcion_listado): #como el .strip() hace la variable una string, aqui la cambiamos a int
    
            case 1: #1- Agregar un pais

                pais_valor=input("Introduce el nombre del país: ").strip().capitalize() #gracias a capitalize, siempre sera asi
                print()

                if pais_valor.isalpha(): #Validacion Pais si es string
                    if pais_valor not in lista_paises: #Validacion Pais si esta ya en base.csv usando la lista creada con la funcion

                        poblacion_valor=input(f"Introduce la cantidad de habitantes de {pais_valor}: ").strip()
                        print()
                        if poblacion_valor.isnumeric() and int(poblacion_valor)>0: #al igual que con superficie_valor, ya con que pase el primer filtro, el segundo no va a dar error

                            superficie_valor=input(f"Introduce la superficie que abarca {pais_valor} en km²: ").strip()
                            print()
                            if superficie_valor.isnumeric() and int(superficie_valor)>0:
                            
                                print(f"Introduce el nombre del continente (sin tildes) en donde se ubica {pais_valor}.\n-\nLos continentes posibles son: America, Antartida, Asia, Africa, Europa, OceanIa\n-")
                                continente_valor=input(f"Tu elección: ").strip().capitalize()
                                print()
                                if continente_valor.isalpha() and continente_valor in lista_continente: #Se verifica en la lista de continentes, asi no inventa
                                    agregar_pais_a_base(pais_valor,poblacion_valor,superficie_valor,continente_valor) #Se llama la funcion que se encarga del proceso
                                    time.sleep(5)

                                else:
                                    print("Nombre de continente no valido.")
                                    time.sleep(5)
                            else:
                                print("Solo puedes colocar un valor numerico positivo y entero para la superficie del territorio")
                                time.sleep(5)
                        else:
                            print("Solo puedes colocar un valor numerico positivo y entero para la poblacion.")
                            time.sleep(5)
                    else:
                        print("Ya has registrado ese país.")
                        time.sleep(5)
                else:
                    print("Nombre de pais no valido.")
                    time.sleep(5)

            case 2:#2- Actualizar los datos de la poblacion de un país
                pais=input("Introduce el nombre del país que quieres cambiar: ").strip().capitalize()
                if pais.isalpha(): #si es alfabetica
                    if pais in lista_paises: #si esta en la lista de paises actualizada
                        poblacion=encontrar_poblacion(pais) #usamos la funcion especifica para este caso.
                        print(f"{pais} tiene {poblacion} habitantes")
                        nueva_poblacion=input("Introduce el nuevo numero de habitantes para cambiar el archivo\n>> ").strip()
                        if nueva_poblacion.isnumeric() and int(nueva_poblacion)>=0: #tiene que ser positivo
                            cambiar_poblacion(pais,nueva_poblacion)
                            time.sleep(5)
                        elif nueva_poblacion.isnumeric() and int(nueva_poblacion)==int(poblacion): #si son iguales
                            print(f"{pais} ya tiene registrada esa cantidad de habitantes.")
                            time.sleep(5)
                        else:
                            print("Solo puedes colocar un numero entero y positivo.")
                            time.sleep(5)
                    else:
                        print(f"{pais} no esta registrado.") #no esta en la lista
                        time.sleep(5)
                else:
                    print("Debes introducir un nombre valido.")
                    time.sleep(5)

            case 3:#3- Actualizar los datos de la superficie de un país
                pais=input("Introduce el nombre del país que quieres cambiar: ").strip().capitalize()
                if pais.isalpha():
                    if pais in lista_paises:
                        superficie=encontrar_superficie(pais) #llamamos a la funcion que se encarga de buscar la superficie
                        print(f"{pais} abarca {superficie} km²")
                        nueva_superficie=input("Introduce el numero de km² para cambiar el archivo\n>> ").strip()
                        if nueva_superficie.isnumeric() and int(nueva_superficie)>=0: #tiene que ser positivo
                            cambiar_superficie(pais,nueva_superficie)
                            time.sleep(5)
                        elif nueva_superficie.isnumeric() and int(nueva_superficie)==int(superficie): #si son iguales
                            print(f"{pais} ya tiene registrada esa cantidad de km².")
                            time.sleep(5)
                        else:
                            print("Solo puedes colocar un numero entero y positivo.")
                            time.sleep(5)
                    else:
                        print(f"{pais} no esta registrado.")
                        time.sleep(5)
                else:
                    print("Debes introducir un nombre valido.")
                    time.sleep(5)
            
            case 4:#4- Buscar un país por nombre
                pais=input("Introduce el nombre del país que quieres buscar: ").strip().capitalize()
                if pais.isalpha()==True:
                    if encontrar_nombre_pais_bool(pais): #Si hay una cierta coincidencia, esta funcion la toma y el programa prosigue con la coincidencia
                        pais=encontrar_nombre_pais_string(pais) #remplazamos el valor de pais por el de la coincidencia
                        poblacion=encontrar_poblacion(pais) #sacamos poblacion de la coincidencia
                        superficie=encontrar_superficie(pais) #= con superficie
                        continente=encontrar_continente(pais) #= con continente
                        print(f"{pais} tiene {poblacion} habitantes, abarca {superficie} y se ubica en {continente}")
                        time.sleep(5)
                    else:
                        print(f"{pais} no esta registrado.")
                        time.sleep(5)
                else:
                    print("Debes introducir un nombre valido.")
                    time.sleep(5)

            case 5:#5- Filtrar Paises
                filtro=input("Introduce cual tipo de dato quieres usar para filtrar los paises.\n(Poblacion, Territorio o Continente)\n>>  ").strip().lower() #lower para que quede todo igual
                if filtro=="poblacion":
                    rango_min=input("Introduce el numero de poblacion para buscar entre los paises: ").strip()
                    if rango_min.isnumeric and int(rango_min)>=0:
                        rango_min=int(rango_min)
                        rango_max=input("Introduce el rango maximo de km² para buscar entre los paises: ").strip()
                        if rango_max.isnumeric and rango_min<int(rango_max)>=0:
                            rango_max=int(rango_max)
                            filtrar_por_rango_poblacion(rango_min,rango_max)
                            time.sleep(5)
                        else:
                            print("Solo puedes introducir un numero entero positivo por encima del rango minimo.")
                            time.sleep(5)
                    else:
                        print("Solo puedes introducir un numero entero positivo.")
                        time.sleep(5)
                    
                elif filtro=="territorio":
                    rango_min=input("Introduce el rango minimo de km² para buscar entre los paises: ").strip()
                    if rango_min.isnumeric and int(rango_min)>=0:
                        rango_min=int(rango_min)
                        rango_max=input("Introduce el rango maximo de km² para buscar entre los paises: ").strip()
                        if rango_max.isnumeric and rango_min<int(rango_max)>=0:
                            rango_max=int(rango_max)
                            filtrar_por_rango_superficie(rango_min,rango_max)
                            time.sleep(5)
                        else:
                            print("Solo puedes introducir un numero entero positivo por encima del rango minimo.")
                            time.sleep(5)
                    else:
                        print("Solo puedes introducir un numero entero positivo.")
                        time.sleep(5)
            
                elif filtro=="continente":
                    continente=input("Introduce el nombre del continente (sin tildes): ").strip().capitalize()
                    if continente in lista_continente:
                        filtrar_por_continente(continente)
                        time.sleep(5)
                    else:
                        print("No se encontró ese continente.")
                        time.sleep(5)
                else:
                    print("Solo puedes seleccionar entre los datos de poblacion, territorio o continente")
                    time.sleep(5)

            case 6:#6- Ordenar paises por parametro
                criterio_orden=str(input("Introduce el nombre del criterio por el que quieres ordenar (Pais, poblacion o superficie): ")).strip().lower()
                if criterio_orden.isalpha():
                    opcion_modo=input("Elije entre que se presenten los datos de manera ascendente (1) o descendente (2): ").strip()
                    if opcion_modo=="1":
                        modo=True #ascendente
                        resultado_orden=ordenar_paises(criterio_orden,modo)#una lista con la tabla en listas ordenadas con ese criterio
                        if resultado_orden: #si la lista tiene elementos, o sea, si la funcion actuo
                            for fila in resultado_orden:
                                print(fila)
                            time.sleep(5)
                        else: #Si el usuario puso un input inesperado
                            print("Solo se puede seleccionar un criterio de orden valido.\n")
                            time.sleep(5)
                    elif opcion_modo=="2":
                        modo=False #descendente
                        resultado_orden=ordenar_paises(criterio_orden,modo)#una lista con la tabla en listas ordenadas con ese criterio
                        time.sleep(5)
                        if resultado_orden: #si la lista tiene elementos, o sea, si la funcion actuo
                            for fila in resultado_orden:
                                print(fila)
                            time.sleep(5)
                        else: #Si el usuario puso un input inesperado
                            print("Solo se puede seleccionar un criterio de orden valido.\n")
                            time.sleep(5)
                    else:
                        print("Solo puedes introducir 1 o 2.")
                        time.sleep(5)
                else:
                    print("Solo puedes introducir los criterios presentados.")
                    time.sleep(5)
    
            case 7:#7- Mostrar estadisticas
                mostrar_estadisticas()
                time.sleep(5)

            case 8: #8- Salir
                print("*******************\nFinalizando programa...\n*******************")
                break #Rompe el bucle
        
            case _: #Comodin si se pone otro numero
                print("*Error: Debes colocar un numero entre los que estan en la lista (del 1 al 8).\n")
                time.sleep(5)

    except TypeError: #TypeError abarca los errores que sobresalen a las capacidades de un tipo de objeto.
        print("Solo puedes introducir un valor numerico entero")
        time.sleep(5)