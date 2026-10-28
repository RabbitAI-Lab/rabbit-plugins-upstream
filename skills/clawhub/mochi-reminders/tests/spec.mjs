import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {transact,safePath} from '../scripts/store.mjs';
import {handle} from '../scripts/core.mjs';
const slug='mochi-reminders';
const root=fs.mkdtempSync(path.join(os.tmpdir(),slug+'-test-'));
let seq=0;
const fresh=()=>{const p=path.join(root,'w'+(++seq));fs.mkdirSync(p);return p;};
const call=(w,i)=>transact(w,slug,i,handle);
test.after(()=>fs.rmSync(root,{recursive:true,force:true}));
const spec=()=>({name:'weekly report',message:'Submit weekly report',timezone:'Asia/Shanghai',schedule:{kind:'cron',value:'0 20 * * 5'},delivery:{agentId:'family',channel:'openclaw-weixin',accountId:'fictional-account',to:'fictional-recipient'}});
test('prepare preserves exact owner, account, recipient and timezone without scheduling',()=>{const w=fresh(),p=call(w,{action:'prepare',...spec()}).plan;assert.equal(p.status,'prepared');assert.deepEqual(p.cliArguments.slice(0,2),['automations','add']);assert.equal(p.cliArguments[p.cliArguments.indexOf('--account')+1],'fictional-account');assert.equal(p.cliArguments[p.cliArguments.indexOf('--tz')+1],'Asia/Shanghai');assert.equal(call(w,{action:'list'}).jobs.length,0);});
test('receipt must match native route, schedule and a future enabled next run',()=>{const w=fresh(),p=spec(),receipt={jobId:'fixture-job',timezone:'Asia/Shanghai',enabled:true,nextRunAtMs:Date.now()+3600000,schedule:{value:'0 20 * * 5',kind:'cron'},delivery:{to:p.delivery.to,channel:p.delivery.channel,accountId:p.delivery.accountId,agentId:p.delivery.agentId}};assert.throws(()=>call(w,{action:'record',requestId:'bad',plan:p,receipt:{...receipt,delivery:{...receipt.delivery,accountId:'another-account'}}}));assert.throws(()=>call(w,{action:'record',requestId:'past',plan:p,receipt:{...receipt,nextRunAtMs:1}}));assert.equal(call(w,{action:'record',requestId:'ok',plan:p,receipt}).job.status,'scheduled');assert.equal(call(w,{action:'update-receipt',requestId:'pause',jobId:'fixture-job',state:'disabled',confirmedByScheduler:true}).job.enabled,false);});
test('a job from another workspace cannot be managed and invalid times are rejected',()=>{const w=fresh();assert.throws(()=>call(w,{action:'update-receipt',requestId:'x',jobId:'unknown',state:'removed',confirmedByScheduler:true}));assert.throws(()=>call(w,{action:'prepare',...spec(),timezone:'Not/A_Zone'}));assert.throws(()=>call(w,{action:'prepare',...spec(),schedule:{kind:'at',value:'2020-01-01T00:00:00Z'}}));});

test('cron ranges and timezone receipts are verified',()=>{const w=fresh();assert.throws(()=>call(w,{action:'prepare',...spec(),schedule:{kind:'cron',value:'99 25 * * *'}}));assert.throws(()=>call(w,{action:'record',requestId:'tz',plan:spec(),receipt:{jobId:'wrong-zone',enabled:true,nextRunAtMs:Date.now()+3600000,schedule:spec().schedule,delivery:spec().delivery,timezone:'UTC'}}));});

test('workspace confinement rejects traversal',()=>{const w=fresh();assert.throws(()=>safePath(w,'../outside'));});
test('two workspace stores do not share data',()=>{const a=fresh(),b=fresh();const h=(i,s)=>{s.records.push(i.value);return {changed:true,result:{records:s.records}};};transact(a,slug,{requestId:'a',value:'first'},h);const out=transact(b,slug,{action:'list'},(i,s)=>({result:{records:s.records}}));assert.equal(out.records.length,0);});
test('retry returns the saved result and rejects changed input',()=>{const w=fresh();let count=0;const h=()=>{count++;return {changed:true,result:{value:count}};};transact(w,slug,{requestId:'same',v:1},h);assert.equal(transact(w,slug,{requestId:'same',v:1},h).replayed,true);assert.equal(count,1);assert.throws(()=>transact(w,slug,{requestId:'same',v:2},h));});
test('busy state does not overwrite another operation',()=>{const w=fresh();const d=path.join(w,'.mochilab',slug);fs.mkdirSync(d,{recursive:true});fs.writeFileSync(path.join(d,'write.lock'),'active');assert.throws(()=>call(w,{action:'list'}),/busy/);assert.equal(fs.readFileSync(path.join(d,'write.lock'),'utf8'),'active');});
test('a failed operation preserves the previous state',()=>{const w=fresh();transact(w,slug,{requestId:'good'},(i,s)=>{s.records.push('saved');return {changed:true,result:{done:true}};});const file=path.join(w,'.mochilab',slug,'state.json'),before=fs.readFileSync(file,'utf8');assert.throws(()=>transact(w,slug,{requestId:'bad'},(i,s)=>{s.records.push('unsaved');throw new Error('failed');}));assert.equal(fs.readFileSync(file,'utf8'),before);});
test('linked paths are rejected when supported by the host',t=>{const w=fresh(),outside=fresh();try{fs.symlinkSync(outside,path.join(w,'linked'),process.platform==='win32'?'junction':'dir');}catch{t.skip('Host does not allow symlink creation');return;}assert.throws(()=>safePath(w,'linked/secret.txt'));});
