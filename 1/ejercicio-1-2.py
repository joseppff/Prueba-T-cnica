# ejercicio-1 solucion 2
def ordenar_eliminar(lista):
    # Eliminar duplicados manualmente
    nueva_lista= []
    for num in lista:
        if num not in nueva_lista:
            nueva_lista.append(num)
    # Ordenar manualmente
    for i in range(len(nueva_lista) - 1):
        for j in range(len(nueva_lista) - 1 - i):
            if nueva_lista[j] > nueva_lista[j + 1]:
                nueva_lista[j], nueva_lista[j + 1] = nueva_lista[j + 1], nueva_lista[j]
    return nueva_lista

import ast

if __name__ == "__main__":
    entrada = input("Introducir lista")
    lista = ast.literal_eval(entrada)
    print(ordenar_eliminar(lista))

"""

Parte 1: Lógica de Programación (30 puntos)
Problema:
Escribe una función que reciba una lista de números enteros y devuelva una nueva
lista con los números ordenados, eliminando los duplicados.
Ejemplo:
entrada = [4, 2, 7, 2, 4, 9, 1]
salida = [1, 2, 4, 7, 9]

Solución:
Se implementa una solución sin usar funciones integradas de Python para eliminar duplicados y ordenar la lista.
1. Resivo la lista
2. transformo la lista string entregada por una lista de enteros
3. Llamo a la funcion ordenar_eliminar
4. Dentro de la funcion: 
    A. Se recorre la lista original y se añaden a una nueva_lista SOLO los numero que no se encuentren ya la nueva_lista
    B. Luego se ordena la nueva_lista usando el algoritmo de ordenamiento burbuja.
    Len toma la cantidad de elementos y range genera el indice para recorrer la lista.
    Con doble for se hace un recorrido en doble imension para comparar cada elemento con los demas y ordenarlos.

5. Finalmente entrego la nueva_lista ordenada y sin duplicados

"""