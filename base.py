import funciones as fn 

while True:
    print("1. Registrar Pedido.")
    print("2. Listar todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa")

    opc = int(input("Ingrese una opción: "))

    if opc == 1:
        fn.registrar_pedido()
    elif opc == 2:
        fn.listar_pedidos()
    elif opc == 3: 
        fn.imprimirhojaderuta()
    elif opc == 4:
        print("Adios!.")
        break
