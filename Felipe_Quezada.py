import json

precios_pizzas = {
    "cuatro quesos": {
        "Pequeña": 6000,
        "Mediana": 9000,
        "Familia": 12000
    },
    "hawaiana": {
        "Pequeña": 6000,
        "Mediana": 9000,
        "Familia": 12000
    },
    "napolitana": {
        "Pequeña": 5500,
        "Mediana": 8500,
        "Familia": 11000
    },
    "pepperoni": {
        "Pequeña": 7000,
        "Mediana": 10000,
        "Familia": 13000
    }
}
    
ventas = []
##registro_venta------------------------------------------------------------------------------------------------------------------------------------------
def registrar_ventas():
    cliente = input("Ingrese el nombre del cliente: ")
    print("Que pizza desea?")
    print("[--Cuatro Quesos--]")
    print("[--Hawaiana--]")
    print("[--Napolitana--]")
    print("[--Pepperoni--]")
    tipo_pizza = input("Escriba la pizza que desea: ").lower()
    print("[--Pequeña--]")
    print("[--Mediana--]")
    print("[--Familia--]")
    tamaño = input("Escriba la pizza que desea: ").capitalize()
    cantidad = int(input("Ingrese la cantidad de pizzas que desea: "))

#precios-----------------------------------------------------------------------------------------------------------------------------------------------------------
    precio_unidad = precios_pizzas[tipo_pizza][tamaño]
    total_precio = cantidad * precio_unidad

#descuentos-----------------------------------------------------------------------------------------------------------------------------------------------------------
    print("que tipo de cliente es?")
    print("[--diurno--]")
    print("[--vespertino--]")
    print("[--administrativo--]")
    tipo_descuento = input("Escriba el tipo de cliente: ").lower()
    descuento = 0
    if tipo_descuento == "diurno":
        descuento = 0.12
    elif tipo_descuento == "vespertino":
        descuento = 0.14
    elif tipo_descuento == "administrativo":
        descuento = 0.10
    
    precio_final = total_precio * (1 - descuento)

#guardado-ventas-----------------------------------------------------------------------------------------------------------------------------------------------------------

    venta = {
        "cliente": cliente,
        "tipo_pizza": tipo_pizza,
        "tamaño": tamaño,
        "cantidad": cantidad,
        "precio_unitario": precio_unidad,
        "precio_total": total_precio,
        "tipo_descuento": tipo_descuento,
        "descuento_aplicado": descuento,
        "precio_final": precio_final
    }
    ventas.append(venta)
    print("se registro la venta correctamente.")

##mostrar_ventas----------------------------------------------------------------------------------------------------------------------------------------------------

def mostrar_ventas():
    print("\nListado de las ventas:")
    for venta in ventas:
        print(f"Cliente: {venta['cliente']}, Pizza: {venta['tipo_pizza']} ({venta['tamaño']}), Cantidad: {venta['cantidad']}, Precio Total: ${venta['precio_total']:.2f}")

##buscar_clientes----------------------------------------------------------------------------------------------------------------------------------------------------

def buscar_por_cliente():
    buscar_cliente = input("Ingrese el nombre del cliente a buscar: ")
    print(f"\nVentas encontradas para '{buscar_cliente}':")
    encontradas = False
    for venta in ventas:
        if venta['cliente'].lower() == buscar_cliente.lower():
            encontradas = True
            print(f"Pizza: {venta['tipo_pizza']} ({venta['tamaño']}), Cantidad: {venta['cantidad']}, Precio Total: ${venta['precio_total']:.2f}")
    if not encontradas:
        print(f"No se encontraron ventas para '{buscar_cliente}'.")

##guardado_ventas----------------------------------------------------------------------------------------------------------------------------------------------------

def guardar_ventas():
    with open("ventas.json", "w") as file:
        json.dump(ventas, file)
    print("Ventas guardadas en el archivo 'ventas.json'.")

##cargar_ventas----------------------------------------------------------------------------------------------------------------------------------------------------

def cargar_ventas():
    global ventas
    try:
        with open("ventas.json", "r") as file:
            ventas = json.load(file)
        print("Ventas cargadas desde 'ventas.json'.")
    except FileNotFoundError:
        print("No se encontró el archivo 'ventas.json'. No hay ventas cargadas.")

#generar_boleta----------------------------------------------------------------------------------------------------------------------------------------------------

def generar_boleta():
    cliente = input("Ingrese el nombre del cliente para generar la boleta: ")
    encontrado = False
    for venta in ventas:
        if venta['cliente'].lower() == cliente.lower():
            encontrado = True
            print("\n-----------------Boleta-----------------")
            print(f"Cliente: {venta['cliente']}")
            print(f"Pizza: {venta['tipo_pizza']} ({venta['tamaño']})")
            print(f"Cantidad: {venta['cantidad']}")
            print(f"Precio sin descuento: ${venta['precio_total']:.2f}")
            print(f"Descuento del: {venta['descuento_aplicado']*100}%")
            print(f"Precio total con descuento: ${venta['precio_final']:.2f}")
            print("---------------------------------------")
    if not encontrado:
        print(f"No se encontraron ventas para '{cliente}'.")

##cancelar_ventas----------------------------------------------------------------------------------------------------------------------------------------------------

def anular_venta():
    cliente = input("Ingrese el nombre del cliente para eliminar la venta: ")
    encontrada = False
    for venta in ventas:
        if venta['cliente'].lower() == cliente.lower():
            encontrada = True
            confirmacion = input(f"¿Está seguro que desea eliminar la venta de {venta['tipo_pizza']} ({venta['tamaño']}) al cliente {cliente}? (s/n): ")
            if confirmacion.lower() == 's':
                ventas.remove(venta)
                print("Venta eliminada correctamente.")
                break
    if not encontrada:
        print(f"No se encontraron ventas para '{cliente}'.")

##menu----------------------------------------------------------------------------------------------------------------------------------------------------

def menu():
    while True:
        print("\n-----sistema de ventas de pizzas-----")
        print("[1] - Registrar una venta")
        print("[2] - Mostrar todas las ventas")
        print("[3] - Buscar ventas por cliente")
        print("[4] - Guardar las ventas en un archivo")
        print("[5] - Cargar las ventas desde un archivo")
        print("[6] - Generar Boleta")
        print("[7] - Anular venta")
        print("[8] - Salir del programa")

        opcion = input("\nIngrese una opcion: ")

        if opcion == '1':
            registrar_ventas()
        elif opcion == '2':
            mostrar_ventas()
        elif opcion == '3':
            buscar_por_cliente()
        elif opcion == '4':
            guardar_ventas()
        elif opcion == '5':
            cargar_ventas()
        elif opcion == '6':
            generar_boleta()
        elif opcion == '7':
            anular_venta()
        elif opcion == '8':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()