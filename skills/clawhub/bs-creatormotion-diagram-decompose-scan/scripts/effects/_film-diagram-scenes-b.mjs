import {filmKit} from './_film-diagram-kit.mjs';
// Diagram shots drawn directly on the canvas grid. Every coordinate comes from the design canvas of the
// requested aspect (ctx.width × ctx.height) and stays between the top band and the caption safe area.
// Each shot keeps one per-aspect table; portrait usually stacks what landscape places side by side.
const area=(ctx,side,pad=24)=>{const W=ctx.width||1920,H=ctx.height||1080,s=ctx.safe||{top:72,bottom:250},top=s.top+pad,bottom=H-s.bottom-pad;return {W,H,side,x0:side,x1:W-side,w:W-2*side,top,bottom,h:bottom-top,cx:W/2,cy:(top+bottom)/2};};
const pick=(ctx,table)=>table[ctx.aspect]||table['16:9'];
// The destination glyph follows the destination wording; anything unmatched gets a neutral arrow.
const destinationKind=v=>{const t=String(v||'').toLowerCase();for(const [re,kind] of [[/video|watch|play|record|film|stream|\u89c6\u9891|\u64ad\u653e|\u5f55/,'play'],[/learn|read|book|study|lesson|course|\u5b66|\u8bfb|\u4e66|\u8bfe/,'book'],[/goal|target|outcome|aim|focus|\u76ee\u6807/,'target'],[/done|finish|complete|ready|ship|check|\u5b8c\u6210|\u68c0\u67e5|\u4e0a\u7ebf/,'check'],[/write|draft|note|edit|\u5199|\u7b14\u8bb0|\u8349\u7a3f/,'pen'],[/team|people|meet|class|audience|\u56e2\u961f|\u4f1a\u8bae|\u89c2\u4f17/,'people'],[/idea|insight|think|\u60f3\u6cd5|\u7075\u611f/,'bulb'],[/search|find|research|explore|\u641c|\u627e|\u7814\u7a76/,'search'],[/archive|store|save|\u5f52\u6863|\u4fdd\u5b58/,'archive']])if(re.test(t))return kind;return 'arrow';};
const arrowIcon=size=>`<svg class="fd-icon" viewBox="0 0 100 100" width="${size}" height="${size}" aria-hidden="true"><path d="M50 12A38 38 0 1 0 50 88A38 38 0 1 0 50 12 M30 50H68 M53 35L68 50L53 65"/></svg>`;
export function buildScene(name,ctx){
 const k=filmKit(ctx),d=ctx.data,{e,icon,image,text,box,glyph,path,tween,draw,reveal,add,css}=k,portrait=!!ctx.portrait;
 if(name==='quadrant-positioning'){
  // A full plot fills the safe region; items keep their literal x/y positions inside it.
  const L=pick(ctx,{'16:9':{side:150,gw:340,gh:220,label:48,icon:100,axis:40},'4:3':{side:56,gw:300,gh:200,label:44,icon:88,axis:38},'3:4':{side:48,gw:290,gh:230,label:50,icon:96,axis:40},'9:16':{side:48,gw:330,gh:270,label:58,icon:120,axis:46}});
  const R=area(ctx,L.side,20),px0=R.x0,px1=R.x1,py0=R.top,py1=R.bottom,cx=(px0+px1)/2,cy=(py0+py1)/2,ah=L.axis*1.5;
  add(path('axis-x',`M${px0} ${cy}H${px1}m-24 -14l24 14l-24 14`)+path('axis-y',`M${cx} ${py1}V${py0}m-14 24l14 -24l14 24`));
  draw('axis-x',.16,.55);draw('axis-y',.28,.48);
  const lw=Math.min(520,(px1-px0)/2-40);
  add(text('axis-left',px0,cy+12,lw,ah,d.horizontal[0],L.axis,'light')+text('axis-right',px1-lw,cy+12,lw,ah,d.horizontal[1],L.axis,'light')+text('axis-top',cx+26,py0,lw,ah,d.vertical[1],L.axis+4)+text('axis-bottom',cx+26,py1-ah,lw,ah,d.vertical[0],L.axis,'light muted'));
  for(const id of ['axis-left','axis-right','axis-top','axis-bottom'])reveal(id,.65,{y:0,duration:.2});
  // Item centres map into the plot inset by half a glyph, so every glyph stays inside the safe region.
  const mx=L.gw/2+10,my=L.gh/2+10;
  d.items.slice(0,6).forEach((v,i)=>{const ix=px0+mx+(px1-px0-2*mx)*Number(v.x),iy=py1-my-(py1-py0-2*my)*Number(v.y);add(glyph('plot-'+i,ix-L.gw/2,iy-L.gh/2,L.gw,L.gh,v.label,['search','check','book','pen','bulb','archive'][i%6]));reveal('plot-'+i,.88+i*.36,{scale:.64,y:0,duration:.35,ease:'expo.out'});});
  css(`#axis-right{justify-content:flex-end;text-align:right}.fd-glyph{font-size:${L.label}px;gap:16px}.fd-glyph .fd-icon{width:${L.icon}px;height:${L.icon}px}`);return k.finish(6.4);
 }
 if(name==='decompose-scan'){
  // Landscape: parts in a row, scanned left to right. Portrait: parts in a column, scanned top to bottom.
  const L=pick(ctx,{'16:9':{side:195,qw:1350,qh:150,qf:76,ph:130,part:44,bw:1000,bh:230,cw:200,ch:220,copy:58},'4:3':{side:60,qw:1240,qh:150,qf:68,ph:130,part:38,bw:940,bh:220,cw:190,ch:210,copy:52},'3:4':{side:48,qh:170,qf:72,step:110,part:52,bh:230,cw:180,ch:210,copy:50,stack:true},'9:16':{side:48,qh:210,qf:86,step:130,part:62,bh:260,cw:210,ch:240,copy:58,stack:true}});
  const R=area(ctx,L.side),qw=Math.min(L.qw||R.w,R.w),parts=d.parts.slice(0,6),n=parts.length;
  add(box('big-question',R.cx-qw/2,R.top,qw,L.qh,e(d.problem),'fd-solid'));
  let bx,by,bw,cxp,cyp,step,scanAt;
  if(!L.stack){
   const py=R.top+L.qh+50;step=R.w/n;const w=step-26;
   parts.forEach((v,i)=>{add(box('part-'+i,R.x0+i*step,py,w,L.ph,`<small>${String(i+1).padStart(2,'0')}</small><span>${e(v)}</span>`,'part'));reveal('part-'+i,.55+i*.09,{scale:.94,y:25,duration:.28});});
   add(box('scan-ring',R.x0-7,py-7,w+14,L.ph+14,'','scan-ring'));scanAt={x:step};
   bw=L.bw;by=py+L.ph+56;bx=R.cx-(bw+30+L.cw)/2;cxp=bx+bw+30;cyp=Math.min(R.bottom-L.ch,by+L.bh-L.ch*.55);
  }else{
   bw=R.w-L.cw-20;by=R.bottom-L.bh-30;bx=R.x0;cxp=R.x1-L.cw;cyp=R.bottom-L.ch;
   const top=R.top+L.qh+40,bottom=by-36;step=Math.min(L.step,(bottom-top)/n);const h=step-14,y0=top+(bottom-top-step*n)/2;
   parts.forEach((v,i)=>{add(box('part-'+i,R.x0,y0+i*step,R.w,h,`<small>${String(i+1).padStart(2,'0')}</small><span>${e(v)}</span>`,'part row'));reveal('part-'+i,.55+i*.09,{scale:.94,y:25,duration:.28});});
   add(box('scan-ring',R.x0-7,y0-7,R.w+14,h+14,'','scan-ring'));scanAt={y:step};
  }
  reveal('scan-ring',1.05,{y:0,duration:.16});parts.forEach((_,i)=>{if(i)tween('to','#scan-ring',{[scanAt.x?'x':'y']:i*(scanAt.x||scanAt.y),duration:.22,ease:'power2.inOut'},1.1+i*.46);});
  // The balloon body and tail are drawn for the bubble size of this aspect; the tail points at the character.
  const bh=L.bh,bb=bh-55,r=34,tail=`M${r} 0H${bw-r}Q${bw} 0 ${bw} ${r}V${bb-r}Q${bw} ${bb} ${bw-r} ${bb}H${bw*.84}L${bw*.95} ${bh}L${bw*.68} ${bb}H${r}Q0 ${bb} 0 ${bb-r}V${r}Q0 0 ${r} 0Z`;
  add(`<div id="scan-question" style="position:absolute;left:${bx}px;top:${by}px;width:${bw}px;height:${bh}px"><svg viewBox="0 0 ${bw} ${bh}" aria-hidden="true" style="position:absolute;inset:0;width:100%;height:100%"><path d="${tail}" fill="var(--ink)"/></svg>${text('scan-copy',40,18,bw-80,bb-36,d.question,L.copy,'center')}</div>`);
  add(box('thinking-character',cxp,cyp,L.cw,L.ch,image('thinking-character','Thinking character','scan-character')));const end=1.55+n*.46;reveal('thinking-character',end,{y:20,scale:.96,duration:.3});reveal('big-question',.16,{scale:.92,y:0,duration:.3,ease:'expo.out'});reveal('scan-question',end,{y:20,scale:.96,duration:.3});
  css(`#big-question{font-size:${L.qf}px;line-height:1.05;padding:20px 40px}.part{font-size:${L.part}px;gap:9px}.part.row{flex-direction:row;justify-content:flex-start;gap:32px;padding:0 28px}.part small{font:400 ${portrait?26:23}px var(--mono);color:var(--muted)}.scan-ring{border:4px solid var(--ink);border-radius:5px;pointer-events:none}#scan-copy{color:var(--bg)}.scan-character{display:block;width:100%;height:100%;object-fit:contain;object-position:center}`);return k.finish(7.2);
 }
 if(name==='list-bridge'){
  // Landscape: list enclosure left, bridge right, destination right. Portrait: list on top, bridge down, destination below.
  const L=pick(ctx,{'16:9':{side:170,lw:720,item:52,bridge:330,dw:480,label:64,icon:170,sym:80},'4:3':{side:48,lw:620,item:46,bridge:250,dw:440,label:56,icon:150,sym:72},'3:4':{side:56,lh:500,item:58,bridge:130,dh:330,label:62,icon:150,sym:64},'9:16':{side:56,lh:680,item:68,bridge:150,dh:380,label:74,icon:164,sym:76}});
  const R=area(ctx,L.side),list=d.items.slice(0,6),n=list.length,kind=destinationKind(d.destination),dIcon=size=>kind==='arrow'?arrowIcon(size):icon(kind,size);
  const sym=String(d.symbol??''),turn=portrait&&/^(>|->|→|»|›)$/.test(sym.trim());
  if(!portrait){
   const fx=R.x0,fy=R.top,fh=R.h,lx0=fx+L.lw+20,lx1=lx0+L.bridge,dx=lx1+20,dh=Math.min(R.h,460),step=(fh-80)/n;
   add(box('list-frame',fx,fy,L.lw,fh,'','fd-outline'));list.forEach((v,i)=>{add(text('bridge-item-'+i,fx+56,fy+40+i*step,L.lw-112,step,v,Math.min(L.item,step*.5)));reveal('bridge-item-'+i,.16+i*.17,{x:-28,y:0,duration:.28});});
   add(path('bridge',`M${lx0} ${R.cy}H${lx1}m-22 -14l22 14l-22 14`));add(box('destination',dx,R.cy-dh/2,Math.min(L.dw,R.x1-dx),dh,`${dIcon(L.icon)}<span>${e(d.destination)}</span>`,'fd-glyph'));
   add(text('bridge-symbol',(lx0+lx1)/2-80,R.cy-L.sym*1.5,160,L.sym*1.2,sym,L.sym,'center'));
  }else{
   const fx=R.x0,fy=R.top,fw=R.w,by0=fy+L.lh+20,by1=by0+L.bridge,dy=by1+16,step=(L.lh-60)/n;
   add(box('list-frame',fx,fy,fw,L.lh,'','fd-outline'));list.forEach((v,i)=>{add(text('bridge-item-'+i,fx+50,fy+30+i*step,fw-100,step,v,Math.min(L.item,step*.5)));reveal('bridge-item-'+i,.16+i*.17,{x:-28,y:0,duration:.28});});
   add(path('bridge',`M${R.cx} ${by0}V${by1}m-14 -22l14 22l14 -22`));add(box('destination',fx,dy,fw,Math.min(L.dh,R.bottom-dy),`${dIcon(L.icon)}<span>${e(d.destination)}</span>`,'fd-glyph'));
   add(text('bridge-symbol',R.cx+30,(by0+by1)/2-L.sym*.6,160,L.sym*1.2,sym,L.sym,turn?'center':''));
  }
  draw('bridge',1.55,.65);reveal('destination',2.1,{[portrait?'y':'x']:40,...(portrait?{}:{y:0}),duration:.35,ease:'expo.out'});reveal('bridge-symbol',2.2,{y:0,duration:.18});
  css(`#list-frame{border:3px solid var(--ink);border-radius:16px;background:transparent}#destination{font-size:${L.label}px;gap:${portrait?28:40}px}#destination .fd-icon{width:${L.icon}px;height:${L.icon}px}${turn?'#bridge-symbol{transform:rotate(90deg)}':''}`);return k.finish(6.1);
 }
 if(name==='branch-reveal'){
  // Landscape: roots on top, a bus, leaves in one row. Portrait: each root heads a column whose trunk drops
  // down its left edge and branches into a stacked list of leaves.
  const L=pick(ctx,{'16:9':{side:150,rw:560,rh:150,root:64,leafH:210,leaf:44,relay:36},'4:3':{side:48,rw:480,rh:140,root:58,leafH:200,leaf:40,relay:32},'3:4':{side:48,rh:150,root:68,row:210,leaf:54,relay:32},'9:16':{side:48,rh:190,root:80,row:250,leaf:64,relay:36}});
  const R=area(ctx,L.side),roots=d.roots.slice(0,2),branches=d.branches.slice(0,6),nr=roots.length,anyRelay=branches.some(v=>v.relay);
  const rootOf=(v,i)=>Math.min(nr-1,v.rootIndex??Math.floor(i*nr/branches.length));
  const rootReveal=i=>reveal('root-'+i,.16+i*.12,{y:d.rootShift?50:0,scale:.96,duration:.35});
  if(!portrait){
   const centers=nr===1?[R.cx]:[R.x0+R.w*.25,R.x0+R.w*.75],rb=R.top+L.rh,leafTop=R.bottom-L.leafH,relayY=leafTop-150,bus=rb+((anyRelay?relayY:leafTop)-rb)*.42;
   roots.forEach((v,i)=>{add(box('root-'+i,centers[i]-L.rw/2,R.top,L.rw,L.rh,e(v),'fd-solid'));rootReveal(i);});
   const step=R.w/branches.length,w=step-30;
   branches.forEach((v,i)=>{const x=R.x0+i*step+15,cx=x+w/2,rx=centers[rootOf(v,i)];add(path('route-'+i,`M${rx} ${rb+10}V${bus}H${cx}V${v.relay?relayY-6:leafTop-8}`,d.connectorStyle==='dotted'?'dots':''));draw('route-'+i,.65+i*.43,.55);
    if(v.relay){add(text('relay-'+i,x,relayY,w,96,v.relay,L.relay,'center light')+path('relay-link-'+i,`M${cx} ${relayY+100}V${leafTop-8}`));reveal('relay-'+i,1.15+i*.43,{y:0});draw('relay-link-'+i,1.42+i*.43,.3);}
    add(box('leaf-'+i,x,leafTop,w,L.leafH,`<small>${String(i+1).padStart(2,'0')}</small><span>${e(v.label)}</span>`,'fd-outline leaf'));reveal('leaf-'+i,(v.relay?1.7:1.15)+i*.43,{y:26,duration:.32});});
  }else{
   const gap=40,colW=(R.w-gap*(nr-1))/nr,rb=R.top+L.rh,top=rb+50,cols=roots.map((_,c)=>branches.map((v,i)=>({v,i})).filter(o=>rootOf(o.v,o.i)===c)),most=Math.max(1,...cols.map(c=>c.length)),row=Math.min(L.row,(R.bottom-top)/most);
   roots.forEach((v,c)=>{const x=R.x0+c*(colW+gap);add(box('root-'+c,x,R.top,colW,L.rh,e(v),'fd-solid'));rootReveal(c);
    // A relay sits as a small label above its leaf: trunk → relay → short link down → leaf.
    const tx=x+40,lx=x+90,rh=anyRelay?L.relay*1.5:0;
    cols[c].forEach(({v,i},j)=>{const y=top+j*row,ly=y+8+rh+(rh?20:0),lh=row-16-rh-(rh?20:0),cy=v.relay?y+8+rh/2:ly+lh/2;add(path('route-'+i,`M${tx} ${rb+10}V${cy}H${lx-8}`,d.connectorStyle==='dotted'?'dots':''));draw('route-'+i,.65+i*.43,.55);
     if(v.relay){add(text('relay-'+i,lx,y+8,x+colW-lx,rh,v.relay,L.relay,'light')+path('relay-link-'+i,`M${lx+24} ${y+10+rh}V${ly-3}`));reveal('relay-'+i,1.15+i*.43,{y:0});draw('relay-link-'+i,1.42+i*.43,.3);}
     add(box('leaf-'+i,lx,ly,x+colW-lx,lh,`<small>${String(i+1).padStart(2,'0')}</small><span>${e(v.label)}</span>`,'fd-outline leaf row'));reveal('leaf-'+i,(v.relay?1.7:1.15)+i*.43,{x:26,y:0,duration:.32});});});
  }
  css(`[id^="root-"]{font-size:${L.root}px;padding:16px 28px}.leaf{font-size:${portrait&&nr>1?Math.round(L.leaf*.85):L.leaf}px;gap:21px;border-color:var(--ink);border-radius:12px;background:transparent}.leaf.row{flex-direction:row;justify-content:flex-start;gap:28px;padding:0 30px}.leaf small{font:400 ${portrait?28:25}px var(--mono);color:var(--muted)}.fd-path.dots path{stroke-dasharray:.005 .012}`);return k.finish(7);
 }
 if(name==='sequence-lanes'){
  // Three lanes span the safe region; the messages step down it at even intervals.
  const L=pick(ctx,{'16:9':{side:110,lanes:[.172,.5,.828],hw:440,hh:130,head:48,hicon:70,msg:36,mh:66,wait:30,ww:460},'4:3':{side:48,lanes:[.17,.5,.83],hw:380,hh:126,head:44,hicon:64,msg:34,mh:66,wait:30,ww:400},'3:4':{side:48,lanes:[.16,.5,.84],hw:320,hh:170,head:48,hicon:70,msg:34,mh:84,wait:30,ww:380,col:true},'9:16':{side:48,lanes:[.16,.5,.84],hw:340,hh:210,head:56,hicon:84,msg:36,mh:90,wait:34,ww:420,col:true}});
  const R=area(ctx,L.side),people=d.participants.slice(0,3),xs=L.lanes.map(f=>R.W*f),laneTop=R.top+L.hh+12,kinds=['people','bulb','archive'];
  people.forEach((v,i)=>{add(glyph('participant-'+i,xs[i]-L.hw/2,R.top,L.hw,L.hh,v,kinds[i]));add(path('lane-'+i,`M${xs[i]} ${laneTop}V${R.bottom}`,'quiet'));draw('lane-'+i,.3,.5);reveal('participant-'+i,.16+i*.1,{y:0,duration:.25});});
  const messages=d.messages.slice(0,4),n=messages.length,first=laneTop+L.mh+30,step=n>1?(R.bottom-30-first)/(n-1):0,ys=messages.map((_,i)=>first+i*step);
  messages.forEach((v,i)=>{const y=ys[i],from=xs[v.from],to=xs[v.to],sign=Math.sign(to-from)||1,time=.62+i*.95+(i>1?.7:0),x=Math.min(from,to)+20,w=Math.abs(to-from)-40;add(path('message-'+i,`M${from} ${y}H${to-sign*8}m${-sign*20} -12l${sign*20} 12l${-sign*20} 12`)+box('message-copy-'+i,x,y-L.mh-8,w,L.mh,e(v.label),i===0?'fd-focus msg':'msg'));draw('message-'+i,time,.4);reveal('message-copy-'+i,time+.24,{y:0,duration:.2});});
  // The wait note sits on the lane the second message reaches, between that arrow and the next label.
  const wl=messages[1]?xs[messages[1].to]:xs[2],wy=ys[1]!==undefined&&ys[2]!==undefined?(ys[1]+ys[2]-L.mh-8)/2:ys[0]+step/2,wh=L.wait*2.4,wx=Math.max(R.x0,Math.min(R.x1-L.ww,wl-L.ww/2));
  add(box('wait',wx,wy-wh/2,L.ww,wh,`${icon('search',L.wait*1.3)}<span>${e(d.waitLabel)}</span>`,'wait'));reveal('wait',2.15,{x:20,y:0,duration:.2});tween('to','#wait',{opacity:0,duration:.16},3.1);
  css(`[id^="participant-"]{flex-direction:${L.col?'column':'row'};font-size:${L.head}px;gap:${L.col?14:24}px;padding:6px}.fd-glyph .fd-icon{width:${L.hicon}px;height:${L.hicon}px}.msg{font-size:${L.msg}px;line-height:1.08;padding:8px 18px;border-radius:3px}.wait{font-size:${L.wait}px;flex-direction:row;gap:14px;background:var(--bg);border:1px solid var(--rule);border-radius:6px}.wait .fd-icon{width:${Math.round(L.wait*1.3)}px;height:${Math.round(L.wait*1.3)}px}`);return k.finish(7.3);
 }
 if(name==='tier-pyramid'){
  // The pyramid stands on the left, each tier's note sits level with it on the right under a divider.
  const L=pick(ctx,{'16:9':{side:110,px:.31,top:120,base:470,gap:90,label:64,note:48,maxStep:240},'4:3':{side:40,px:.3,top:96,base:390,gap:60,label:58,note:44,maxStep:240},'3:4':{side:40,px:.31,top:100,base:292,gap:44,label:60,note:44,maxStep:320},'9:16':{side:40,px:.31,top:110,base:300,gap:44,label:66,note:50,maxStep:360}});
  const R=area(ctx,L.side),tiers=d.tiers.slice(0,4),n=tiers.length,step=Math.min(L.maxStep,R.h/n),top=R.cy-step*n/2,px=R.W*L.px,half=i=>L.top+i*(L.base-L.top)/n,nx=px+L.base+L.gap,nw=R.x1-nx;
  tiers.forEach((v,i)=>{const y1=top+i*step,y2=y1+step-8,l1=px-half(i),r1=px+half(i),l2=px-half(i+1),r2=px+half(i+1),tone=i===0?'var(--ink)':i===1?'var(--accent)':'var(--surface)',ink=i===0?'var(--bg)':i===1?'var(--accent-ink)':'var(--ink)',lw=(half(i)+half(i+1))-30;
   add(`<svg class="fd-path" viewBox="0 0 ${R.W} ${R.H}"><path id="tier-shape-${i}" d="M${l1} ${y1}H${r1}L${r2} ${y2}H${l2}Z" style="fill:${tone};stroke:var(--ink);stroke-width:2;stroke-dasharray:none"/></svg>`+text('tier-label-'+i,px-lw/2,y1+(step-8)*.25,lw,(step-8)*.5,v.label,Math.min(L.label,step*.3),'center')+path('tier-rule-'+i,`M${nx-40} ${y2}H${R.x1}`,'quiet')+text('tier-note-'+i,nx,y1+16,nw,step-40,v.note,L.note));
   css(`#tier-label-${i}{color:${ink}}`);reveal('tier-shape-'+i,.2+i*.16,{y:32,duration:.32});reveal('tier-label-'+i,.8+i*.55,{y:20,duration:.3});draw('tier-rule-'+i,.98+i*.55,.35);reveal('tier-note-'+i,1.15+i*.55,{x:25,y:0,duration:.26});});
  return k.finish(6.8);
 }
 throw new Error('Unknown diagram shot: '+name);
}
