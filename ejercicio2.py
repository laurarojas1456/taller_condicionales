#
ingresos = float(input("Ingrese sus ingresos mensuales: "))

    
    # Verificación de los requisitos
if ingresos > 945200:
    deudas = float(input("Ingrese el total de sus deudas pendientes: "))
    if deudas==0:
        print("Su préstamo ha sido aprobado ")
    else:
            print("Lo sentimos, no cumple con los requisitos para obtener un préstamo.")

else:
    print("Lo sentimos, no cumple con los requisitos para obtener un préstamo.")
