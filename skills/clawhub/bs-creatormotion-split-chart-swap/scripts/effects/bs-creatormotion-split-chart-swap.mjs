export const meta={"slug": "bs-creatormotion-split-chart-swap", "name": "Chart Presenter Swap", "category": "split", "duration": 6.8, "description": "A large graph owns the main field while the speaker occupies a narrow edge. Short positional exchanges reframe the comparison, and the two strokes draw in distinct reading intervals."};
export const defaults={"series":[[16,24,32,49,54,72],[14,16,24,31,36,45]],"axisLabels":["W1","W2","W3","W4","W5","W6"]};

// A hard split: the presenter fills one half edge to edge and the line chart sits directly on the canvas grid in
// the other half, its axis labels ending above the caption band. Landscape: the two halves trade places in two short
// coordinated edits (presenter left -> right -> left). Portrait keeps the chart on top and the presenter in the lower
// half (the chart cannot move into the caption band), so the same two edits reframe both halves in place: the plot
// pushes in on the later weeks while the presenter crop tightens around the head, then both return.
// Portrait follows ctx.split: the presenter fills [0, presenterTop, W, presenterHeight] so the whole head shows,
// and the chart fits between contentTop and contentBottom.
const layout={
 '16:9':{pad:56,title:76,key:30,tick:24,axis:28,stroke:7},
 '4:3':{pad:40,title:64,key:28,tick:22,axis:26,stroke:6},
 '3:4':{pad:44,title:64,key:30,tick:22,axis:28,stroke:7},
 '9:16':{pad:48,title:84,key:34,tick:24,axis:30,stroke:8},
};

