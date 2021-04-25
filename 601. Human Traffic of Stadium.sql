/* Write your T-SQL query statement below */

-- Table: Stadium

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | visit_date    | date    | PK
-- | people        | int     |
-- +---------------+---------+

-- Write an SQL query to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.
-- Return the result table ordered by visit_date in ascending order.


-- given:
-- visit dates unique
-- id's sequential?

-- sub query / CTE?
-- unbounded preceding?
    -- THREE or more allows us to partition using a preceding following
    -- edge case of [1,1,1]?
    -- UNBOUNDED PRECEDING tells the windowing function and aggregrates to use the current value, and all values in the partition before the current value.

-- LEAD() LAG() lets us perform a look ahead / behind?
    -- basically a cursor?


--------------
-- FIRST PASS
--------------

-- CTE using row number diffs on an (assumed sequentially increasing id column) 


-- with RN_gte100 AS           -- CTE of each row with >=100 and relative distance from last >=100 (might get problematic if large gaps in ids with 100)
-- (
-- SELECT
    
--     (id - ROW_NUMBER() OVER(order by visit_date)) as rn_diff,
--     *
-- FROM
--     Stadium 
-- WHERE 
--     people>99
-- )SELECT 
--     id,
--     visit_date,
--     people 
--  FROM RN_gte100
--  WHERE
--     rn_diff in(             -- if the diff has a count >2 then it has 3+ sequential rows with >100
--         SELECT rn_diff 
--         FROM RN_gte100
--         group by rn_diff having count(rn_diff) > 2
--     )
--  ORDER BY visit_date ASC
 


-- speed is sloooow.
-- increase by not materialising table using WITH or rn_diff IN inside WHERE clause



SELECT
    id,
    visit_date,
    people
FROM(
    SELECT id, visit_date, people, count(*) OVER (partition by diff) as cnt
    FROM(
        select id, visit_date, people,  (id - row_number() over(order by visit_date)) as diff
        FROM stadium where people >99
        ) d  --rn_diff
    ) c -- count partitioned instead of group and in rn_diff
    where cnt>2
    order by visit_date