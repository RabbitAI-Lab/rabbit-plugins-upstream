import {finish} from './_film-comparison.mjs';
export const defaults={"options":["Solo workspace","Team workspace"],"rows":[{"dimension":"Focus","values":["Personal projects","Shared delivery"]},{"dimension":"Setup","values":["Start immediately","Configure roles"]},{"dimension":"Review","values":["Self review","Shared checkpoints"]}]};
export const meta={"slug":"bs-creatormotion-comparison-feature-matrix","name":"Feature Matrix Reveal","category":"comparison","duration":10,"description":"Fixed option headings establish a common comparison grid. Each dimension appears first, followed by a left-to-right reveal of both values on the same baseline."};

// A ruled table typeset directly on the grid and centred between the safe bands. Landscape keeps the dimension
// as the first column; portrait gives each dimension its own line above the two value cells, so values get the full width.
const layout={
 '16:9':{stack:false,side:96,dimCol:260,gap:32,head:54,dim:34,cell:38,rowH:132,rowGap:14,headGap:40},
 '4:3':{stack:false,side:64,dimCol:200,gap:28,head:46,dim:30,cell:32,rowH:120,rowGap:12,headGap:34},
 '3:4':{stack:true,side:60,gap:36,head:62,dim:34,cell:48,rowH:0,rowGap:54,headGap:48},
 '9:16':{stack:true,side:56,gap:36,head:74,dim:40,cell:58,rowH:0,rowGap:84,headGap:72},
};

export default function build(ctx){
 const d=ctx.data,e=ctx.esc,L=layout[ctx.aspect||'16:9'],H=ctx.height;
 const top=ctx.safe.top+20,bottom=H-ctx.safe.bottom-20,cols=L.stack?'repeat(2,minmax(0,1fr))':`${L.dimCol}px repeat(2,minmax(0,1fr))`;
 const html=`<div id="matrix-stage"><div id="matrix"><div class="matrix-header">${L.stack?'':'<div></div>'}${d.options.map(t=>`<h1>${e(t)}</h1>`).join('')}</div>${d.rows.map((r,i)=>`<div class="matrix-row" id="matrix-row-${i}"><div class="dimension">${e(r.dimension)}</div>${r.values.map((v,k)=>`<div class="matrix-cell" id="matrix-cell-${i}-${k}">${e(v)}</div>`).join('')}</div>`).join('')}</div></div>`;
 const css=`#matrix-stage{position:absolute;left:${L.side}px;right:${L.side}px;top:${top}px;height:${bottom-top}px;display:flex;flex-direction:column;justify-content:center}
.matrix-header,.matrix-row{display:grid;grid-template-columns:${cols};column-gap:${L.gap}px}
.matrix-header{align-items:end;margin-bottom:${L.headGap}px}
.film-comparison .matrix-header h1{font-size:${L.head}px;line-height:1.1;font-weight:400;letter-spacing:-.01em;padding-bottom:${Math.round(L.head*.35)}px;border-bottom:3px solid var(--ink);text-wrap:balance}
.matrix-row{margin-top:${L.rowGap}px}
.matrix-row>div{display:flex;align-items:center;line-height:1.2}
.matrix-cell{font-size:${L.cell}px;${L.stack?`padding:${Math.round(L.cell*.3)}px 0 ${Math.round(L.cell*.5)}px`:`min-height:${L.rowH}px;padding:20px 0`};border-bottom:2px solid var(--rule)}
.matrix-row .dimension{font-size:${L.dim}px;color:var(--muted);border-left:4px solid var(--accent);padding:${L.stack?'4px 0 4px 18px':'0 0 0 22px'};${L.stack?'grid-column:1/-1;margin-bottom:12px;align-self:start;justify-self:start':`min-height:${L.rowH}px;border-bottom:2px solid var(--rule)`}}`;
 let js=`tl.from('.matrix-header',{clipPath:'inset(0 100% 0 0)',duration:.4,ease:'expo.out'},.16);`;
 d.rows.forEach((r,i)=>{const t=1+i*1.6;js+=`tl.from('#matrix-row-${i} .dimension',{scaleX:0,transformOrigin:'left',duration:.24,ease:'power3.out'},${t});`;r.values.forEach((_,j)=>js+=`tl.from('#matrix-cell-${i}-${j}',{clipPath:'inset(0 100% 0 0)',duration:.4,ease:'power2.out'},${t+.35+j*.35});`);});
 return finish(html,css,js,10);
}
