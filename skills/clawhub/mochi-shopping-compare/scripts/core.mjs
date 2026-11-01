import {assert,text,date,minor,currency,id} from './store.mjs';
function url(value){const u=new URL(text(value,'url',2000));assert(['https:','http:'].includes(u.protocol)&&!u.username&&!u.password,'Use an ordinary product URL without credentials');return u.href;}
export function handle(i,s,c){
 if(i.action==='show'){const row=s.records.find(r=>r.id===i.id);assert(row,'Comparison not found');return {result:{comparison:row}};}
 assert(i.action==='compare','action: compare or show');assert(Array.isArray(i.items)&&i.items.length>=2&&i.items.length<=20,'Compare 2..20 products');const asOf=date(i.asOf);
 const items=i.items.map(p=>{const row={id:id(),name:text(p.name,'name',300),url:url(p.url),observedOn:date(p.observedOn),currency:currency(p.currency),quantity:p.quantity===undefined?1:p.quantity,specs:p.specs||{},evidence:text(p.evidence,'evidence',3000)};assert(row.observedOn<=asOf,'Observation is after comparison date');assert(Number.isSafeInteger(row.quantity)&&row.quantity>0&&row.quantity<=10000,'quantity: 1..10000');
  if(p.price!==undefined)row.priceMinor=minor(p.price);if(p.shipping!==undefined)row.shippingMinor=minor(p.shipping);row.discountMinor=minor(p.discount||'0');
  row.missing=[];if(row.priceMinor===undefined)row.missing.push('price');if(row.shippingMinor===undefined)row.missing.push('shipping');
  if(!row.missing.length){row.totalMinor=row.priceMinor*row.quantity+row.shippingMinor-row.discountMinor;assert(Number.isSafeInteger(row.totalMinor)&&row.totalMinor>=0,'Discount exceeds total');row.unitTotalMinor=row.totalMinor/row.quantity;}return row;});
 const row={id:id(),asOf,items,rankings:Object.fromEntries([...new Set(items.map(p=>p.currency))].map(curr=>[curr,items.filter(p=>p.currency===curr&&p.totalMinor!==undefined).sort((a,b)=>a.totalMinor-b.totalMinor).map(p=>({id:p.id,totalMinor:p.totalMinor,quantity:p.quantity,unitTotalMinor:p.unitTotalMinor}))])),criteria:i.criteria||[]};s.records.push(row);return {changed:true,result:{comparison:row}};
}
