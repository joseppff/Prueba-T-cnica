import React, { useState, useEffect } from 'react';
import './App.css';
import BookList from './components/BookList';
import AddBook from './components/AddBook';


// Componente principal
// useState: para manejar el estado de la página actual y la lista de libros
// useEffect: para cargar los libros desde el backend
function App() {
  // Estado de página actual y la lista de libros
  const [page, setPage] = useState('home');
  const [books, setBooks] = useState([]);

  // Cargar libros al iniciar
  useEffect(() => {
    // petición HTTP GET, pasar formato JSON, guardar los datos y manejar errror
    fetch('http://localhost:4000/api/libros')
      .then(res => res.json())
      .then(data => setBooks(data))
      .catch(() => setBooks([]));
  }, []);

  // Función para agregar un libro
  const handleAddBook = (book) => {
    // petición HTTP POST, enviar datos en JSON y actualizar la lista
    fetch('http://localhost:4000/api/libros', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(book)
    })
      .then(res => res.json())
      .then(() => {
        fetch('http://localhost:4000/api/libros')
          .then(res => res.json())
          .then(data => setBooks(data));
        setPage('home');
      });
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1 style={{ color: '#61dafb' }}>Biblioteca Virtual</h1>
        <nav>
          <button
            className={`nav-btn${page === 'home' ? ' active' : ''}`}
            onClick={() => setPage('home')}
          >
            Home
          </button>
          <button
            className={`nav-btn${page === 'add' ? ' active' : ''}`}
            onClick={() => setPage('add')}
          >
            Agregar Libro
          </button>
        </nav>
      </header>
  <main className="main-content">
        {page === 'home' && <BookList books={books} />}
        {page === 'add' && <AddBook onAdd={handleAddBook} />}
      </main>
    </div>
  );
}

export default App;
