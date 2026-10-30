import {assert,text,date,id} from './store.mjs';
export function handle(i,s,c){
 if(i.action==='add'){
  assert(['note','task','idea'].includes(i.kind),'kind: note, task or idea');
  const tags=i.tags||[];assert(Array.isArray(tags)&&tags.length<=3,'Use up to 3 tags');tags.forEach(t=>text(t,'tag',40));
  const row={id:id(),kind:i.kind,text:text(i.text),tags,status:'open',createdAt:c.now};if(i.due)row.due=date(i.due);
  s.records.push(row);return {changed:true,result:{record:row}};
 }
 if(i.action==='complete'||i.action==='archive'){
  const row=s.records.find(r=>r.id===i.id);assert(row,'Record not found');assert(i.action!=='complete'||row.kind==='task','Only tasks can be completed');row.status=i.action==='complete'?'done':'archived';row.updatedAt=c.now;return {changed:true,result:{record:row}};
 }
 assert(['list','search'].includes(i.action),'action: add, list, search, complete, archive');
 const q=i.query?text(i.query).normalize('NFKC').toLowerCase():'';assert(i.action!=='search'||q,'Search needs query');
 const rows=s.records.filter(r=>(i.status?r.status===i.status:r.status!=='archived')&&(!i.kind||r.kind===i.kind)&&(!q||(r.text+' '+r.tags.join(' ')).normalize('NFKC').toLowerCase().includes(q)));
 return {result:{records:rows}};
}
