pedidos = []
tamanopaquete = ['Pequeño', 'Mediano', 'Grande']
pedidosnorte = []
pedidoscentro = []
pedidossur = []

def registrar_pedido(): 
    Nombre = input("Ingrese el nombre y apellido del cliente: ")
    Dircliente = input("Ingrese la direccion del cliente: ")
    sector = input("Ingrese el sector donde reside el cliente(Norte/Centro/Sur): ").lower()
    
    paquetepequeno = int(input("Ingrese la cantidad de paquetes pequeños que enviará, de no enviar ingrese 0: "))
    paquetemediano = int(input("Ingrese la cantidad de paquetes medianos que enviará, de no enviar ingrese 0: "))
    paquetegrande = int(input("Ingrese la cantidad de paquetes grande que enviará, de no enviar ingrese 0: "))

    datospedido = {
        'Cliente' : Nombre,
        'Dirección' : Dircliente,
        'Sector' : sector,
        'Paquetes pequeños: ' : paquetepequeno,
        'Paquetes medianos: ' : paquetemediano,
        'Paquetes grandes: ' : paquetegrande        
        }
    
    pedidos.append(datospedido)
    if sector == "norte":
        pedidosnorte.append(datospedido)
    elif sector == "centro":
        pedidoscentro.append(datospedido)
    elif sector == "sur":
        pedidossur.append(datospedido)


def listar_pedidos():
    print(pedidos)

def imprimirhojaderuta():
    zonaelegida = input("Ingrese la zona a recorrer para listar pedidos: ").lower()
    if zonaelegida == "norte":
        print(pedidosnorte)
        
    elif zonaelegida == "sur":
        print(pedidossur)
        
    elif zonaelegida == "centro":
        print(pedidoscentro)
