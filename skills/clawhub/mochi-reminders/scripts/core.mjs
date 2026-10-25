import {assert,text,id} from './store.mjs';
const canonical=v=>v&&typeof v==='object'&&!Array.isArray(v)?Object.fromEntries(Object.keys(v).sort().map(k=>[k,canonical(v[k])])):v;
const equals=(a,b)=>JSON.stringify(canonical(a))===JSON.stringify(canonical(b));
export function prepare(i){
 const name=text(i.name,'name',120),message=text(i.message,'message',4000),timezone=text(i.timezone,'timezone',100);new Intl.DateTimeFormat('en',{timeZone:timezone}).format();
 const d=i.delivery;assert(d&&typeof d==='object','Delivery route is required');const delivery={agentId:text(d.agentId,'agentId',120),channel:text(d.channel,'channel',120),accountId:text(d.accountId,'accountId',200),to:text(d.to,'recipient',500)};
 const schedule=i.schedule;assert(schedule&&['at','cron','every'].includes(schedule.kind),'schedule.kind: at, cron or every');const value=text(schedule.value,'schedule.value',200);
 if(schedule.kind==='at'){assert(/(?:Z|[+-]\d\d:\d\d)$/.test(value)&&Number.isFinite(Date.parse(value)),'Use an ISO time with an explicit timezone offset');assert(Date.parse(value)>Date.now(),'One-shot time is in the past');}
 if(schedule.kind==='cron'){
  const parts=value.trim().split(/\s+/),ranges=[[0,59],[0,23],[1,31],[1,12],[0,7]];assert(parts.length===5,'Use a five-field cron expression');
  parts.forEach((part,n)=>part.split(',').forEach(term=>{const m=term.match(/^(\*|\d+(?:-\d+)?)(?:\/(\d+))?$/);assert(m,'Invalid cron field');if(m[2])assert(Number(m[2])>0&&Number(m[2])<=ranges[n][1]-ranges[n][0]+1,'Invalid cron step');if(m[1]!=='*'){const pair=m[1].split('-').map(Number);assert(pair.every(x=>x>=ranges[n][0]&&x<=ranges[n][1])&&(pair.length===1||pair[0]<=pair[1]),'Cron value is outside field range');}}));
 }
 if(schedule.kind==='every')assert(/^\d+[smhd]$/.test(value)&&parseInt(value)>0,'Use an interval such as 30m or 1d');
 const args=['automations','add','--name',name,'--agent',delivery.agentId,'--session','isolated','--message',message,'--'+schedule.kind,value];if(schedule.kind==='cron')args.push('--tz',timezone);args.push('--announce','--channel',delivery.channel,'--account',delivery.accountId,'--to',delivery.to,'--json');
 return {name,message,timezone,schedule:{kind:schedule.kind,value},delivery,cliArguments:args,status:'prepared'};
}
export function handle(i,s,c){
 if(i.action==='prepare')return {result:{plan:prepare(i)}};
 if(i.action==='record'){
  const plan=prepare(i.plan),r=i.receipt;assert(r&&typeof r==='object','Provide scheduler read-back receipt');assert(r.enabled===true&&Number.isFinite(r.nextRunAtMs)&&r.nextRunAtMs>Date.now(),'Receipt must include enabled state and a future next run');
  const jobId=text(r.jobId,'scheduler job ID',200);assert(equals(r.delivery,plan.delivery),'Receipt delivery does not match the requested route');assert(equals(r.schedule,plan.schedule),'Receipt schedule differs from the request');assert(r.timezone===plan.timezone,'Receipt timezone differs from the request');assert(!s.records.some(x=>x.jobId===jobId),'Job already recorded');
  const row={id:id(),jobId,name:plan.name,timezone:plan.timezone,schedule:plan.schedule,delivery:plan.delivery,nextRunAtMs:r.nextRunAtMs,enabled:true,status:'scheduled',createdAt:c.now};s.records.push(row);return {changed:true,result:{job:row}};
 }
 if(i.action==='update-receipt'){
  const row=s.records.find(x=>x.jobId===i.jobId);assert(row,'This job was not created in the current workspace');assert(['enabled','disabled','removed'].includes(i.state),'state: enabled, disabled or removed');assert(i.confirmedByScheduler===true,'Read back the scheduler before recording the new state');row.enabled=i.state==='enabled';row.status=i.state;return {changed:true,result:{job:row}};
 }
 assert(i.action==='list','action: prepare, record, list or update-receipt');return {result:{jobs:s.records,authority:'Reconcile current enabled state, schedule, run and delivery status with the native scheduler'}};
}
