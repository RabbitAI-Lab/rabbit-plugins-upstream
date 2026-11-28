import {imageSlot} from './_media-image-slots.mjs';
export const meta={"slug": "bs-creatormotion-pip-chat-response", "name": "Chat Response Presenter", "category": "pip", "duration": 6.8, "description": "A page and circular speaker establish context before a short exchange unfolds. The question, waiting beat and answer expansion have separate timing, with a restrained camera push during the reading hold."};
export const defaults={"pageTitle":"Weekly review","question":"What should I improve next week?","reply":"Protect one focused hour. Review the result before adding another task."};

// The browser page is the demonstration (a depicted window, square corners, no drop shadow); the presenter is a
// small camera inset in the top-right corner. Landscape keeps the conversation inside the page, beside its notes.
// Portrait puts the page beside the presenter on top and lets the conversation run full width below, directly on
// the grid. Everything ends above the caption band.
const layout={
 '16:9':{pip:[1600,72,264,330],page:[56,72,1500,752],head:64,col:600,pad:56,h1:88,intro:32,photo:330,bubble:34,inside:true},
 '4:3':{pip:[1122,64,270,320],page:[48,64,1050,762],head:60,col:440,pad:44,h1:64,intro:28,photo:250,bubble:30,inside:true},
 '3:4':{pip:[776,72,264,300],page:[40,72,704,476],head:52,col:624,pad:40,h1:60,intro:28,photo:176,bubble:34,chat:[40,584,1000,490]},
 '9:16':{pip:[776,170,264,330],page:[40,170,704,536],head:56,col:624,pad:40,h1:76,intro:32,photo:220,bubble:44,chat:[40,760,1000,590]},
};

export default function build(ctx){
 const {data:d,media,esc:e,aspect='16:9'}=ctx,L=layout[aspect];
 const rect=([l,t,w,h])=>`left:${l}px;top:${t}px;width:${w}px;height:${h}px`;
 const [,,pw,ph]=L.page,asideLeft=L.pad*2+L.col;
 const thread=`<aside id="chat-thread" class="chat-panel"><div class="chat-panel-label mono">${imageSlot(ctx,'chat-avatar','Conversation partner','chat-agent-avatar')}REFLECT</div><div id="chat-question" class="chat-bubble question">${e(d.question)}</div><div id="chat-wait" class="chat-wait"><i></i><i></i><i></i></div><div id="chat-reply" class="chat-bubble reply">${e(d.reply)}</div></aside>`;
 return {duration:6.8,
 html:`<div id="chat-page" class="chat-page"><header class="mono">WORKING NOTES</header><section><h1>${e(d.pageTitle)}</h1><p class="chat-intro">A small question can clarify the next step.</p>${imageSlot(ctx,'page-image','Workshop visual','chat-page-photo')}</section>${L.inside?thread:''}</div>${L.inside?'':thread}<div id="chat-person" class="chat-person"><video id="chat-person-video" src="${e(media)}" muted playsinline data-start="0" data-duration="6.8" data-track-index="0"></video></div>`,
 css:`.chat-page{position:absolute;${rect(L.page)};box-sizing:border-box;border:1.5px solid var(--rule);border-radius:8px;background:var(--surface);overflow:hidden;transform-origin:60% 50%}
.chat-page header{height:${L.head}px;box-sizing:border-box;border-bottom:1.5px solid var(--rule);padding:0 ${L.pad}px;display:flex;align-items:center;font-size:22px;letter-spacing:.08em;color:var(--muted)}
.chat-page section{padding:${Math.round(L.pad*.8)}px ${L.pad}px 0;width:${L.col+L.pad*2}px;box-sizing:border-box;height:calc(100% - ${L.head}px);padding-bottom:${L.pad}px;display:flex;flex-direction:column;gap:${Math.round(L.pad*.4)}px}
.chat-page h1{font-size:${L.h1}px;line-height:1.04;margin:0;font-weight:400;letter-spacing:-.01em}
.chat-intro{font-size:${L.intro}px;line-height:1.3;color:var(--muted);margin:0}
.chat-page .chat-page-photo{display:block;width:100%;flex:1 1 0;min-height:0;margin-top:${Math.round(L.pad*.3)}px;object-fit:cover;object-position:0 0;border-radius:4px}
.chat-panel{position:absolute;${L.inside?`left:${asideLeft}px;right:${L.pad}px;top:${L.head+Math.round(L.pad*.8)}px;bottom:${L.pad}px`:rect(L.chat)};display:flex;flex-direction:column;gap:${L.inside?22:26}px}
.chat-panel-label{display:flex;align-items:center;gap:16px;font-size:22px;letter-spacing:.08em;color:var(--muted)}.chat-agent-avatar{width:52px;height:52px;border-radius:50%;object-fit:cover}
.chat-bubble{padding:${Math.round(L.bubble*.75)}px ${Math.round(L.bubble*.85)}px;font-size:${L.bubble}px;line-height:1.3;border-radius:16px;box-sizing:border-box}
.question{background:var(--accent);color:var(--accent-ink);align-self:flex-end;max-width:86%}
.reply{background:${L.inside?'var(--bg)':'var(--surface)'};border:1.5px solid var(--rule);align-self:flex-start;max-width:92%}
.chat-wait{display:flex;gap:15px;height:28px;margin:4px 24px;align-items:center}.chat-wait i{width:17px;height:17px;border-radius:50%;background:var(--muted)}
.chat-person{position:absolute;${rect(L.pip)};border-radius:28px;overflow:hidden;border:3px solid var(--surface);box-sizing:border-box}
.chat-person video{width:100%;height:100%;object-fit:cover;object-position:${ctx.frame(L.pip[2],L.pip[3])}}`,
 js:`tl.from('#chat-page',{opacity:0,scale:.985,duration:.38,ease:'power2.out'},.16);tl.from('#chat-person',{opacity:0,duration:.25},.16);${L.inside?'':`tl.from('#chat-thread .chat-panel-label',{opacity:0,duration:.25},.4);`}tl.from('#chat-question',{clipPath:'inset(0 0 100% 0)',y:8,duration:.32,ease:'power2.out'},.65);tl.from('#chat-wait',{opacity:0,duration:.16},1.2);tl.to('#chat-wait i',{y:-6,duration:.2,stagger:.1,yoyo:true,repeat:2,ease:'sine.inOut'},1.25);tl.to('#chat-wait',{opacity:0,duration:.12},2.2);tl.from('#chat-reply',{clipPath:'inset(0 0 100% 0)',opacity:0,duration:.42,ease:'power2.out'},2.34);tl.to('#chat-page',{scale:1.03,duration:4.1,ease:'none'},2.7);`};
}
