export const defaults={title:'Practice and consistency',points:[[0,12],[1,18],[2,16],[3,29],[4,31],[5,42]],trend:[[0,10],[5,40]],axisLabels:['Weeks of practice','Quality score'],conclusion:'Repeated practice creates a visible trend.'};
export const meta={"slug":"bs-creatormotion-comparison-line-trend","name":"Line and Trend Draw","category":"comparison","duration":10,"description":"Observed data draws across a full-shot plot, with each point landing at its measured position. A separate dashed trend follows, then a restrained conclusion strip resolves the graph."};

// Title, plot and conclusion stack on the canvas grid between the top band and the caption safe area. The plot's
// SVG is laid out at its real pixel size per aspect, so text never scales. The optional presenter is a round
// picture-in-picture in the top-right corner: landscape narrows the plot beside it, portrait starts the plot below it.
const layout={
 '16:9':{side:100,titleTop:88,title:82,conc:32,concLines:1,yAxis:150,xAxis:112,tick:27,axisTitle:30,pip:210,r:10},
 '4:3':{side:72,titleTop:84,title:76,conc:30,concLines:1,yAxis:140,xAxis:108,tick:26,axisTitle:28,pip:180,r:10},
 '3:4':{side:56,titleTop:96,title:84,conc:32,concLines:2,yAxis:132,xAxis:112,tick:26,axisTitle:30,pip:170,r:11},
 '9:16':{side:56,titleTop:210,title:96,conc:38,concLines:2,yAxis:140,xAxis:124,tick:30,axisTitle:34,pip:190,r:13},
};

