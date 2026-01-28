# Write your MySQL query statement below
SELECT a.firstName, a.lastName, b.city, b.state FROM Person a
LEFT OUTER JOIN Address b
ON a.personId = b.personId