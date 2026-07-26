const cheerio = require('cheerio');
const fs = require('fs');
const data = JSON.parse(fs.readFileSync('./last_article_raw.json', 'utf-8'));
const $ = cheerio.load(data.msg_content || '');
const paras = [];
$('p,section,blockquote,h1,h2,h3,h4,li').each((i, el) => {
  const t = $(el).text().replace(/\s+/g, ' ').trim();
  if (t && t.length > 1) paras.push(t);
});
const md = paras.join('\n\n');
fs.writeFileSync('./last_article.md', md);
console.log('PARAS:', paras.length);
console.log('CHARS:', md.length);
console.log('---FIRST 3000---');
console.log(md.substring(0, 3000));
console.log('---LAST 1500---');
console.log(md.substring(md.length - 1500));
