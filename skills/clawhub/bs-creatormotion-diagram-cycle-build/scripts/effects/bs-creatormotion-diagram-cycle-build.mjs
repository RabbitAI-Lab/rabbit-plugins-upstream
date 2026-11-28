import {buildScene} from './_film-diagram-scenes-d.mjs';
export const defaults={"nodes":["Observe","Plan","Practice","Reflect"]};
export const meta={"slug":"bs-creatormotion-diagram-cycle-build","name":"Cycle Build and Close","category":"diagram","description":"Add nodes around a ring and complete the loop with a final return connection. Keep the closing edge as the payoff.","duration":7.2};
export default ctx=>{
 const scene=buildScene('cycle-build',ctx);
 ctx.data.nodes.slice(0,5).forEach((value,i)=>{const units=[...String(value)].reduce((n,c)=>n+(/[^\x00-\xff]/.test(c)?2:1),0);if(units>20)scene.css+=`#build-node-${i}{font-size:36px;gap:12px}#build-node-${i} .fd-icon{width:64px;height:64px}#build-node-${i} span{text-wrap:balance}`;});
 return scene;
};
