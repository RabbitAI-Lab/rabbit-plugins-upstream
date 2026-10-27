import {assert,text,date,id,integer,addDays} from './store.mjs';
export function handle(i,s,c){
 if(i.action==='add'){
  const row={id:id(),topic:text(i.topic,'topic',150),question:text(i.question),answer:text(i.answer),source:text(i.source,'source',1000),due:date(i.date),stage:0,reviews:[]};s.records.push(row);return {changed:true,result:{card:row}};
 }
 if(i.action==='grade'){
  const row=s.records.find(r=>r.id===i.id);assert(row,'Card not found');const day=date(i.date),grade=integer(i.grade,0,3);assert(!row.reviews.length||day>=row.reviews.at(-1).date,'Review date precedes prior review');row.stage=grade<2?0:Math.min(row.stage+1,5);row.due=addDays(day,[1,2,4,7,14,30][row.stage]);row.reviews.push({date:day,grade,response:text(i.response,'response'),feedback:text(i.feedback,'feedback')});return {changed:true,result:{card:row}};
 }
 assert(['due','show'].includes(i.action),'action: add, grade, due, show');if(i.action==='show'){const row=s.records.find(r=>r.id===i.id);assert(row,'Card not found');return {result:{card:row}};}
 const day=date(i.date);return {result:{date:day,cards:s.records.filter(r=>r.due<=day&&(!i.topic||r.topic===i.topic)).map(({answer,reviews,...r})=>r)}};
}
