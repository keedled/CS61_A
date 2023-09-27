.read data.sql


CREATE TABLE bluedog AS
    select color,pet from students where color = "blue" and pet = "dog";
--     SELECT color, pet FROM students WHERE color='blue' AND pet='dog';
-- CREATE TABLE bluedog AS
-- SELECT color, pet
-- FROM student
-- WHERE color = "blue" AND pet = "cat";

CREATE TABLE bluedog_songs AS
--   SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
    select color,pet,song from students where color = "blue" and pet = "dog";

CREATE TABLE matchmaker AS
--   SELECT "REPLACE THIS  LINE WITH YOUR SOLUTION";
    select a.pet,b.song,a.color,b.color
        from students as a,students as b where a.pet = b.pet and a.song = b.song and a.time < b.time;

CREATE TABLE sevens AS
--   SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
  select a.seven from students as a,numbers as b
                 where a.number = 7 and b.'7' = 'True' and a.time = b.time ;

CREATE TABLE favpets AS
--   SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
    select pet,count(*) as count from students group by pet order by count desc limit 10;

CREATE TABLE dog AS
--   SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
    select pet,count(*) as count from students where pet = 'dog' group by pet ;

CREATE TABLE bluedog_agg AS
--   SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
    select song,count(*) as count from bluedog_songs group by song order by count desc;

CREATE TABLE instructor_obedience AS
--   SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
    select seven,instructor,count(*) from students where seven = '7' group by instructor;
