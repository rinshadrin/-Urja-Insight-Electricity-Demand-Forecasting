CREATE DATABASE electricity_db;
USE electricity_db;

SELECT * FROM electricity_data;

DESCRIBE electricity_data;

SELECT COUNT(*) FROM electricity_data;

SELECT *
FROM electricity_data
ORDER BY `Peak Demand` DESC
LIMIT 5;

SELECT AVG(`Peak Demand`)
FROM electricity_data;

SELECT Year,
       AVG(`Peak Demand`) AS Avg_Demand
FROM electricity_data
GROUP BY Year;