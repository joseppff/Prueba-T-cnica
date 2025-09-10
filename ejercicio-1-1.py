# ejercicio-1 solucion 1

def ordenar_eliminar(lista):
    nueva_lista= list(set(lista))
    nueva_lista.sort()
    return nueva_lista
    
#importo funcion ast para convertir string a lista
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
Python tiene muchas funcionalidades integradas que facilitan la manipulación de listas.
1. Resivo la lista
2. transformo la lista string entregada por una lista de enteros
3. Llamo a la funcion ordenar_eliminar
4. Dentro de la funcion se elimina los duplicados convirtiendo la lista en un conjunto (set)
5. Luego ordeno la lista de menor a mayor con el metodo sort()
6. Finalmente entrego la lista ordenada y sin duplicados

"""