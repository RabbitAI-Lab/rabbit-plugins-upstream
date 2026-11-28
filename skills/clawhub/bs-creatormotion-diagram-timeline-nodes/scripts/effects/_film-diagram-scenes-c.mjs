import {filmKit} from './_film-diagram-kit.mjs';
// Every scene sits directly on the canvas grid and is laid out natively per aspect from ctx.width/height/safe.
// T..B is the readable band between the top margin and the caption safe area; nothing readable goes below B.
const geo=ctx=>{const W=ctx.width||1920,H=ctx.height||1080,s=ctx.safe||{top:72,bottom:250};return {W,H,T:s.top,B:H-s.bottom,P:!!ctx.portrait,A:ctx.aspect||'16:9'};};
const textW=(s,size)=>[...String(s)].reduce((n,c)=>n+(/[^\x00-\xff]/.test(c)?1:.5),0)*size;
// Ring arcs that start and end just outside each node's rectangle, on an ellipse (rx, ry) around (cx, cy).
const ringArcs=(cx,cy,rx,ry,angles,rects,pad=16)=>{const n=angles.length,pos=a=>[cx+rx*Math.cos(a*Math.PI/180),cy+ry*Math.sin(a*Math.PI/180)],out=([x,y],[l,t,w,h])=>x<l-pad||x>l+w+pad||y<t-pad||y>t+h+pad;
 return angles.map((a,i)=>{const next=a+360/n,j=(i+1)%n;let s=0,e=0;while(s<170&&!out(pos(a+s),rects[i]))s+=.5;while(e<170&&!out(pos(next-e),rects[j]))e+=.5;if(a+s>=next-e-2){s=Math.max(0,(next-a)/2-1);e=s;}const[x1,y1]=pos(a+s),[x2,y2]=pos(next-e);return `M${x1.toFixed(1)} ${y1.toFixed(1)}A${rx.toFixed(1)} ${ry.toFixed(1)} 0 0 1 ${x2.toFixed(1)} ${y2.toFixed(1)}`;});};
