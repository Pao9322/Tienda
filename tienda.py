
from producto import Producto

class Tienda:
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__productos = []
        self.__costo_delivery = costo_delivery

 # Método para agregar o actualizar productos en la lista de productos
    def agregar_producto(self, producto):       
        if producto not in self.__productos:
            self.__productos.append(producto)
        else:
            existing_product = next(p for p in self.__productos if p == producto)
# Sumar el stock al producto existente
            existing_product + producto  


# Método para listar productos según las especificaciones de cada tipo de tienda
    def listar_productos(self):  
        result = f"\nProductos en la tienda '{self.__nombre}':\n"
        for producto in self.__productos:
            result += str(producto)
            if "Restaurante" in self.__class__.__name__:
                result += "\n"
            elif "Supermercado" in self.__class__.__name__:
                result += f" - {'Pocos productos disponibles' if producto.get_stock() < 10 else ''}\n"
            elif "Farmacia" in self.__class__.__name__:
                result += f" - {'Envío gratis al solicitar este producto' if producto.get_precio() > 15000 else ''}\n"
        return result


# Método para realizar una venta según las especificaciones de cada tipo de tienda
    def realizar_venta(self, nombre_producto, cantidad):        
        producto = next((p for p in self.__productos if p.get_nombre() == nombre_producto), None)
        
# No se hace nada en las tiendas de tipo Restaurante
        if producto:
            if "Restaurante" in self.__class__.__name__:
                pass  
            elif "Farmacia" in self.__class__.__name__:
                if cantidad > 3:
                    print("No se puede vender más de 3 unidades por producto en cada venta.")
                    return
            elif "Supermercado" in self.__class__.__name__:
                if cantidad > producto.get_stock():
                    cantidad = producto.get_stock()

            producto - Producto(producto.get_nombre(), producto.get_precio(), cantidad)
            print(f"Venta realizada en la tienda '{self.__nombre}' - Producto: {nombre_producto}, Cantidad: {cantidad}")
        else:
            print(f"No se encontró el producto '{nombre_producto}' en la tienda '{self.__nombre}'")

    def get_nombre(self):
        return self.__nombre

    def get_costo_delivery(self):
        return self.__costo_delivery

