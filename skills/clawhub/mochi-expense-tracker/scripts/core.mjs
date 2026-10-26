import {assert,text,date,minor,currency,id,integer} from './store.mjs';
export function handle(i,s,c){
 if(i.action==='add'){
  assert(['expense','income','refund'].includes(i.kind),'kind: expense, income or refund');const amountMinor=minor(i.amount);assert(amountMinor>0,'Amount must be positive');
  const row={id:id(),kind:i.kind,date:date(i.date),amountMinor,currency:currency(i.currency),category:text(i.category,'category',80),description:text(i.description||i.category),createdAt:c.now};s.records.push(row);return {changed:true,result:{record:row}};
 }
 if(i.action==='void'){
  const row=s.records.find(r=>r.id===i.id&&r.kind!=='budget');assert(row&&!row.voided,'Active entry not found');row.voided=true;row.voidReason=text(i.reason,'reason',500);return {changed:true,result:{record:row}};
 }
 if(i.action==='budget'){
  assert(/^\d{4}-\d{2}$/.test(i.month||''),'Use YYYY-MM month');date(i.month+'-01');const curr=currency(i.currency),cat=text(i.category,'category',80),amountMinor=minor(i.amount);
  let row=s.records.find(r=>r.kind==='budget'&&r.month===i.month&&r.currency===curr&&r.category===cat);
  if(row)row.amountMinor=amountMinor;else{s.records.push(row={id:id(),kind:'budget',month:i.month,currency:curr,category:cat,amountMinor});}return {changed:true,result:{budget:row}};
 }
 assert(['list','summary'].includes(i.action),'action: add, void, budget, list, summary');
 const from=date(i.from),to=date(i.to);assert(from<=to,'from must be on or before to');
 const rows=s.records.filter(r=>r.kind!=='budget'&&!r.voided&&r.date>=from&&r.date<=to),groups={};
 for(const r of rows){const k=r.currency;groups[k]??={currency:k,incomeMinor:0,expenseMinor:0,refundMinor:0,categories:Object.create(null)};const g=groups[k];g[r.kind+'Minor']+=r.amountMinor;assert(Number.isSafeInteger(g[r.kind+'Minor']),'Summary exceeds safe arithmetic');if(r.kind!=='income')g.categories[r.category]=(g.categories[r.category]||0)+(r.kind==='refund'?-1:1)*r.amountMinor;}
 const budgets=s.records.filter(r=>r.kind==='budget'&&r.month+'-01'<=to&&r.month+'-31'>=from).map(b=>({...b,spentMinor:s.records.filter(r=>!r.voided&&r.kind!=='budget'&&r.kind!=='income'&&r.currency===b.currency&&r.category===b.category&&r.date.startsWith(b.month)).reduce((a,r)=>a+(r.kind==='refund'?-1:1)*r.amountMinor,0)}));
 return {result:{from,to,records:i.action==='list'?rows:undefined,totals:Object.values(groups).map(g=>({...g,netExpenseMinor:g.expenseMinor-g.refundMinor})),budgets}};
}
