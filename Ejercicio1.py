# Sistema de Gestión de Inventario de Productos

# ¡Buena pregunta, Camila! El ejercicio que te propuse es más bien una práctica para aprender y dominar conceptos de **recursión**, **árboles binarios** y **list comprehension**, pero no es exactamente un ejercicio típico que te pedirían en una **empresa importante**. Aunque puede ser útil para aprender lógica y estructuras de datos, en un entorno laboral real el enfoque suele ser más en la resolución de **problemas específicos** que afecten directamente a las operaciones, como optimización, análisis de datos o desarrollo de aplicaciones que agreguen valor al negocio.

# Si estás buscando un **ejercicio más orientado a la industria** o algo que te pueda ser **relevante para un trabajo profesional**, te propongo algo un poco más realista. Aquí tienes un nuevo ejercicio que combina **recursión**, **árboles binarios** y **list comprehension**, pero aplicado a **gestión de inventarios** o **gestión de productos**, un área bastante común en empresas importantes:

# ---

# ### 📝 **Ejercicio: Sistema de Gestión de Inventario de Productos**

# #### **Contexto:**
# Imagina que trabajas en una empresa de **logística o ventas** que necesita organizar un **sistema de inventario**. Los productos en el inventario están organizados en un **árbol jerárquico**, donde cada nodo representa un **producto** o **categoría de productos**. 

# El objetivo es poder gestionar los productos de manera eficiente, almacenar sus detalles (como nombre, precio y cantidad disponible), y realizar algunas consultas o cálculos importantes.

# #### **Objetivos del ejercicio:**

# 1. **Modelar el inventario con un árbol binario**: Cada nodo representa un producto con su nombre, precio y cantidad. Un nodo puede tener dos tipos de productos relacionados (subcategorías o productos adicionales).
   
# 2. **Calcular el valor total del inventario** usando recursión: Sumar el valor total de todos los productos en el inventario.
   
# 3. **Filtrar productos por precio**: Crear un método que filtre los productos cuyo precio sea superior a un valor determinado utilizando **list comprehension**.

# 4. **Imprimir el inventario en un formato jerárquico** (recorrido preorden) usando recursión para mostrar la relación entre productos y categorías.

# ---

# ### **Guía paso a paso:**

# #### **Paso 1: Definir la clase `Product` (Producto)**

# - Cada **producto** tiene un:
#   - **Nombre**.
#   - **Precio**.
#   - **Cantidad disponible** (cuántos productos hay en stock).
  
# Define esta clase de manera que pueda representar un producto individual.

# ---

# #### **Paso 2: Crear la clase `InventoryTree` (Árbol de Inventario)**

# - Crea un **árbol binario** de productos, donde cada nodo puede tener dos productos relacionados (por ejemplo, una subcategoría de productos).

# La clase debe tener un atributo `root` que será el producto principal de la categoría.

# ---

# #### **Paso 3: Calcular el valor total del inventario con recursión**

# - El valor total del inventario es la **suma de todos los productos**. Esto puede calcularse con recursión al sumar el valor de cada producto (precio * cantidad) y recorrer las subcategorías.

# ---

# #### **Paso 4: Filtrar productos por precio usando list comprehension**

# - Implementa un método que recorra el árbol y devuelva **una lista de productos cuyo precio sea mayor que un valor determinado**. Esto debe hacerse utilizando **list comprehension** para obtener los productos.

# ---

# #### **Paso 5: Imprimir el inventario (recorrido preorden)**

# - Haz un recorrido **preorden** del árbol para imprimir todos los productos en un formato jerárquico. Esto ayudará a visualizar cómo está organizado el inventario.

# ---

# ### **Por qué este ejercicio es relevante en la industria:**

# 1. **Gestión de inventarios**: Las empresas de ventas, logística o distribución gestionan grandes cantidades de productos, y tener un sistema bien organizado es crucial para la eficiencia.
   
# 2. **Optimización y eficiencia**: Saber organizar datos en estructuras como árboles binarios ayuda a optimizar la búsqueda, inserción y eliminación de productos.

# 3. **Recursión y procesamiento eficiente**: La recursión te permite manejar árboles de manera eficiente y aplicar cálculos a grandes conjuntos de datos.

# 4. **Aplicación práctica de list comprehension**: Filtrar y organizar datos es una habilidad muy útil para el análisis de inventarios y precios.

# ---

# Este ejercicio es más adecuado para el tipo de proyectos en empresas importantes, donde la eficiencia, la organización y el análisis de datos son fundamentales. Además, puedes ampliar este tipo de sistema para integrarlo con bases de datos o interfaces de usuario en una aplicación real.

# ¿Cómo lo ves? ¿Te gustaría intentarlo?