export function buildScene(name,ctx){
 const k=filmKit(ctx),d=ctx.data,{e,icon,image,text,box,glyph,paper,path,tween,draw,reveal,add,css}=k,{W,H,T,B,P,A}=geo(ctx);
 if(name==='milestone-detail'){
  const L={'16:9':{m:250,name:58,nameH:120,top:110,r:88,detail:56,dW:700,gap:122},'4:3':{m:170,name:52,nameH:110,top:96,r:84,detail:52,dW:560,gap:120},'3:4':{m:120,name:50,nameH:120,top:90,r:84,detail:62,dW:600,gap:240},'9:16':{m:110,name:60,nameH:150,top:150,r:104,detail:74,dW:640,gap:300}}[A];
  const ms=d.milestones.slice(0,5),n=ms.length,a=Math.max(0,Math.min(n-1,d.activeIndex)),step=(W-2*L.m)/(n-1||1),xs=ms.map((_,i)=>n>1?L.m+i*step:W/2),ax=xs[a],r=L.r;
  const nameW=Math.min(400,n>1?step-16:700),nameSize=Math.min(L.name,Math.floor(nameW/4.4)),nameTop=T+L.top,ay=nameTop+L.nameH+28+r/2;
  add(path('milestone-track',`M${xs[0]} ${ay}H${xs[n-1]}`,'strong'));draw('milestone-track',.16,.7);
  ms.forEach((v,i)=>{add(box('milestone-'+i,xs[i]-r/2,ay-r/2,r,r,String(i+1).padStart(2,'0'),i===a?'fd-round fd-focus ms-node':i<a?'fd-round ms-node ms-done':'fd-round ms-node ms-next')+text('milestone-name-'+i,xs[i]-nameW/2,nameTop,nameW,L.nameH,v,nameSize,i>a?'center muted ms-name':'center ms-name'));reveal('milestone-'+i,.36+i*.13,{scale:.7,y:0,duration:.23});reveal('milestone-name-'+i,.4+i*.13,{y:-20,duration:.3});});
  const details=d.details.slice(0,4),nd=details.length,side=ax>W*.6?-1:1,dH=Math.round(L.detail*2.3),dStart=ay+r/2+90,gap=nd>1?Math.min(L.gap,(B-20-dH/2-dStart)/(nd-1)):0,dW=Math.min(L.dW,side>0?W-40-(ax+66):ax-66-40),yLast=dStart+(nd-1)*gap;
  add(path('milestone-stem',`M${ax} ${ay+r/2}V${yLast}`));draw('milestone-stem',1.5,.5);
  details.forEach((v,i)=>{const y=dStart+i*gap,x=side>0?ax+66:ax-66-dW;add(path('detail-link-'+i,`M${ax} ${y}h${side*46}`)+text('detail-'+i,x,y-dH/2,dW,dH,v,L.detail,side>0?'':'ms-right'));draw('detail-link-'+i,1.85+i*.32,.22);reveal('detail-'+i,2.03+i*.32,{x:side*20,y:0,duration:.28});});
  css(`.ms-node{font:400 ${Math.round(r*.32)}px var(--mono);letter-spacing:.02em}.ms-done{background:var(--ink);color:var(--bg);border-color:var(--ink)}.ms-next{color:var(--muted)}.ms-right{justify-content:flex-end;text-align:right}.ms-name{align-items:flex-end}`);
  return k.finish(6.6);
 }
 if(name==='cycle-traversal'){
  // Landscape keeps the loop beside its round log; portrait stacks heading, loop and log.
  const L={'16:9':{mode:'side',ring:[50,1080],log:[1140,1850],node:[270,200],nf:46,icon:88,round:84,status:40,row:118},'4:3':{mode:'side',ring:[30,800],log:[840,1400],node:[240,190],nf:42,icon:80,round:72,status:36,row:108},'3:4':{mode:'stack',node:[280,210],nf:50,icon:92,round:84,status:46,row:86},'9:16':{mode:'stack',node:[300,230],nf:56,icon:104,round:110,status:52,row:100}}[A];
  const nodes=d.nodes.slice(0,5),n=nodes.length,f=n>=5?.86:1,nw=L.node[0]*f,nh=L.node[1]*f,statuses=d.statuses.slice(0,n),ns=statuses.length,roundH=Math.round(L.round*1.3);
  let cx,cy,rx,ry,head,rowTop,rowH,logX,logW;
  if(L.mode==='side'){const[r0,r1]=L.ring;cx=(r0+r1)/2;cy=(T+B)/2;ry=(B-T-50-nh)/2;rx=Math.min((r1-r0-nw)/2,ry*1.35);rowH=Math.min(L.row,(B-T-80-roundH)/Math.max(1,ns));const block=roundH+40+ns*rowH;logX=L.log[0];logW=L.log[1]-L.log[0];head=T+(B-T-block)/2;rowTop=head+roundH+40;}
  else{logX=70;logW=W-140;head=T+30;rowH=Math.min(L.row,(B-T-roundH-460)/Math.max(1,ns));rowTop=B-20-ns*rowH;const top=head+roundH+40,bot=rowTop-40;ry=(bot-top-nh)/2;cy=(top+bot)/2;cx=W/2;rx=(W-80-nw)/2;}
  const angles=nodes.map((_,i)=>-90+i*360/n),pos=a=>[cx+rx*Math.cos(a*Math.PI/180),cy+ry*Math.sin(a*Math.PI/180)];
  const rects=angles.map((a,i)=>{const[x,y]=pos(a),w=Math.min(nw,Math.max(L.icon,textW(nodes[i],L.nf*f)+10));return [x-w/2,y-nh/2,w,nh];}),arcDs=ringArcs(cx,cy,rx,ry,angles,rects);
  angles.forEach((a,i)=>{add(path('cycle-base-'+i,arcDs[i],'quiet'));const[x,y]=pos(a);add(glyph('cycle-node-'+i,x-nw/2,y-nh/2,nw,nh,nodes[i],['bulb','pen','check','archive','book'][i],'cycle-node'));reveal('cycle-node-'+i,.16+i*.13,{scale:.92,y:0,duration:.25});});
  const rounds=d.rounds.slice(0,3),roundSpan=Math.max(3.1,n*.82+.5);rounds.forEach((v,i)=>{add(text('round-'+i,logX,head,logW,roundH,v,L.round,'cycle-round'));reveal('round-'+i,.45+i*roundSpan,{y:18,duration:.25});if(i<rounds.length-1)tween('to','#round-'+i,{opacity:0,duration:.14},.35+(i+1)*roundSpan);});
  statuses.forEach((v,i)=>{add(box('status-'+i,logX,rowTop+i*rowH,logW,rowH,`<b>${String(i+1).padStart(2,'0')}</b><span>${e(v)}</span>`,'cycle-status'+(i?'':' first')));reveal('status-'+i,.5+i*.1,{y:0,duration:.2});});
  const on=(i,at)=>{tween('to','#status-'+i,{color:'var(--ink)',duration:.18},at);tween('to','#status-'+i+' b',{backgroundColor:'var(--accent)',color:'var(--accent-ink)',borderColor:'var(--accent)',duration:.18},at);},off=(i,at)=>{tween('to','#status-'+i,{color:'var(--muted)',duration:.15},at);tween('to','#status-'+i+' b',{backgroundColor:'rgba(0,0,0,0)',color:'var(--muted)',borderColor:'var(--rule)',duration:.15},at);};
  rounds.forEach((_,round)=>{angles.forEach((a,i)=>{const at=.65+round*roundSpan+i*.82,id='cycle-route-'+round+'-'+i,si=i%Math.max(1,ns);add(path(id,arcDs[i],'strong'));draw(id,at,.76);if(ns)on(si,at+.66);if(round<rounds.length-1&&ns)off(si,.3+(round+1)*roundSpan);});if(round<rounds.length-1)tween('to','[id^="cycle-route-'+round+'-"]',{opacity:0,duration:.12},.3+(round+1)*roundSpan);});
  const sf=Math.min(L.status,Math.round(rowH*.42));
  css(`.cycle-node{font-size:${Math.round(L.nf*f)}px;gap:14px;padding:0}.cycle-node .fd-icon{width:${Math.round(L.icon*f)}px;height:${Math.round(L.icon*f)}px}.cycle-round{align-items:flex-end}.cycle-status{flex-direction:row;justify-content:flex-start;text-align:left;gap:${P?26:22}px;font-size:${sf}px;padding:0 4px;color:var(--muted);border-top:1.5px solid var(--rule)}.cycle-status.first{border-top:0}.cycle-status b{flex:none;font:400 ${Math.max(22,Math.round(sf*.6))}px var(--mono);width:${Math.round(sf*1.6)}px;height:${Math.round(sf*1.1)}px;display:grid;place-items:center;border-radius:999px;border:1.5px solid var(--rule);color:var(--muted)}`);return k.finish(Math.max(7.8,rounds.length*roundSpan+1.6));
 }
 if(name==='additive-equation'){
  // Landscape reads as one equation row; portrait puts the terms in a row, then '=' and the result beneath.
  const L={'16:9':{m:60,op:96,opF:96,img:200,lab:54,res:280,resLab:64,val:44},'4:3':{m:40,op:76,opF:80,img:160,lab:44,res:220,resLab:54,val:38},'3:4':{m:40,op:70,opF:84,img:200,lab:48,res:250,resLab:62,val:42},'9:16':{m:40,op:70,opF:90,img:250,lab:54,res:340,resLab:72,val:48}}[A];
  const parts=d.components.slice(0,3),n=parts.length,icons=['book','bulb','pen'],termH=L.img+24+Math.round(L.lab*2.3),valH=Math.round(L.val*1.6),resH=L.res+30+Math.round(L.resLab*2.3);
  let termW,termY,eqX,eqY,eqW,eqH,res;const xs=[];
  if(!P){const resW=Math.max(L.res+40,1.28*((W-2*L.m-n*L.op)/(n+1.28)));termW=(W-2*L.m-n*L.op-resW)/n;const total=Math.max(termH+20+valH,resH),top=T+(B-T-total)/2;termY=top+(total-termH-20-valH)/2;for(let i=0;i<n;i++)xs.push(L.m+i*(termW+L.op));eqX=L.m+n*termW+(n-1)*L.op;eqW=L.op;eqY=termY;eqH=L.img;res=[eqX+L.op,termY+(L.img-L.res)/2,resW,resH];}
  else{termW=(W-2*L.m-(n-1)*L.op)/n;const total=termH+20+valH+20+L.opF*1.2+20+resH,top=T+(B-T-total)/2;termY=top;for(let i=0;i<n;i++)xs.push(L.m+i*(termW+L.op));eqW=W-2*L.m;eqX=L.m;eqY=termY+termH+20+valH+20;eqH=L.opF*1.2;const rw=Math.max(L.res+60,W*.7);res=[(W-rw)/2,eqY+eqH+20,rw,resH];}
  parts.forEach((v,i)=>{const x=xs[i];add(glyph('term-'+i,x,termY,termW,termH,v.label,icons[i],'eq-term','term-image-'+(i+1)));add(text('value-'+i,x,termY+termH+20,termW,valH,v.value||'',L.val,'center light muted'));
   reveal('term-'+i,.16+i*.6,{scale:.9,y:20,duration:.32,ease:'expo.out'});reveal('value-'+i,2.75+i*.18,{y:0,duration:.22});if(i<n-1){add(text('plus-'+i,x+termW,termY,L.op,L.img,'+',L.opF,'center eq-op'));reveal('plus-'+i,.54+i*.6,{y:0,scale:.8,duration:.18});}});
  add(text('equals',eqX,eqY,eqW,eqH,'=',L.opF,'center eq-op')+glyph('equation-result',res[0],res[1],res[2],res[3],d.result,'check','eq-term eq-result','result-image'));reveal('equals',1.4,{y:0,duration:.18});if(!d.resultInitiallyVisible)reveal('equation-result',1.8,P?{y:40,duration:.35,ease:'expo.out'}:{x:40,y:0,duration:.35,ease:'expo.out'});
  css(`.eq-term{justify-content:flex-start;padding:0;gap:24px;font-size:${L.lab}px;line-height:1.08}.eq-term .fd-glyph-image{width:${L.img}px;height:${L.img}px;border-radius:10px}.eq-op{font-family:var(--mono);color:var(--muted)}#equation-result{font-size:${L.resLab}px;gap:30px}#equation-result .fd-glyph-image{width:${L.res}px;height:${L.res}px;outline:6px solid var(--accent);outline-offset:6px}`);return k.finish(6.6);
 }
 if(name==='timeline-nodes'){
  const ms=d.milestones.slice(0,5),n=ms.length,pip=!!(d.presenter&&ctx.media),ps=P?220:200;
  if(!P){
   const L={'16:9':{m:230,date:120,cap:52},'4:3':{m:180,date:100,cap:46}}[A],step=(W-2*L.m)/(n-1||1),colW=Math.min(420,n>1?step-24:800),date=Math.min(L.date,Math.floor(colW/3.3)),dateH=Math.round(date*1.3),capH=Math.round(L.cap*1.2*2.2);
   const ty=Math.max(T+(B-T-dateH-capH-60)/2+dateH+30,pip?T+ps+40+dateH+30:0);add(path('time-track',`M${L.m-60} ${ty}H${W-L.m+60}`));draw('time-track',.18,.75);
   ms.forEach((v,i)=>{const x=n>1?L.m+i*step:W/2;add(box('time-point-'+i,x-13,ty-13,26,26,'','time-point')+text('time-date-'+i,x-colW/2,ty-30-dateH,colW,dateH,v.date,date,'center time-date')+text('time-caption-'+i,x-colW/2,ty+32,colW,capH,v.caption,L.cap,'center light time-cap'));reveal('time-point-'+i,.55+i*.7,{scale:.2,y:0,duration:.22});reveal('time-date-'+i,.65+i*.7,{y:25,duration:.3});reveal('time-caption-'+i,.83+i*.7,{y:15,duration:.25});});
  }else{
   // Portrait: the same track runs vertically on the left, dates and captions read to its right.
   const L={'3:4':{tx:110,date:128,cap:56,pad:60},'9:16':{tx:110,date:150,cap:64,pad:70}}[A],capH=Math.round(L.cap*1.25*2),y0=T+L.pad+L.date*.6,s=n>1?Math.min(420,(B-L.pad-capH-L.date*.6-y0)/(n-1)):0,yL=y0+(n-1)*s,cw=W-60-L.tx-60-(pip?ps+40:0);
   add(path('time-track',`M${L.tx} ${y0-L.date*.6-10}V${yL+L.date*.6+capH}`));draw('time-track',.18,.75);
   ms.forEach((v,i)=>{const y=y0+i*s;add(box('time-point-'+i,L.tx-14,y-14,28,28,'','time-point')+text('time-date-'+i,L.tx+60,y-L.date*.6,cw,L.date*1.2,v.date,L.date,'time-date')+text('time-caption-'+i,L.tx+60,y+L.date*.6+4,cw,capH,v.caption,L.cap,'light time-cap'));reveal('time-point-'+i,.55+i*.7,{scale:.2,y:0,duration:.22});reveal('time-date-'+i,.65+i*.7,{y:25,duration:.3});reveal('time-caption-'+i,.83+i*.7,{y:15,duration:.25});});
  }
  // Optional presenter picture-in-picture: a round window in the top-right corner, face framed by ctx.frame.
  if(pip){add(`<div id="timeline-presenter-frame" style="position:absolute;left:${W-60-ps}px;top:${T+20}px;width:${ps}px;height:${ps}px;border-radius:50%;overflow:hidden"><video id="timeline-presenter" src="${e(ctx.media)}" muted playsinline data-start="0" data-duration="6.6" data-track-index="1" style="width:100%;height:100%;object-fit:cover;object-position:${ctx.frame?ctx.frame(ps,ps):'50% 30%'}"></video></div>`);reveal('timeline-presenter-frame',.16);}
  css(`.time-point{background:var(--ink);border-radius:50%}.time-date{letter-spacing:-.02em}${P?'':'.time-date{align-items:flex-end}'}.time-cap{align-items:flex-start;color:var(--muted)}`);return k.finish(6.6);
 }
 if(name==='funnel-absorption'){
  const L={'16:9':{fw:1300,sw:150,fTop:T+10,fH:470,g:[200,170],gi:104,gl:36,pw:440,ph:74,pf:40,pi:50,rf:76,cf:34},'4:3':{fw:1220,sw:140,fTop:T+10,fH:460,g:[190,160],gi:96,gl:34,pw:420,ph:72,pf:38,pi:48,rf:70,cf:32},'3:4':{fw:1020,sw:150,fTop:T+20,fH:620,g:[230,200],gi:124,gl:40,pw:480,ph:88,pf:46,pi:60,rf:88,cf:40},'9:16':{fw:1040,sw:160,fTop:T+30,fH:720,g:[260,230],gi:150,gl:46,pw:560,ph:100,pf:52,pi:68,rf:100,cf:46}}[A];
  const ins=d.inputs.slice(0,7),n=ins.length,cx=W/2,fBot=L.fTop+L.fH,[gw,gh]=L.g,half=y=>(L.fw-(y-L.fTop)/L.fH*(L.fw-L.sw))/2;
  // Scattered seats inside the silhouette: [u across the funnel width at that height, v down the funnel].
  const seats={1:[[0,.12]],2:[[-.42,.08],[.42,.14]],3:[[-.55,.06],[.5,.1],[0,.45]],4:[[-.58,.06],[.08,.02],[.62,.1],[-.05,.46]],5:[[-.6,.06],[.02,.02],[.62,.09],[-.45,.46],[.45,.5]],6:[[-.62,.04],[0,.01],[.62,.06],[-.45,.38],[.45,.4],[0,.7]],7:[[-.66,.04],[-.22,.01],[.22,.06],[.66,.02],[-.45,.38],[.45,.4],[0,.7]]}[n]||[];
  add(`<svg class="fd-path" viewBox="0 0 ${W} ${H}"><path id="funnel" d="M${cx-L.fw/2} ${L.fTop}H${cx+L.fw/2}L${cx+L.sw/2} ${fBot}H${cx-L.sw/2}Z" style="fill:color-mix(in srgb,var(--ink) 7%,transparent);stroke:var(--rule);stroke-width:2;stroke-dasharray:none"/></svg>`);reveal('funnel',.65,{y:0,scale:.94,duration:.45});
  ins.forEach((v,i)=>{const[u,vv]=seats[i],gy=L.fTop+vv*L.fH+8,gx=cx+u*half(gy+gh/2)-gw/2;add(glyph('funnel-input-'+i,gx,gy,gw,gh,v,['bulb','page','play','search','book','pen','audio'][i],'funnel-in','input-image-'+(i+1)));reveal('funnel-input-'+i,.16+i*.11,{scale:.8,y:20,duration:.26});tween('to','#funnel-input-'+i,{x:cx-gx-gw/2,y:fBot-30-gy-gh/2,scale:.08,opacity:0,duration:.72,ease:'power3.in'},1.4+i*.10);});
  const py=fBot+14,ry=py+L.ph+22,rh=Math.round(L.rf*1.2),cy2=ry+rh+16;
  add(box('processor',cx-L.pw/2,py,L.pw,L.ph,image('output-image',d.processor,'funnel-output-image')+`<span>${e(d.processor)}</span>`,'fd-solid'));reveal('processor',1.13,{scale:.92,y:0,duration:.25});add(text('funnel-result',60,ry,W-120,rh,d.result,L.rf,'center'));reveal('funnel-result',2.65,{y:28,duration:.35,ease:'expo.out'});add(text('funnel-recipient',60,cy2,W-120,Math.round(L.cf*1.3),d.recipient,L.cf,'center light muted'));reveal('funnel-recipient',3.35,{y:0,duration:.22});
  css(`.funnel-in{font-size:${L.gl}px;gap:10px;padding:0}.funnel-in .fd-icon,.funnel-in .fd-glyph-image{width:${L.gi}px;height:${L.gi}px}#processor{font-size:${L.pf}px;flex-direction:row;gap:18px;padding:10px 22px;border-radius:999px}.funnel-output-image{width:${L.pi}px;height:${L.pi}px;object-fit:cover;border-radius:50%;flex:none}`);return k.finish(6.5);
 }
 if(name==='convergence-evidence'){
  // Phase one: source rows converge on the finding (rows left, finding right, in every aspect; portrait uses taller rows). Phase two: one camera move compacts that network into a corner
  // while the observation sheet and audience take the open space. All rectangles stay between T and B.
  const L={'16:9':{mode:'row',ix:110,iw:560,inF:46,row:112,pw:600,disc:170,pf:58,net:[1150,T+30,700,300],aud:[1180,T+380,640,330],audF:46,audI:150,sheet:[80,T+40,1000,688],st:56,sr:32,simg:380},
   '4:3':{mode:'row',ix:70,iw:460,inF:42,row:104,pw:520,disc:150,pf:52,net:[860,T+30,540,260],aud:[860,T+340,540,330],audF:42,audI:130,sheet:[50,T+40,760,690],st:50,sr:30,simg:250},
   '3:4':{mode:'row',ix:60,iw:440,inF:56,row:150,pw:340,disc:170,pf:56,net:[40,T+20,580,320],aud:[640,T+30,400,300],audF:42,audI:130,sheet:[40,T+360,1000,620],st:58,sr:38,simg:320},
   '9:16':{mode:'row',ix:60,iw:440,inF:60,row:180,pw:340,disc:190,pf:60,net:[40,T+20,580,400],aud:[640,T+40,400,360],audF:48,audI:150,sheet:[40,T+430,1000,740],st:68,sr:44,simg:340}}[A];
  const ins=d.inputs.slice(0,6),n=ins.length,labH=Math.round(L.pf*2.3);let h='',px,py,dcx,dcy,rowY,rowsEnd;
  if(L.mode==='row'){const rowH=Math.min(L.row,(B-T-60)/n);rowY=i=>T+(B-T-n*rowH)/2+i*rowH;rowsEnd=rowY(n)-12;px=P?W-40-L.pw:W-60-L.pw;dcx=P?px+L.disc/2:px+L.pw/2;dcy=(T+B)/2-labH/2-10;py=dcy-L.disc/2;
   ins.forEach((v,i)=>{const y=rowY(i),yc=y+rowH/2-6;h+=text('evidence-in-'+i,L.ix,y,L.iw,rowH-12,v,L.inF);h+=path('evidence-route-'+i,`M${L.ix+L.iw+30} ${yc}C${(L.ix+L.iw+dcx)/2} ${yc} ${dcx-L.disc} ${dcy} ${dcx-L.disc/2-18} ${dcy}`);});}
  else{const rowH=L.row;rowY=i=>T+30+i*rowH;rowsEnd=rowY(n)-12;py=T+30+n*rowH+150;px=(W-L.pw)/2;dcx=W/2;dcy=py+L.disc/2;
   ins.forEach((v,i)=>{const y=rowY(i),yc=y+rowH/2-6;h+=text('evidence-in-'+i,L.ix,y,L.iw,rowH-12,v,L.inF);const x1=L.ix+Math.min(L.iw,textW(v,L.inF))+28;h+=path('evidence-route-'+i,`M${x1.toFixed(1)} ${yc}C${(x1+180).toFixed(1)} ${yc} ${dcx} ${py-240} ${dcx} ${py-18}`);});}
  ins.forEach((_,i)=>{reveal('evidence-in-'+i,.16+i*.13,{x:-20,y:0,duration:.26});draw('evidence-route-'+i,.55+i*.14,.48);});
  h+=box('evidence-processor',px,py,L.pw,L.disc+20+labH,`<i class="ev-disc">${icon('search',Math.round(L.disc*.5))}</i><span>${e(d.processor)}</span>`,'ev-proc');
  add(`<div id="evidence-network" style="position:absolute;inset:0">${h}</div>`);reveal('evidence-processor',1.4,{scale:.85,y:0,duration:.35});
  const bx=Math.min(L.ix,px),by=rowY(0),bw=Math.max(px+L.pw,L.ix+L.iw+40)-bx,bh=Math.max(rowsEnd,py+L.disc+20+labH)-by,[nx,ny,nw,nh]=L.net,s=Math.min(nw/bw,nh/bh);
  tween('to','#evidence-network',{scale:+s.toFixed(4),x:+(nx+(nw-bw*s)/2-bx*s).toFixed(1),y:+(ny+(nh-bh*s)/2-by*s).toFixed(1),transformOrigin:'0px 0px',duration:.65,ease:'power3.inOut'},2.25);
  const[sx,sy,sw,sh]=L.sheet;add(box('evidence-sheet',sx,sy,sw,sh,`<small>OBSERVATION NOTES</small><strong>${e(d.evidenceTitle)}</strong><div class="evidence-body">${image('evidence-image',d.evidenceTitle,'evidence-image')}<div class="evidence-notes">${d.evidenceRows.slice(0,4).map((v,i)=>`<p><b>${String(i+1).padStart(2,'0')}</b>${e(v)}</p>`).join('')}</div></div>`,'evidence-sheet'));
  reveal('evidence-sheet',2.8,{x:-70,y:0,rotation:-1.4,duration:.42,ease:'expo.out'});const[ax,ay,aw,ah]=L.aud;add(glyph('evidence-audience',ax,ay,aw,ah,d.audienceLabel,'people','ev-aud'));reveal('evidence-audience',3.65,{scale:.9,y:0,duration:.3});
  css(`.ev-proc{justify-content:flex-start;${P?'align-items:flex-start;text-align:left;':''}gap:20px;font-size:${L.pf}px;line-height:1.08}.ev-disc{flex:none;display:grid;place-items:center;width:${L.disc}px;height:${L.disc}px;border-radius:50%;background:var(--accent);color:var(--accent-ink)}.ev-aud{font-size:${L.audF}px;gap:18px;padding:0}.ev-aud .fd-icon{width:${L.audI}px;height:${L.audI}px}.evidence-sheet{align-items:stretch;justify-content:flex-start;text-align:left;background:var(--ink);color:var(--bg);padding:${P?34:38}px;gap:16px;border-radius:3px}.evidence-sheet small{font:400 22px var(--mono);letter-spacing:.1em;opacity:.7}.evidence-sheet strong{font-size:${L.st}px;line-height:1.04;font-weight:400;max-width:100%}.evidence-body{display:grid;grid-template-columns:${L.simg}px minmax(0,1fr);gap:28px;min-height:0;flex:1}.evidence-image{width:100%;height:100%;min-height:0;object-fit:cover;object-position:50% 16%;display:block;border-radius:2px}.evidence-notes{min-width:0}.evidence-sheet p{display:flex;gap:16px;font-size:${L.sr}px;line-height:1.2;margin:0 0 10px;padding:10px 0;border-top:1px solid color-mix(in srgb,var(--bg) 20%,transparent)}.evidence-sheet p b{font:400 22px var(--mono);padding-top:5px;flex:none}`);return k.finish(7.1);
 }
 throw new Error('Unknown diagram shot: '+name);
}
