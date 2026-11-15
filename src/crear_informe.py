from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
ROOT=Path(__file__).resolve().parents[1]
rows=json.loads((ROOT/'datos/partidos.json').read_text())
NAVY='#101820'; BLUE='#47B9E8'; BLACK='#101010'; BG='#F3F9FC'; GRAY='#465D69'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'text.color':NAVY,'axes.labelcolor':GRAY,'xtick.color':GRAY,'ytick.color':GRAY,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,'axes.spines.bottom':False})
blocks={}; groups={}
for t in ['Apertura','Clausura']:
 a=sorted([r for r in rows if r['torneo']==t],key=lambda r:r['orden_disputado']);groups[t]=a
 blocks[t]=[sum(r['puntos'] for r in a[i:i+4]) for i in range(0,16,4)]
fig,ax=plt.subplots(figsize=(9,5),facecolor=BG);ax.set_facecolor(BG)
x=np.arange(4)
for t,off,col in [('Apertura',-.19,BLACK),('Clausura',.19,BLUE)]:
 bars=ax.bar(x+off,blocks[t],.34,color=col,label=t)
 ax.bar_label(bars,padding=8,fontsize=20,fontweight='bold')
ax.set_xticks(x,['Partidos 1–4','Partidos 5–8','Partidos 9–12','Partidos 13–16']);ax.set_ylim(0,12);ax.set_yticks([0,3,6,9,12]);ax.set_ylabel('Puntos (máximo: 12)');ax.grid(axis='y',alpha=.13);ax.set_axisbelow(True);ax.legend(frameon=False,ncol=2,loc='upper left',bbox_to_anchor=(0,1.15));fig.tight_layout();fig.savefig(ROOT/'graficos/bloques.png',dpi=180);plt.close(fig)
fig,ax=plt.subplots(figsize=(9,5),facecolor=BG);ax.set_facecolor(BG)
for t,col in [('Apertura',BLACK),('Clausura',BLUE)]:
 a=groups[t];y=[0]+[r['puntos_acumulados'] for r in a];ax.plot(range(17),y,color=col,marker='o',lw=3,label=t);ax.text(16.25,y[-1],str(y[-1]),color=col,fontsize=20,weight='bold',va='center')
ax.axvspan(12,16,alpha=.07,color=BLUE);ax.set_xlim(0,17.2);ax.set_ylim(0,30);ax.set_xticks([0,4,8,12,16]);ax.set_ylabel('Puntos acumulados');ax.set_xlabel('Partidos disputados, en orden cronológico');ax.grid(axis='y',alpha=.13);ax.legend(frameon=False,loc='upper left');fig.tight_layout();fig.savefig(ROOT/'graficos/evolucion.png',dpi=180);plt.close(fig)
font_dir=ROOT/'recursos/fuentes'
if not (font_dir/'DejaVuSans.ttf').exists(): font_dir=Path('/usr/share/fonts/truetype/dejavu')
font=str(font_dir/'DejaVuSans.ttf');bold=str(font_dir/'DejaVuSans-Bold.ttf')
pdfmetrics.registerFont(TTFont('Sans',font));pdfmetrics.registerFont(TTFont('Bold',bold))
W,H=720,900
c=canvas.Canvas(str(ROOT/'informe/Belgrano_2026_analisis.pdf'),pagesize=(W,H));c.setTitle('Belgrano 2026: números parecidos, cierres diferentes');c.setAuthor('Lucas Carrizo')
def txt(x,y,s,size=18,color=NAVY,bold=False):
 c.setFillColor(HexColor(color));c.setFont('Bold' if bold else 'Sans',size);c.drawString(x,y,s)
def lines(x,y,ss,size=18,leading=29,color=NAVY,bold=False):
 for s in ss:txt(x,y,s,size,color,bold);y-=leading
 return y
