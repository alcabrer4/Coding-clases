DROP DATABASE IF EXISTS BLOCKBUSTER;

CREATE DATABASE BLOCKBUSTER;

USE BLOCKBUSTER;

CREATE TABLE Video_Stores(
    store_id BIGINT NOT NULL AUTO_INCREMENT,
    store_adress VARCHAR(512) UNIQUE,
    store_phone BIGINT UNIQUE,
    store_email VARCHAR(512) UNIQUE,
    PRIMARY KEY (store_id)
);

CREATE TABLE Format_Types(
    format_type_code BIGINT NOT NULL AUTO_INCREMENT,
    format_type_description VARCHAR(512) UNIQUE,
    PRIMARY KEY (format_type_code)
);

CREATE TABLE Genres_Codes(
    genre_code BIGINT NOT NULL AUTO_INCREMENT,
    genre_description VARCHAR(512) UNIQUE,
    PRIMARY KEY (genre_code)
);

CREATE TABLE Movies(
    movie_id BIGINT NOT NULL AUTO_INCREMENT,
    format_type_code BIGINT,
    genre_code BIGINT,
    store_id BIGINT,
    release_year BIGINT,
    movie_title VARCHAR(512) UNIQUE,
    number_in_stock BIGINT,
    rental_daily_rate FLOAT,
    sale_price FLOAT,
    PRIMARY KEY (movie_id),
    FOREIGN KEY (format_type_code) REFERENCES Format_Types(format_type_code),
    FOREIGN KEY (genre_code) REFERENCES Genres_Codes(genre_code),
    FOREIGN KEY (store_id) REFERENCES Video_Stores(store_id)
);

CREATE TABLE Actors(
    actor_id BIGINT NOT NULL AUTO_INCREMENT,
    actor_first_name VARCHAR(512),
    actor_last_name VARCHAR(512),
    actor_gender VARCHAR(512),
    PRIMARY KEY (actor_id)
);

CREATE TABLE Movie_Cast(
    movie_id BIGINT,
    actor_id BIGINT,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    FOREIGN KEY (actor_id) REFERENCES Actors(actor_id),
    PRIMARY KEY (movie_id, actor_id)
);

CREATE TABLE Rental_Status_Codes(
    rental_status_code BIGINT NOT NULL AUTO_INCREMENT,
    rental_status_description VARCHAR(512) UNIQUE,
    PRIMARY KEY (rental_status_code)
);

CREATE TABLE Costumers(
    costumer_id BIGINT NOT NULL AUTO_INCREMENT,
    costumer_first_name VARCHAR(512),
    costumer_last_name VARCHAR(512),
    costumer_phone BIGINT UNIQUE,
    costumer_email VARCHAR(512) UNIQUE,
    costumer_address VARCHAR(512),
    PRIMARY KEY (costumer_id)
);

CREATE TABLE Costumer_Rentals(
    item_rental_id BIGINT NOT NULL AUTO_INCREMENT,
    costumer_id BIGINT,
    movie_id BIGINT,
    rental_status_code BIGINT,
    rental_date_out DATE,
    rental_date_returned DATE,
    rental_amount_due FLOAT,
    PRIMARY KEY (item_rental_id),
    FOREIGN KEY (costumer_id) REFERENCES Costumers(costumer_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    FOREIGN KEY (rental_status_code) REFERENCES Rental_Status_Codes(rental_status_code)
);

CREATE TABLE Payment_Methods(
    payment_method_code BIGINT NOT NULL UNIQUE AUTO_INCREMENT,
    payment_method_description VARCHAR(512) UNIQUE,
    PRIMARY KEY (payment_method_code)
);

CREATE TABLE Accounts(
    account_id BIGINT NOT NULL AUTO_INCREMENT,
    costumer_id BIGINT,
    payment_method_code BIGINT,
    account_name VARCHAR(512) UNIQUE,
    PRIMARY KEY (account_id),
    FOREIGN KEY (costumer_id) REFERENCES Costumers(costumer_id),
    FOREIGN KEY (payment_method_code) REFERENCES Payment_Methods(payment_method_code)
);

CREATE TABLE Transaction_Types(
    transaction_type_code BIGINT NOT NULL AUTO_INCREMENT,
    transaction_type_description VARCHAR(512) UNIQUE,
    PRIMARY KEY (transaction_type_code)
);

CREATE TABLE Financial_Transactions(
    transaction_id BIGINT NOT NULL AUTO_INCREMENT,
    account_id BIGINT,
    item_rental_id BIGINT,
    transaction_type_code BIGINT,
    transaction_date DATE,
    transaction_ammount FLOAT,
    PRIMARY KEY (transaction_id),
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id),
    FOREIGN KEY (item_rental_id) REFERENCES Costumer_Rentals(item_rental_id),
    FOREIGN KEY (transaction_type_code) REFERENCES Transaction_Types(transaction_type_code)
);

/* INSERT INTO Tiendas(direccion, telefono, email) VALUES ('casa', 0954, 'hola@mail.com'), 
('house', 1234, 'adios@mail.com');*/

INSERT INTO Video_Stores(store_adress, store_phone, store_email) 
VALUES('AV. 16 DE SEPTIEMBRE, 145', 7471500954, 'al.cabrer4@gmail.com'), ('av. naval militar, 132', 5537162214, 'santigm@gmail.com');

INSERT INTO Format_Types(format_type_description) 
VALUES('vhs'), ('blue ray');

INSERT INTO Genres_Codes(genre_description) 
VALUES('horror'), ('action');

INSERT INTO Movies(format_type_code, genre_code, store_id, release_year, movie_title, number_in_stock, rental_daily_rate, sale_price)
VALUES(1, 1, 1, 1985, 'Freddie Krueger', 5, 49.99, 199.99), (2, 2, 2, 2001, 'Mision Imposible', 3, 19.99, 99.99);

INSERT INTO Actors(actor_first_name, actor_last_name, actor_gender) 
VALUES('Leonardo', 'DiCrapio', 'Male'), ('Tom', 'Cruise', 'Male');

INSERT INTO Movie_Cast(movie_id, actor_id)
VALUES(1, 1), (2, 2);

INSERT INTO Rental_Status_Codes(rental_status_description)
VALUES('rented'), ('returned');

INSERT INTO Costumers(costumer_first_name, costumer_last_name, costumer_phone, costumer_email, costumer_address)
VALUES('Alejandro', 'Cabrera', 7471200222, 'al.cabrer4@icloud.com', 'Escorpion, 12'), ('Victor', 'Garcia', 5567890123, 'vicgrv@gmail.com', 'Jalapa, 33');

INSERT INTO Costumer_Rentals(costumer_id, movie_id, rental_status_code, rental_date_out, rental_date_returned, rental_amount_due)
VALUES(1, 1, 1, '2021-12-03', '2021-12-07', 195), (2, 2, 2, '2020-12-10', '2020-12-20', 195);

INSERT INTO Payment_Methods(payment_method_description)
VALUES('VISA'), ('MASTERCARD'), ('AMEX'), ('CASH'), ('DEBIT');

INSERT INTO Accounts(costumer_id, payment_method_code, account_name)
VALUES(1, 1, 'a1s2d3'), (2, 2, 'q0w9e8');

INSERT INTO Transaction_Types(transaction_type_description)
VALUES('payment'), ('refund');

INSERT INTO Financial_Transactions(account_id, item_rental_id, transaction_type_code, transaction_date, transaction_ammount)
VALUES(1, 1, 2, '2021-12-06', -195), (2, 2, 1, '2020-12-20', 195);