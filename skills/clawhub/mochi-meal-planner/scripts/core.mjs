import {assert,text,date,id,integer,minor,currency} from './store.mjs';
const units={g:['g',1],kg:['g',1000],克:['g',1],千克:['g',1000],ml:['ml',1],l:['ml',1000],毫升:['ml',1],升:['ml',1000],个:['个',1]};
function quantity(x){assert(typeof x==='number'&&Number.isFinite(x)&&x>=0&&x<=1e6,'quantity: expected a finite number from 0 to 1000000');return x;}
const norm=s=>text(s,'ingredient',100).normalize('NFKC').trim().toLowerCase();
function ingredient(x){const name=norm(x.name),u=text(x.unit,'unit',30).toLowerCase(),[unit,factor]=units[u]||[u,1];return {name,unit,quantity:quantity(x.quantity)*factor};}
export function handle(i,s,c){
 if(i.action==='show'){const row=s.records.find(r=>r.id===i.id);assert(row,'Meal plan not found');return {result:{plan:row}};}
 assert(i.action==='plan','action: plan or show');assert(Array.isArray(i.meals)&&i.meals.length&&i.meals.length<=42,'Provide 1..42 meals');const exclusions=(i.exclude||[]).map(norm);const shopping=new Map();
 const meals=i.meals.map(m=>{assert(['breakfast','lunch','dinner'].includes(m.slot),'slot: breakfast, lunch or dinner');const ingredients=m.ingredients.map(ingredient);assert(ingredients.length,'Provide meal ingredients');for(const x of ingredients){assert(!exclusions.some(t=>x.name.includes(t)),'Ingredient conflicts with an exclusion: '+x.name);const k=JSON.stringify([x.name,x.unit]);shopping.set(k,{name:x.name,unit:x.unit,quantity:(shopping.get(k)?.quantity||0)+x.quantity});}return {date:date(m.date),slot:m.slot,dish:text(m.dish,'dish',200),servings:integer(m.servings,1,50),ingredients};});
 const slots=meals.map(m=>m.date+':'+m.slot);assert(new Set(slots).size===slots.length,'One meal per date and slot; combine dishes into a meal');
 for(const p of (i.pantry||[]).map(ingredient)){const item=shopping.get(JSON.stringify([p.name,p.unit]));if(item)item.quantity=Math.max(0,item.quantity-p.quantity);}
 const row={id:id(),meals,exclude:exclusions,shopping:[...shopping.values()].map(x=>({...x,quantity:Math.round(x.quantity*1e6)/1e6})).filter(x=>x.quantity>0),createdAt:c.now};
 if(i.budget)row.budget={amountMinor:minor(i.budget.amount),currency:currency(i.budget.currency)};s.records.push(row);return {changed:true,result:{plan:row}};
}
