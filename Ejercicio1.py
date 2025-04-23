# Sistema de Gestión de Inventario de Productos

# Definir la clase producto.
class Product:
    def __init__(self, nombre:str, precio:int, cantidad:int):
        self._nombre: str = nombre
        self._precio: int = precio
        self._cantidad: int = cantidad 
    
    def __str__(self):
        return f"Nombre Producto: {self._nombre}, Precio: {self._precio}, Cantidad: {self._cantidad}"
    
# Crear una clase que represente un node del árbol binario.
class InventoryNode:
    def __init__(self, producto: Product):
        self.producto = producto
        self.izquierda = None
        self.derecha = None

class InventoryTree:
    def __init__(self):
        self.raiz = None

    def agregar_producto(self, producto: Product):
        if self.raiz is None:
            self.raiz = InventoryNode(producto)
        else:
            self._agregar_recursivo(self.raiz, producto)
    
        def agregar_recursivo (self, nodo: InventoryNode, producto: Product):
            