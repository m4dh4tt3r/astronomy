SELECT p.koi_name, p.radius, s.radius
FROM Star as s
JOIN Planet as p USING(kepler_id)
WHERE s.kepler_id IN (
  SELECT kepler_id
  FROM Star
  ORDER BY radius DESC
  LIMIT 5
);