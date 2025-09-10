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

"""