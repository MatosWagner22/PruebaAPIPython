import React, { useEffect, useState } from 'react';

const MovieList = () => {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    const fetchedMovies = [
      { id: 1, titulo: 'Inception', director: 'Christopher Nolan', descripcion: 'A mind-bending thriller', genero: 'Sci-Fi', fechaEstreno: '2010-07-16', estreno: true, esAnimada: false },
      { id: 2, titulo: 'Toy Story', director: 'John Lasseter', descripcion: 'A story about toys', genero: 'Animation', fechaEstreno: '1995-11-22', estreno: true, esAnimada: true },
    ];
    setMovies(fetchedMovies);
  }, []);

  return (
    <div className="table-responsive shadow-sm rounded">
      <table className="table table-hover table-bordered align-middle">
        <thead className="bg-gradient bg-success text-white text-center">
          <tr>
            <th>ID</th>
            <th>Título</th>
            <th>Director</th>
            <th>Descripción</th>
            <th>Género</th>
            <th>Fecha Estreno</th>
            <th>Estreno</th>
            <th>Animada</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {movies.map((movie) => (
            <tr key={movie.id}>
              <td>{movie.id}</td>
              <td>{movie.titulo}</td>
              <td>{movie.director}</td>
              <td>{movie.descripcion}</td>
              <td>{movie.genero}</td>
              <td>{movie.fechaEstreno}</td>
              <td>{movie.estreno ? 'Sí' : 'No'}</td>
              <td>{movie.esAnimada ? 'Sí' : 'No'}</td>
              <td className="text-center">
                <a href={`/editar/${movie.id}`} className="btn btn-primary btn-sm me-2" title="Editar">
                  <i className="fas fa-edit"></i>
                </a>
                <button className="btn btn-danger btn-sm" title="Eliminar">
                  <i className="fas fa-trash-alt"></i>
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default MovieList;