SELECT S.kepler_id, S.t_eff, S.radius
FROM Star S
LEFT OUTER JOIN Planet P USING(kepler_id)
WHERE P.koi_name IS NULL
ORDER BY t_eff DESC;