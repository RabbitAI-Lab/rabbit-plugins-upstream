import {enter,finish,requiredImage} from './_film-comparison.mjs';
export const defaults={"leftLabel":"Before","rightLabel":"After","pairs":[["draft-1.png","refined-1.png"],["draft-2.png","refined-2.png"],["draft-3.png","refined-3.png"]],"stepCaption":"Refine the same idea"};
export const meta={"slug":"bs-creatormotion-comparison-paired-swap","name":"Paired Result Swap","category":"comparison","duration":8,"description":"Fixed before-and-after labels anchor a rapid sequence of complete visual pairs. Each pair changes together in a clean editorial cut, preserving the viewer's point of comparison."};

// Two equal inspection windows sit side by side in every aspect, so before and after always read left to right.
// Landscape windows are widescreen; portrait windows grow tall to fill the frame. Labels, windows and the step
// caption form one block centred between the top band and the caption safe area.
const layout={
 '16:9':{side:110,gap:50,label:56,ratio:.64,caption:38},
 '4:3':{side:72,gap:40,label:50,ratio:.7,caption:34},
 '3:4':{side:64,gap:32,label:52,ratio:1.6,caption:38},
 '9:16':{side:64,gap:32,label:60,ratio:1.95,caption:46},
};

export default function build(ctx){
 const d=ctx.data,e=ctx.esc,L=layout[ctx.aspect||'16:9'],W=ctx.width,H=ctx.height;
 const regionTop=ctx.safe.top,regionH=H-ctx.safe.bottom-regionTop;
 const labelH=Math.round(L.label*1.2+32),captionH=Math.round(L.caption*1.25),gapA=36,gapB=32;
 const frameW=(W-2*L.side-L.gap)/2,frameH=Math.min(frameW*L.ratio,regionH-labelH-gapA-gapB-captionH-16);
 const top=regionTop+(regionH-(labelH+gapA+frameH+gapB+captionH))/2,stageTop=top+labelH+gapA;
 const html=`<div id="paired-labels"><h1>${e(d.leftLabel)}</h1><h1>${e(d.rightLabel)}</h1></div><div id="pair-stage">${d.pairs.map((p,i)=>`<div class="result-pair" id="pair-${i}"><div class="result-frame">${requiredImage(ctx,p[0])}</div><div class="result-frame">${requiredImage(ctx,p[1])}</div></div>`).join('')}</div><p id="pair-caption">${e(d.stepCaption)}</p>`;
 const css=`#paired-labels{position:absolute;left:${L.side}px;right:${L.side}px;top:${top.toFixed(1)}px;display:grid;grid-template-columns:1fr 1fr;gap:${L.gap}px}
#paired-labels h1{justify-self:center;font-size:${L.label}px;line-height:1.2;letter-spacing:-.01em;background:var(--ink);color:var(--bg);padding:16px 30px;border-radius:3px;transform:rotate(-1deg)}
#paired-labels h1+h1{transform:rotate(1deg)}
#pair-stage{position:absolute;left:${L.side}px;right:${L.side}px;top:${stageTop.toFixed(1)}px;height:${frameH.toFixed(1)}px}
.result-pair{position:absolute;inset:0;display:grid;grid-template-columns:1fr 1fr;gap:${L.gap}px}
.result-frame{height:${frameH.toFixed(1)}px;overflow:hidden;border:1.5px solid var(--rule);border-radius:3px;background:var(--surface)}
.ev .result-frame .evidence-image{object-fit:contain;background:var(--surface)}
.result-frame .doc{border:0;border-radius:3px;padding:34px}
#pair-caption{position:absolute;left:${L.side}px;right:${L.side}px;top:${(stageTop+frameH+gapB).toFixed(1)}px;font-size:${L.caption}px;line-height:1.25;color:var(--ink)}`;
 let js=enter('#paired-labels')+enter('#pair-caption',.5,{y:12});const slot=5.7/d.pairs.length;
 d.pairs.forEach((_,i)=>{const t=.6+i*slot;js+=`tl.set('#pair-${i}',{opacity:0},0);tl.set('#pair-${i}',{opacity:1},${t.toFixed(2)});`;if(i<d.pairs.length-1)js+=`tl.set('#pair-${i}',{opacity:0},${(t+slot).toFixed(2)});`;});
 return finish(html,css,js,8);
}
