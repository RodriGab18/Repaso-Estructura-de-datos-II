import os 

detenerse = False

while detenerse == False:
    os.system("cls")
    print("Ingrese la opción que requiera.")
    print("1. Ingresar número.")
    print("2. Salir.")
    opcion = int(input("Opción: "))

    if opcion == 1:
        os.system("cls")
        print("Ingrese el número a convertir.")
        numeroAConvertir = int(input("Número: "))


        input("Presione cualquier tecla para continuar.")

    elif opcion == 2: 
        print("Rodrigo Gabriel Pérez Vásquez, 1576224.")

    else: 
        print("Ingrese una opción válida.")