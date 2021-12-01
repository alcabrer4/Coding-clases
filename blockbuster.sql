DROP DATABASE IF EXISTS BLOCKBUSTER;

CREATE DATABASE BLOCKBUSTER;

USE BLOCKBUSTER;

CREATE TABLE Tiendas(
    id BIGINT NOT NULL AUTO_INCREMENT,
    direccion VARCHAR(256) UNIQUE,
    telefono BIGINT UNIQUE,
    email VARCHAR(200) UNIQUE,
    PRIMARY KEY (id)
);

CREATE TABLE Formatos(
    id BIGINT NOT NULL AUTO_INCREMENT,
    formato VARCHAR(100) UNIQUE,
    PRIMARY KEY (id)
);

CREATE TABLE Generos(
    id BIGINT NOT NULL AUTO_INCREMENT,
    genero VARCHAR(100) UNIQUE,
    PRIMARY KEY (id)
);

CREATE TABLE Peliculas(
    id BIGINT NOT NULL AUTO_INCREMENT,
    formato_id BIGINT,
    genero_id BIGINT,
    tienda_id BIGINT,
    año BIGINT,
    titulo VARCHAR(100) UNIQUE,
    en_stock BIGINT,
    precio_renta FLOAT,
    precio_compra FLOAT,
    vendidas BIGINT,
    PRIMARY KEY (id),
    FOREIGN KEY (formato_id) REFERENCES Formatos(id),
    FOREIGN KEY (genero_id) REFERENCES Generos(id),
    FOREIGN KEY (tienda_id) REFERENCES Tiendas(id)
);

CREATE TABLE Actores(
    id BIGINT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    sexo VARCHAR(100),
    PRIMARY KEY (id)
);

CREATE TABLE Elenco(
    id BIGINT NOT NULL AUTO_INCREMENT,
    pelicula_id BIGINT UNIQUE,
    actor_id BIGINT,
    reparto_id BIGINT,
    PRIMARY KEY (id),
    FOREIGN KEY (pelicula_id) REFERENCES Peliculas(id),
    FOREIGN KEY (actor_id) REFERENCES Actores(id),
    FOREIGN KEY (reparto_id) REFERENCES Actores(id)
);

CREATE TABLE Status_Renta(
    id BIGINT NOT NULL AUTO_INCREMENT,
    estado VARCHAR(100) UNIQUE,
    PRIMARY KEY (id)
);

CREATE TABLE Clientes(
    id BIGINT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    telefono BIGINT UNIQUE,
    email VARCHAR(200) UNIQUE,
    direccion VARCHAR(100),
    PRIMARY KEY (id)
);

CREATE TABLE Rentas_Clientes(
    id BIGINT NOT NULL AUTO_INCREMENT,
    cliente_id BIGINT,
    pelicula_id BIGINT,
    status_renta_id BIGINT,
    dia_renta DATE,
    dia_entrega DATE,
    costo_renta FLOAT,
    PRIMARY KEY (id),
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
    FOREIGN KEY (pelicula_id) REFERENCES Peliculas(id),
    FOREIGN KEY (status_renta_id) REFERENCES Status_Renta(id)
);

INSERT INTO Tiendas(direccion, telefono, email) VALUES ('casa', 0954, 'hola@mail.com'), 
('house', 1234, 'adios@mail.com');
