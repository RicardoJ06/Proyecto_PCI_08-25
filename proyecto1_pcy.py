#Aqui se ira haciendo el desarrollo para el proyecto para mejorar un negocio ovinocultor



#ALGORITMO

#ENTRADAS:

# Iniciamos las listas para guardar borregas
ovejas = []          # Lista principal para guardar datos de cada borrega
ganancias = []       # Lista para registrar las ganancias de cada borrega

c = ("Si")

while c == "Si":
    # 1. - Solicitar datos al usuario
    print("Sistema de gestión de fertilidad ovina")
    print("Por favor, ingrese los siguientes datos")

    # 1.1 - Datos de la oveja
    nombre_oveja = input("Arete oveja: ")
    edad_oveja = int(input("Edad de la oveja (años): "))

    # 1.2 - Datos reproductivos
    crías_por_parto = int(input("Número de corderos por parto: "))
    partos_por_año = int(input("Partos por cada 2 años: "))
    supervivencia_de_corderos = int(input("Cuantas crías sobreviven por parto(UN PORCENTAJE): "))
    años_producción = int(input("Años para producir a calcular (numero par): "))

    # 1.3 - Datos económicos
    costo_oveja = float(input("Costo oveja: "))
    costo_crianza = float(input("Costo crianza corderos: "))
    precio_venta = float(input("Precio de venta por cordero: "))

    # 2. - Resultados de análisis
    print("Resultados de análisis")

    # 2.1 - Calcular producción total
    total_partos = partos_por_año * años_producción
    total_crías = total_partos * crías_por_parto

    # 2.2 - Calcular costos e ingresos
    costos_totales = total_crías * costo_crianza
    ingresos_totales = total_crías * precio_venta
    ganancia_neta = ingresos_totales - costos_totales

    # 3. - Mostrar Resultados
    print(f"Oveja: {nombre_oveja} Edad: {edad_oveja} años")
    print(f"Producción analizando: {años_producción} años")
    print(f"Partos Totales en el tiempo: {total_partos}")
    print(f"Crias Totales producidas: {total_crías}")
    print("---")
    print(f"Inversión Total en crianza: $ {costos_totales:.2f}")
    print(f"Ingresos por venta: $ {ingresos_totales:.2f}")
    print(f"Ganancia NETA: $ {ganancia_neta:.2f}")
    print("---")

    # 4. - Evaluar Rentabilidad
    if ganancia_neta > 0:
        print("NEGOCIO RENTABLE - RECOMENDADO")
    elif ganancia_neta == 0:
        print("NEGOCIO EQUILIBRADO - SIN GANANCIAS NI PÉRDIDAS")
    else:
        print("NEGOCIO NO RENTABLE - REVISAR CALCULOS")

    # 5. - CALCULOS
    total_crias = total_partos * crías_por_parto
    costos_totales_cria = total_crias * costo_crianza
    print(f"Crías totales ({total_crias}) * Costo/cría ($ {costo_crianza}) = $ {costos_totales_cria:,.2f} en crianza")

    ingresos_totales = total_crias * precio_venta
    print(f"Crías totales ({total_crias}) * Precio venta ($ {precio_venta}) = $ {ingresos_totales:,.2f} ingresos totales")

    crias_logradas = int((supervivencia_de_corderos / 100) * total_crías)
    print(f"De {total_crías} crías totales, sobreviven {crias_logradas} crías ({supervivencia_de_corderos} % ) ")

    # 6. - FUNCIONES
    def pedir_datos_oveja():
        nombre = input("Arete oveja: ")
        edad = int(input("Edad de la oveja (años): "))
        return nombre, edad

    def pedir_datos_reproductivos():
        crías_por_parto = int(input("Numero de corderos por parto: "))
        partos_por_año = int(input("Partos por año: "))
        años_producción = int(input("Años para producir: "))
        return crías_por_parto, partos_por_año, años_producción

    def pedir_datos_economicos():
        costo_oveja = float(input("Costo oveja: "))
        costo_cria = float(input("Costo crianza corderos: "))
        precio_venta = float(input("Precio de ventas por cordero: "))
        return costo_oveja, costo_cria, precio_venta

    def calcular_produccion(partos_por_año, años, crias_por_parto):
        total_partos = partos_por_año * años
        total_crias = total_partos * crias_por_parto
        return total_partos, total_crias

    def calcular_economia(total_crias, costo_cria, precio_venta):
        costos = total_crias * costo_cria
        ingresos = total_crias * precio_venta
        ganancia = ingresos - costos
        return costos, ingresos, ganancia

    def mostrar_resultados(nombre, edad, años, total_partos, total_crias, costos, ingresos, ganancia):
        print("--- RESULTADOS DEL ANÁLISIS ---")
        print(f"Oveja: {nombre}, edad: {edad} años")
        print(f"Partos totales: {total_partos}")
        print(f"Crías totales: {total_crias}")
        print(f"Inversión total de crianza: ${costos:.2f}")
        print(f"Ingresos totales por venta: ${ingresos:.2f}")
        print(f"Ganancia total: ${ganancia:.2f}")

    # 7. - ESTRUCTURAS DE DECISIÓN BÁSICAS
    #Si es rentable o no:
        if ganancia > 0:
            print("NEGOCIO RENTABLE - MUY BUENO")
        elif ganancia == 0:
            print("Negocio Sin Ganancias - Ni pérdidas")
        else:
            print("NEGOCIO NO RENTABLE - REVISAR")

    #Evaluar si es joven o adulta la borrega:
    if edad_oveja < 1:
        print("La oveja todavia no se puede reproducir(menor a 1 año) ")
    elif edad_oveja < 3:
        print("La oveja es JOVEN(menor a 3 años) ")
    elif edad_oveja <= 6:
        print("La oveja es ADULTA(entre 3 y 6 años) ")
    else:
        print("La oveja ya esta VIEJA(más de 6 años) ")

    #Verificar si la producción de crías es buena
    if total_crías >= 14:
        print("La producción de crías es ALTA ")
    elif total_crías >= 8:
        print("La producción de crías es REGULAR ")
    else:
        print("La producción de crías es BAJA ")

    #Evaluar la edad de la oveja junto con su producción
    if edad_oveja <= 5:
        if total_crías >= 10:
            print("La oveja es joven y muy productiva ")
        else:
            print("La oveja es jovena pero poco productiva ")
    else:
        if total_crías >= 10:
            print("La oveja es vieja pero todavía produce buenas crías ")
        else:
            print("La oveja es vieja y no produce casi nada ")

    # Evaluamos la calidad de la producción por borrega
    if supervivencia_de_corderos >= 90:
        print("LA CALIDAD ES EXCELENTE - La mayoría de las crías sobreviven.")
    elif supervivencia_de_corderos >= 70:
        print("LA CALIDAD ES BUENA - Buen número de crías sobreviven.")
    elif supervivencia_de_corderos >= 50:
        print("LA CALIDAD ES REGULAR - La mitad de las crías sobreviven.")
    else:
        print("LA CALIDAD ES MUY MALA - Muy pocas crías sobreviven.")



    c = str(input("Desea continuar con la siguiente borrega? (Si / No): "))

    print(f"Lista de ovejas registradas hasta ahora: {ovejas}")

    # 8. - Guardar en listas
    ovejas.append(nombre_oveja)       # Sirve para guardar el nombre en la lista
    ganancias.append(ganancia_neta)   # Sirve para guardar la ganancia en la otra lista

    # Ahora damos la opción al usuario para revisar las borregas registradas
    op = "Si"
    while op == "Si":
        print("\n--- RESUMEN DE OVEJAS REGISTRADAS ---")
        for i in range(len(ovejas)):
            print(f"{i+1} Oveja: {ovejas[i]} | Ganancia neta: ${ganancias[i]:.2f}")
        op = input("¿Desea volver a ver el resumen? (Si / No): ")

