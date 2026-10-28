import {assert,text,date,id,integer} from './store.mjs';
export function handle(i,s,c){
 if(i.action==='plan'){
  const day=date(i.date);assert(!s.records.some(r=>r.date===day),'A plan exists for this date; use show, complete or rollover');assert(Array.isArray(i.tasks)&&i.tasks.length&&i.tasks.length<=100,'Provide 1..100 tasks');
  const row={id:id(),date:day,availableMinutes:integer(i.availableMinutes,1,1440),tasks:i.tasks.map(t=>({id:id(),title:text(t.title,'task',500),minutes:integer(t.minutes,1,1440),priority:integer(t.priority,1,3),status:'open'}))};row.tasks.sort((a,b)=>a.priority-b.priority);s.records.push(row);return {changed:true,result:summary(row)};
 }
 if(i.action==='rollover'){
  const from=date(i.from),to=date(i.to);assert(to>from,'Rollover target must be a later date');const old=s.records.find(r=>r.date===from);assert(old,'Source plan not found');let target=s.records.find(r=>r.date===to);if(!target)s.records.push(target={id:id(),date:to,availableMinutes:integer(i.availableMinutes,1,1440),tasks:[]});
  for(const t of old.tasks.filter(t=>t.status==='open')){if(!target.tasks.some(x=>x.sourceTaskId===t.id))target.tasks.push({...t,id:id(),sourceTaskId:t.id});t.status='deferred';}target.tasks.sort((a,b)=>a.priority-b.priority);return {changed:true,result:summary(target)};
 }
 const row=s.records.find(r=>r.date===date(i.date));assert(row,'Plan not found');
 if(i.action==='complete'){const t=row.tasks.find(t=>t.id===i.taskId);assert(t&&t.status==='open','Open task not found');t.status='done';return {changed:true,result:summary(row)};}
 assert(i.action==='show','action: plan, show, complete, rollover');return {result:summary(row)};
}
function summary(row){const plannedMinutes=row.tasks.filter(t=>t.status==='open').reduce((a,t)=>a+t.minutes,0);return {plan:row,remainingPlannedMinutes:plannedMinutes,overCapacityMinutes:Math.max(0,plannedMinutes-row.availableMinutes),completed:row.tasks.filter(t=>t.status==='done').length};}
