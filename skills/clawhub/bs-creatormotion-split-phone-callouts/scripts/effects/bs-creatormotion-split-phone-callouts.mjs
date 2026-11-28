import {imageSlot} from './_media-image-slots.mjs';
export const meta={"slug": "bs-creatormotion-split-phone-callouts", "name": "Phone Feature Callouts", "category": "split", "duration": 6.8, "description": "A tall presenter crop sits beside an oversized phone demonstration. Two short capability labels land decisively inside the device after the main message is established."};
export const defaults={"phoneTitle":"Quick capture","message":"Keep a good idea before it disappears.","callouts":["Works offline","Organizes later"]};

// A hard split: the presenter fills one half edge to edge with no frame, the head centred in that half, and the
// phone stands directly on the canvas grid in the other half, as large as the space between the safe bands
// allows. Landscape: presenter left, phone right. Portrait: phone on top, presenter in the lower half.
// The callout labels stamp inside the device, never beside it, and the whole phone ends above the caption band.
// phone: [width, height] centred in the content half; type sizes are per aspect.
// Portrait follows ctx.split: the presenter fills [0, presenterTop, W, presenterHeight] so the whole head shows,
// and the phone (shorter and wider there) fits between contentTop and contentBottom. 3:4 lays the two tags in a row.
// avatar/kicker/inPad default to the landscape values.
const layout={
 '16:9':{phone:[470,744],pad:[60,36,30],h1:64,msg:38,tag:36,input:28},
 '4:3':{phone:[430,744],pad:[60,32,28],h1:58,msg:34,tag:32,input:28},
 '3:4':{phone:[580,496],pad:[46,26,18],h1:46,msg:30,tag:28,input:28,avatar:40,kicker:22,inPad:13,tagRow:true},
 '9:16':{phone:[620,600],pad:[54,30,22],h1:58,msg:34,tag:32,input:28,avatar:46,kicker:22,inPad:16},
};

export default function build(ctx){
 const {data:d,media,esc:e,aspect='16:9',portrait:P,width:W,height:H,safe}=ctx,L=layout[aspect],tags=(d.callouts||defaults.callouts).slice(0,2);
 // Regions: [left, top, width, height].
 const video=P?[0,ctx.split.presenterTop,W,ctx.split.presenterHeight]:[0,0,W/2,H];
 const top=P?ctx.split.contentTop:safe.top,bottom=P?ctx.split.contentBottom:H-safe.bottom,[pw,ph]=L.phone;
 const av=L.avatar||52,kicker=L.kicker||22,inPad=L.inPad||Math.round(L.input*.7);
 const phone=[P?(W-pw)/2:W/2+(W/2-pw)/2,Math.round(top+(bottom-top-ph)/2),pw,ph];
 const rect=([l,t,w,h])=>`left:${l}px;top:${t}px;width:${w}px;height:${h}px`,[pt,px,pb]=L.pad;
 return {duration:6.8,
 html:`<div id="callout-person" class="callout-person"><video id="callout-video" src="${e(media)}" muted playsinline data-start="0" data-duration="6.8" data-track-index="0"></video></div><div id="callout-phone" class="callout-phone">${imageSlot(ctx,'mobile-screen','Mobile capture workspace','callout-screen-image')}<i class="callout-notch"></i><div class="callout-header"><div class="callout-partner">${imageSlot(ctx,'chat-avatar','Conversation partner','callout-avatar')}<span class="mono">YOUR WORKSPACE</span></div><h1>${e(d.phoneTitle)}</h1></div><p id="callout-message">${e(d.message)}</p><div class="callout-tags">${tags.map((x,i)=>`<span id="callout-tag-${i}">${e(x)}</span>`).join('')}</div><div class="callout-input">Add a thought…</div></div>`,
 css:`.callout-person{position:absolute;${rect(video)};overflow:hidden}
.callout-person video{width:100%;height:100%;object-fit:cover;object-position:${ctx.frame(video[2],video[3])}}
.callout-phone{position:absolute;${rect(phone)};box-sizing:border-box;padding:${pt}px ${px}px ${pb}px;border:6px solid var(--ink);border-radius:56px;background:var(--surface);overflow:hidden;isolation:isolate;display:flex;flex-direction:column;gap:${Math.round(pt*.32)}px}
.callout-screen-image{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 0;z-index:-2}
.callout-phone::before{content:"";position:absolute;inset:0;background:color-mix(in srgb,var(--surface) 74%,transparent);z-index:-1}
.callout-notch{position:absolute;top:16px;left:50%;width:130px;height:18px;margin-left:-65px;border-radius:12px;background:var(--ink);z-index:2}
.callout-header{margin:${-pt}px ${-px}px 0;padding:${pt}px ${px}px ${Math.round(pt*.36)}px;background:var(--surface);display:flex;flex-direction:column;gap:${Math.round(pt*.26)}px}
.callout-partner{display:flex;align-items:center;gap:14px}.callout-avatar{width:${av}px;height:${av}px;border-radius:50%;object-fit:cover}.callout-partner span{font-size:${kicker}px;letter-spacing:.08em;color:var(--muted)}
.callout-phone h1{font-size:${L.h1}px;line-height:1.02;letter-spacing:-.01em;margin:0;font-weight:400}
.callout-phone p{margin:0;font-size:${L.msg}px;line-height:1.24;padding:${Math.round(L.msg*.55)}px ${Math.round(L.msg*.6)}px;background:var(--surface);border:1.5px solid var(--rule);border-radius:12px;box-shadow:0 6px 20px rgba(0,0,0,.14)}
.callout-tags{display:flex;flex-direction:${L.tagRow?'row':'column'};align-items:flex-start;gap:${Math.round(L.tag*.45)}px}
.callout-tags span{display:block;font-size:${L.tag}px;line-height:1.1;background:var(--accent);color:var(--accent-ink);padding:${Math.round(L.tag*.32)}px ${Math.round(L.tag*.55)}px;border-radius:4px;box-shadow:0 6px 16px rgba(0,0,0,.16)}
.callout-input{margin-top:auto;background:var(--surface);border:1.5px solid var(--rule);border-radius:14px;padding:${inPad}px 22px;color:var(--muted);font-size:${L.input}px;line-height:1.1}`,
 js:`tl.from('#callout-person',{opacity:0,duration:.28},.16);tl.from('#callout-phone',{y:80,opacity:0,duration:.45,ease:'power3.out'},.16);tl.from('#callout-message',{clipPath:'inset(0 100% 0 0)',duration:.8,ease:'none'},.65);${tags.map((_,i)=>`tl.from('#callout-tag-${i}',{scale:1.08,opacity:0,rotation:${i?-2:2},duration:.25,ease:'power3.out'},${(2.05+i*1.05).toFixed(2)});`).join('')}`};
}
