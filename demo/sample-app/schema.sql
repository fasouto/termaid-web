CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    sku TEXT UNIQUE NOT NULL,
    price_cents INTEGER NOT NULL
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    status TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL
);

CREATE TABLE order_items (
    order_id INTEGER NOT NULL REFERENCES orders(id),
    product_id INTEGER NOT NULL REFERENCES products(id),
    quantity INTEGER NOT NULL,
    PRIMARY KEY (order_id, product_id)
);
