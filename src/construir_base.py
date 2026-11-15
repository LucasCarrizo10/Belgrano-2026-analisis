"""Reconstruye la base y sus indicadores con Python estándar. Ejecutar desde cualquier carpeta."""
from pathlib import Path
import json, sqlite3
ROOT=Path(__file__).resolve().parents[1]
rows=json.loads((ROOT/'datos/partidos_fuente.json').read_text())
assert len(rows)==32
assert len({(r['torneo'],r['jornada']) for r in rows})==32
summaries=[]
for torneo,expected in [('Apertura',(26,17,13)),('Clausura',(23,17,15))]:
    group=sorted([r for r in rows if r['torneo']==torneo],key=lambda r:r['fecha'])
    assert len(group)==16 and {r['jornada'] for r in group}==set(range(1,17))
    acumulados=0
    for order,r in enumerate(group,1):
        gf,gc=r['goles_favor'],r['goles_contra']
        assert gf>=0 and gc>=0 and r['condicion'] in ['Local','Visitante']
        r['resultado']='G' if gf>gc else 'E' if gf==gc else 'P'
        r['puntos']=3 if gf>gc else 1 if gf==gc else 0
        acumulados+=r['puntos']
        r['orden_disputado']=order
        r['puntos_acumulados']=acumulados
        r['valla_invicta']=int(gc==0)
        r['sin_marcar']=int(gf==0)
    totals=tuple(sum(r[k] for r in group) for k in ['puntos','goles_favor','goles_contra'])
    assert totals==expected,(torneo,totals)
    summary={'torneo':torneo,'partidos':16,'puntos':totals[0],'gf':totals[1],'gc':totals[2],
             'ganados':sum(r['resultado']=='G' for r in group),'empatados':sum(r['resultado']=='E' for r in group),
             'perdidos':sum(r['resultado']=='P' for r in group),'vallas_invictas':sum(r['valla_invicta'] for r in group),
             'sin_marcar':sum(r['sin_marcar'] for r in group),'ultimos_4_puntos':sum(r['puntos'] for r in group[-4:]),
             'puntos_local':sum(r['puntos'] for r in group if r['condicion']=='Local'),
             'puntos_visitante':sum(r['puntos'] for r in group if r['condicion']=='Visitante')}
    summaries.append(summary)
rows.sort(key=lambda r:(r['torneo'],r['orden_disputado']))
for filename,data in [('partidos.json',rows),('resumen.json',summaries)]:
    (ROOT/'datos'/filename).write_text(json.dumps(data,ensure_ascii=False,indent=2))
con=sqlite3.connect(ROOT/'datos/belgrano_2026.sqlite')
with con:
    con.execute('DROP TABLE IF EXISTS partidos')
    keys=list(rows[0]); ints={k for k,v in rows[0].items() if isinstance(v,int)}
    con.execute('CREATE TABLE partidos ('+', '.join(k+(' INTEGER' if k in ints else ' TEXT') for k in keys)+', PRIMARY KEY(torneo,jornada))')
    con.executemany('INSERT INTO partidos VALUES ('+','.join('?' for k in keys)+')',[[r[k] for k in keys] for r in rows])
con.close()
print(json.dumps(summaries,ensure_ascii=False,indent=2))
print('Validación correcta: 32 partidos; 16 jornadas por torneo; sin duplicados; totales conciliados.')

# Carga de indicadores complementarios y exportaciones para herramientas BI.
import csv
extra={name:json.loads((ROOT/'datos'/f'{name}.json').read_text()) for name in
       ['metricas_torneo','remates_cierre','delanteros_clausura']}
for r in extra['delanteros_clausura']:
    assert 0 <= r['goles'] <= r['al_arco'] <= r['remates']
    r['precision_pct']=round(100*r['al_arco']/r['remates'],2)
    r['conversion_pct']=round(100*r['goles']/r['remates'],2)
for t in ['Apertura','Clausura']:
    closing=[r for r in extra['remates_cierre'] if r['torneo']==t]
    assert len(closing)==4
    dates={r['fecha'] for r in rows if r['torneo']==t and r['orden_disputado']>=13}
    assert {r['fecha_local'] for r in closing}==dates
for m in extra['metricas_torneo']:
    assert round(m['remates_totales']/m['partidos'],1 if m['remates_promedio_redondeado'] else 2)==m['remates_por_partido']
with sqlite3.connect(ROOT/'datos/belgrano_2026.sqlite') as con:
    for name,data in extra.items():
        normalized=[{k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()} for r in data]
        keys=list(dict.fromkeys(k for r in normalized for k in r))
        types={k:'INTEGER' if isinstance(next((r[k] for r in normalized if r.get(k) is not None),None),(int,bool)) else 'REAL' if isinstance(next((r[k] for r in normalized if r.get(k) is not None),None),float) else 'TEXT' for k in keys}
        con.execute(f'DROP TABLE IF EXISTS {name}')
        con.execute(f'CREATE TABLE {name} ('+', '.join(f'{k} {types[k]}' for k in keys)+')')
        con.executemany(f'INSERT INTO {name} VALUES ('+','.join('?' for _ in keys)+')',[[r.get(k) for k in keys] for r in normalized])
        with (ROOT/'datos'/f'{name}.csv').open('w',newline='',encoding='utf-8-sig') as f:
            writer=csv.DictWriter(f,fieldnames=keys);writer.writeheader();writer.writerows(normalized)
with (ROOT/'datos/partidos.csv').open('w',newline='',encoding='utf-8-sig') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
print('Carga completa: resultados, indicadores, remates del cierre y delanteros. Exportaciones CSV disponibles.')
