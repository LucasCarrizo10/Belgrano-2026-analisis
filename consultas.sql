-- Resultados generales (SQLite)
SELECT torneo, COUNT(*) AS pj, SUM(puntos) AS puntos,
       SUM(goles_favor) AS gf, SUM(goles_contra) AS gc,
       SUM(valla_invicta) AS vallas_invictas,
       ROUND(100.0*SUM(puntos)/(3*COUNT(*)),2) AS porcentaje_puntos
FROM partidos GROUP BY torneo;

-- Últimos cuatro partidos en orden real, no por jornada nominal.
SELECT torneo, SUM(puntos) AS puntos_cierre,
       SUM(goles_favor) AS gf, SUM(goles_contra) AS gc
FROM partidos WHERE orden_disputado >= 13 GROUP BY torneo;

-- Mismos rivales, con localía invertida: comparación descriptiva.
SELECT a.rival, a.condicion AS condicion_apertura,
       c.condicion AS condicion_clausura,
       a.puntos AS puntos_apertura, c.puntos AS puntos_clausura,
       c.puntos-a.puntos AS cambio_puntos
FROM partidos a JOIN partidos c ON a.rival=c.rival
WHERE a.torneo='Apertura' AND c.torneo='Clausura'
ORDER BY cambio_puntos, a.rival;

-- Cuatro bloques de cuatro partidos.
SELECT torneo, CAST((orden_disputado-1)/4 AS INTEGER)+1 AS bloque,
       SUM(puntos) AS puntos
FROM partidos GROUP BY torneo,bloque ORDER BY torneo,bloque;

-- Volumen de remates recibidos en el cierre.
SELECT torneo, COUNT(*) AS partidos, SUM(remates_recibidos) AS remates,
       ROUND(AVG(remates_recibidos),2) AS por_partido
FROM remates_cierre GROUP BY torneo;

-- Precisión y conversión de los delanteros del Clausura.
SELECT jugador, remates, al_arco, goles,
       ROUND(100.0*al_arco/remates,1) AS precision_pct,
       ROUND(100.0*goles/remates,1) AS conversion_pct
FROM delanteros_clausura;

-- Conversión del grupo: cociente de sumas, no promedio de porcentajes individuales.
SELECT SUM(remates) AS remates, SUM(al_arco) AS al_arco, SUM(goles) AS goles,
       ROUND(100.0*SUM(al_arco)/SUM(remates),1) AS precision_pct,
       ROUND(100.0*SUM(goles)/SUM(remates),1) AS conversion_pct
FROM delanteros_clausura;