export default function build(ctx){
 const d=ctx.data,e=ctx.esc,L=layout[ctx.aspect||'16:9'],W=ctx.width,H=ctx.height,portrait=ctx.portrait,pts=d.points;
 const maxX=Math.max(...pts.map(p=>p[0]),...d.trend.map(p=>p[0])),maxY=Math.ceil(Math.max(...pts.map(p=>p[1]),...d.trend.map(p=>p[1]))/10)*10;
 const limit=H-ctx.safe.bottom,pipTop=ctx.safe.top,pipRight=Math.max(L.side,64),pipW=ctx.media?L.pip+36:0;
 const titleW=W-2*L.side-pipW,lines=Math.max(1,Math.ceil(String(d.title).length*.4*L.title/titleW)),titleBottom=L.titleTop+lines*L.title*1.08;
 const concH=Math.round(L.conc*1.3*L.concLines),concTop=limit-14-concH;
 const plotTop=Math.round(Math.max(titleBottom+28,portrait&&ctx.media?pipTop+L.pip+24:0));
 const boxL=L.side-20,boxW=W-2*L.side+20-(portrait?0:pipW),boxH=concTop-28-plotTop;
 // Chart area inside the plot box: y ticks and the rotated y title on the left, x ticks and title below.
 const x0=L.yAxis,x1=boxW-24,y0=24,y1=boxH-L.xAxis,span=x1-x0;
 const xy=p=>[x0+p[0]/maxX*span,y1-p[1]/maxY*(y1-y0)];
 const path=p=>p.map((v,i)=>`${i?'L':'M'}${xy(v).map(n=>n.toFixed(1)).join(',')}`).join(' ');
 const grid=Array.from({length:6},(_,i)=>{const y=(y1-i*(y1-y0)/5).toFixed(1);return `<line x1="${x0}" y1="${y}" x2="${x1}" y2="${y}" stroke="var(--rule)" stroke-width="2"/><text x="${x0-26}" y="${(+y+L.tick*.35).toFixed(1)}" text-anchor="end" class="axis mono">${Math.round(maxY*i/5)}</text>`;}).join('');
 const ticks=pts.map(p=>`<text x="${xy(p)[0].toFixed(1)}" y="${(y1+L.tick*1.7).toFixed(1)}" text-anchor="middle" class="axis mono">${e(p[0])}</text>`).join('');
 const marks=pts.map((p,i)=>`<circle id="point-${i}" cx="${xy(p)[0].toFixed(1)}" cy="${xy(p)[1].toFixed(1)}" r="${L.r}" fill="var(--accent)" stroke="var(--ink)" stroke-width="2"/>`).join('');
 const presenter=ctx.media?`<video id="presenter" src="${e(ctx.media)}" muted playsinline data-start="0" data-duration="6.8" data-track-index="1"></video>`:'';
 const clip=id=>`<clipPath id="${id}"><rect id="${id}-rect" x="${x0-14}" y="0" width="${span+28}" height="${boxH}"/></clipPath>`;
 const html=`<div class="trend-scene"><div class="trend-heading"><h1>${e(d.title)}</h1></div><div id="plot-plane"><svg viewBox="0 0 ${boxW} ${boxH}"><defs>${clip('observed-reveal')}${clip('trend-reveal')}</defs>${grid}${ticks}<path id="observed-line" d="${path(pts)}" clip-path="url(#observed-reveal)" fill="none" stroke="var(--ink)" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><path id="trend-line" d="${path(d.trend)}" clip-path="url(#trend-reveal)" fill="none" stroke="var(--accent)" stroke-width="3.5" stroke-dasharray="11 10"/>${marks}<text x="${(x0+span/2).toFixed(1)}" y="${(boxH-8).toFixed(1)}" class="axis-title" text-anchor="middle">${e(d.axisLabels[0])}</text><text transform="translate(${Math.round(L.axisTitle*.9)} ${((y0+y1)/2).toFixed(1)}) rotate(-90)" class="axis-title" text-anchor="middle">${e(d.axisLabels[1])}</text></svg></div><p id="conclusion">${e(d.conclusion)}</p>${presenter}</div>`;
 const css=`.trend-scene{position:absolute;inset:0;color:var(--ink)}
.trend-heading{position:absolute;left:${L.side}px;top:${L.titleTop}px;width:${titleW}px;z-index:2}
.trend-heading h1{font-size:${L.title}px;line-height:1.04;letter-spacing:-.01em;margin:0;text-wrap:balance}
#plot-plane{position:absolute;left:${boxL}px;top:${plotTop}px;width:${boxW}px;height:${boxH}px;transform-origin:44% 60%}
#plot-plane svg{width:100%;height:100%;overflow:visible}
.axis{font-size:${L.tick}px;fill:var(--muted)}.axis-title{font-size:${L.axisTitle}px;fill:var(--ink)}
#conclusion{position:absolute;left:${L.side+L.yAxis-20}px;right:${L.side}px;top:${concTop}px;margin:0;font-size:${L.conc}px;line-height:1.3;padding-left:22px;border-left:4px solid var(--accent);text-wrap:balance}
#presenter{position:absolute;top:${pipTop}px;right:${pipRight}px;width:${L.pip}px;height:${L.pip}px;border-radius:50%;object-fit:cover;object-position:${ctx.media?ctx.frame(L.pip,L.pip):'50% 50%'};border:3px solid var(--accent);z-index:8}`;
 let js=`tl.from('.trend-heading',{clipPath:'inset(0 100% 0 0)',duration:.36,ease:'expo.out'},.16);tl.from('#plot-plane',{scale:.91,opacity:0,duration:.85,ease:'power3.out'},.3);tl.fromTo('#observed-reveal-rect',{attr:{width:0}},{attr:{width:${(span+28).toFixed(1)}},duration:4.4,ease:'none'},1.1);tl.fromTo('#trend-reveal-rect',{attr:{width:0}},{attr:{width:${(span+28).toFixed(1)}},duration:3.6,ease:'none'},2.5);tl.from('#conclusion',{opacity:0,y:15,duration:.65},6.4);`;
 pts.forEach((p,i)=>{js+=`tl.from('#point-${i}',{opacity:0,scale:.8,transformOrigin:'center',duration:.22,ease:'power2.out'},${(1.1+i/(pts.length-1)*4.4).toFixed(3)});`});
 if(ctx.media)js+=`tl.from('#presenter',{opacity:0,scale:.9,duration:.4},.2);tl.to('#presenter',{opacity:0,duration:.4},6.4);`;
 js+=`tl.to({}, {duration:.01},9.99);`;
 return {html,css,js,duration:10};
}
