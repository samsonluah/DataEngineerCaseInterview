SELECT
    manufacturers.name,
    COUNT(*) AS quantity_sold
FROM manufacturers
JOIN cars ON manufacturers.id = cars.manufacturer
JOIN transactions ON car.id = transactions.car_id
WHERE date_trunc('month', transactions.transaction_date) = date_trunc('month', CURRENT_DATE())
GROUP by manufacturers.name
ORDER BY quantity_sold DESC
LIMIT 3;