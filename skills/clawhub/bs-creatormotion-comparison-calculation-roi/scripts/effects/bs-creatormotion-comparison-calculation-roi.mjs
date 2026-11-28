import {fmt,counter,enter,finish} from './_film-comparison.mjs';
export const defaults={"unitAmount":240,"quantity":5,"investment":600,"currency":"$","labels":["Value per project","Projects recovered","Monthly value"],"conclusion":"Two times the initial cost"};
export const meta={"slug":"bs-creatormotion-comparison-calculation-roi","name":"Calculation to Return","category":"comparison","duration":11,"description":"A clear multiplication resolves to an exact monetary value. The calculation shifts aside as a second measured view compares that value with the investment and states the return multiple."};

// The calculation and the return comparison sit directly on the grid, without cards. Landscape places them
// side by side and the calculation starts centred, then slides left; portrait stacks them and the calculation
// starts centred in the safe region, then rises to the top as the return opens below. Everything ends above the caption band.
const layout={
 '16:9':{stack:false,side:110,calcW:900,gap:130,eyebrow:24,row:38,val:68,total:96,head:46,label:30,rval:34,track:28,mult:84,concl:30,rowGap:44,retGap:34},
 '4:3':{stack:false,side:72,calcW:650,gap:80,eyebrow:22,row:32,val:56,total:80,head:40,label:28,rval:30,track:24,mult:70,concl:28,rowGap:38,retGap:28},
 '3:4':{stack:true,side:72,split:.47,eyebrow:24,row:36,val:62,total:90,head:44,label:30,rval:34,track:28,mult:76,concl:30,rowGap:26,retGap:20},
 '9:16':{stack:true,side:64,split:.46,eyebrow:26,row:42,val:74,total:108,head:52,label:36,rval:40,track:34,mult:94,concl:36,rowGap:34,retGap:28},
};

export default function build(ctx){
 const d=ctx.data,e=ctx.esc,L=layout[ctx.aspect||'16:9'],W=ctx.width,H=ctx.height;
 const result=d.unitAmount*d.quantity,ratio=result/d.investment,max=Math.max(result,d.investment);
 const top=ctx.safe.top+(ctx.portrait?30:40),bottom=H-ctx.safe.bottom-30,region=bottom-top;
 // Regions: [left, top, width, height].
 let calc,ret,from;
 if(L.stack){const ch=Math.round(region*L.split),gap=36;calc=[L.side,top,W-2*L.side,ch];ret=[L.side,top+ch+gap,W-2*L.side,region-ch-gap];from={x:0,y:Math.round(region/2-ch/2)};}
 else{calc=[L.side,top,L.calcW,region];const rl=L.side+L.calcW+L.gap;ret=[rl,top,W-L.side-rl,region];from={x:Math.round((W-L.calcW)/2-L.side),y:0};}
 const rect=([l,t,w,h])=>`left:${l}px;top:${t}px;width:${w}px;height:${h}px`;
 const html=`<div id="calculation"><span class="calc-eyebrow mono">Make the value visible</span><div id="calc-unit" class="calc-row"><span>${e(d.labels[0])}</span><strong class="num">${e(d.currency)}${fmt(d.unitAmount)}</strong></div><div id="calc-quantity" class="calc-row"><span>${e(d.labels[1])}</span><strong class="num">× ${e(d.quantity)}</strong></div><div id="calc-answer"><span>${e(d.labels[2])}</span><strong id="calc-total" class="num">${e(d.currency)}0</strong></div></div><div id="return-card"><h3>The return</h3><div class="return-row"><div class="return-head"><span>Investment</span><b class="num">${e(d.currency)}${fmt(d.investment)}</b></div><div class="return-track"><div id="invest-fill" style="width:${d.investment/max*100}%;background:var(--muted)"></div></div></div><div class="return-row"><div class="return-head"><span>Value created</span><b class="num">${e(d.currency)}${fmt(result)}</b></div><div class="return-track"><div id="return-fill" style="width:${result/max*100}%;background:var(--accent)"></div></div></div><div id="return-multiple"><span>Return multiple</span><strong class="num" id="multiple">0×</strong></div><p id="return-conclusion">${e(d.conclusion)}</p></div>`;
 const css=`#calculation{position:absolute;${rect(calc)};display:flex;flex-direction:column;justify-content:center}
.calc-eyebrow{font-family:var(--mono);font-size:${L.eyebrow}px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.calc-row{display:flex;justify-content:space-between;align-items:baseline;gap:30px;margin-top:${L.rowGap}px;font-size:${L.row}px;line-height:1.2}
.ev .num{font-family:var(--font),sans-serif;font-variant-numeric:tabular-nums;letter-spacing:-.01em}
.calc-row strong{font-size:${L.val}px;line-height:1.1;font-weight:400;white-space:nowrap}
#calc-answer{border-top:3px solid var(--ink);margin-top:${L.rowGap}px;padding-top:${Math.round(L.rowGap*.8)}px;display:flex;justify-content:space-between;align-items:baseline;gap:30px;font-size:${L.row}px;color:var(--muted)}
#calc-total{font-size:${L.total}px;line-height:1.05;font-weight:400;color:var(--ink);white-space:nowrap}
#return-card{position:absolute;${rect(ret)};display:flex;flex-direction:column;justify-content:center}
.ev #return-card h3{font-size:${L.head}px;line-height:1.15;font-weight:400;margin-bottom:${L.retGap+6}px}
.return-row{margin-bottom:${L.retGap}px}
.return-head{display:flex;justify-content:space-between;align-items:baseline;gap:20px;font-size:${L.label}px;margin-bottom:12px}
.return-head b{font-size:${L.rval}px;font-weight:400;white-space:nowrap}
.return-track{height:${L.track}px;background:var(--rule)}.return-track>div{height:100%;transform-origin:left center}
#return-multiple{display:flex;justify-content:space-between;align-items:center;gap:20px;border-top:2px solid var(--rule);padding-top:${Math.round(L.retGap*.7)}px;font-size:${L.label}px;color:var(--muted)}
#multiple{font-size:${L.mult}px;line-height:1.05;font-weight:400;color:var(--ink)}
.ev #return-conclusion{align-self:flex-start;margin-top:${L.retGap}px;border-left:4px solid var(--accent);padding:6px 0 6px 18px;font-size:${L.concl}px;line-height:1.25}`;
 const js=`tl.set('#calculation',{x:${from.x},y:${from.y}},0);tl.from('#calculation',{opacity:0,clipPath:'inset(0 100% 0 0)',duration:.38,ease:'expo.out'},.16);tl.to('#calculation',{x:0,y:0,duration:.7,ease:'power3.inOut'},4.1);`+enter('#calc-unit',.7,{y:10})+enter('#calc-quantity',1.8,{y:10})+enter('#calc-answer',2.7,{y:10})+counter('calc-total',result,3,1.4,{prefix:d.currency})+`tl.from('#return-card',{clipPath:'inset(0 100% 0 0)',duration:.5,ease:'power3.out'},4.8);tl.from('#invest-fill',{scaleX:0,duration:.9},5.4);tl.from('#return-fill',{scaleX:0,duration:1.4},6.1);`+counter('multiple',ratio,6.1,1.4,{digits:1,suffix:'×'})+enter('#return-conclusion',7.9,{y:10});
 return finish(html,css,js,11);
}
