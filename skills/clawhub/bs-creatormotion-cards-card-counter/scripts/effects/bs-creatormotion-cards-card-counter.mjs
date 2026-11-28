export const defaults={"items": ["Session 1", "Session 2", "Session 3", "Session 4", "Session 5", "Session 6"], "valuePerItem": 25, "unit": "minutes", "summary": "Six small sessions add up"};
export const meta={"slug": "bs-creatormotion-cards-card-counter", "name": "Accumulating Cards and Counter", "category": "cards", "description": "Add repeated cards while updating a total in lockstep. Resolve the accumulation with a summary badge.", "duration": 7};

// Receipt strips accumulate in a two-column grid directly on the canvas; the count and the aggregate sit beside them
// as plain typography (landscape) or as a row above them (portrait). The summary line resolves beneath the receipts.
// The whole group is centred between the top band and the caption band. Faint slot outlines mark where each receipt
// will land, so the first frame already reads as a tally; the counters are odometers whose digit strips roll forward
// in sync with each arrival.
const layout={
 '16:9':{m:96,colGap:32,counterW:600,gapX:96,rowH:164,rowGap:28,label:52,count:290,value:190,eyebrow:30,summary:88,portrait:false},
 '4:3':{m:64,colGap:26,counterW:440,gapX:64,rowH:132,rowGap:24,label:40,count:210,value:140,eyebrow:28,summary:68,portrait:false},
 '3:4':{m:48,colGap:26,counterH:360,gapY:56,rowH:168,rowGap:24,label:38,count:240,value:190,eyebrow:28,summary:80,portrait:true},
 '9:16':{m:48,colGap:26,counterH:400,gapY:64,rowH:176,rowGap:30,label:40,count:290,value:230,eyebrow:30,summary:98,portrait:true},
};
// Arrival rhythm: first receipt at 0.08 s, one every 0.4 s; each counter roll starts just after its receipt lands.
const T0=0,STEP=.4,ENTER=.6,ROLL=.38;

