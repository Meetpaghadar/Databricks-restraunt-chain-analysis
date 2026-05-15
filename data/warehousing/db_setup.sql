-- =========================================
-- Create Schema
-- =========================================

CREATE SCHEMA restaurant;

-- =========================================
-- Customers Table
-- =========================================

CREATE TABLE restaurant.customers (
    customer_id VARCHAR(256) PRIMARY KEY,
    name VARCHAR(256),
    email VARCHAR(256),
    phone VARCHAR(256),
    city VARCHAR(256),
    join_date DATE
);

-- =========================================
-- Restaurants Table
-- =========================================

CREATE TABLE restaurant.restaurants (
    restaurant_id VARCHAR(256) PRIMARY KEY,
    name VARCHAR(256),
    city VARCHAR(256),
    country VARCHAR(256),
    address VARCHAR(MAX),
    opening_date DATE,
    phone VARCHAR(256)
);

-- =========================================
-- Historical Orders Table
-- =========================================

CREATE TABLE restaurant.historical_orders (
    order_id VARCHAR(256) PRIMARY KEY,
    order_timestamp DATETIME2,
    restaurant_id VARCHAR(256),
    customer_id VARCHAR(256),
    order_type VARCHAR(256),
    items VARCHAR(MAX),
    total_amount DECIMAL(10,2),
    payment_method VARCHAR(256),
    order_status VARCHAR(256)
);

-- =========================================
-- Reviews Table
-- =========================================

CREATE TABLE restaurant.reviews (
    review_id VARCHAR(256) PRIMARY KEY,
    order_id VARCHAR(256),
    customer_id VARCHAR(256),
    restaurant_id VARCHAR(256),
    review_text VARCHAR(MAX),
    rating INT,
    review_timestamp DATETIME2
);

-- =========================================
-- Menu Items Table
-- =========================================

CREATE TABLE restaurant.menu_items (
    restaurant_id VARCHAR(256),
    item_id VARCHAR(256),
    name VARCHAR(256),
    category VARCHAR(256),
    price DECIMAL(10,2),
    ingredients VARCHAR(256),
    is_vegetarian BIT,
    spice_level VARCHAR(256),
    PRIMARY KEY (restaurant_id, item_id)
);

-- =========================================
-- Enable Change Tracking at Database Level
-- =========================================

-- ALTER DATABASE db_sqlserver
-- SET CHANGE_TRACKING = ON
-- (CHANGE_RETENTION = 14 DAYS, AUTO_CLEANUP = ON);

-- =========================================
-- Enable Change Tracking for Tables
-- =========================================

ALTER TABLE restaurant.customers
ENABLE CHANGE_TRACKING;

ALTER TABLE restaurant.restaurants
ENABLE CHANGE_TRACKING;

ALTER TABLE restaurant.historical_orders
ENABLE CHANGE_TRACKING;

ALTER TABLE restaurant.reviews
ENABLE CHANGE_TRACKING;

ALTER TABLE restaurant.menu_items
ENABLE CHANGE_TRACKING;