SELECT
    customers.name,
    SUM(cars.price) as total_spending
FROM customers 
JOIN transactions
ON customers.id = transactions.customer_id
JOIN cars 
ON transactions.car_id = car.id
GROUP BY customers.id;