export default function build({data:d,media,esc:e,style,aspect='16:9',portrait,width:W,height:H,safe,split,frame}){
 const L=layout[aspect],m=portrait?36:40,secondary=style==='midnight-ice'?'var(--muted)':'var(--ink)';
 const rect=([l,t,w,h])=>`left:${l}px;top:${t}px;width:${w}px;height:${h}px`;
 // Regions: [left, top, width, height].
 const video=portrait?[0,split.presenterTop,W,split.presenterHeight]:[0,0,W/2,H];
 const pane=portrait?[0,split.contentTop,W,split.contentBottom-split.contentTop]:[W/2,safe.top+24,W/2,H-safe.bottom-safe.top-24];
 const series=(d.series||defaults.series).slice(0,2).map(v=>v.slice(0,6).map(x=>Math.max(0,Number(x)||0)));
 const n=Math.max(2,...series.map(s=>s.length)),labels=(d.axisLabels||[]).slice(0,n);
 const keyGap=portrait?16:24,plotGap=portrait?18:32;
 // Portrait push-in on the presenter scales around the head (the middle of the visible band above the captions).
 const headY=portrait?Math.round(((H-safe.bottom-split.presenterTop)/2)/split.presenterHeight*100):50;
 const pw=pane[2]-2*L.pad,ph=Math.round(pane[3]-L.title*1.1-keyGap-L.key*1.3-plotGap);
 const max=Math.max(1,...series.flat()),step=max>60?20:max>30?10:5,top=Math.ceil(max*1.06/step)*step;
 const left=Math.round(L.tick*2.6),right=Math.round(L.axis*.9),axisRow=Math.round(L.axis*2),plotT=Math.round(L.tick*.7),base=ph-axisRow;
 const X=i=>left+i*(pw-left-right)/(n-1),Y=v=>base-(v/top)*(base-plotT);
 const ticks=[0,1,2,3,4].map(i=>top*i/4);
 const paths=series.map(vals=>vals.map((v,i)=>`${i?'L':'M'} ${X(i).toFixed(1)} ${Y(v).toFixed(1)}`).join(' '));
 const svg=`<svg viewBox="0 0 ${pw} ${ph}" width="${pw}" height="${ph}">${ticks.map(t=>`<line x1="${left}" y1="${Y(t).toFixed(1)}" x2="${pw-right}" y2="${Y(t).toFixed(1)}" stroke="var(--rule)" stroke-width="${t?1.5:2.5}"/><text x="${left-14}" y="${(Y(t)+L.tick*.35).toFixed(1)}" text-anchor="end" fill="var(--muted)" font-family="var(--mono)" font-size="${L.tick}">${Math.round(t)}</text>`).join('')}${paths.map((p,i)=>`<path id="swap-line-${i}" d="${p}" fill="none" stroke="${i?secondary:'var(--accent)'}" stroke-width="${L.stroke}" stroke-linecap="round" stroke-linejoin="round" pathLength="100" stroke-dasharray="100"/>`).join('')}${labels.map((x,i)=>`<text x="${X(i).toFixed(1)}" y="${base+L.axis*1.5}" text-anchor="middle" fill="var(--muted)" font-family="var(--mono)" font-size="${L.axis}">${e(x)}</text>`).join('')}</svg>`;
 const swapX=W/2,js=portrait
  ?`tl.to('#swap-plot',{scale:1.2,duration:.62,ease:'power3.inOut'},1.95);tl.to('#swap-video',{scale:1.12,duration:.62,ease:'power3.inOut'},1.95);tl.to('#swap-plot',{scale:1,duration:.62,ease:'power3.inOut'},4.5);tl.to('#swap-video',{scale:1,duration:.62,ease:'power3.inOut'},4.5);`
  :`tl.to('#swap-person',{x:${swapX},duration:.62,ease:'power3.inOut'},1.95);tl.to('#swap-chart',{x:-${swapX},duration:.62,ease:'power3.inOut'},1.95);tl.to('#swap-person',{x:0,duration:.62,ease:'power3.inOut'},4.5);tl.to('#swap-chart',{x:0,duration:.62,ease:'power3.inOut'},4.5);`;
 return {duration:6.8,
 html:`<section id="swap-chart" class="swap-chart"><h1>Two ways to improve</h1><div class="swap-key"><span><i></i>Focused practice</span><span><i></i>Unstructured effort</span></div><div class="swap-plot-clip"><div id="swap-plot" class="swap-plot">${svg}</div></div></section><div id="swap-person" class="swap-person"><video id="swap-video" src="${e(media)}" muted playsinline data-start="0" data-duration="6.8" data-track-index="0"></video></div>`,
 css:`.swap-person{position:absolute;${rect(video)};overflow:hidden;z-index:2}
.swap-person video{width:100%;height:100%;object-fit:cover;object-position:${frame(video[2],video[3])};transform-origin:50% ${headY}%}
.swap-chart{position:absolute;${rect(pane)};padding:0 ${L.pad}px;box-sizing:border-box;display:flex;flex-direction:column}
.swap-chart h1{font-size:${L.title}px;line-height:1.1;letter-spacing:-.01em;margin:0 0 ${keyGap}px}
.swap-key{display:flex;gap:36px;font-size:${L.key}px;line-height:1.3;color:var(--ink);margin-bottom:${plotGap}px}
.swap-key span{display:flex;align-items:center;gap:14px}
.swap-key i{display:block;width:${Math.round(L.key*1.5)}px;height:${L.stroke}px;border-radius:9px;background:var(--accent)}
.swap-key span+span i{background:${secondary}}
.swap-plot-clip{width:${pw}px;height:${ph}px;overflow:hidden}
.swap-plot{width:${pw}px;height:${ph}px;transform-origin:100% 45%}
.swap-plot svg{display:block}`,
 js:`tl.from('#swap-chart h1',{opacity:0,duration:.28},.16);tl.from('.swap-key',{opacity:0,duration:.28},.24);tl.from('#swap-line-0',{strokeDashoffset:100,duration:1.2,ease:'none'},.32);${js}tl.from('#swap-line-1',{strokeDashoffset:100,duration:1.1,ease:'none'},2.7);`};
}
