class Producto:
#  Constructor con atributos privados
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
 # Métodos getter para obtener valores privados 
    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

# El stock no puede ser menor a 0
    def set_stock(self, stock):
        self.__stock = max(stock, 0)  

#Compara dos objetos Producto por su nombre.
    def __eq__(self, other):
        return self.__nombre == other.get_nombre()
    
# Sobrecarga del operador '+' para sumar el stock al agregar un producto existente
    def __add__(self, other):
        if self == other:
            self.__stock += other.get_stock()
        return self
    
 # Sobrecarga del operador '-' para restar el stock al realizar una venta
    def __sub__(self, other):      
        if self == other:
            self.__stock -= other.get_stock()
# Asegurar que el stock no sea menor a 0            
            self.set_stock(self.__stock)  
        return self


# Método especial para representación en cadena
    def __str__(self):
        return f"Producto: {self.__nombre}, Precio: {self.__precio}, Stock: {self.__stock}"

