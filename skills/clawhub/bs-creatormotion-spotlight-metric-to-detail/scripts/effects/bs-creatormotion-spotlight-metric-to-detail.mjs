import {CSS,end,counter,image,requiredImage} from './_evidence-kit.mjs';
export const defaults={"interface":"content-library.png","metric":100,"metricLabel":"Collection reviewed","cameraTarget":[0.06,0.47,0.88,0.38],"detailRegions":[[0.20,0.746,0.083,0.065],[0.46,0.746,0.083,0.065],[0.72,0.746,0.083,0.065]]};
export const meta={"slug": "bs-creatormotion-spotlight-metric-to-detail", "name": "Metric to Interface Detail", "category": "spotlight", "duration": 10, "description": "A large circular figure temporarily overlays a moving interface. Once the camera reaches the evidence, the figure clears and precise frames identify the supporting details in place."};

// The interface plane keeps its 1600×780 coordinate system (cameraTarget and detailRegions are normalized to it)
// and is moved by one camera transform inside a clipping window centred between the safe bands. Landscape windows
// share the plane's aspect, so the camera starts on the whole interface and pushes toward the target. Portrait
// windows are taller: the camera starts on the whole interface fitted to the width and pushes in until the
// plane fills the window, centred on the target. win = [width, height]; ring = metric figure size.
const PW=1600,PH=780;
const layout={
 '16:9':{win:[1480,722],ring:240,pct:62,label:30,card:380},
 '4:3':{win:[1300,634],ring:230,pct:58,label:30,card:360},
 '3:4':{win:[984,740],ring:270,pct:70,label:34,card:440},
 '9:16':{win:[1000,760],ring:300,pct:78,label:38,card:480},
};

export default function build(ctx){
 const d=ctx.data,e=ctx.esc,L=layout[ctx.aspect]||layout['16:9'],W=ctx.width,band=ctx.height-ctx.safe.bottom;
 requiredImage(ctx,d.interface);
 const [ww,wh]=L.win,wx=Math.round((W-ww)/2),wy=Math.round(ctx.safe.top+(band-ctx.safe.top-wh)/2);
 const [tx,ty,tw,th]=d.cameraTarget,cx=tx+tw/2,cy=ty+th/2;
 const clamp=(v,a,b)=>Math.min(b,Math.max(a,v)),r2=v=>Math.round(v*100)/100,r4=v=>Math.round(v*10000)/10000;
 const s0=ww/PW,x0=0,y0=(wh-PH*s0)/2;
 const s1=Math.max(s0*Math.min(1.75,1/tw),wh/PH);
 const x1=clamp(ww/2-cx*PW*s1,ww-PW*s1,0),y1=PH*s1>=wh?clamp(wh/2-cy*PH*s1,wh-PH*s1,0):(wh-PH*s1)/2;
 const r=82,c=2*Math.PI*r;
 const html=`<div id="detail-window"><div id="interface-plane">${image(ctx,d.interface)}${d.detailRegions.map((b,i)=>`<div class="detail-region" id="detail-region-${i}" style="left:${b[0]*PW}px;top:${b[1]*PH}px;width:${b[2]*PW}px;height:${b[3]*PH}px"></div>`).join('')}</div></div><div id="overlay-metric"><div class="overlay-ring"><svg viewBox="0 0 240 240"><circle cx="120" cy="120" r="${r}" fill="none" stroke="var(--rule)" stroke-width="11"/><circle id="overlay-ring" cx="120" cy="120" r="${r}" fill="none" stroke="var(--accent)" stroke-width="11" stroke-linecap="round" stroke-dasharray="${c}" stroke-dashoffset="${c*(1-d.metric/100)}" transform="rotate(-90 120 120)"/></svg><strong id="overlay-percent" class="mono">0%</strong></div><p>${e(d.metricLabel)}</p></div>`;
 const css=`#detail-window{position:absolute;left:${wx}px;top:${wy}px;width:${ww}px;height:${wh}px;overflow:hidden;border-radius:6px}
#interface-plane{position:absolute;left:0;top:0;width:${PW}px;height:${PH}px;transform-origin:0 0;transform:translate(${r2(x0)}px,${r2(y0)}px) scale(${r4(s0)});border:2px solid var(--rule);border-radius:6px;overflow:hidden;background:var(--surface)}
.detail-region{position:absolute;border:3px solid var(--accent);border-radius:2px;box-shadow:0 0 0 2px var(--accent-ink)}
#overlay-metric{position:absolute;left:${Math.round(wx+ww/2-L.card/2)}px;top:${Math.round(wy+wh/2-(L.ring+L.label*1.4+60)/2)}px;width:${L.card}px;padding:24px 30px 30px;text-align:center;background:var(--surface);border:1.5px solid var(--rule);border-radius:8px;box-shadow:0 20px 50px #0004;z-index:3}
.overlay-ring{position:relative;width:${L.ring}px;height:${L.ring}px;margin:0 auto}.overlay-ring svg{width:100%;height:100%}
#overlay-percent{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-family:var(--mono);font-size:${L.pct}px;font-weight:500;letter-spacing:-.03em}
#overlay-metric p{font-size:${L.label}px;line-height:1.25;margin-top:6px}`;
 let js=`tl.from('#detail-window',{opacity:0,y:15,duration:.33,ease:'power3.out'},.16);tl.fromTo('#interface-plane',{x:${r2(x0)},y:${r2(y0)},scale:${r4(s0)}},{x:${r2(x1)},y:${r2(y1)},scale:${r4(s1)},duration:3.25,ease:'sine.inOut'},.9);tl.from('#overlay-metric',{opacity:0,scale:.94,y:20,duration:.33,ease:'power3.out'},1);tl.from('#overlay-ring',{strokeDashoffset:${c},duration:1.6,ease:'power2.out'},1.35);`+counter('overlay-percent',d.metric,1.35,1.6,{suffix:'%'})+`tl.to('#overlay-metric',{opacity:0,duration:.32},4.3);`;
 d.detailRegions.forEach((_,i)=>js+=`tl.from('#detail-region-${i}',{opacity:0,scale:1.035,duration:.45,ease:'power3.out'},${(4.9+i*.6).toFixed(2)});`);
 return {html:`<div class="ev">${html}</div>`,css:CSS+css,js:js+end(10),duration:10};
}
