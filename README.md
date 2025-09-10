# Prueba-T-cnica
Prueba Técnica - Software Developer Entry Level (Trainee)
Parte 3: Desarrollo Web Básico (40 puntos)

! Tienes que ser capaz de explicar el desarrollo ¡

Criterios de Evaluación
-> Correcta implementación de la funcionalidad solicitada.
-> Uso adecuado de las tecnologías indicadas.
-> Claridad y organización del código.
-> Buenas prácticas de desarrollo (nombres descriptivos, separación de
responsabilidades, etc.).
-> Documentación mínima.

Solucion 1-1
Python tiene muchas funcionalidades integradas que facilitan la manipulación de listas.
1. Resivo la lista
2. transformo la lista string entregada por una lista de enteros
3. Llamo a la funcion ordenar_eliminar
4. Dentro de la funcion se elimina los duplicados convirtiendo la lista en un conjunto (set)
5. Luego ordeno la lista de menor a mayor con el metodo sort()
6. Finalmente entrego la lista ordenada y sin duplicados

Solucion 1-2
Se implementa una solución sin usar funciones integradas de Python para eliminar duplicados y ordenar la lista.
1. Resivo la lista
2. transformo la lista string entregada por una lista de enteros
3. Llamo a la funcion ordenar_eliminar
4. Dentro de la funcion: 
    A. Se recorre la lista original y se añaden a una nueva_lista SOLO los numero que no se encuentren ya la nueva_lista
    B. Luego se ordena la nueva_lista usando el algoritmo de ordenamiento burbuja.
    -> Len toma la cantidad de elementos y range genera el indice para recorrer la lista.
    -> Con doble for se hace un recorrido en doble imension para comparar cada elemento con los demas y ordenarlos.
5. Finalmente entrego la nueva_lista ordenada y sin duplicados

Solucion 2
1. Se define la clase ColaMinimo: Es un constructor que inicializa una lista vacía para almacenar los elementos de la cola.
    -> self se refiere a la instancia actual de la clase (cola).
2. El método encolar(valor) añade un nuevo valor al final de la lista.
    -> append(valor) agrega el valor al final de la lista.
3. El método desencolar() elimina y devuelve el primer elemento de la lista o None si la cola está vacía.
    -> pop(0) elimina y devuelve el elemento en el índice 0.
4. El método minimo() utiliza la función integrada min() para encontrar y devolver el valor mínimo en la lista, o None si la cola está vacía.

5. En la función main(), se crean instancias de la clase ColaMinim.
    Se agregan varios elementos a la cola y se imprime el estado actual de la cola y el minimo.
    Se crea una condicion while para desencolar elementos hasta que la cola esté vacía, imprimiendo:
     1.El elemento eliminado
     2.El estado actual de la cola
     3.El mínimo después de cada operación.

Solucion 3
App.js
Main donde se establece los componentes principales.
1. Manejo de useState y useEffect para control de estados de la pagina y carga de datos del backend.
2. Se crea funcion para listar los libros del bakcend.
3. Se crea funcion para agregar los libros hacia al backend.
4. Se crea header principal para el HOME y ADD.
5. Se crea botones que dirigen a las paginas de HOME y ADD

Book.js
Componente donde se visualizan los libros listados.
1. Retorna mensaje si "No hay libros disponibles"
2. Muestra los libros mapeados en el backend con su [titulo, genero, autor]

AddBook.js
Componente donde se agrega los libros al backend.
1. Se crear los estados.
2. Se crear un control el submit del formulario
3. Se crear el header para el estilo del formulario.

App.css
Estilos de todos los elementos de la web

index.js
Control del backend.
1. Se crean constantes para la conexion con puertos y del archivo "libros.json"
2. Lee el archivo "libros.json" y devuelve la lista de libros que se hayan almacenado en JSON.
3. Recibe datos de un libro, los agrega al array de libros y los guarda en "libros.json"
4. Control de errores.
