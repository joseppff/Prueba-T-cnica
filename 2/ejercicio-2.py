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

Solución:
1. Se define la clase ColaMinimo: Es un constructor que inicializa una lista vacía para almacenar los elementos de la cola.
    a. self se refiere a la instancia actual de la clase (cola).
2. El método encolar(valor) añade un nuevo valor al final de la lista.
    a. append(valor) agrega el valor al final de la lista.
3. El método desencolar() elimina y devuelve el primer elemento de la lista o None si la cola está vacía.
    a. pop(0) elimina y devuelve el elemento en el índice 0.
4. El método minimo() utiliza la función integrada min() para encontrar y devolver el valor mínimo en la lista, o None si la cola está vacía.

5. En la función main(), se crean instancias de la clase ColaMinim.
    Se agregan varios elementos a la cola y se imprime el estado actual de la cola y el minimo.
    Se crea una condicion while para desencolar elementos hasta que la cola esté vacía, imprimiendo:
     1.El elemento eliminado
     2.El estado actual de la cola
     3.El mínimo después de cada operación.

"""