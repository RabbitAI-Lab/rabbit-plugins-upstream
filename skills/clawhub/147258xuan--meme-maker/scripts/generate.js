#!/usr/bin/env node
const { findTemplate, generateMeme, TEMPLATES } = require('../index');

const args = process.argv.slice(2);
const params = {};
for (const arg of args) {
  const m = arg.match(/^--(\w[\w-]*)=(.*)$/);
  if (m) params[m[1]] = m[2];
}

async function main() {
  let tid = params.template;
  if (tid && !/^\d+$/.test(tid)) {
    const matches = findTemplate(tid);
    if (!matches.length) {
      console.error(`"${tid}" not found. Available:`);
      TEMPLATES.forEach(t => console.log(`  - ${t.name}`));
      process.exit(1);
    }
    tid = matches[0].id;
    console.log(`Template: ${matches[0].name}`);
  }
  if (!tid) { console.error('Usage: --template="Drake" --top="text" --bottom="text"'); process.exit(1); }
  try {
    const r = await generateMeme({ 
      templateId: tid, 
      topText: params.top||'', 
      bottomText: params.bottom||'',
      username: process.env.IMGFLIP_USER,
      password: process.env.IMGFLIP_PASS
    });
    console.log(`\nMeme URL: ${r.url}\nPage: ${r.page_url}`);
  } catch (e) { console.error('Error:', e.message); process.exit(1); }
}
main();
