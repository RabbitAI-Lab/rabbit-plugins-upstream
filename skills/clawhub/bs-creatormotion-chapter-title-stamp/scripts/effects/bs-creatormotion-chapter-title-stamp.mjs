export const meta={"slug":"bs-creatormotion-chapter-title-stamp","name":"Chapter Title Stamp","category":"chapter","duration":6.8,"description":"A compact chapter title lands with a slight angular settle, followed by its small ordinal. A geometric aperture connects it to the next scene."};
export const defaults={"title":"Remove the extra step","ordinal":"CHAPTER 02","nextSceneTitle":"Make room for focus","nextSceneBody":"One decision. One action."};

// Both shots sit on the grid canvas, centred in the space between the caption bands. The stamp is an optically
// condensed uppercase title (an inner scaleX keeps the GSAP stamp transform on the outer element). The second shot
// is a document layout: a tilted photo print beside the copy in landscape, above it in portrait.
const layout={
 '16:9':{title:150,maxw:1500,ord:30,row:true,photo:[840,620],copyW:700,gap:90,h2:100,body:40},
 '4:3':{title:132,maxw:1200,ord:28,row:true,photo:[640,540],copyW:560,gap:70,h2:80,body:34},
 '3:4':{title:150,maxw:940,ord:30,row:false,photo:[940,580],copyW:940,gap:56,h2:96,body:40},
 '9:16':{title:172,maxw:940,ord:32,row:false,photo:[940,780],copyW:940,gap:64,h2:116,body:48},
};

export default function build({data:d,images={},esc:e,aspect='16:9',width:W,height:H,safe}){
 if(!images['next-scene-image'])throw new Error('Missing next-scene-image. Use a bundled default or a user image.');
 const L=layout[aspect],sx=.79,regionH=H-safe.top-safe.bottom,[pw,ph]=L.photo;
 const copyH=L.h2*1.1*2+L.body*1.4+70,nw=L.row?pw+L.gap+L.copyW:L.copyW,nh=L.row?Math.max(ph,copyH):ph+L.gap+copyH;
 const nx=Math.round((W-nw)/2),ny=Math.round(safe.top+(regionH-nh)/2);
 return {duration:6.8,
 html:`<section class="stamp-stage"><div id="stamp-title" data-layout-allow-occlusion="aperture-transition"><span class="stamp-condensed">${e(d.title)}</span></div><div id="stamp-ordinal" class="mono" data-layout-allow-occlusion="aperture-transition">${e(d.ordinal)}</div></section><section id="stamp-next" class="stamp-next"><div class="stamp-doc"><div class="stamp-photo"><img src="${e(images['next-scene-image'])}" alt="Workshop scene"/></div><div class="stamp-copy"><h2>${e(d.nextSceneTitle)}</h2><i class="stamp-rule"></i><p>${e(d.nextSceneBody)}</p></div></div></section><div id="stamp-mask-a" class="stamp-mask a"></div><div id="stamp-mask-b" class="stamp-mask b"></div>`,
 css:`.stamp-stage,.stamp-next{position:absolute;inset:0;background:var(--canvas-bg)}
.stamp-stage{padding:${safe.top}px 0 ${safe.bottom}px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:30px;text-align:center}
#stamp-title{width:${L.maxw}px;display:flex;justify-content:center}
.stamp-condensed{flex:none;width:${Math.round(L.maxw/sx)}px;font-size:${L.title}px;line-height:1;letter-spacing:-.01em;text-transform:uppercase;text-wrap:balance;transform:scaleX(${sx})}
#stamp-ordinal{font-size:${L.ord}px;letter-spacing:.10em;text-transform:uppercase;color:var(--ink)}
.stamp-doc{position:absolute;left:${nx}px;top:${ny}px;width:${nw}px;display:flex;flex-direction:${L.row?'row':'column'};align-items:${L.row?'center':'stretch'};gap:${L.gap}px}
.stamp-photo{flex:none;width:${pw}px;height:${ph}px;overflow:hidden;border:12px solid var(--surface);box-shadow:0 22px 60px rgba(0,0,0,.2);transform:rotate(-2deg)}
.stamp-photo img{width:100%;height:100%;object-fit:cover;display:block}
.stamp-copy{width:${L.copyW}px;display:flex;flex-direction:column;gap:28px}
.stamp-copy h2{font-size:${L.h2}px;line-height:1.08;letter-spacing:-.01em;text-wrap:balance}
.stamp-rule{display:block;width:100%;height:2px;background:var(--rule)}
.stamp-copy p{font-size:${L.body}px;line-height:1.4;color:var(--muted);text-wrap:balance}
.stamp-mask{position:absolute;inset:0;background:var(--accent);pointer-events:none}
.stamp-mask.a{clip-path:polygon(0 0,100% 0,0 100%)}.stamp-mask.b{clip-path:polygon(100% 0,100% 100%,0 100%)}`,
 js:`tl.from('#stamp-title',{scale:.80,rotation:-7,opacity:0,duration:.34,ease:'power4.out'},.16);tl.from('#stamp-ordinal',{opacity:0,duration:.18},.53);tl.fromTo('#stamp-mask-a',{xPercent:0,yPercent:0},{xPercent:-105,yPercent:-105,duration:.26,ease:'power2.inOut'},.12);tl.fromTo('#stamp-mask-b',{xPercent:0,yPercent:0},{xPercent:105,yPercent:105,duration:.26,ease:'power2.inOut'},.12);tl.from('#stamp-next',{opacity:0,duration:.001},3.2);tl.to('#stamp-mask-a',{xPercent:0,yPercent:0,duration:.22,ease:'power3.in'},2.96);tl.to('#stamp-mask-b',{xPercent:0,yPercent:0,duration:.22,ease:'power3.in'},2.96);tl.set('#stamp-title,#stamp-ordinal',{opacity:0},3.2);tl.to('#stamp-mask-a',{xPercent:-105,yPercent:-105,duration:.32,ease:'power3.out'},3.22);tl.to('#stamp-mask-b',{xPercent:105,yPercent:105,duration:.32,ease:'power3.out'},3.22);`};
}
