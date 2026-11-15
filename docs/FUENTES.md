# Fuentes y trazabilidad

| Fuente | Uso | Alcance |
|---|---|---|
| [AFA: campaña de Belgrano campeón](https://www.afa.com.ar/historiadel/posts/la-campana-de-belgrano-de-cordoba-campeon-del-torneo-apertura-2026) | Resultados del Apertura y antecedente del título | Se separa fase regular de playoffs |
| [TyC: Apertura](https://www.tycsports.com/liga-profesional-de-futbol/fixture-del-apertura-2026-calendario-de-partidos-y-resultados-id703472.html) | Cotejo de marcadores | Fase regular |
| [TyC: Clausura](https://www.tycsports.com/liga-profesional-de-futbol/fixture-del-clausura-2026-calendario-de-partidos-y-resultados-id750943.html) | Calendario y resultados | Fase regular |
| [LPF Data: cierre del Apertura](https://www.ligaprofesional.ar/wp-content/uploads/2026/05/LPF-Data-Fecha-9-Torneo-Apertura-Mercado-Libre-2026.pdf) | Posesión y remates | Páginas 8 y 13; cobertura de 16 PJ en página 9 |
| [LPF Data: Clausura fecha 16](https://www.ligaprofesional.ar/wp-content/uploads/2026/11/LPF-Data-Prensa-Fecha-16.pdf) | Posesión y promedio de remates | Páginas 4 y 9 |
| [Statz: remates de Belgrano](https://statz.ai/team/belgrano/shots-total) | Remates realizados y recibidos por partido | Filtrado por torneo y fase |
| [MatchScan: Belgrano](https://matchscan.co/en/database/liga-profesional-argentina/belgrano) | Cotejo de 234 remates y totales del Clausura | 16 partidos |
| [OffsideData: Belgrano](https://offsidedata.com/equipo/belgrano) | Cotejo de indicadores agregados | Se distingue torneo de acumulado anual |

## Delanteros del Clausura

- [Statz: Nicolás Fernández](https://statz.ai/player/nicolas-fernandez/394568): tabla por partido, 33 remates hasta River. [KiqStat: Fernández](https://www.kiqstat.app/football/player/nicolas-fernandez--c4ed5400-9aac-501b-821b-2fe60b3a103d) aporta el último partido ante Gimnasia: un remate y cero tiros al arco. Total del recuento seleccionado: 34 remates, 12 al arco, 2 goles.
- [Scout Picks: Passerini](https://scoutpicks.app/es/jugadores/liga-profesional-argentina/lucas-passerini-396373): 15 actuaciones del Clausura. [KiqStat: Passerini](https://www.kiqstat.app/football/player/lucas-passerini--d8ba0639-7ca7-54ea-aa7a-b4766fa65483) permite completar y cotejar las 16, incluyendo Gimnasia (3 remates y 1 al arco). Total: 33, 14 y 5 goles.
- [Statz: Gutiérrez](https://statz.ai/player/lautaro-gutierrez/37748127): suma de las nueve actuaciones de Clausura. Total: 6 remates, 4 al arco y 1 gol.

Los totales anuales de las fichas no se utilizan como totales del Clausura. El registro estructurado se conserva en `datos/delanteros_clausura.json`.

## Criterios ante discrepancias

**Remates recibidos:** se usa Statz para los ocho encuentros del cierre. Barracas figura con 21 remates en Statz y con 20 en [Tinku](https://tinku.lat/matches/belgrano-cordoba-vs-barracas-central-2026-11-01/stats). Se conserva una fuente homogénea para esta comparación. El total de 62 no es un recuento universal entre proveedores.

**Fernández:** KiqStat/FotMob registra 35 remates en el Clausura; Statz/Scout Picks registra uno menos ante Estudiantes de Río Cuarto. El análisis adopta 34 y explicita esa elección. Con el criterio KiqStat, el grupo de tres delanteros sumaría 74 remates, con 40,5% al arco y 10,8% de conversión, frente a 73, 41,1% y 11,0% en el recuento presentado.

**Remates totales del equipo:** 234 procede de la suma de los partidos en Statz y del total publicado por MatchScan, no de multiplicar 14,6 por 16. Ese producto no recuperaría necesariamente un total exacto.

**Fechas:** se usa el calendario local de Argentina. Algunas páginas muestran un día posterior para partidos nocturnos. El cruce se realiza también por rival, localía y marcador.

**Tiros al arco del equipo:** no se utiliza un promedio comparativo global por diferencias entre fuentes. Los tiros al arco de la tabla de delanteros son un recorte específico, con fuentes propias.

## Identidad visual

[Escudo de Belgrano](https://img.sofascore.com/api/v1/team/3203/image). Se utiliza para identificar al club; no implica afiliación ni autoría institucional del informe.
