-- Question 1: Count titles by type
SELECT type, COUNT(*) AS total_titles
FROM titles
GROUP BY type;
-- Question 2: Top 10 highest rated titles
SELECT title, imdb_score
FROM titles
WHERE imdb_score IS NOT NULL
ORDER BY imdb_score DESC
LIMIT 10;
-- Question 3: Average IMDb score by type
SELECT 
    type,
    ROUND(AVG(imdb_score)::numeric, 2) AS avg_score
FROM titles
WHERE imdb_score IS NOT NULL
GROUP BY type;

--Question 4: Top 10 Actors with the most appearances
SELECT name, COUNT(*) AS appearances
FROM credits
WHERE role ='ACTOR'
GROUP BY name
ORDER BY appearances DESC
LIMIT 10;
--Question 5: Directors with the most titles
SELECT name, COUNT(DISTINCT id) AS total_titles
FROM credits
WHERE role='DIRECTOR'
GROUP BY name
ORDER BY total_titles DESC
LIMIT 10;
--Question 6:Top rated titles with their directors
SELECT t.title, t.imdb_score, c.name AS director
FROM titles t
JOIN credits c
ON t.id = c.id
WHERE c.role = 'DIRECTOR'
AND t.imdb_score IS NOT NULL
ORDER BY t.imdb_score DESC
LIMIT 10;


--Question 7:Most common genres
SELECT 
    TRIM(g.genre) AS genre,
    COUNT(*) AS total_titles
FROM titles t
CROSS JOIN LATERAL unnest(
    string_to_array(
        replace(replace(replace(t.genres,'[',''),']',''),'''',''),
        ','
    )
) AS g(genre)
WHERE t.genres <> '[]'
GROUP BY TRIM(g.genre)
ORDER BY total_titles DESC
LIMIT 10;
--Question 8:Titles released per year
SELECT release_year, COUNT(*) AS total_titles
FROM titles
GROUP BY release_year
ORDER BY release_year;
--Question 9: Average IMDb score by year
SELECT 
    release_year,
    ROUND(AVG(imdb_score)::numeric, 2) AS avg_score
FROM titles
WHERE imdb_score IS NOT NULL
GROUP BY release_year
ORDER BY release_year;

--Question 10:Best directors by average IMDB score
 SELECT 
    c.name AS director,
    ROUND(AVG(t.imdb_score)::numeric, 2) AS avg_score,
    COUNT(DISTINCT t.id) AS total_titles
FROM credits c
JOIN titles t
ON c.id = t.id
WHERE c.role = 'DIRECTOR'
AND t.imdb_score IS NOT NULL
GROUP BY c.name
HAVING COUNT(DISTINCT t.id) >= 3
ORDER BY avg_score DESC
LIMIT 10;
