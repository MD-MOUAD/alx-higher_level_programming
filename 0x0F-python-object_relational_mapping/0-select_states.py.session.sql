
-- @block
SELECT cities.name
FROM `cities` INNER JOIN `states` ON cities.state_id = states.id
WHERE states.name LIKE BINARY 'Texas' ORDER BY cities.id ASC;
