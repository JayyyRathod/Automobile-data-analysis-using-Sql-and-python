create database Automobile;

use Automobile;

select * from Automobile_data_mileage ;
select * from Automobile_data_price ;

-- Que 1. What is the average price of automobiles for each company? --

select company , avg(price) as avg_price 
from Automobile_data_price
group by company;

-- Que 2. What are the total number of companies in the database?--

select count( distinct company)
from Automobile_data_price;

 -- Que 3.What is the lowest price for an automobile in each company?--

 select company , min(price) as min_price 
 from Automobile_data_price
 group by company;

-- Que 4. Which automobile has the lowest mileage? --


SELECT  top 1 company, average_mileage
FROM Automobile_data_mileage
ORDER BY average_mileage ASC;

-- Que 5. List all companies that have automobiles priced above price 20000.--

select distinct company , price
from Automobile_data_price
where price > 20000;

-- Que 6. Which company offers the highest mileage on average?--

SELECT top 1 company, AVG(average_mileage) AS avg_mileage
FROM Automobile_data_mileage
GROUP BY company
ORDER BY avg_mileage DESC ;

-- Que 7. Which company provides the best price-to-mileage ratio? --

SELECT top 1 p.company, AVG(p.price / m.average_mileage) AS price_to_mileage_ratio
FROM Automobile_data_price AS p
JOIN Automobile_data_mileage AS m ON p.company = m.company
GROUP BY p.company
ORDER BY price_to_mileage_ratio ASC;


