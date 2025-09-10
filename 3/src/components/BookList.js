import React from 'react';

const BookList = ({ books }) => (
  <div className="book-list">
    <h2>Lista de Libros</h2>
    <ul>
      {books.length === 0 ? (
        <li>No hay libros disponibles.</li>
      ) : (
        books.map((book, idx) => (
          <li key={idx}>
            <strong>{book.titulo}</strong> - {book.genero} - {book.autor}
          </li>
        ))
      )}
    </ul>
  </div>
);

export default BookList;
