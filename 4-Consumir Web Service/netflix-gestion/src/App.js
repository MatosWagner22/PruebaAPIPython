import React from 'react';
import Sidebar from './components/Sidebar';
import MovieList from './components/MovieList';

const App = () => {
  return (
    <div className="d-flex">
      {/* Sidebar */}
      <Sidebar />

      {/* Main Content */}
      <div className="container-fluid px-4 py-5">
        <div className="content bg-white rounded shadow-lg p-5">
          <nav className="navbar navbar-expand-lg navbar-light bg-light rounded mb-4">
            <div className="container-fluid">
              <a className="navbar-brand fw-bold text-success" href="#">
                <i className="fas fa-film me-2"></i> Gestión de Películas
              </a>
            </div>
          </nav>

          <div className="d-flex justify-content-between align-items-center mb-4">
            <h2 className="text-success fw-bold">
              <i className="fas fa-film me-2"></i>Listado de Películas
            </h2>
            <a className="btn btn-outline-primary d-flex align-items-center shadow-sm" href="/agregar">
              <i className="fas fa-plus-circle me-2"></i> Agregar Película
            </a>
          </div>

          {/* Movie List Component */}
          <MovieList />
        </div>
      </div>
    </div>
  );
};

export default App;