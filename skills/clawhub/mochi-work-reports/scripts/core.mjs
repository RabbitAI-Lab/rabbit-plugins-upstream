import {assert,text,date,id,minor} from './store.mjs';
export function handle(i,s,c){
 if(i.action==='add'){
  assert(['done','in-progress','blocked'].includes(i.status),'status: done, in-progress or blocked');assert(Array.isArray(i.evidence)&&i.evidence.length,'Provide evidence references such as a note path or user statement ID');const row={id:id(),date:date(i.date),title:text(i.title,'title',500),detail:text(i.detail,'detail'),status:i.status,evidence:i.evidence.map(x=>text(x,'evidence',1000)),createdAt:c.now};if(i.minutes!==undefined){assert(Number.isSafeInteger(i.minutes)&&i.minutes>=0&&i.minutes<=1440,'minutes: 0..1440');row.minutes=i.minutes;}s.records.push(row);return {changed:true,result:{record:row}};
 }
 assert(i.action==='report','action: add or report');const from=date(i.from),to=date(i.to);assert(from<=to,'Invalid report period');const records=s.records.filter(r=>r.date>=from&&r.date<=to);return {result:{from,to,records,sections:Object.fromEntries(['done','in-progress','blocked'].map(k=>[k,records.filter(r=>r.status===k)])),recordedMinutes:records.reduce((a,r)=>a+(r.minutes||0),0),recordsWithoutDuration:records.filter(r=>r.minutes===undefined).length}};
}
