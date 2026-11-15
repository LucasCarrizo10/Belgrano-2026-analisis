# Metodología

## Universo y unidad de análisis

Primera División masculina de Argentina: Belgrano de Córdoba, Apertura y Clausura 2026. El universo principal incluye 32 encuentros de fase regular, 16 por torneo. Se excluyen copas y playoffs de los cálculos comparativos. La campaña campeona del Apertura aparece únicamente como contexto editorial.

## Criterios temporales

La jornada nominal no equivale al orden de disputa. La fecha 9 del Apertura, contra Sarmiento, se jugó el 3 de mayo después de la fecha 16. El Clausura también presenta fechas disputadas fuera de su secuencia nominal. Los acumulados y los bloques usan la fecha real.

«Cierre» significa los últimos cuatro partidos disputados de cada fase regular. No equivale necesariamente a las jornadas 13 a 16 del fixture.

## Fórmulas

| Indicador | Cálculo |
|---|---|
| Puntos | 3 victoria; 1 empate; 0 derrota |
| Puntos acumulados | Suma por torneo y orden cronológico |
| Bloque de cuatro | Parte entera de (orden − 1) / 4 + 1 |
| Remates por partido | Remates totales / partidos |
| Variación porcentual | (Clausura − Apertura) / Apertura × 100 |
| Proporción de goles recibidos en el cierre | Goles recibidos últimos 4 / goles recibidos del torneo × 100 |
| Precisión de remates | Tiros al arco / remates × 100 |
| Conversión | Goles / remates × 100 |

Las tasas conjuntas de delanteros se calculan a partir de sumas. Se incluyen penales. Los tiros al arco y los goles no constituyen categorías excluyentes.

## Diccionario

| Campo | Definición |
|---|---|
| `torneo`, `temporada`, `fase` | Identificadores del período y la competición |
| `jornada` | Fecha nominal del fixture |
| `fecha` / `fecha_local` | Día del encuentro en Argentina, YYYY-MM-DD |
| `rival`, `condicion` | Oponente normalizado y localía de Belgrano |
| `goles_favor`, `goles_contra` | Marcador desde la perspectiva de Belgrano |
| `resultado`, `puntos` | Resultado G/E/P y puntos obtenidos |
| `orden_disputado`, `puntos_acumulados` | Secuencia real y acumulado |
| `valla_invicta`, `sin_marcar` | Indicadores binarios, 1 sí y 0 no |
| `remates_recibidos` | Intentos totales del rival, incluidos los que no van al arco |
| `remates_totales`, `remates_por_partido` | Intentos realizados por Belgrano |
| `posesion_promedio_pct` | Promedio publicado por LPF Data |
| `jugador`, `remates`, `al_arco`, `goles` | Totales del jugador en el recorte definido |
| `fuente_url`, `fuente`, `fuentes` | Enlace o lista de enlaces de procedencia |
| `fecha_consulta`, `consulta` | Metadatos de adquisición, fuera del diseño de las filminas |

## Calidad y límites

El procesamiento comprueba unicidad, cantidad de encuentros, marcadores no negativos, resultados conciliados, correspondencia del cierre y coherencia de tasas. Los insumos no rellenan ausencias estadísticas con cero.

Las fuentes y sus divergencias se detallan en [FUENTES.md](docs/FUENTES.md). Las métricas de diferentes proveedores no se consideran idénticas automáticamente. Los totales y porcentajes dependen del recuento seleccionado.

Los cierres son muestras de cuatro partidos con rivales y localías diferentes. No hay ajuste por dificultad del rival, expulsiones, minutos en ventaja o calidad de las ocasiones. La tabla de delanteros se limita a Fernández, Passerini y Gutiérrez en el Clausura; no incluye extremos ni mediapuntas. La conversión no separa el efecto de la calidad de los remates del de su ejecución.

Las conclusiones son descriptivas e incluyen hipótesis explícitas; no estiman causalidad ni probabilidades de salir campeón.
