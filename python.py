# Invertir una cadena de texto

def invertir_cadena(cadena):
    return cadena[::-1] # cadena[inicio:fin:paso] el paso en -1 invierte la cadena


# Ejemplo de uso
if __name__ == "__main__": # sirve para que el código solo se ejecute si este archivo es el principal
    texto = "Hola, mundo!"
    texto_invertido = invertir_cadena(texto)
    print(f"Texto original: {texto}")
    print(f"Texto invertido: {texto_invertido}")
    # Salida esperada:
    # Texto original: Hola, mundo!
    # Texto invertido: !odnum ,aloH


# Palindromo
def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")  # Convertir a minúsculas y eliminar espacios
    return cadena == cadena[::-1]  # Compara la cadena con su versión invertida 

# Ejemplo de uso
if __name__ == "__main__":
    texto = "Anita lava la tina"
    if es_palindromo(texto):
        print(f"'{texto}' es un palíndromo.")
    else:
        print(f"'{texto}' no es un palíndromo.")
    # Salida esperada:
    # 'Anita lava la tina' es un palíndromo.
    # 'Hola mundo' no es un palíndromo.
    texto2 = "Hola mundo"
    if es_palindromo(texto2):
        print(f"'{texto2}' es un palíndromo.")
    else:
        print(f"'{texto2}' no es un palíndromo.")
    # Salida esperada:
    # 'Hola mundo' no es un palíndromo.     

       
# Fibonacci
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Ejemplo de uso
if __name__ == "__main__":
    n = 10
    secuencia_fib = fibonacci(n)
    print(f"Los primeros {n} números de la secuencia de Fibonacci son: {secuencia_fib}")
    # Salida esperada:
    # Los primeros 10 números de la secuencia de Fibonacci son: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# Numero más frecuente en un array

def numero_mas_frecuente(arr):
    if not arr:
        return None
    
    frecuencia = {}
    for num in arr:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num] = 1
    
    max_frecuencia = max(frecuencia.values())
    numeros_frecuentes = [num for num, freq in frecuencia.items() if freq == max_frecuencia]
    
    return numeros_frecuentes

# Ejemplo de uso
if __name__ == "__main__":
    arr = [1, 2, 3, 2, 4, 3, 2]
    resultado = numero_mas_frecuente(arr)
    print(f"El número(s) más frecuente(s) en el array {arr} es/son: {resultado}")
    # Salida esperada:
    # El número(s) más frecuente(s) en el array [1, 2, 3, 2, 4, 3, 2] es/son: [2]


#Anagrama
def son_anagramas(cadena1, cadena2):
    # Eliminar espacios y convertir a minúsculas
    cadena1 = cadena1.replace(" ", "").lower()
    cadena2 = cadena2.replace(" ", "").lower()
    
    # Comparar las cadenas ordenadas
    return sorted(cadena1) == sorted(cadena2)
    
# Ejemplo de uso
if __name__ == "__main__": 
    cadena1 = "amor"
    cadena2 = "Roma"
    if son_anagramas(cadena1, cadena2):
        print(f"'{cadena1}' y '{cadena2}' son anagramas.")
    else:
        print(f"'{cadena1}' y '{cadena2}' no son anagramas.")
    # Salida esperada:
    # 'amor' y 'Roma' son anagramas.
    
    cadena3 = "hola"
    cadena4 = "adios"
    if son_anagramas(cadena3, cadena4):
        print(f"'{cadena3}' y '{cadena4}' son anagramas.")
    else:
        print(f"'{cadena3}' y '{cadena4}' no son anagramas.")
    # Salida esperada:
    # 'hola' y 'adios' no son anagramas.


# Eliminar duplicados de una lista
def eliminar_duplicados(lista):
    return list(set(lista))  # Convierte la lista a un conjunto para eliminar duplicados y luego vuelve a convertirla a lista

# Ejemplo de uso
if __name__ == "__main__":
    lista = [1, 2, 3, 2, 4, 3, 2]
    lista_sin_duplicados = eliminar_duplicados(lista)
    print(f"Lista original: {lista}")
    print(f"Lista sin duplicados: {lista_sin_duplicados}")
    # Salida esperada:
    # Lista original: [1, 2, 3, 2, 4, 3, 2]
    # Lista sin duplicados: [1, 2, 3, 4]


# Suma de los dígitos de un número
def suma_digitos(numero):
    return sum(int(digito) for digito in str(numero))  # Convierte el número a cadena, itera sobre cada dígito y suma

# Ejemplo de uso
if __name__ == "__main__":
    numero = 12345
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")
    # Salida esperada:
    # La suma de los dígitos de 12345 es: 15    