def base(n,kicker,cancha=True):
 c.setFillColor(HexColor(BG));c.rect(0,0,W,H,fill=1,stroke=0)
 # Encabezado de club, escudo original y línea celeste.
 c.setFillColor(HexColor(BLACK));c.rect(0,817,W,83,fill=1,stroke=0)
 c.setFillColor(HexColor(BLUE));c.rect(0,811,W,6,fill=1,stroke=0)
 c.drawImage(str(ROOT/'graficos/escudo.png'),600,827,58,58,mask='auto')
 txt(44,867,'BELGRANO',24,'#FFFFFF',True)
 txt(44,843,'CÓRDOBA  /  APERTURA vs. CLAUSURA 2026',10,BLUE,True)
 txt(44,790,kicker.upper(),11,'#167AA5',True)
 # Media cancha tenue: identidad futbolera sin interferir en los datos.
 if cancha:
  c.saveState();c.setStrokeColor(HexColor('#DDEEF6'));c.setLineWidth(1)
  c.rect(576,80,110,125,fill=0,stroke=1);c.line(576,142,686,142)
  c.circle(631,142,23,fill=0,stroke=1);c.rect(608,80,46,17,fill=0,stroke=1);c.rect(608,188,46,17,fill=0,stroke=1)
  c.restoreState()
 c.setStrokeColor(HexColor('#BDDCEB'));c.line(44,63,676,63)
 txt(44,42,'LUCAS CARRIZO · ANÁLISIS DE DATOS',9,GRAY,True)
 txt(44,25,'FASES REGULARES · 16 PARTIDOS POR TORNEO · SIN PLAYOFFS',8,GRAY)
 txt(635,40,f'{n:02d} / 06',9,GRAY)
def end():c.showPage()
def card(x,y,w,h,label,value,col=BLUE):
 c.setFillColor(HexColor(col));c.roundRect(x,y,w,h,12,fill=1,stroke=0)
 ink='#FFFFFF' if col==BLACK else NAVY
 txt(x+22,y+h-32,label,13,ink,True);txt(x+22,y+27,value,43,ink,True)
base(1,'Apertura vs. Clausura')
lines(44,716,['Números parecidos,','cierres diferentes.'],43,57,bold=True)
lines(44,560,['Tres puntos separan las campañas.','Los últimos cuatro partidos cuentan','una historia mucho más distinta.'],22,34)
card(44,294,300,150,'APERTURA · PUNTOS','26',BLACK);card(364,294,312,150,'CLAUSURA · PUNTOS','23')
lines(44,225,['32 partidos analizados. Dos torneos completos.','Una mirada sobre el recorrido, no solo el total.'],17,28,GRAY)
txt(44,102,'Fuentes: AFA y TyC Sports. Cálculos propios.',10,GRAY);end()
base(2,'El recorrido')
lines(44,724,['La diferencia se abrió','en el cierre.'],34,45,bold=True)
lines(44,604,['Tras 12 partidos: Apertura 19 puntos, Clausura 22.','Al terminar: Apertura 26, Clausura 23.'],18,29)
c.drawImage(str(ROOT/'graficos/evolucion.png'),30,210,width=660,height=345,mask='auto')
lines(44,164,['El Clausura llegó mejor al partido 12, pero sumó','solo un punto en los cuatro encuentros restantes.'],18,28)
txt(44,88,'Orden real de disputa: la fecha 9 del Apertura se jugó al final.',10,GRAY);end()
base(3,'Regularidad · cuatro bloques iguales')
lines(44,724,['Del mejor tramo','al cierre más débil.'],34,45,bold=True)
txt(44,601,'Puntos obtenidos en cada bloque de cuatro partidos.',18)
c.drawImage(str(ROOT/'graficos/bloques.png'),30,215,width=660,height=367,mask='auto')
lines(44,166,['Clausura: 10 de 12 puntos en el tercer bloque;','1 de 12 en el cuarto. El promedio del torneo oculta el cambio.'],17,28)
txt(44,88,'Bloques cronológicos de igual tamaño; no ajustados por dificultad del rival.',10,GRAY);end()
base(4,'Defensa · últimos cuatro partidos')
lines(44,724,['El quiebre también','se ve atrás.'],34,45,bold=True)
card(44,445,300,155,'APERTURA · GOLES RECIBIDOS','1',BLACK);card(364,445,312,155,'CLAUSURA · GOLES RECIBIDOS','8')
lines(44,381,['El 53% de los goles recibidos en el Clausura','se concentró en sus últimos cuatro partidos.'],21,32,bold=True)
shots=json.loads((ROOT/'datos/remates_cierre.json').read_text())
totals={t:sum(r['remates_recibidos'] for r in shots if r['torneo']==t) for t in groups}
assert all(sum(r['torneo']==t for r in shots)==4 for t in groups)
txt(44,294,'REMATES RECIBIDOS EN EL CIERRE',14,NAVY,True)
txt(44,272,'Total en cuatro partidos · escala común desde cero',11,GRAY)
for t,y,col in [('Apertura',220,BLACK),('Clausura',164,BLUE)]:
 value=totals[t]
 txt(44,y+9,t,15,NAVY,True)
 c.setFillColor(HexColor(col));c.rect(151,y,390*value/70,32,fill=1,stroke=0)
 txt(151+390*value/70+10,y+7,str(value),23,NAVY,True)
 txt(579,y+10,f"{value/4:.2f}".replace('.',','),18,NAVY,True)
