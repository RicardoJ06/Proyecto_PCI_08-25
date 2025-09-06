#Aqui se ira haciendo el desarrollo para el proyecto para mejorar un negocio ovinocultor

"""

#ALGORITMO

ENTRADAS:
    1. - Solicitar datos al usuario
        print("sistema de gestión de fertilidad ovina")
        print("por favor, ingrese los siguientes datos")
             1.1 - Datos de la oveja
                   nombre_oveja = input("arete oveja")
                   edad_oveja = int(input("edad de la oveja (años): "))
             1.2 - Datos reproductivos
                   crías_por_parto = int(input("número de corderos por parto: "))
                   partos_por_año =  int(input("partos por año: "))
                   años_para_producir = int(input("años para producir a calcular: "))
             1.3 - Datos económicos
                   costo_oveja = float(input("Costo oveja: "))
                   costo_crianza = float(input("Costo crianza corderos: "))
                   precio_venta = float(input("Precio de venta por cordero: "))
    
    2. -Resultados de análisis
        print("Resultados de análisis")
             2.1 -Calcular producción total
                  total_partos = partos_por_año *
                  años_producción
                  total_crías = total_partos *
                  crías_por_parto
             2.2 - Calcular costos e ingresos
                  costos_totales = total_crías *
                  costo_crianza
                  ingresos_totales = total_crías *
                  precio_venta
                  ganancia_neta = ingresos_totales - costos_totales

    3. -Mostrar Resultados
        print(f"Oveja: {nombre_oveja}) (Edad: {edad_oveja} años)")
        print(f"Producción analizando: {años_produccion} años")
        print(f"Partos Totales en el tiempo: {total_partos} años")
        print(f"Crias  Totales producidas: {total_crias}")
        print("---")
        print(f"Inversión Total en crianza: $ {costos_totales: .2f}")
        print(f"Ingresos por venta: $ {ingresos_totales: .2f}")
        print(f"Ganaancia NETA: $ {ganancia_neta: .2f}")
        print("---")
    
    4. -Evaluar Rentabilidad
        if ganancia_neta > 0:
           print(" NEGOCIO RENTABLE - RECOMENDADO")
        elif ganancia_neta == 0:
           print(" NEGOCIO EQUILIBRADO - SIN GANANCIAS NI PÉRDIDAS")
        else:
           print("NEGOCIO NO RENTABLE - REVISAR CALCULOS")

    5. -CALCULOS
        total_crias = total_partos * crías_por_parto
        print(f"Crías totales ({total_crias}) * Costo/cría ($ {costo_cria}) = $
        {costos_totales_cria:,.2f} en crianza")

        ingresos_totales = total_crias * precio_venta
        print(f"crias totales ({total_crias}) * Precio venta ($ {precio_venta}) = $
        {ingresos_totales:,.2f} ingresos totales")

    6. -FUNCIONES
        def pedir_datos_oveja():
            nombre = input("Arete oveja: ")
            edad = int(input("Edad de la oveja (años): "))
            return nombre, edad

        def pedir_datos_reproductivos():
            crías_por_parto = input("Numero de corderos por parto: ")
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

        def calcular_economia (total_crias, costo_cria, precio_venta)
            costos = total_crias * costo_cria
            ingresos = total_crias * precio_venta
            ganancia = ingresos - costos
            return costos, ingresos, ganancias

        def mostrar_resultados (nombre, edad, años, total_partos, total_de_crias, costos, ingresos, ganancias)
            print(" --- RESULTADOS_DEL_ ANALISIS --- ")
            print(f"oveja: {nombre}, edad: {edad} años")
            print(f"partos totales: {total_partos}")
            print(f"crias totales: {total_crias}")
            print(f"Inversion total de crianza: ${costos: .2f}")
            print(f"Ingresos totales por venta: ${ingresos: .2f}")
            print(f"Ganacia total: ${ganancia: .2f}")

            if ganancia > 0:
               print(" NEGOCIO RENTABLE - MUY BUENO ")
            elif ganancia == 0:
               print(" Negocio Sin Ganancias - Ni perdidas ")
            else:
               print(" NEGOCIO NO RENTABLE - REVISAR ")



"""