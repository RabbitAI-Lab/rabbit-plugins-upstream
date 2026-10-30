import fs from 'node:fs';import path from 'node:path';import {assert,text,integer,safePath} from './store.mjs';
export function handle(i,s,c){
 assert(['read','search'].includes(i.action),'action: read or search');const relative=text(i.file,'file',1000),file=safePath(c.workspace,relative,true);assert(['.txt','.md','.csv','.tsv','.json','.log'].includes(path.extname(file).toLowerCase()),'Convert PDF, Word or image content to UTF-8 text with an available reader first');assert(fs.statSync(file).isFile()&&fs.statSync(file).size<=2*1024*1024,'Text document must be at most 2 MiB');
 const bytes=fs.readFileSync(file);const content=new TextDecoder('utf-8',{fatal:true}).decode(bytes);assert(!content.includes('\0'),'Binary data is not a text document');const lines=content.replace(/^\uFEFF/,'').split(/\r?\n/),limit=i.limit===undefined?60:integer(i.limit,1,200);let result;
 if(i.action==='search'){const q=text(i.query,'query',1000).normalize('NFKC').toLowerCase();result=lines.map((v,k)=>({line:k+1,text:v})).filter(r=>r.text.normalize('NFKC').toLowerCase().includes(q));}
 else {const start=i.start===undefined?1:integer(i.start,1,Math.max(1,lines.length));result=lines.map((v,k)=>({line:k+1,text:v})).slice(start-1);}
 const rows=result.slice(0,limit).map(r=>({...r,text:r.text.slice(0,2000),lineTruncated:r.text.length>2000}));return {result:{file:relative,totalLines:lines.length,matches:result.length,returned:rows.length,truncated:result.length>limit,lines:rows,citationFormat:relative+':LINE'}};
}
