// Real-browser validation; install Playwright separately or set PLAYWRIGHT_MODULE.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import crypto from 'node:crypto';
const args=process.argv.slice(2);const file=path.resolve(args[0]||'');const out=path.resolve(args[1]||'browser-qa');
if(!args[0])throw new Error('Usage: node qa_report.mjs report.html evidence-directory');
fs.mkdirSync(out,{recursive:true});
const {chromium}=await import(process.env.PLAYWRIGHT_MODULE||'playwright');
const browser=await chromium.launch({headless:true});const checks=[];let external=0;
try{
for(const [name,width,height,color] of [['desktop',1440,900,'light'],['mobile',390,844,'light'],['dark',1440,900,'dark']]){
 const context=await browser.newContext({viewport:{width,height},colorScheme:color,javaScriptEnabled:false});
 const page=await context.newPage();
 page.on('request',r=>{if(/^https?:/.test(r.url()))external++});
 await page.goto(pathToFileURL(file).href);await page.screenshot({path:path.join(out,name+'-cover.png')});
 const state=await page.evaluate(()=>({width:innerWidth,scroll:document.documentElement.scrollWidth,nav:getComputedStyle(document.querySelector('nav')).position,sections:document.querySelectorAll('section.report-section').length,links:[...document.querySelectorAll('nav a')].map(a=>a.getAttribute('href'))}));
 if(state.scroll>state.width||state.nav!=='fixed'||state.sections!==4)throw Error(name+' layout failed');
 checks.push(name+' viewport and fixed navigation');
 for(const href of state.links){
  await page.locator('nav a[href="'+href+'"]').click();
  const position=await page.evaluate(h=>({top:document.querySelector(h).getBoundingClientRect().top,bottom:document.querySelector('nav').getBoundingClientRect().bottom}),href);
  if(position.top<position.bottom-1)throw Error(name+' navigation obscures '+href);
  checks.push(name+' '+href);
 }
 await page.locator('nav a[href="#section-01"]').click();await page.screenshot({path:path.join(out,name+'-scope.png')});
 await page.locator('nav a[href="#search-intents"]').click();await page.screenshot({path:path.join(out,name+'-intent.png')});
 await page.locator('nav a[href="#section-04"]').click();await page.screenshot({path:path.join(out,name+'-competition.png')});
 await context.close();
}
if(external)throw Error('Unexpected external requests');
const result={status:'PASS',html_sha256:crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex'),checks,external_requests:external,javascript:false};
fs.writeFileSync(path.join(out,'browser_qa.json'),JSON.stringify(result,null,2));console.log(JSON.stringify({status:result.status,checks:checks.length,external_requests:external}));
}finally{await browser.close()}
