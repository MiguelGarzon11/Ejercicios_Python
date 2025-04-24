# Sistema de Gestión de Inventario de Productos

# Crea un sistema de inventario donde cada ítem se representa como un nodo en un árbol binario de búsqueda (BST). El inventario se organiza por el nombre del producto (orden alfabético). El sistema debe permitir:

# ✅ Funcionalidades requeridas:

# Insertar productos (nombre, cantidad).

# Buscar un producto y retornar su cantidad.

# Eliminar un producto.

# Listar todos los productos en orden alfabético (inorden).

# Contar cuántos productos hay con cantidad mayor a un valor dado (usa recursión y list comprehension aquí).

# Mostrar productos con nombre que empieza por una letra específica (usa list comprehension).

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre: str = nombre
        self.precio: int = precio
        self.cantidad: int = cantidad

class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None
    
    # Metodo para insertar un valor en el árbol
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor) # Si el árbol esta vacio, el nuevo nodo se convierte en la raíz.
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, producto):
        if producto.nombre < nodo.valor.nombre:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(producto)
            else:
                self._insertar_recursivo(nodo.izquierda, producto)
        elif producto.nombre > nodo.valor.nombre:
            if nodo.derecha is None:
                nodo.derecha = Nodo(producto)
            else:
                self._insertar_recursivo(nodo.derecha, producto)
        else:
            nodo.valor.cantidad += producto.cantidad

    def buscar(self, nombre):
        return self._buscar_recursivo(self.raiz, nombre)

    def _buscar_recursivo(self, nodo, nombre):
        if nodo is None:
            return None
        if nombre == nodo.valor.nombre:
            return nodo.valor.nombre
        elif nombre < nodo.valor.nombre:
            return self._buscar_recursivo(nodo.izquierda, nombre)
        else:
            return self._buscar_recursivo(nodo.derecha, nombre)
        
    def eliminar(self, nombre):
        self.raiz = self._eliminar_recursivo(self.raiz, nombre)

    def _eliminar_recursivo(self,nodo,nombre):
        if nodo is None:
            return None
        
        if nombre < nodo.valor.nombre:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, nombre)
        elif nombre > nodo.valor.nombre:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, nombre)
        else:
            # Caso 1: Sin hijos
            if nodo.izquierda is None and nodo.derecha is None:
                return None
            # Caso 2: Un solo hijo
            if nodo.izquierda is None:
                return nodo.derecha
            if nodo.derecha is None:
                return nodo.izquierda
            # Caso 3: Dos hijos
            sucesor = self._encontrar_min(nodo.derecha)
            nodo.valor = sucesor.valor
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, sucesor.valor.nombre)

        return nodo
    
    def _encontrar_min(self, nodo):
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo
    
    def listar_productos(self):
        return self._inorden(self.raiz)
    
    def _inorden(self, nodo):
        if nodo is None:
            return []
        return self._inorden(nodo.izquierda) + [nodo.valor] + self._inorden(nodo.derecha)
    
    def contar_mayores(self, cantidad_minima):
        productos = self._inorden(self.raiz)
        return len([p for p in productos if p.cantidad > cantidad_minima])
    
    def productos_por_letra(self, letra):
        productos = self._inorden(self.raiz)
        return [p for p in productos if p.nombre.lower().startswith(letra.lower())]
    

    # Crear el árbol
inventario = Arbol()

# Insertar productos
inventario.insertar(Producto("Manzana", 3000, 10))
inventario.insertar(Producto("Banano", 2000, 15))
inventario.insertar(Producto("Mandarina", 2500, 8))

# Buscar
print(inventario.buscar("Banano"))  # 15

# Eliminar
inventario.eliminar("Mandarina")

# Listar en orden
for p in inventario.listar_productos():
    print(p.nombre, p.precio, p.cantidad)

# Contar productos con más de 9 unidades
print(inventario.contar_mayores(9))

# Productos que comienzan por "M"
print([p.nombre for p in inventario.productos_por_letra("M")])
