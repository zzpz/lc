--Given two tables as below, write a query to display the comparison result (higher/lower/same) 
--of the average salary of employees in a department to the company's average salary.

-- | id | employee_id | amount | pay_date   |
-- |----|-------------|--------|------------|
-- | 1  | 1           | 9000   | 2017-03-31 |
-- | 2  | 2           | 6000   | 2017-03-31 |
-- | 3  | 3           | 10000  | 2017-03-31 |
-- | 4  | 1           | 7000   | 2017-02-28 |
-- | 5  | 2           | 6000   | 2017-02-28 |
-- | 6  | 3           | 8000   | 2017-02-28 |

-- | employee_id | department_id |
-- |-------------|---------------|
-- | 1           | 1             |
-- | 2           | 2             |
-- | 3           | 2             |

/* Write your T-SQL query statement below */

-- ~twice as fast, less table scans, possible to leverage indexes on salary
SELECT distinct
pay_month,
department_id,
CASE 
    WHEN dpay > cpay THEN 'higher'
    WHEN dpay < cpay THEN 'lower'
    ELSE 'same'
END as comparison
FROM
( 
    select  LEFT(pay_date,7) as pay_month, department_id,
    avg(amount) over (partition by LEFT(pay_date,7)) as cpay, --partition by a better set
    avg(amount) over (partition by LEFT(pay_date,7),department_id) as dpay
    from
    salary s
    join
        employee e
    on e.employee_id = s.employee_id
) g



-- ~2xSLOWER
-- has to scan multiple tables throughout
-- has to join unindexed tables (no pk)

-- with paid
-- as(

-- select 
-- format(pay_date,N'yyyy-MM') pay_month,
-- department_id,
-- amount
-- from
--     salary s
-- join
--     employee e
-- on e.employee_id = s.employee_id
-- ),
-- a as
-- (
-- select 
-- pay_month,department_id, avg(amount) as numba
-- from paid
-- group by pay_month,department_id
-- ),
-- fin as
-- (
-- select a.*, b.numbo from
-- a
-- left join
-- (select
-- pay_month,
-- avg(amount) as numbo
-- from paid
-- group by pay_month) b
-- on a.pay_month = b.pay_month
-- )
-- select pay_month,department_id,
--     CASE 
--     WHEN numba > numbo THEN 'higher'
--     WHEN numba < numbo THEN 'lower'
--     ELSE 'same'
--     END as comparison
-- from fin