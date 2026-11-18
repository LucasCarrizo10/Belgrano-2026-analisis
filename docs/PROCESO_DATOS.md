# Obtención y preparación de los datos

## Extracción y estructuración

Recopilé resultados y estadísticas de páginas públicas y de informes PDF. Para los marcadores usé la campaña publicada por AFA y los fixtures de TyC Sports. Para posesión y remates agregados consulté LPF Data. Los registros de remates por partido y por jugador proceden de las fuentes detalladas en `FUENTES.md`.

Los documentos de LPF Data se descargaron para leer su texto con pdfplumber y verificar visualmente los indicadores en las páginas correspondientes. Como los formatos difieren entre torneos, se seleccionaron las métricas comparables y se transcribieron sus valores a JSON. No se aplicó una extracción automática general de todas las tablas del PDF.

Las tablas web se consultaron y sus hechos relevantes se estructuraron en JSON. Se conserva la URL y el alcance de cada fuente; los datos no proceden de las filminas de referencia. Los enlaces son rastreables, pero no se distribuyen copias completas de artículos de terceros.

## Transformación en Python

`src/construir_base.py` lee los insumos y realiza las siguientes operaciones:

1. Valida que haya 32 partidos y 16 jornadas distintas por torneo.
2. Ordena por fecha real y asigna `orden_disputado`.
3. Calcula resultado, puntos, acumulado, valla invicta y encuentros sin marcar.
4. Resume resultados generales y puntos del cierre.
5. Comprueba la correspondencia entre los ocho registros de remates recibidos y los últimos cuatro encuentros de cada fase.
6. Calcula precisión y conversión de los delanteros y comprueba que goles ≤ tiros al arco ≤ remates.

Los nombres de rivales, fechas y localía se normalizaron al estructurar los insumos. Los goles se expresan desde la perspectiva de Belgrano, incluso cuando juega de visitante. Los valores numéricos usan punto decimal en JSON y coma en la presentación.

## Carga en SQLite

La base `datos/belgrano_2026.sqlite` contiene cuatro tablas:

| Tabla | Granularidad | Filas |
|---|---|---:|
| `partidos` | Partido de Belgrano en fase regular | 32 |
| `metricas_torneo` | Torneo | 2 |
| `remates_cierre` | Partido del cierre | 8 |
| `delanteros_clausura` | Jugador seleccionado en el Clausura | 3 |

La clave de `partidos` es torneo + jornada. El script reconstruye las tablas a partir de los insumos: ejecutarlo varias veces no acumula duplicados. Los CSV se exportan con codificación UTF-8 con BOM para facilitar su lectura en Excel. Las listas de fuentes y páginas se serializan como texto JSON cuando se cargan en SQLite o CSV.

## Visualización y publicación

`src/crear_informe.py` usa Matplotlib y NumPy para calcular y dibujar las curvas de puntos y los bloques. ReportLab compone el PDF de seis páginas. Los totales de remates recibidos y las filas de delanteros se leen desde JSON. El relato y parte de las etiquetas del carrusel están definidos para este recorte de 2026; ante otro período se deben revisar también los textos.

Poppler convierte el PDF en imágenes PNG de 1080 × 1350. Las páginas se inspeccionan visualmente para comprobar legibilidad, márgenes y coherencia de colores. Apertura se representa en negro y Clausura en celeste.
