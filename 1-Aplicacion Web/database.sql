-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 05, 2024 at 02:58 PM
-- Server version: 10.4.21-MSQLSERVER
-- PYPHON Version: 7.4.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `EstudianteDB`
--

-- --------------------------------------------------------

--
-- Table structure for table `estudiantes`
--


Create Database EstudianteDB

CREATE TABLE `estudiantes` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  `apellido` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `telefono` VARCHAR(20) NOT NULL,
  `fecha_nacimiento` DATE NOT NULL,
  `direccion` VARCHAR(255),
  `ciudad` VARCHAR(100),
  `codigo_postal` VARCHAR(10),
  `carrera` VARCHAR(100),
  `semestre` INT(2) NOT NULL,
  `promedio` DECIMAL(3,2) DEFAULT 0.00,
  `fecha_registro` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `estudiantes`
--

INSERT INTO `estudiantes` 
(`nombre`, `apellido`, `email`, `telefono`, `fecha_nacimiento`, `direccion`, `ciudad`, `codigo_postal`, `carrera`, `semestre`, `promedio`) 
VALUES
('Juan', 'Pérez', 'juan.perez@email.com', '8091234567', '2000-05-15', 'Calle 123', 'Santo Domingo', '10101', 'Ingeniería de Software', 6, 3.85),
('Ana', 'Gómez', 'ana.gomez@email.com', '8099876543', '1999-12-22', 'Av. Principal 45', 'Santiago', '51000', 'Medicina', 4, 4.20),
('Carlos', 'López', 'carlos.lopez@email.com', '8095551234', '2001-07-30', 'Calle Secundaria 12', 'La Vega', '41000', 'Derecho', 2, 3.60),
('Lucía', 'Martínez', 'lucia.martinez@email.com', '8093339876', '1998-11-10', 'Boulevard Central 3', 'Puerto Plata', '57000', 'Arquitectura', 8, 3.90),
('Pedro', 'Rodríguez', 'pedro.rodriguez@email.com', '8094443210', '2000-01-25', 'Callejón 8', 'San Cristóbal', '91000', 'Contabilidad', 7, 3.75);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `estudiantes`
--
ALTER TABLE `estudiantes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
COMMIT;
