#Aqui se ira haciendo el desarrollo para el proyecto para mejorar un negocio ovinocultor

"""
ALGORITMO

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

    3 - Mostrar Resultados
    ...


"""