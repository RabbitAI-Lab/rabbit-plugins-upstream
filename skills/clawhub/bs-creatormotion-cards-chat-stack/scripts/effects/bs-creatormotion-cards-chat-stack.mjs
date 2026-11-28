export const defaults={"messages": ["What should I work on today?", "Choose one task that would make tomorrow easier.", "Make the first step small enough to finish in fifteen minutes."], "placeholder": "Write the next question"};
export const meta={"slug": "bs-creatormotion-cards-chat-stack", "name": "Chat Message Stack", "category": "cards", "description": "Add chat messages into a stable conversation shell. Preserve message wrapping and the shared input area as the stack grows.", "duration": 7};

// The conversation sits directly on the canvas grid: a quiet header, one speaker marker, balloons that size to their
// copy, and the input line right below them; the group is centred between the top band and the caption band. No panel
// frames the conversation.
const layout={
 '16:9':{m:180,header:36,msg:54,msgMax:1300,avatar:108,gap:28,input:36,inputH:100},
 '4:3':{m:96,header:34,msg:48,msgMax:1040,avatar:96,gap:26,input:34,inputH:92},
 '3:4':{m:56,header:36,msg:56,msgMax:800,avatar:92,gap:30,input:36,inputH:100},
 '9:16':{m:56,header:42,msg:68,msgMax:820,avatar:110,gap:38,input:44,inputH:124},
};

export default function build(ctx){
 const d=ctx.data,e=ctx.esc,L=layout[ctx.aspect||'16:9'],W=ctx.width,H=ctx.height,top=ctx.safe.top,bottom=H-ctx.safe.bottom,A=[];
 const img=(key,alt)=>{if(!ctx.images?.[key])throw new Error(`Supply ${key} in --images. Real image content is required.`);return `<img src="${e(ctx.images[key])}" alt="${e(alt)}">`;};
 const messages=(d.messages||[]).slice(0,4),inset=Math.round(L.msg*.6);
 let html=`<section id="chat-shell" class="chat-shell" style="left:${L.m}px;top:${top+24}px;width:${W-2*L.m}px;height:${bottom-top-48}px"><header id="chat-header" class="chat-header"><span class="chat-mark"></span>Conversation</header><div class="chat-body"><div id="chat-avatar" class="chat-avatar">${img('chatAvatar','Conversation participant portrait')}</div><div class="chat-messages">`;
 messages.forEach((v,i)=>{html+=`<div id="message-${i}" class="message">${e(v)}</div>`;A.push(`tl.from('#message-${i}',{opacity:0,scale:.93,y:14,duration:.22,ease:'power4.out'},${(.5+i*1.05).toFixed(2)});`);});
 html+=`</div></div><div id="chat-input" class="chat-input"><b class="chat-add">+</b><span class="chat-placeholder">${e(d.placeholder)}</span><span class="chat-send"><svg viewBox="0 0 24 24"><path d="M12 19V5M5 12l7-7 7 7"/></svg></span></div></section>`;
 A.push(`tl.to({}, {duration:.01},6.99);`);
 const css=`.stage{position:absolute;inset:0;overflow:hidden}
.chat-shell{position:absolute;display:flex;flex-direction:column;justify-content:center;gap:${Math.round(L.gap*1.6)}px}
.chat-header{display:flex;align-items:center;gap:16px;font-size:${L.header}px;color:var(--muted);padding-bottom:${Math.round(L.gap*.8)}px;border-bottom:1.5px solid var(--rule)}
.chat-mark{display:block;width:${Math.round(L.header*1.15)}px;height:${Math.round(L.header*.95)}px;border:2.5px solid currentColor;border-radius:10px 10px 10px 3px}
.chat-body{flex:none;display:flex;align-items:flex-start;gap:${Math.round(L.avatar*.32)}px}
.chat-avatar{width:${L.avatar}px;height:${L.avatar}px;flex:none;overflow:hidden;border-radius:50%;background:var(--surface);border:2px solid var(--rule)}
.chat-avatar img{display:block;width:100%;height:100%;object-fit:cover;object-position:50% 40%}
.chat-messages{display:flex;flex-direction:column;align-items:flex-start;gap:${L.gap}px;min-width:0;padding-top:${Math.round(L.avatar*.1)}px}
.message{position:relative;max-width:${L.msgMax}px;padding:${Math.round(L.msg*.5)}px ${Math.round(L.msg*.75)}px;font-size:${L.msg}px;line-height:1.2;letter-spacing:-.005em;border-radius:${inset}px ${inset}px ${inset}px 8px;background:var(--ink);color:var(--bg);transform-origin:0 100%;text-wrap:pretty}
.message:before{content:"";position:absolute;left:-12px;bottom:0;width:28px;height:24px;background:var(--ink);clip-path:polygon(100% 0,100% 100%,0 100%,50% 60%)}
.chat-input{flex:none;height:${L.inputH}px;display:flex;align-items:center;gap:${Math.round(L.input*.7)}px;padding:0 ${Math.round(L.inputH*.16)}px 0 ${Math.round(L.input*.9)}px;border-radius:999px;background:var(--surface);border:1.5px solid var(--rule);font-size:${L.input}px;color:var(--muted)}
.chat-add{font-weight:400;font-size:${Math.round(L.input*1.4)}px;line-height:1}
.chat-placeholder{flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.chat-send{width:${Math.round(L.inputH*.68)}px;height:${Math.round(L.inputH*.68)}px;flex:none;display:grid;place-items:center;border-radius:50%;background:var(--accent)}
.chat-send svg{width:55%;height:55%}.chat-send path{fill:none;stroke:var(--accent-ink);stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}`;
 return {html:`<div class="stage">${html}</div>`,css,js:A.join('\n'),duration:7};
}
