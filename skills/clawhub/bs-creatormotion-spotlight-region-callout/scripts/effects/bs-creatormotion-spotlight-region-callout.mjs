export const defaults={region:[.274,.225,.49,.21],callout:'Keep only the essential rules',step:'01 · Clarify the brief',documentTitle:'The working brief',sectionTitle:'What the team needs',rules:['One clear outcome','The information needed to begin','A visible definition of done']};
export const meta={"slug": "bs-creatormotion-spotlight-region-callout", "name": "Region Callout", "category": "spotlight", "duration": 9, "description": "A document is framed as a single evidence plane, then a precise region becomes the reading focus. A connected margin note explains its significance before the full context returns."};

// `region` keeps its 1.x meaning: normalized to a 1600×710 window holding the 16:9 document image letterboxed.
// It is converted to image coordinates. 16:9 puts the step label and margin note in a right-hand column with a
// horizontal connector; the other aspects put them above the window with a vertical connector. Portrait windows
// are taller and show a closer crop centred on the region. The dimming stays inside the window, and the whole
// source-and-annotation system moves in one short camera push.
// win = [x, y, w, maxH] (y null = centre between the bands); note = font size; side = right-hand column.
const AI=16/9,AW=1600/710;
const layout={
 '16:9':{win:[100,null,1240],note:40,step:26,side:[1400,420]},
 '4:3':{win:[220,240,1000],note:40,step:26,stepY:92},
 '3:4':{win:[48,316,984,740],note:46,step:26,stepY:120},
 '9:16':{win:[40,470,1000,820],note:54,step:28,stepY:262},
};

export default function build(ctx){
 const d=ctx.data,e=ctx.esc,L=layout[ctx.aspect]||layout['16:9'],band=ctx.height-ctx.safe.bottom;
 const supplied=ctx.images.document||ctx.images.image;
 if(!supplied)throw new Error('Missing document image. Use a bundled default or a user image.');
 const clamp=(v,a,b)=>Math.min(b,Math.max(a,v)),r1=v=>Math.round(v*10)/10;
 const rx=(d.region[0]*AW-(AW-AI)/2)/AI,rw=d.region[2]*AW/AI,ry=d.region[1],rh=d.region[3];
 const [wx,wy0,ww,maxH]=L.win,wh=Math.round(maxH?Math.min(maxH,ww*.9/(rw*AI)):ww/AI),wy=wy0??Math.round(ctx.safe.top+(band-ctx.safe.top-wh)/2);
 const iw=Math.max(ww,wh*AI),ih=iw/AI,ox=clamp(ww/2-(rx+rw/2)*iw,ww-iw,0),oy=clamp(wh/2-(ry+rh/2)*ih,wh-ih,0);
 const fx=ox+rx*iw,fy=oy+ry*ih,fw=rw*iw,fh=rh*ih,gx=wx+fx,gy=wy+fy;
 let path,noteCss,stepCss;
 if(L.side){const [nx,nw]=L.side,ny=Math.round(Math.max(ctx.safe.top+60,gy-14)),ly=gy+Math.min(30,fh/4);
  stepCss=`left:${nx}px;top:${ny-L.step*2}px;width:${nw}px`;noteCss=`left:${nx}px;top:${ny}px;width:${nw}px`;
  path=`M ${r1(gx+fw)} ${r1(ly)} L ${nx} ${r1(ly)}`;}
 else{const noteTop=L.stepY+L.step*1.9,noteBottom=noteTop+L.note*1.25+34,lx=Math.max(wx+30,gx+30);
  stepCss=`left:${wx}px;top:${L.stepY}px;width:${ww}px`;noteCss=`left:${wx}px;top:${Math.round(noteTop)}px;min-width:${Math.round(lx-wx+60)}px;max-width:${ww}px`;
  path=`M ${r1(lx)} ${r1(gy)} L ${r1(lx)} ${r1(noteBottom)}`;}
 const html=`<div id="region-shot"><div id="evidence-window"><div class="evidence-plane"><img src="${e(supplied)}" alt="Supplied document"/></div><div id="focus-region"></div></div><svg id="callout-leader" viewBox="0 0 ${ctx.width} ${ctx.height}"><path d="${path}" pathLength="1" fill="none" stroke="var(--accent)" stroke-width="3" stroke-dasharray="1"/></svg><div id="step-footer">${e(d.step)}</div><div id="callout-note">${e(d.callout)}</div></div>`;
 const css=`#region-shot{position:absolute;inset:0;transform-origin:${r1(gx+fw/2)}px ${r1(gy+fh/2)}px}
#evidence-window{position:absolute;left:${wx}px;top:${wy}px;width:${ww}px;height:${wh}px;overflow:hidden;border-radius:5px;background:var(--surface);box-shadow:0 18px 55px #0003;outline:1.5px solid var(--rule);outline-offset:-1.5px}
.evidence-plane{position:absolute;left:${r1(ox)}px;top:${r1(oy)}px;width:${r1(iw)}px;height:${r1(ih)}px}.evidence-plane>img{width:100%;height:100%;object-fit:cover;display:block}
#focus-region{position:absolute;left:${r1(fx)}px;top:${r1(fy)}px;width:${r1(fw)}px;height:${r1(fh)}px;border:3px solid var(--accent);border-radius:5px;box-shadow:0 0 0 3000px rgba(0,0,0,.36);z-index:2}
#callout-leader{position:absolute;inset:0;width:100%;height:100%;z-index:3;pointer-events:none}
#step-footer{position:absolute;${stepCss};font-family:var(--mono);font-size:${L.step}px;line-height:1.2;letter-spacing:.06em;color:var(--muted);z-index:4}
#callout-note{position:absolute;${noteCss};box-sizing:border-box;font-size:${L.note}px;line-height:1.25;background:var(--surface);color:var(--ink);padding:17px 24px;border:1.5px solid var(--rule);border-left:4px solid var(--accent);border-radius:5px;box-shadow:0 12px 30px #0003;z-index:4}`;
 const js=`tl.from('#evidence-window',{opacity:0,duration:.28},.16);tl.from('#focus-region',{opacity:0,duration:.25},.65);tl.to('#region-shot',{scale:1.025,duration:.7,ease:'power3.inOut'},.65);tl.fromTo('#callout-leader path',{strokeDashoffset:1},{strokeDashoffset:0,duration:.38,ease:'power2.out'},1.1);tl.from('#callout-note',{clipPath:'inset(0 100% 0 0)',duration:.3,ease:'power2.out'},1.45);tl.from('#step-footer',{opacity:0,y:8,duration:.3},1.7);tl.to(['#focus-region','#callout-leader','#callout-note'],{opacity:0,duration:.35},6.7);tl.to('#region-shot',{scale:1,duration:.7,ease:'power3.inOut'},6.8);tl.to({}, {duration:.01},8.99);`;
 return {html,css,js,duration:9};
}
