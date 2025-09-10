const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
const PORT = 4000;
const DATA_FILE = path.join(__dirname, 'libros.json');

app.use(cors());
app.use(express.json());

// Obtener todos los libros
app.get('/api/libros', (req, res) => {
  fs.readFile(DATA_FILE, 'utf8', (err, data) => {
    if (err) {
      if (err.code === 'ENOENT') return res.json([]);
      return res.status(500).json({ error: 'Error al leer la base de datos' });
    }
    res.json(JSON.parse(data));
  });
});

// Agregar un libro
app.post('/api/libros', (req, res) => {
  const { titulo, genero, autor } = req.body;
  if (!titulo || !genero || !autor) {
    return res.status(400).json({ error: 'Faltan campos requeridos' });
  }
  fs.readFile(DATA_FILE, 'utf8', (err, data) => {
    let libros = [];
    if (!err) {
      libros = JSON.parse(data);
    }
    const nuevoLibro = { titulo, genero, autor };
    libros.push(nuevoLibro);
    fs.writeFile(DATA_FILE, JSON.stringify(libros, null, 2), (err) => {
      if (err) return res.status(500).json({ error: 'Error al guardar el libro' });
      res.status(201).json(nuevoLibro);
    });
  });
});

app.listen(PORT, () => {
  console.log(`Servidor backend escuchando en http://localhost:${PORT}`);
});
