import React, { useState, useEffect } from 'react';
import './App.css';
import BookList from './components/BookList';
import AddBook from './components/AddBook';



function App() {
  const [page, setPage] = useState('home');
  const [books, setBooks] = useState([]);

  // Cargar libros al iniciar
  useEffect(() => {
    fetch('http://localhost:4000/api/libros')
      .then(res => res.json())
      .then(data => setBooks(data))
      .catch(() => setBooks([]));
  }, []);

  const handleAddBook = (book) => {
    fetch('http://localhost:4000/api/libros', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(book)
    })
      .then(res => res.json())
      .then(() => {
        // Recargar la lista después de agregar
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
      <main style={{ background: '#fff', color: '#222', minHeight: '60vh', borderRadius: 8, margin: 24, padding: 24, boxShadow: '0 2px 8px #e3e3e3' }}>
        {page === 'home' && <BookList books={books} />}
        {page === 'add' && <AddBook onAdd={handleAddBook} />}
      </main>
    </div>
  );
}

export default App;
