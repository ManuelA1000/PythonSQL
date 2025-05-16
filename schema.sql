#'order_id', 'order_date', 'ship_mode', 'segment', 'country', 'city',
       #'state', 'postal_code', 'region', 'category', 'sub_category',
       #'product_id', 'quantity', 'discount', 'selling_price', 'profit'
CREATE TABLE IF NOT EXISTS orders (
    order_id VARCHAR(50) PRIMARY KEY,
    order_date DATE,
    ship_mode VARCHAR(20),
    segment VARCHAR(20),
    country VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    region VARCHAR(50),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    product_id VARCHAR(50),
    quantity INTEGER,
    discount DECIMAL(5,2),
    selling_price DECIMAL(10,2),
    profit DECIMAL(10,2)
);
