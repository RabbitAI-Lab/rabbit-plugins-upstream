export const meta={"slug":"bs-creatormotion-chapter-character-reveal","name":"Chapter Character Reveal","category":"chapter","duration":6.8,"description":"A chapter label introduces a headline that becomes readable one character at a time. The completed phrase holds on a quiet full-screen stage."};
export const defaults={"label":"PART 03","title":"Make feedback visible"};

// Label strip and headline sit directly on the grid, centred in the space between the caption bands. Glyphs are
// grouped per word so lines only break between words (the space is a real, hanging space so wrapped lines stay centred); portrait wraps to a taller block with larger type.
// The faint diagonal watermark is sized to stay inside the canvas.
const layout={
 '16:9':{title:184,label:34,max:1650,wm:400},
 '4:3':{title:164,label:32,max:1260,wm:320},
 '3:4':{title:196,label:34,max:940,wm:300},
 '9:16':{title:212,label:38,max:940,wm:320},
};

export default function build({data:d,esc:e,aspect="16:9",width:W,height:H,safe}){
 const L=layout[aspect],chars=Array.from(d.title),cjk=/[\u2e80-\u9fff\uf900-\ufaff\uff00-\uffef]/;
 const wm=Math.min(L.wm,Math.floor(W*.8/(Math.max(1,Array.from(d.label).length)*.56)));
 let i=0,html='',word='';
 const flush=()=>{if(word){html+=`<span class="word">${word}</span>`;word='';}};
 for(const c of chars){const id=`char-${i++}`;
  if(c===' '){flush();html+=`<span class="char char-space" id="${id}"> </span>`;}
  else if(cjk.test(c)){flush();html+=`<span class="char" id="${id}">${e(c)}</span>`;}
  else word+=`<span class="char" id="${id}">${e(c)}</span>`;}
 flush();
 return {duration:6.8,
 html:`<section class="char-stage"><div class="char-watermark" aria-hidden="true">${e(d.label)}</div><div id="char-label" class="mono">${e(d.label)}</div><h1 id="char-title">${html}</h1></section>`,
 css:`.char-stage{position:absolute;inset:0;padding:${safe.top}px 64px ${safe.bottom}px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:36px;text-align:center}
.char-watermark{position:absolute;left:50%;top:${Math.round((safe.top+H-safe.bottom)/2)}px;font-size:${wm}px;line-height:1;letter-spacing:-.02em;transform:translate(-50%,-50%) rotate(-8deg);opacity:.04;white-space:nowrap;pointer-events:none}
#char-label{font-size:${L.label}px;letter-spacing:.06em;text-transform:uppercase;background:var(--accent);color:var(--accent-ink);padding:6px 16px 5px;border-radius:0}
#char-title{font-size:${L.title}px;line-height:1.04;letter-spacing:-.015em;max-width:${L.max}px;text-wrap:balance}
.word{display:inline-block;white-space:nowrap}.char{display:inline-block}.char-space{display:inline;word-spacing:.04em;letter-spacing:0}`,
 js:`tl.from('#char-label',{opacity:0,scale:.9,duration:.18,ease:'power2.out'},.16);tl.from('#char-title .char',{opacity:.045,duration:.12,stagger:${(.88/Math.max(1,chars.length)).toFixed(4)},ease:'none'},.50);`};
}
