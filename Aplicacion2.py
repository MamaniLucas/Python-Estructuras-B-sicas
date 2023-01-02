#2.	Elabore un programa que calcule e imprima el pago de 5
#trabajadores que laboran en la empresa.
#Los datos que se leerán serán los siguientes: Apellidos,
# Nombres, Las horas trabajadas, El sueldo por hora, El tipo 
# de trabajador(A.-obrero. B - empleado).
#Para calcular los pagos considerar lo siguiente:
#-	Los obreros pagan 10 % de impuesto
#-	Los empleados pagan 12 % de impuesto.
#-	Los trabajadores(obreros y empleados) que reciban un pago 
# menor de 1000 soles no pagan impuesto.
#-	Al final se deberá imprimir el total a pagar a los obreros 
# y a los empleados, así como el número de empleados por tipo
#Todo el proceso estará en un archivo Libreria.py y el menú en
#un archivo Aplicacion2.py
#a.	Registro
#b.	Reporte
#c.	Salir

#Paso 1. crear el menu
while True:
    print("Escoja una opción del menu:")
    print("1. Registro")
    print("2. Reporte")
    print("3. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        print("***** Registrar números *****")
        a = int(input("Ingrese el valor de a: "))
        b = int(input("Ingrese el valor de b: "))
        c = int(input("Ingrese el valor de c: "))
        print("************************")

    if opcion == "2":
        print("***** IMPRIMIR RAÍCES *****")
        raices = Libreria.calcular_raices(a, b, c)
        print("Las raíces son: ", raices)
        print("************************")

    if opcion == "3":
        print("***** GUARDANDO ARCHIVO *****")
        Libreria.guardar_archivo(raices)
        print("************************")

    if opcion == "4":
        print("***** LEER ARCHIVO *****")
        Libreria.leer_archivo()
        print("************************")

    if opcion == "5":
        print("Saliendo...")
        break
    
