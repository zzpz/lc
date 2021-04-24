-- The Employee table holds all employees. Every employee has an Id, and there is also a column for the department Id.
-- The Department table holds all departments of the company.

-- Write a SQL query to find employees who earn the top three salaries in each of the department. For the above tables, your SQL query should return the following rows (order of rows does not matter).


/* Write your T-SQL query statement below */

-- top 3 salry in each department


--  execute this function for each row in this table


select d.name [Department] ,tvf.name [Employee], tvf.salary [Salary] from department d
CROSS APPLY(
select 
    dense_rank() OVER (order by salary DESC) drank,
    name,
    salary
FROM
    Employee e
    where e.departmentID = d.id
) tvf
where tvf.drank < 4

-- have to deal with duplicates using a rank order --> can't just top 3 
