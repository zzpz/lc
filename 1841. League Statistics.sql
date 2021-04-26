/* Write your T-SQL query statement below */

-- Write an SQL query to report the statistics of the league. The statistics should be built using the played matches where the winning team gets three points and the losing team gets no points. If a match ends with a draw, both teams get one point.

-- +----------------+---------+
-- | Column Name    | Type    |
-- +----------------+---------+
-- | team_id        | int     |
-- | team_name      | varchar |
-- +----------------+---------+

-- +-----------------+---------+
-- | Column Name     | Type    |
-- +-----------------+---------+
-- | home_team_id    | int     |
-- | away_team_id    | int     |
-- | home_team_goals | int     |
-- | away_team_goals | int     |
-- +-----------------+---------+

-- determine points and select from there?


-- step 1, bring home and away matches under single 'matches' column
with
 home_away as
(
Select
home_team_id as [team_id],
home_team_goals as [goal_for],
away_team_goals as [goal_against],
home_team_goals - away_team_goals as goal_diff,
    CASE
        WHEN home_team_goals > away_team_goals THEN 3
        WHEN home_team_goals = away_team_goals THEN 1
        ELSE 0
    END as points
from Matches as home -- as a home team
UNION ALL
(
Select
away_team_id as [team_id],
away_team_goals as [goal_for],
home_team_goals as [goal_against],
away_team_goals - home_team_goals as goal_diff,
    CASE
        WHEN away_team_goals > home_team_goals THEN 3
        WHEN away_team_goals = home_team_goals THEN 1
        ELSE 0
    END as points
from Matches as away -- as an away team
) 
)

-- step 2, join the rolled up stats back to team name
select 
    team_name,
    matches_played,
    points,
    goal_for,
    goal_against,
    goal_diff
from
    Teams 
    join
    (
    select
        team_id,
        count(team_id) as matches_played,
        sum(points) as points,
        sum(goal_for) as goal_for,
        sum(goal_against) as goal_against,
        sum(goal_diff) as goal_diff
    FROM
        home_away
    group by
        team_id
    ) as stats
    on 
    Teams.team_id = stats.team_id
    ORDER BY
    points DESC
    , goal_diff DESC
    , team_name