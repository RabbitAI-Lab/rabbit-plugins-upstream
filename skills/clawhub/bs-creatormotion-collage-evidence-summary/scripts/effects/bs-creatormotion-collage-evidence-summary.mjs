import {imageSlot} from './_media-image-slots.mjs';
export const defaults={"documents": [{"title": "Itinerary", "lines": ["Day 1: Coast walk", "Day 2: Mountain trail", "Day 3: City market"]}, {"title": "City walks", "lines": ["Old town", "Morning light", "Slow streets"]}, {"title": "Photo picks", "lines": ["Best light", "One subject", "No crowds"]}, {"title": "Train route", "lines": ["Coast line", "Mountain pass", "City loop"]}], "summary": "One trip, many useful notes", "presenter": true};
export const meta={"slug": "bs-creatormotion-collage-evidence-summary", "name": "Evidence Wall Summary", "category": "collage", "description": "A varied wall of source notes stays available behind a concise conclusion. A small speaker appears only after the material is established, preserving the documents as the main evidence.", "duration": 7};

// Everything sits between the top margin and the caption band. The conclusion is set as a headline across the
// top, with the optional round presenter window in the top-right corner beside it; the evidence wall of four
// document pages fills the space below (one row in landscape, a 2x2 grid in portrait).
const layout={
 '16:9':{side:110,top:92,summary:80,pip:176,cols:4,gap:40,wallGap:52,cap:30},
 '4:3':{side:64,top:84,summary:66,pip:156,cols:4,gap:28,wallGap:44,cap:27},
 '3:4':{side:56,top:88,summary:78,pip:180,cols:2,gap:28,wallGap:36,cap:32},
 '9:16':{side:56,top:184,summary:96,pip:210,cols:2,gap:32,wallGap:48,cap:36},
};

export default function build(ctx){
 const d=ctx.data,e=ctx.esc,L=layout[ctx.aspect||'16:9'],W=ctx.width,H=ctx.height,P=ctx.portrait;
 const docs=(d.documents||defaults.documents).slice(0,4),pip=Boolean(d.presenter&&ctx.media);
 const lines=P?2:1,headH=Math.max(Math.round(L.summary*1.12*lines),pip?L.pip:0);
 const wallTop=L.top+headH+L.wallGap,wallH=H-ctx.safe.bottom-24-wallTop,wallW=W-2*L.side;
 const rows=Math.ceil(docs.length/L.cols),cw=(wallW-(L.cols-1)*L.gap)/L.cols,ch=(wallH-(rows-1)*L.gap)/rows;
 const cell=i=>[L.side+(i%L.cols)*(cw+L.gap),wallTop+Math.floor(i/L.cols)*(ch+L.gap)];
 const rect=([l,t],w,h)=>`left:${l.toFixed(1)}px;top:${t.toFixed(1)}px;width:${w.toFixed(1)}px;height:${h.toFixed(1)}px`;
 const html=`<div class="stage">${docs.map((item,i)=>`<div id="doc-${i}" class="sheet document" style="${rect(cell(i),cw,ch)}">${imageSlot(ctx,item.image||`document-${i+1}`,item.title,'evidence-document-image')}<div class="image-document-caption"><b>${e(item.title)}</b><span class="mono">0${i+1}</span></div></div>`).join('')}<h1 id="evidence-summary" class="evidence-summary">${e(d.summary)}</h1>${pip?`<div id="evidence-presenter" class="evidence-presenter"><video id="evidence-presenter-video" src="${e(ctx.media)}" muted playsinline data-start="0" data-duration="6.8" data-track-index="1"></video></div>`:''}</div>`;
 const css=`.stage{position:absolute;inset:0;overflow:hidden}
.document{position:absolute;box-sizing:border-box;overflow:hidden;background:var(--surface);color:var(--ink);border:1px solid var(--rule);border-radius:2px;box-shadow:0 14px 32px #0002}
.evidence-document-image{display:block;width:100%;height:calc(100% - ${Math.round(L.cap*2.3)}px);object-fit:cover;object-position:50% 15%}
.image-document-caption{position:absolute;bottom:0;left:0;right:0;height:${Math.round(L.cap*2.3)}px;padding:0 22px;box-sizing:border-box;background:var(--surface);display:flex;align-items:center;justify-content:space-between;gap:16px;border-top:1px solid var(--rule)}
.image-document-caption b{font-size:${L.cap}px;font-weight:400;line-height:1.1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.image-document-caption span{font-size:22px;color:var(--muted);flex:none}
.evidence-summary{position:absolute;left:${L.side}px;top:${L.top}px;width:${wallW-(pip?L.pip+40:0)}px;height:${headH}px;margin:0;display:flex;align-items:center;font-size:${L.summary}px;line-height:1.08;letter-spacing:-.01em;color:var(--ink);text-wrap:balance}
.evidence-presenter{position:absolute;left:${W-L.side-L.pip}px;top:${L.top+(headH-L.pip)/2}px;width:${L.pip}px;height:${L.pip}px;border-radius:50%;overflow:hidden;border:3px solid var(--surface);box-shadow:0 10px 26px #0003;background:var(--surface);position:absolute}
.evidence-presenter video{position:absolute;left:${-Math.round(L.pip*.3)}px;top:${-Math.round(L.pip*.3)}px;width:${Math.round(L.pip*1.6)}px;height:${Math.round(L.pip*1.6)}px;object-fit:cover;object-position:${pip?ctx.frame(Math.round(L.pip*1.6),Math.round(L.pip*1.6),{x:.5,y:.52}):'50% 50%'}}`;
 const js=`tl.from('.document',{opacity:0,duration:.24},.16);tl.from('#evidence-summary',{clipPath:'inset(0 100% 0 0)',duration:.55,ease:'power2.out'},1.4);${pip?"tl.from('#evidence-presenter',{opacity:0,scale:.96,duration:.32,ease:'power2.out'},2.8);tl.to('#evidence-presenter',{opacity:0,duration:.16},6.6);":''}tl.to({},{duration:.01},6.99);`;
 return {html,css,js,duration:7};
}
