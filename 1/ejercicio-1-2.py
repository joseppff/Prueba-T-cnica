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


"""