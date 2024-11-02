const express = require('express');
const fetch = require('node-fetch');
const cors = require('cors');
const app = express();
const PORT = 3000;

app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');
app.use(express.static('public'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cors()); // Enable CORS

const API_URL = 'http://localhost:8000/api/peliculas';

// Main route: List all movies
app.get('/', async (req, res) => {
  try {
    const response = await fetch(API_URL);
    const peliculas = await response.json();
    console.log(peliculas);
    res.render('index', { peliculas });
  } catch (error) {
    console.error('Error fetching API:', error.message);
    res.send('Error loading movies.');
  }
});

// Route to show the add movie form
app.get('/agregar', (req, res) => {
  res.render('agregar');
});

// Route to add a new movie
app.post('/agregar', async (req, res) => {
  const nuevaPelicula = req.body;
  console.log('New movie data:', nuevaPelicula); // Log received data

  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(nuevaPelicula),
    });

    const result = await response.json(); // Capture the API response
    console.log('API Response:', result); // Log API response

    res.status(201).json({ message: 'Movie added successfully.' });
  } catch (error) {
    console.error('Error adding movie:', error.message);
    res.status(500).json({ message: 'Error adding the movie.' });
  }
});

// Route to delete a movie
app.post('/eliminar/:id', async (req, res) => {
  const { id } = req.params;
  try {
    await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
    res.redirect('/?eliminado=true');
  } catch (error) {
    console.error('Error deleting movie:', error.message);
    res.send('Error deleting the movie.');
  }
});

// Route to edit a movie
app.get('/editar/:id', async (req, res) => {
  const { id } = req.params;

  try {
    const response = await fetch(`${API_URL}/${id}`);
    const pelicula = await response.json();

    res.render('editar', { pelicula });
  } catch (error) {
    console.error('Error loading movie:', error.message);
    res.send('Error loading the movie.');
  }
});

app.put('/editar/:id', async (req, res) => {
  const { id } = req.params; // Capture the ID from the route parameter
  const peliculaActualizada = req.body; // Capture the sent data

  try {
    const response = await fetch(`${API_URL}/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(peliculaActualizada),
    });

    const result = await response.json(); // Capture the API response
    console.log('API Response:', result); // Log API response

    res.status(200).json({ message: 'Movie edited successfully.' });
  } catch (error) {
    console.error('Error editing movie:', error.message);
    res.status(500).json({ message: 'Error editing the movie.' });
  }
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
