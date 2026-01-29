SELECT MAX(CASE WHEN rk = 2 THEN salary END) AS SecondHighestSalary
FROM (
  SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rk
  FROM Employee
) t;