export default function build(ctx){
 const d=ctx.data,e=ctx.esc,L=layout[ctx.aspect||'16:9'],W=ctx.width,H=ctx.height,top=ctx.safe.top,region=H-ctx.safe.bottom-top;
 const rows=(d.items||[]).slice(0,8),n=rows.length,per=Number(d.valuePerItem)||0,A=[];
 const rect=([l,t,w,h])=>`left:${Math.round(l)}px;top:${Math.round(t)}px;width:${Math.round(w)}px;height:${Math.round(h)}px`;
 const img=(key,alt)=>{if(!ctx.images?.[key])throw new Error(`Supply ${key} in --images. Real image content is required.`);return `<img src="${e(ctx.images[key])}" alt="${e(alt)}">`;};
 const itemsH=Math.ceil(n/2)*L.rowH+(Math.ceil(n/2)-1)*L.rowGap,sumGap=Math.round(L.summary*.9),sumH=Math.round(L.summary*1.2);
 let items,counter,summary;
 if(L.portrait){
  const total=L.counterH+L.gapY+itemsH+sumGap+sumH,y0=top+(region-total)/2;
  counter=[L.m,y0,W-2*L.m,L.counterH];items=[L.m,y0+L.counterH+L.gapY,W-2*L.m,itemsH];summary=[L.m,items[1]+itemsH+sumGap,W-2*L.m,sumH];
 }else{
  const total=itemsH+sumGap+sumH,y0=top+(region-total)/2,itemsW=W-2*L.m-L.gapX-L.counterW;
  items=[L.m,y0,itemsW,itemsH];summary=[L.m,y0+itemsH+sumGap,itemsW,sumH];counter=[W-L.m-L.counterW,y0,L.counterW,total];
 }
 const at=i=>T0+i*STEP,rollAt=i=>at(i)+.2;
 // Odometer: one clipped column per digit; each column's strip repeats 0-9 and only ever rolls forward.
 const odometer=(id,vals,size)=>{
  const digits=String(Math.max(...vals)).length,colW=Math.round(size*.6),dig=(v,j)=>Math.floor(v/10**j)%10;let out='';
  for(let j=digits-1;j>=0;j--){
   let p=0;const pos=[0];for(let k=1;k<vals.length;k++){p+=(dig(vals[k],j)-dig(vals[k-1],j)+10)%10;pos.push(p);}
   const cells=p+1,on=vals[0]>=10**j||j===0;
   out+=`<span id="${id}-c${j}" class="odo-col" style="width:${on?colW:0}px;opacity:${on?1:0}"><span class="odo-strip">${Array.from({length:cells},(_,c)=>`<i>${c%10}</i>`).join('')}</span></span>`;
   for(let k=1;k<vals.length;k++){
    const t=rollAt(k-1).toFixed(2),y=(-pos[k]/cells*100).toFixed(4);
    // A column that becomes significant takes its digit at once and grows in from above; others roll forward.
    if(!on&&vals[k]>=10**j&&vals[k-1]<10**j)A.push(`tl.set('#${id}-c${j} .odo-strip',{yPercent:${y}},${t});tl.to('#${id}-c${j}',{width:${colW},opacity:1,duration:${ROLL},ease:'power3.out'},${t});tl.from('#${id}-c${j} .odo-strip',{y:${-Math.round(size*.5)},duration:${ROLL},ease:'power3.out'},${t});`);
    else if(pos[k]!==pos[k-1])A.push(`tl.to('#${id}-c${j} .odo-strip',{yPercent:${y},duration:${ROLL},ease:'power3.inOut'},${t});`);
   }
  }
  return out;
 };
 const steps=Array.from({length:n+1},(_,k)=>k),odoOK=Number.isInteger(per)&&per>=0&&n*per<1e6;
 const countHTML=odometer('count',steps,L.count);
 let valueHTML;
 if(odoOK)valueHTML=odometer('value',steps.map(k=>k*per),L.value);
 else{valueHTML='0';A.push(`const valueState={v:0};const updateValue=()=>{document.getElementById('value').textContent=(Math.round(valueState.v*10)/10).toLocaleString('en-US');};`);
  steps.slice(1).forEach(k=>A.push(`tl.to(valueState,{v:${k*per},duration:${ROLL},ease:'power2.inOut',onUpdate:updateValue},${rollAt(k-1).toFixed(2)});`));}
 let html=`<div id="count-items" class="count-items" style="${rect(items)}">`;
 rows.forEach((v,i)=>{html+=`<div class="count-slot"><span class="count-ghost"></span><div id="count-card-${i}" class="count-receipt"><span class="receipt-mark">${img('itemImage'+(i+1),v)}</span><strong>${e(v)}</strong><small class="mono">+${e(per)}</small></div></div>`;
  A.push(`tl.fromTo('#count-card-${i}',{opacity:${i?0:.3},x:-28,y:34,rotation:-2.5,scale:.9},{opacity:1,x:0,y:0,rotation:0,scale:1,duration:${ENTER},ease:'back.out(1.5)'},${at(i).toFixed(2)});tl.fromTo('#count-pulse',{scale:1.9},{scale:1,duration:.45,ease:'power3.out'},${rollAt(i).toFixed(2)});`);});
 html+=`</div><div id="count-panel" class="count-panel${L.portrait?' row':''}" style="${rect(counter)}"><div class="count-block"><span id="count-label" class="count-eyebrow mono">Sessions completed</span><strong id="count" class="mono odo">${countHTML}</strong></div><div class="count-block value-block"><span id="unit" class="count-eyebrow mono"><i id="count-pulse"></i>${e(d.unit)}</span><strong id="value" class="mono odo">${valueHTML}</strong><b id="value-bar" class="value-bar"></b></div></div><p id="count-summary" class="count-summary" style="${rect(summary)}">${e(d.summary)}</p>`;
 // Settle: once the last roll finishes the total is underlined, the summary wipes in, then a quiet hold.
 const end=rollAt(n-1)+ROLL;
 A.push(`tl.fromTo('#value-bar',{scaleX:0},{scaleX:1,duration:.45,ease:'power3.inOut'},${(end-.05).toFixed(2)});tl.fromTo('#count-summary',{opacity:0,y:18,clipPath:'inset(0 100% 0 0)'},{opacity:1,y:0,clipPath:'inset(0 0% 0 0)',duration:.6,ease:'power3.out'},${(end+.15).toFixed(2)});tl.to({}, {duration:.01},6.99);`);
 const thumb=L.rowH-28;
 const css=`.stage{position:absolute;inset:0;overflow:hidden}
.count-items{position:absolute;display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:${L.rowH}px;column-gap:${L.colGap}px;row-gap:${L.rowGap}px}
.count-slot{position:relative;min-width:0}
.count-ghost{position:absolute;inset:0;border:2px dashed color-mix(in srgb,var(--muted) 55%,transparent);border-radius:16px}
.count-receipt{position:absolute;inset:0;display:flex;align-items:center;gap:${Math.round(L.label*.5)}px;padding:0 ${Math.round(L.label*.7)}px 0 14px;background:var(--surface);border:1.5px solid var(--rule);border-radius:16px;min-width:0}
.count-receipt strong{font-weight:400;font-size:${L.label}px;line-height:1.1;flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.count-receipt small{font-size:${Math.round(L.label*.82)}px;color:var(--muted);flex:none}
.receipt-mark{width:${thumb}px;height:${thumb}px;flex:none;border-radius:10px;overflow:hidden;background:var(--bg)}.receipt-mark img{display:block;width:100%;height:100%;object-fit:cover}
.count-panel{position:absolute;display:flex;flex-direction:column;justify-content:center;gap:${Math.round(L.count*.18)}px}
.count-panel:not(.row) .count-block{align-items:flex-end}
.count-panel.row{flex-direction:row;justify-content:space-between;align-items:flex-end;gap:40px}
.count-block{position:relative;display:flex;flex-direction:column;gap:12px;min-width:0}
.count-panel:not(.row) .value-block{padding-top:${Math.round(L.count*.14)}px;border-top:2px solid var(--rule)}
.count-panel.row .value-block{align-items:flex-end;text-align:right}
.count-eyebrow{display:flex;align-items:center;gap:12px;font-size:${L.eyebrow}px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.count-eyebrow i{width:14px;height:14px;border-radius:50%;background:var(--accent);flex:none}
.odo{display:flex;font-weight:500;line-height:1;white-space:nowrap}
#count{font-size:${L.count}px}#value{font-size:${L.value}px}
.odo-col{display:block;height:1.16em;overflow:hidden;flex:none;-webkit-mask-image:linear-gradient(transparent,#000 16%,#000 84%,transparent);mask-image:linear-gradient(transparent,#000 16%,#000 84%,transparent)}
.odo-strip{display:block}.odo-strip i{display:block;height:1.16em;line-height:1.16em;font-style:normal;text-align:center}
.value-bar{display:block;height:8px;width:100%;margin-top:6px;background:var(--accent);border-radius:4px;transform-origin:100% 50%}
.count-summary{position:absolute;font-size:${L.summary}px;line-height:1.15;letter-spacing:-.01em;white-space:nowrap${L.portrait?';text-align:center':''}}`;
 return {html:`<div class="stage">${html}</div>`,css,js:A.join('\n'),duration:7};
}
