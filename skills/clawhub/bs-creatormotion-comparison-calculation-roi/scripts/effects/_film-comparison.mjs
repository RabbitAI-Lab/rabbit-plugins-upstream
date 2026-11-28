import {CSS,end} from './_evidence-kit.mjs';
export * from './_evidence-kit.mjs';
export function finish(html,css,js,duration){return {html:`<div class="ev film-comparison">${html}</div>`,css:CSS+`.film-comparison h1{font-size:86px;font-weight:680;letter-spacing:-.036em}.film-comparison .surface{box-shadow:none;border-radius:6px}.film-comparison .top-title{top:74px}.film-comparison .tag{border-radius:3px}.film-comparison .number{font-family:var(--font),sans-serif;font-weight:650}.film-comparison .presenter{border-width:2px}`+css,js:js+end(duration),duration};}
export const wipe=(selector,t,d=.35)=>`tl.from(${JSON.stringify(selector)},{clipPath:'inset(0 100% 0 0)',duration:${d},ease:'expo.out'},${t});`;
export const pop=(selector,t,d=.24)=>`tl.from(${JSON.stringify(selector)},{scale:.92,opacity:0,duration:${d},ease:'power3.out'},${t});`;
