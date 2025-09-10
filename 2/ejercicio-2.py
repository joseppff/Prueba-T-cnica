# ejercicio-2.py


class ColaMinimo:
    # Constructor
    def __init__(self):
        self.cola = []

    # Se agrega un elemento a la cola
    def encolar(self, valor):
        self.cola.append(valor)

    # Se elimina y devuelve el primer elemento de la cola
    def desencolar(self):
        if self.cola:
            return self.cola.pop(0)
        else:
            return None

    def minimo(self):
        if self.cola:
            return min(self.cola)
        else:
            return None

def main():
    cola = ColaMinimo()
    #datos a la cola
    cola.encolar(5)
    cola.encolar(3)
    cola.encolar(7)
    cola.encolar(1)
    cola.encolar(8)
    cola.encolar(2)
    cola.encolar(3)
    cola.encolar(9)
    cola.encolar(8)
    print("Cola inicial:", cola.cola)
    print("Mínimo actual:", cola.minimo())

    while cola.cola:
        eliminado = cola.desencolar()
        print(f"Eliminado: {eliminado}, Cola ahora: {cola.cola}, Mínimo: {cola.minimo()}")


if __name__ == "__main__":
    main()


"""

Parte 2: Estructuras de Datos (30 puntos)
Problema:
Implementa una clase “ColaMinimo” que funcione como una cola (FIFO), pero que
además tenga un método “minimo()” que devuelva el valor mínimo actual en la
cola.
Métodos esperados:
- encolar(valor)
- desencolar()
- minimo()
"""