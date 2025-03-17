CREATE TABLE manufacturers (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE salespersons (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20)
);

CREATE TABLE cars (
    id INT PRIMARY KEY,
    manufacturer INT REFERENCES manufacturers(id),
    model_name VARCHAR(100) NOT NULL,
    serial_number VARCHAR(100) NOT NULL UNIQUE,
    weight DECIMAL(10, 2),
    price DECIMAL(10,2)
);

CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20)
);

CREATE TABLE transactions (
    id INT PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    salesperson_id INT REFERENCES salespersons(id),
    car_id INT REFERENCES cars(id),
    transaction_date timestamp
);