#14, 15, 16 están ocupados. 
#asientos.remove(ubicacion)
#asientos.insert(ubicacion-1, "x")
#if ubicacion >= 1 and ubicacion <= 100:
funcion = []
asientos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
compra = {'rut': '198000892', 'ubicacion': '14' '15' '16' '45'}
listado_rut = [198000892]

def ganancias_totales():
    contador_platinum = 0
    contador_gold = 0
    contador_silver = 0
    print("estas son las ganancias totales")
    for asientos in asientos(1, 21):
        if asientos == "x":
            contador_platinum +=1
    for asientos in asientos(21,51):
        if asientos == "x":
            contador_gold +=1
    for asientos in asientos(51,101):
        if asientos == "x":
            contador_silver +=1
    tot_ganancias = contador_platinum*120000+contador_gold*80000+contador_silver*50000
    return(print(tot_ganancias))

def ubicaciones():
    asientos.remove(14)
    asientos.remove(15)
    asientos.remove(16)
    asientos.remove(45)
    asientos.insert(13,"x")
    asientos.insert(14,"x")
    asientos.insert(15,"x")
    asientos.insert(44,"x")
ubicaciones()

def salida():
    input("VUELVA PRONTO\nFABIAN ESTEBAN MELLA BARRA\nFECHA 10/07/2023\nPRESIONE ENTER PARA TERMINAR\n".center(50, "="))

def comprar_entradas():
    while True:
        try:
            cantidad_entradas = int(input("¿Cuántas entradas desea comprar?\n"))
            if cantidad_entradas >= 1 and cantidad_entradas <= 3:
                print(f"Bienvenido, comprarás {cantidad_entradas} Entradas\n")
                print(asientos)
                rut_compra = int (input("Ingresa tu RUT: "))
                compra ['rut'] = rut_compra
                listado_rut.append(rut_compra)
                while True:
                    try:
                        for i in range(cantidad_entradas):
                            ubicacion = int (input("Escoge una ubicación\n"))
                            if ubicacion >= 1 and ubicacion <= 100:
                                asientos.remove(ubicacion)
                                asientos.insert(ubicacion-1, "x")
                                compra ['ubicacion'] = ubicacion
                                funcion.append(compra)
                                print(f"Tu entrada {cantidad_entradas} ha sido comprada correctamente\n")
                                print(f"{asientos}")
                                input("Presione ENTER para continuar...")
                                #print(f"{compra ['rut']}")
                                #print(f"{compra ['ubicacion']}")
                                cantidad_entradas -= 1
                            else:
                                print("INGRESA SOLO NÚMEROS ENTROS POSITIVOS MENORES O IGUALES A 100 Y/O MAYORES O IGUALES A 1")
                        break
                    except:
                        print("INGRESA SOLO CARÁCTERES PERMITIDOS")
            else:
                print("INGRESA SOLO NÚMEROS ENTEROS POSITIVOS MENORES O IGUALES A 3 Y/O MAYORES O IGUALES A 1")
        except:
            print("INGRESA SOLO CARÁCTERES PERMITIDOS")
        break
    menu()


def mostrar_ubicaciones_disponibles():
    input("Presiona ENTER para mostrar todas las ubicaciones disponibles:\n")
    print(asientos)
    menu()

def listado_asistentes():
    listado_rut.sort()
    print(f"{listado_rut}".center(20, "+"))
    #print(f"La cantidad de asistentes es: {int(len(compra['ubicacion'])/2)}")


def menu():
    print("MENU CREATIVOS.CL".center(50,"-"))
    print(f"1. Comprar entradas\n2. Mostrar ubicaciones disponibles\n3. Ver listado de asistencias\n4. Mostrar Ganancias totales\n5. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        comprar_entradas()
    elif opcion == 2:
        mostrar_ubicaciones_disponibles()
    elif opcion == 3:
        listado_asistentes()
    elif opcion == 4:
        ganancias_totales()
    elif opcion == 5:
        salida()
menu()