export const defaults={"tasks": [{"label": "Review the notes", "at": 1.4}, {"label": "Choose one action", "at": 3.1}, {"label": "Try it this week", "at": 4.8}], "screenTitle": "Session checklist", "presenter": false, "screenMediaKey": "screen-recording"};
export const meta={"slug": "bs-creatormotion-cards-action-checklist", "name": "Synchronized Action Checklist", "category": "cards", "description": "Track a screen demonstration with a checklist that completes at matching moments. Keep the checklist and media aligned in one composition.", "duration": 7};

// The checklist sits directly on the canvas grid; the phone is the only object. The list and phone form one centred
// pair in every aspect (portrait keeps them side by side so the phone stays large enough to read), between the top band
// and the caption band.
// Layout is settled from frame 0: only the checks change, each at its task's own timestamp.
const layout={
 '16:9':{listW:760,gap:140,phoneMax:740,title:96,label:56,box:64,row:44},
 '4:3':{listW:640,gap:96,phoneMax:740,title:80,label:46,box:56,row:38},
 '3:4':{listW:480,gap:48,phoneMax:900,title:72,label:42,box:52,row:36},
 '9:16':{listW:450,gap:40,phoneMax:980,title:84,label:46,box:58,row:40},
};
const RATIO=875/1798,PAD=14;

export default function build(ctx){
 const d=ctx.data,e=ctx.esc,L=layout[ctx.aspect||'16:9'],W=ctx.width,H=ctx.height,top=ctx.safe.top,bottom=H-ctx.safe.bottom;
 const tasks=(d.tasks||[]).slice(0,4),n=tasks.length,region=bottom-top,rect=([l,t,w,h])=>`left:${l}px;top:${t}px;width:${w}px;height:${h}px`;
 const screen=ctx.images?.[d.screenMediaKey]||ctx.images?.mobileScreen;
 if(!screen)throw new Error('Supply mobileScreen or a screen-recording in --images. A real screen image or video is required.');
 const isScreenVideo=/\.(mp4|webm|mov|m4v)$/i.test(screen);
 const phoneH=Math.min(L.phoneMax,region-24),phoneW=Math.round((phoneH-2*PAD)*RATIO+2*PAD),x0=Math.round((W-L.listW-L.gap-phoneW)/2);
 const phone=[x0+L.listW+L.gap,Math.round(top+(region-phoneH)/2),phoneW,phoneH],list=[x0,top,L.listW,region];
 const A=[];
 let html=`<section id="checklist" class="checklist" style="${rect(list)}"><h1 id="checklist-title">${e(d.screenTitle)}</h1><div class="checklist-rows">`;
 tasks.forEach((v,i)=>{const at=Math.max(.16,Math.min(5.8,Number(v.at)||0)).toFixed(2);
  html+=`<div id="task-${i}" class="task-row"><span class="check-box" id="box-${i}"><svg viewBox="0 0 60 60"><path id="tick-${i}" pathLength="1" d="M12 31L25 44L49 16"/></svg></span><span class="task-label">${e(v.label)}</span></div>`;
  A.push(`tl.set('#box-${i}',{backgroundColor:'var(--accent)',borderColor:'var(--accent)'},${at});tl.fromTo('#tick-${i}',{strokeDashoffset:1},{strokeDashoffset:0,duration:.20,ease:'power2.out'},${at});`);});
 html+=`</div></section><div id="phone" class="phone" style="${rect(phone)}">${isScreenVideo?`<video id="checklist-screen" src="${e(screen)}" muted playsinline data-start="0" data-duration="6.8" data-track-index="2"></video>`:`<img id="checklist-screen-image" src="${e(screen)}" alt="${e(d.screenTitle)}">`}</div>`;
 // Optional presenter: a small round window at the top-right of the list column, never in the caption band.
 const pip=Math.round(L.title*1.6);
 if(d.presenter&&ctx.media){html+=`<div id="checklist-presenter" class="checklist-presenter" style="${rect([list[0]+list[2]-pip,top+12,pip,pip])}"><video id="checklist-presenter-video" src="${e(ctx.media)}" muted playsinline data-start="0" data-duration="6.8" data-track-index="1"></video></div>`;A.push(`tl.from('#checklist-presenter',{opacity:0,scale:.8,duration:.25,ease:'power3.out'},.16);`);}
 const css=`.stage{position:absolute;inset:0;overflow:hidden}
.checklist{position:absolute;display:flex;flex-direction:column;justify-content:center;gap:${Math.round(L.row*1.4)}px}
#checklist-title{font-size:${L.title}px;line-height:1.04;letter-spacing:-.01em;text-wrap:balance${d.presenter&&ctx.media?`;padding-right:${pip+24}px`:''}}
.checklist-rows{display:flex;flex-direction:column;gap:${L.row}px;text-align:left}
.task-row{display:flex;align-items:center;gap:${Math.round(L.box*.42)}px;font-size:${L.label}px;line-height:1.12}
.check-box{display:grid;place-items:center;width:${L.box}px;height:${L.box}px;flex:none;border:2.5px solid color-mix(in srgb,var(--ink) 45%,transparent);border-radius:${Math.round(L.box*.16)}px;color:var(--accent-ink)}
.check-box svg{width:78%;height:78%}.check-box path{fill:none;stroke:currentColor;stroke-width:6;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:1;stroke-dashoffset:1}
.phone{position:absolute;box-sizing:border-box;padding:${PAD}px;border-radius:${Math.round(phoneH*.075)}px;background:var(--surface);border:1.5px solid var(--rule)}
.phone video,.phone img{display:block;width:100%;height:100%;object-fit:contain;border-radius:${Math.round(phoneH*.075-PAD)}px;background:var(--bg)}
.checklist-presenter{position:absolute;overflow:hidden;border-radius:50%;border:3px solid var(--accent)}.checklist-presenter video{width:100%;height:100%;object-fit:cover;object-position:${ctx.frame?ctx.frame(pip,pip):'50% 35%'}}`;
 A.push(`tl.to({}, {duration:.01},6.99);`);
 return {html:`<div class="stage">${html}</div>`,css,js:A.join('\n'),duration:7};
}