txt(575,253,'Por partido',10,GRAY)
delta=totals['Clausura']-totals['Apertura']
txt(44,126,f"{delta} remates más recibidos (+{delta/totals['Apertura']:.0%}).",17,NAVY,True)
txt(44,101,'Fuente: Statz · remates totales del rival. Últimos 4 por orden de disputa.',9,GRAY)
txt(44,83,'Muestra sin ajuste por rival o localía. 53% = 8 / 15 goles. ',9,GRAY);end()
base(5,'Volumen y definición',cancha=False)
lines(44,724,['Más pelota y remates.','Los mismos 17 goles.'],32,44,bold=True)
for y,label,a,b in [(576,'POSESIÓN PROMEDIO','50,4%','54,0%'),(449,'REMATES POR PARTIDO','11,25','14,6')]:
 txt(44,y+54,label,12,GRAY,True)
 txt(44,y,a,40,BLACK,True);txt(355,y,b,40,BLUE,True)
 txt(44,y-24,'Apertura',12,BLACK);txt(355,y-24,'Clausura',12,BLUE)
txt(44,389,'180 remates en el Apertura · 234 en el Clausura',15,NAVY,True)
txt(44,351,'DELANTEROS ANALIZADOS · CLAUSURA',13,NAVY,True)
c.setFillColor(HexColor('#E6EFF4'));c.roundRect(44,168,632,163,10,fill=1,stroke=0)
for x,label in [(58,'Jugador'),(277,'Remates'),(383,'Al arco'),(489,'Goles'),(573,'Gol / tiro')]:txt(x,308,label,12,GRAY,True)
for y,r in zip([278,248,218],json.loads((ROOT/'datos/delanteros_clausura.json').read_text())):
 name,sh,on,g=r['nombre_corto'],r['remates'],r['al_arco'],r['goles']
 txt(58,y,name,14);txt(298,y,str(sh),14);txt(402,y,str(on),14);txt(505,y,str(g),14)
 txt(585,y,f'{g/sh*100:.1f}%'.replace('.',','),14)
txt(58,184,'TOTAL: 73 remates · 30 al arco (41,1%) · 8 goles (11,0%)',14,NAVY,True)
lines(44,139,['La eficacia de los delanteros podría ser parte de la explicación:','Fernández convirtió el 5,9%; Passerini, el 15,2% de sus remates.'],13,20)
txt(44,91,'Fuentes: LPF Data, Statz, Scout Picks y MatchScan. Incluye penales.',9,GRAY)
txt(44,77,'Al arco / remates y goles / remates: porcentajes no excluyentes. Sin extremos ni mediapuntas.',8,GRAY)
end()
base(6,'Lectura final y alcance')
lines(44,724,['¿Llega mejor o peor','a los playoffs?'],34,47,bold=True)
for y,num,title,body in [(575,'01','Balance general cercano','26 vs. 23 puntos; 17 goles en ambos torneos.'),(465,'02','Cierres opuestos','7 vs. 1 punto en los últimos cuatro partidos.'),(355,'03','Una alerta defensiva','1 vs. 8 goles recibidos en ese mismo tramo.')]:
 txt(44,y,num,25,BLUE,True);txt(105,y,title,20,NAVY,True);txt(105,y-32,body,16)
lines(44,265,['Llega con más remates, pero con un cierre menos sólido.'],17,27)
lines(44,225,['La pregunta es si el Pirata puede recuperar la eficacia','en ataque y la solidez defensiva que mostró en los','playoffs del Apertura para volver a coronarse','en el Clausura.'],17,26)
lines(44,106,['Análisis principal: fase regular, 16 partidos por torneo, sin playoffs.','El antecedente del Apertura aporta contexto; no predice el Clausura.'],10,18,GRAY)
end()
c.save()
print('Informe y gráficos generados')
