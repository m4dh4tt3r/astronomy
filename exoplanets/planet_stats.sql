SELECT MIN(radius),
    MAX(radius),
    AVG(radius),
    STDDEV(radius)
FROM Planet
WHERE kepler_name IS NULL;