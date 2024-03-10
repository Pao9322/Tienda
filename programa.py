from tienda import Tienda
from producto import Producto

if __name__ == "__main__":
    # Crear tienda
    tipo_tienda = input("Ingrese el tipo de tienda (Restaurante, Supermercado, Farmacia): ")
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))

    if tipo_tienda == "Restaurante":
        from tienda import Restaurante
        mi_tienda = Restaurante(nombre_tienda, costo_delivery)
    elif tipo_tienda == "Supermercado":
        from tienda import Supermercado
        mi_tienda = Supermercado(nombre_tienda, costo_delivery)
    elif tipo_tienda == "Farmacia":
        from tienda import Farmacia
        mi_tienda = Farmacia(nombre_tienda, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        exit(1)

    # Bucle
    while True:
        print("\n--- Menú ---")
        print("1. Agregar Producto")
        print("2. Listar Productos")
        print("3. Realizar Venta")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        # Agregar un nuevo producto a la tienda
        if opcion == "1":
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_producto = float(input("Ingrese el precio del producto: "))
            stock_producto = int(input("Ingrese el stock inicial del producto: "))

            nuevo_producto = Producto(nombre_producto, precio_producto, stock_producto)
            mi_tienda.agregar_producto(nuevo_producto)
            print("Producto agregado exitosamente.")

        # Listar los productos existentes en la tienda
        elif opcion == "2":
            print(mi_tienda.listar_productos())

        # Realizar una venta
        elif opcion == "3":
            nombre_producto_venta = input("Ingrese el nombre del producto a vender: ")
            cantidad_venta = int(input("Ingrese la cantidad requerida: "))
            mi_tienda.realizar_venta(nombre_producto_venta, cantidad_venta)

        # Salir del programa
        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")