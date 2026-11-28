import {filmKit} from './_film-diagram-kit.mjs';
// Every scene sits directly on the canvas grid and is laid out natively per aspect from ctx.width/height/safe.
// T..B is the readable band between the top margin and the caption safe area; nothing readable goes below B.
const geo=ctx=>{const W=ctx.width||1920,H=ctx.height||1080,s=ctx.safe||{top:72,bottom:250};return {W,H,T:s.top,B:H-s.bottom,P:!!ctx.portrait,A:ctx.aspect||'16:9'};};
const textW=(s,size)=>[...String(s)].reduce((n,c)=>n+(/[^\x00-\xff]/.test(c)?1:.5),0)*size;
const head=(x,y,dx,dy,len=22)=>{const a=Math.atan2(dy,dx),p=a+2.6,q=a-2.6;return `M${x} ${y}L${(x+len*Math.cos(p)).toFixed(1)} ${(y+len*Math.sin(p)).toFixed(1)}M${x} ${y}L${(x+len*Math.cos(q)).toFixed(1)} ${(y+len*Math.sin(q)).toFixed(1)}`;};
export function buildScene(name,ctx){
 const k=filmKit(ctx),d=ctx.data,{e,icon,text,box,glyph,paper,path,tween,draw,reveal,add,css}=k,{W,H,T,B,P,A}=geo(ctx);
 if(name==='handoff-explain'){
  // Landscape: old → new side by side, the camera pans left so the new paper takes the lead and points open on the right.
  // Portrait: old above new, the camera pans up so the new paper leads and the points open beneath it.
  const L={'16:9':{mode:'h',pw:500,ph:560,x0:180,x1:1240,pt:62,pf:54,row:150},'4:3':{mode:'h',pw:420,ph:520,x0:100,x1:900,pt:54,pf:46,row:130},'3:4':{mode:'v',pw:620,ph:420,gap:90,pt:58,pf:54,row:150},'9:16':{mode:'v',pw:720,ph:500,gap:120,pt:66,pf:64,row:190}}[A];
  const points=d.points.slice(0,4),n=points.length;let cam,old,nu,link,px,pw2,top,rowH;
  if(L.mode==='h'){const cy=(T+B)/2,y=cy-L.ph/2;old=[L.x0,y];nu=[L.x1,y];link=`M${L.x0+L.pw+50} ${cy}H${L.x1-50}`+head(L.x1-50,cy,1,0);cam={x:-(L.x1-L.x0)};px=L.x0+L.pw+90;pw2=W-60-px;rowH=Math.min(L.row,(B-T-40)/n);top=cy-n*rowH/2;}
  else{const x=(W-L.pw)/2,y0=T+30,y1=y0+L.ph+L.gap,cx=W/2;old=[x,y0];nu=[x,y1];link=`M${cx} ${y0+L.ph+20}V${y1-20}`+head(cx,y1-20,0,1);cam={y:-(y1-y0)};px=60;pw2=W-120;top=y0+L.ph+50;rowH=Math.min(L.row,(B-20-top)/n);}
  add(`<div id="handoff-camera" style="position:absolute;inset:0">${paper('handoff-old',old[0],old[1],L.pw,L.ph,d.oldState,0,'before-image')}${path('handoff-link',link)}${paper('handoff-new',nu[0],nu[1],L.pw,L.ph,d.newState,1,'after-image')}</div>`);
  reveal('handoff-old',.16,P?{y:-25,duration:.32}:{x:-25,y:0,duration:.32});draw('handoff-link',.62,.52);reveal('handoff-new',1.08,P?{y:25,duration:.3}:{x:25,y:0,duration:.3});tween('to','#handoff-camera',{...cam,duration:.75,ease:'power3.inOut'},2.05);tween('to',['#handoff-old','#handoff-link'],{opacity:0,duration:.45,ease:'power2.in'},2.15);
  points.forEach((v,i)=>{add(box('handoff-point-'+i,px,top+i*rowH,pw2,rowH,`<b>${String(i+1).padStart(2,'0')}</b><span>${e(v)}</span>`,'handoff-point'));reveal('handoff-point-'+i,2.95+i*.34,{x:35,y:0,duration:.32});});
  css(`.fd-paper strong{font-size:${L.pt}px;line-height:1.04}.fd-paper{padding:${P?34:40}px;gap:${P?22:30}px}.handoff-point{flex-direction:row;text-align:left;justify-content:flex-start;gap:32px;font-size:${L.pf}px;line-height:1.1;border-bottom:2px solid var(--rule)}.handoff-point b{flex:none;font:400 25px var(--mono);color:var(--muted)}`);return k.finish(6.8);
 }
 if(name==='radial-branches'){
  // A ring-shaped hub stays fixed; spokes run from its edge to three surrounding peers (top, lower-left, lower-right).
  const L={'16:9':{core:[960,480],cd:340,cf:46,ci:84,peers:[[960,150],[400,710],[1520,710]],pw:460,ph:120,dir:'row',pf:50,pi:90},'4:3':{core:[720,470],cd:320,cf:44,ci:80,peers:[[720,140],[290,715],[1150,715]],pw:400,ph:110,dir:'row',pf:46,pi:80},'3:4':{core:[540,545],cd:380,cf:52,ci:100,peers:[[540,185],[230,920],[850,920]],pw:420,ph:210,dir:'col',pf:54,pi:120},'9:16':{core:[540,745],cd:460,cf:62,ci:124,peers:[[540,300],[220,1190],[860,1190]],pw:420,ph:250,dir:'col',pf:62,pi:150}}[A];
  const ps=d.peers.slice(0,3),[cx,cy]=L.core,bend=[0,-1,1];
  ps.forEach((v,i)=>{const[x,y]=L.peers[i],dx=x-cx,dy=y-cy,len=Math.hypot(dx,dy),ux=dx/len,uy=dy/len,sx=cx+ux*(L.cd/2+14),sy=cy+uy*(L.cd/2+14),tw=L.dir==='row'?L.pi+22+textW(v,L.pf):Math.max(L.pi,textW(v,L.pf)),th=L.dir==='row'?Math.max(L.pi,L.pf*1.2):L.pi+18+L.pf*1.2,t=Math.min(Math.abs(ux)>.001?tw/2/Math.abs(ux):1e9,Math.abs(uy)>.001?th/2/Math.abs(uy):1e9)+16,ex=x-ux*t,ey=y-uy*t,b=Math.min(60,len*.12)*bend[i],qx=(sx+ex)/2-uy*b,qy=(sy+ey)/2+ux*b;
   add(path('radial-route-'+i,`M${sx.toFixed(1)} ${sy.toFixed(1)}Q${qx.toFixed(1)} ${qy.toFixed(1)} ${ex.toFixed(1)} ${ey.toFixed(1)}`,d.connectorStyle==='dotted'?'dots':'')+glyph('radial-peer-'+i,x-L.pw/2,y-L.ph/2,L.pw,L.ph,v,['page','people','play'][i],'radial-peer'));draw('radial-route-'+i,.6+i*.82,.58);reveal('radial-peer-'+i,1.08+i*.82,{scale:.86,y:0,duration:.28});});
  add(box('radial-core',cx-L.cd/2,cy-L.cd/2,L.cd,L.cd,`<i class="radial-disc">${icon('bulb',L.ci)}</i><span>${e(d.center)}</span>`,'radial-core'));reveal('radial-core',.16,{scale:.88,y:0,duration:.34,ease:'expo.out'});
  css(`.radial-core{border-radius:50%;border:5px solid var(--ink);padding:${Math.round(L.cd*.14)}px;gap:16px;font-size:${L.cf}px;line-height:1.05}.radial-disc{flex:none;display:grid;place-items:center;width:${L.ci+34}px;height:${L.ci+34}px;border-radius:50%;background:var(--accent);color:var(--accent-ink)}.radial-disc .fd-icon{width:${L.ci-10}px;height:${L.ci-10}px}.radial-peer{padding:0;font-size:${L.pf}px;gap:${L.dir==='row'?22:18}px;flex-direction:${L.dir==='row'?'row':'column'}}.radial-peer .fd-icon{width:${L.pi}px;height:${L.pi}px}`);return k.finish(6.6);
 }
 if(name==='anchored-callouts'){
  // Each callout i is attached to step i. Landscape: steps sit side by side in the slab; callout 0 leaves step 0's top
  // edge to the upper left, callout 1 leaves step 1's bottom edge, callout 2 leaves step 2's top edge to the upper right.
  // Portrait: the slab stands vertically with one step per row, and each callout leaves its own row's right edge.
  const steps=d.steps.slice(0,3),n=steps.length,calls=d.callouts.slice(0,n);
  const L={'16:9':{mode:'h',stepW:240,sh:300,off:140,m:60,lh:140,lf:54,sf:48},'4:3':{mode:'h',stepW:200,sh:290,off:110,m:40,lh:130,lf:48,sf:42},'3:4':{mode:'v',sx:50,sw:420,gap:110,row:296,lf:60,sf:62,lh:210},'9:16':{mode:'v',sx:50,sw:460,gap:120,row:340,lf:68,sf:72,lh:240}}[A];
  const defs=[];let slab;
  if(L.mode==='h'){const sw=n*L.stepW+40,sx=W/2-sw/2,ly=T+30,sy=ly+L.lh+40,lyB=sy+L.sh+70;slab=[sx,sy,sw,L.sh];
   steps.forEach((_,i)=>{const scx=sx+20+L.stepW*(i+.5);defs.push({step:[sx+20+i*L.stepW,sy+20,L.stepW,L.sh-40]});const spot=n===1?2:i===1?1:i===0?0:2;
    if(spot===0){const r=scx-L.off,my=ly+L.lh/2;Object.assign(defs[i],{lab:[L.m,ly,r-L.m,L.lh],cls:'co-right',p:`M${scx} ${sy-8}C${scx} ${my} ${scx-20} ${my} ${r+18} ${my}`});}
    else if(spot===2){const x=scx+L.off,my=ly+L.lh/2;Object.assign(defs[i],{lab:[x,ly,W-L.m-x,L.lh],cls:'',p:`M${scx} ${sy-8}C${scx} ${my} ${scx+20} ${my} ${x-18} ${my}`});}
    else{const x=scx+L.off,my=lyB+L.lh/2;Object.assign(defs[i],{lab:[x,lyB,W-L.m-x,L.lh],cls:'',p:`M${scx} ${sy+L.sh+8}C${scx} ${my} ${scx+20} ${my} ${x-18} ${my}`});}});}
  else{const rowH=Math.min(L.row,(B-T-80-40)/n),sh=n*rowH+40,sy=T+(B-T-sh)/2,lx=L.sx+L.sw+L.gap,lw=W-50-lx;slab=[L.sx,sy,L.sw,sh];
   steps.forEach((_,i)=>{const my=sy+20+(i+.5)*rowH,ly=my-40,re=L.sx+L.sw;defs.push({step:[L.sx+20,sy+20+i*rowH,L.sw-40,rowH],lab:[lx,ly-L.lh/2,lw,L.lh],cls:'',p:`M${re+8} ${my}C${re+L.gap*.55} ${my} ${re+L.gap*.35} ${ly} ${lx-16} ${ly}`});});}
  add(box('callout-center',slab[0],slab[1],slab[2],slab[3],'','callout-center'));reveal('callout-center',.16,{scale:.94,y:0,duration:.3});
  steps.forEach((v,i)=>{const[x,y,w,h]=defs[i].step;add(box('callout-step-'+i,x,y,w,h,`<small>${String(i+1).padStart(2,'0')}</small><span>${e(v)}</span>`,'callout-step'+(i?' sep':'')));reveal('callout-step-'+i,.32+i*.12,{y:14,duration:.26});});
  calls.forEach((v,i)=>{const{lab:[x,y,w,h],cls,p}=defs[i];add(path('anchored-line-'+i,p)+text('anchored-label-'+i,x,y,w,h,v,L.lf,cls));draw('anchored-line-'+i,.88+i*.75,.52);reveal('anchored-label-'+i,1.33+i*.75,{y:0,filter:'blur(12px)',duration:.34});});
  css(`.callout-center{background:var(--ink);border-radius:6px}.callout-step{color:var(--bg);justify-content:center;gap:${P?18:26}px;font-size:${L.sf}px;padding:14px}.callout-step small{font:400 25px var(--mono);opacity:.65}.callout-step.sep{${P?'border-top':'border-left'}:1px solid color-mix(in srgb,var(--bg) 25%,transparent)}.co-right{justify-content:flex-end;text-align:right}`);return k.finish(6.8);
 }
 if(name==='pipeline-package'){
  // Landscape builds the chain left to right with outputs fanning right; portrait builds it as a row with outputs beneath.
  // The whole group then shrinks into a drawn system boundary and links to the outcome (right in landscape, below in portrait).
  const L={'16:9':{mode:'h',pw:300,ph:400,gap:80,x0:90,ow:400,oh:130,ox:1400,osp:170,pt:50,of:44,oi:78,frame:[70,T+30,1240,690],tf:58,oc:[1440,420],ocd:170,ocf:52},
   '4:3':{mode:'h',pw:260,ph:360,gap:70,x0:70,ow:290,oh:120,ox:1110,osp:150,pt:44,of:40,oi:70,frame:[50,T+30,960,680],tf:50,oc:[1080,320],ocd:150,ocf:46},
   '3:4':{mode:'v',pw:300,ph:400,gap:50,py:T+30,ow:300,oh:130,og:50,ogap:80,pt:46,of:42,oi:72,frame:[40,T+20,1000,660],tf:52,oc:[900,200],ocd:150,ocf:54},
   '9:16':{mode:'v',pw:300,ph:580,gap:50,py:T+60,ow:300,oh:150,og:50,ogap:130,pt:50,of:46,oi:84,frame:[40,T+20,1000,780],tf:60,oc:[900,220],ocd:180,ocf:60}}[A];
  const stages=d.stages.slice(0,3),ns=stages.length,outs=d.outputs.slice(0,3),no=outs.length;let h='',bx,by,bx2,by2;
  if(L.mode==='h'){const cy=(T+B)/2,y=cy-L.ph/2;stages.forEach((v,i)=>{const x=L.x0+i*(L.pw+L.gap);h+=paper('package-stage-'+i,x,y,L.pw,L.ph,v,i,'source-'+(i+1));reveal('package-stage-'+i,.16+i*.63,{y:30,rotation:-1.4,duration:.33});if(i<ns-1){h+=path('package-edge-'+i,`M${x+L.pw+14} ${cy}H${x+L.pw+L.gap-14}`+head(x+L.pw+L.gap-14,cy,1,0,16));draw('package-edge-'+i,.5+i*.63,.35);}});
   const lr=L.x0+(ns-1)*(L.pw+L.gap)+L.pw,oys=outs.map((_,i)=>cy+(i-(no-1)/2)*L.osp);outs.forEach((v,i)=>{const oy=oys[i];h+=path('package-fan-'+i,`M${lr+14} ${cy}C${(lr+L.ox)/2} ${cy} ${(lr+L.ox)/2} ${oy} ${L.ox-14} ${oy}`)+glyph('package-output-'+i,L.ox,oy-L.oh/2,L.ow,L.oh,v,['play','page','audio'][i],'pk-out');draw('package-fan-'+i,1.85+i*.24,.42);reveal('package-output-'+i,2.16+i*.24,{x:20,y:0,duration:.26});});
   bx=L.x0;bx2=L.ox+L.ow;by=Math.min(y,oys[0]-L.oh/2);by2=Math.max(y+L.ph,oys[no-1]+L.oh/2);}
  else{const tw=ns*L.pw+(ns-1)*L.gap,x0=(W-tw)/2,y=L.py,cy=y+L.ph/2;stages.forEach((v,i)=>{const x=x0+i*(L.pw+L.gap);h+=paper('package-stage-'+i,x,y,L.pw,L.ph,v,i,'source-'+(i+1));reveal('package-stage-'+i,.16+i*.63,{y:30,rotation:-1.4,duration:.33});if(i<ns-1){h+=path('package-edge-'+i,`M${x+L.pw+8} ${cy}H${x+L.pw+L.gap-8}`+head(x+L.pw+L.gap-8,cy,1,0,14));draw('package-edge-'+i,.5+i*.63,.35);}});
   const lx=x0+(ns-1)*(L.pw+L.gap)+L.pw/2,y1=y+L.ph+12,oy=y+L.ph+L.ogap,ow0=(W-(no*L.ow+(no-1)*L.og))/2;outs.forEach((v,i)=>{const ox=ow0+i*(L.ow+L.og),ocx=ox+L.ow/2;h+=path('package-fan-'+i,`M${lx} ${y1}C${lx} ${(y1+oy)/2} ${ocx} ${(y1+oy)/2} ${ocx} ${oy-12}`)+glyph('package-output-'+i,ox,oy,L.ow,L.oh,v,['play','page','audio'][i],'pk-out');draw('package-fan-'+i,1.85+i*.24,.42);reveal('package-output-'+i,2.16+i*.24,{y:20,duration:.26});});
   bx=Math.min(x0,ow0);bx2=W-bx;by=y;by2=oy+L.oh;}
  add(`<div id="package-camera" style="position:absolute;inset:0">${h}</div>`);
  const[fx,fy,fw,fh]=L.frame,th=Math.round(L.tf*1.4),ax=fx+30,ay=fy+40+th,aw=fw-60,ah=fh-70-th,bw=bx2-bx,bh=by2-by,s=Math.min(aw/bw,ah/bh);
  tween('to','#package-camera',{scale:+s.toFixed(4),x:+(ax+(aw-bw*s)/2-bx*s).toFixed(1),y:+(ay+(ah-bh*s)/2-by*s).toFixed(1),transformOrigin:'0px 0px',duration:.78,ease:'power3.inOut'},3.4);
  const och=L.mode==='h'?L.ocd+24+Math.round(L.ocf*2.3):L.oc[1],ol=L.mode==='h'?[L.oc[0],fy+fh/2-och/2,L.oc[1],och]:[(W-L.oc[0])/2,fy+fh+90,L.oc[0],och],link=L.mode==='h'?`M${fx+fw+16} ${fy+fh/2}H${ol[0]-16}`+head(ol[0]-16,fy+fh/2,1,0):`M${W/2} ${fy+fh+16}V${ol[1]-16}`+head(W/2,ol[1]-16,0,1);
  add(path('package-frame',`M${fx} ${fy+fh}V${fy}H${fx+fw}V${fy+fh}Z`,'strong')+text('package-title',fx+30,fy+20,fw-60,th,d.system,L.tf,'center')+path('package-outcome-link',link)+box('package-outcome',ol[0],ol[1],ol[2],ol[3],`<i class="pk-disc">${icon('check',Math.round(L.ocd*.5))}</i><span>${e(d.outcome)}</span>`,'pk-outcome'));
  draw('package-frame',4.1,.58);reveal('package-title',4.6,{y:0,duration:.24});draw('package-outcome-link',4.95,.38);reveal('package-outcome',5.3,{scale:.9,y:0,duration:.3});
  css(`.fd-paper strong{font-size:${L.pt}px}.fd-paper{padding:${P?24:26}px;gap:${P?20:24}px}.pk-out{flex-direction:row;font-size:${L.of}px;gap:20px;padding:0}.pk-out .fd-icon{width:${L.oi}px;height:${L.oi}px}.pk-outcome{flex-direction:${L.mode==='h'?'column':'row'};gap:${L.mode==='h'?24:32}px;font-size:${L.ocf}px;line-height:1.06;${L.mode==='h'?'':'text-align:left;'}}.pk-disc{flex:none;display:grid;place-items:center;width:${L.ocd}px;height:${L.ocd}px;border-radius:50%;background:var(--accent);color:var(--accent-ink)}`);return k.finish(7.8);
 }
 if(name==='cycle-build'){
  // Icon discs build around an ellipse that fills the readable band of each aspect; arcs stop at each node's edge.
  const L={'16:9':{node:[300,200],disc:110,nf:48,rx:560,ck:190},'4:3':{node:[270,190],disc:100,nf:44,rx:470,ck:170},'3:4':{node:[320,240],disc:150,nf:60,rx:330,ck:210},'9:16':{node:[360,290],disc:180,nf:70,rx:320,ck:250}}[A];
  const ns=d.nodes.slice(0,5),n=ns.length,[nw,nh]=L.node,cx=W/2,cy=(T+B)/2,rx=L.rx,ry=(B-T-nh)/2-12,pos=a=>[cx+rx*Math.cos(a*Math.PI/180),cy+ry*Math.sin(a*Math.PI/180)],angle=i=>-90+i*360/n;
  const rects=ns.map((v,i)=>{const[x,y]=pos(angle(i)),w=Math.min(nw,Math.max(L.disc,textW(v,L.nf)+10));return [x-w/2,y-nh/2,w,nh];}),out=([x,y],[l,t,w,h])=>x<l-14||x>l+w+14||y<t-14||y>t+h+14;
  ns.forEach((v,i)=>{const a=angle(i),[x,y]=pos(a);add(box('build-node-'+i,x-nw/2,y-nh/2,nw,nh,`<i class="cb-disc">${icon(['search','bulb','pen','book','check'][i],Math.round(L.disc*.56))}</i><span>${e(v)}</span>`,i===0?'build-node cb-first':'build-node'));reveal('build-node-'+i,i===0?.16:.9+(i-1)*1.02,{scale:.9,y:0,duration:.3});
   const next=a+360/n,j=(i+1)%n;let s=0,t=0;while(s<170&&!out(pos(a+s),rects[i]))s+=.5;while(t<170&&!out(pos(next-t),rects[j]))t+=.5;const[x1,y1]=pos(a+s),[x2,y2]=pos(next-t),p=`M${x1.toFixed(1)} ${y1.toFixed(1)}A${rx} ${ry.toFixed(1)} 0 0 1 ${x2.toFixed(1)} ${y2.toFixed(1)}`;add(path('build-arc-'+i,p,i===n-1?'strong':''));draw('build-arc-'+i,.47+i*1.02,i===n-1?.72:.55);});
  const end=.47+(n-1)*1.02+.72;add(box('cycle-closed',cx-L.ck/2,cy-L.ck/2,L.ck,L.ck,icon('check',Math.round(L.ck*.58)),'fd-round'));reveal('cycle-closed',end+.15,{scale:.85,y:0,duration:.3});
  css(`.build-node{font-size:${L.nf}px;gap:14px;padding:0;line-height:1.06}.cb-disc{flex:none;display:grid;place-items:center;width:${L.disc}px;height:${L.disc}px;border-radius:50%;border:3px solid var(--ink);color:var(--ink)}.cb-disc .fd-icon{width:${Math.round(L.disc*.56)}px;height:${Math.round(L.disc*.56)}px}.cb-first .cb-disc{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}#cycle-closed{border-width:4px;border-color:var(--ink);background:transparent}#cycle-closed .fd-icon{width:${Math.round(L.ck*.5)}px;height:${Math.round(L.ck*.5)}px}`);return k.finish(Math.max(7.2,end+2));
 }
 throw new Error('Unknown diagram shot: '+name);
}
