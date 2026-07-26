// Analyze WeChat articles using cheerio (same UA as extract.js uses)
const cheerio = require('cheerio');
const fs = require('fs');
const path = require('path');

const files = [
  'wechat-test1.html',
  'wechat-test4.html'
];

files.forEach(f => {
  const fp = path.join(__dirname, '..', 'scripts', f);
  if (!fs.existsSync(fp)) { console.log(f + ': FILE NOT FOUND'); return; }
  const html = fs.readFileSync(fp, 'utf8');
  const $ = cheerio.load(html);
  const title = $('meta[property="og:title"]').attr('content') || 'NONE';
  const desc = $('meta[property="og:description"]').attr('content') || 'NONE';
  const author = $('meta[property="og:article:author"]').attr('content') || 'NONE';
  const bizM = html.match(/var biz = "([A-Za-z0-9+/=]{10,})"/);
  const biz = bizM ? bizM[1] : 'NONE';
  console.log(f + ':');
  console.log('  title:', title.substring(0, 60));
  console.log('  author:', author);
  console.log('  biz:', biz);
  console.log('  has desc:', desc !== 'NONE' ? 'YES' : 'NO');
  console.log('  html size:', html.length);
});