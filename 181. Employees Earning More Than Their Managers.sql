# Write your MySQL query statement below

select 
    e.name as 'Employee' 
from
    employee e left join employee man
        ON e.managerid = man.id
where 
    e.salary > man.salary