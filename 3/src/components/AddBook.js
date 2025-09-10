import React, { useState } from 'react';

const AddBook = ({ onAdd }) => {
  const [titulo, setTitulo] = useState('');
  const [genero, setGenero] = useState('');
  const [autor, setAutor] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!titulo || !genero || !autor) return;
    onAdd({ titulo, genero, autor });
    setTitulo('');
    setGenero('');
    setAutor('');
  };

  return (
    <div className="add-book">
      <h2>Agregar Libro</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Título"
          value={titulo}
          onChange={e => setTitulo(e.target.value)}
        />
        <input
          type="text"
          placeholder="Género"
          value={genero}
          onChange={e => setGenero(e.target.value)}
        />
        <input
          type="text"
          placeholder="Autor"
          value={autor}
          onChange={e => setAutor(e.target.value)}
        />
        <button type="submit">Agregar</button>
      </form>
    </div>
  );
};

export default AddBook;
