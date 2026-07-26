// Search Sogou for WeChat account biz
const cheerio = require('cheerio');
const request = require('request-promise');

async function main() {
  const query = encodeURIComponent('大白话讲精益数字化');
  const url = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query=' + query + '&ie=utf8&_sug_=n&_sug_type_=';
  const html = await request.get(url, {
    headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' },
    timeout: 15000
  });
  console.log('sogou response length:', html.length);

  // Extract biz values
  const bizMatches = html.match(/biz[=:]\s*['"]([A-Za-z0-9+/=]{10,})['"]/g);
  console.log('biz matches:', bizMatches ? bizMatches.slice(0, 5) : 'none');

  // Try to find mp.weixin.qq.com links
  const $ = cheerio.load(html);
  const links = $('a[href*="mp.weixin.qq.com"]').map((i, el) => $(el).attr('href')).get();
  console.log('mp links count:', links.length);
  if (links.length > 0) console.log('sample links:', links.slice(0, 3));

  // Try to find account info
  const accountName = $('strong[class*="account"]').text() || $('label[class*="account"]').text();
  console.log('account name from page:', accountName);
}

main().catch(e => console.error('error:', e.message));