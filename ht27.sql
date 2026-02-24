CREATE DATABASE IF NOT EXISTS lesson27_hw;
USE lesson27_hw;
CREATE TABLE IF NOT EXISTS migrations (
    id INT PRIMARY KEY,
    distance INT,
    days INT
);

INSERT INTO migrations (id, distance, days) VALUES
(10484, 1000, 107),
(11728, 1531, 56),
(11729, 1370, 37),
(11732, 1622, 62),
(11734, 1491, 58),
(11735, 2723, 82),
(11736, 1571, 52),
(11737, 1957, 92)
;

CREATE TABLE IF NOT EXISTS sea_lions (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    species VARCHAR(100)
);

INSERT INTO sea_lions (id, name, species) VALUES
(10484, 'Ayah', 'Zalophus californianus'),
(11728, 'Spot', 'Zalophus californianus'),
(11729, 'Tiger', 'Zalophus californianus'),
(11732, 'Mabel', 'Zalophus californianus'),
(11734, 'Rick', 'Zalophus californianus'),
(11790, 'Jolee', 'Zalophus californianus')
;

-- INNER CROSS JOIN
SELECT s.id, s.name, m.days, m.distance
FROM migrations m
JOIN sea_lions s ON m.id = s.id
;

-- LEFT OUTER JOIN
SELECT m.id, s.name, m.days, m.distance
FROM migrations m
LEFT JOIN sea_lions s ON m.id = s.id
;

-- RIGHT OUTER JOIN
SELECT s.id, s.name, m.days, m.distance
FROM migrations m
RIGHT JOIN sea_lions s ON m.id = s.id
;
 
-- FULL JOIN
SELECT m.id, s.name, m.days, m.distance
FROM migrations m
LEFT JOIN sea_lions s ON m.id = s.id
UNION
SELECT s.id, s.name, m.days, m.distance
FROM migrations m
RIGHT JOIN sea_lions s ON m.id = s.id
;

SELECT m.id, s.name, m.days, m.distance
FROM migrations m
LEFT JOIN sea_lions s ON m.id = s.id
UNION ALL
SELECT s.id, s.name, m.days, m.distance
FROM migrations m
RIGHT JOIN sea_lions s ON m.id = s.id
;

SELECT m.id, s.name, m.days, m.distance
FROM migrations m
LEFT JOIN sea_lions s ON m.id = s.id
UNION ALL
SELECT s.id, s.name, m.days, m.distance
FROM migrations m
RIGHT JOIN sea_lions s ON m.id = s.id
WHERE m.id IS NULL
;

-- SELECT id FROM sea_lions
-- UNION
-- SELECT id FROM migrations;


-- SELECT id FROM sea_lions
-- UNION ALL
-- SELECT id FROM migrations;

