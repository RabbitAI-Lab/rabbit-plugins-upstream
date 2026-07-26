const cheerio = require('cheerio');
const fs = require('fs');
const path = require('path');
const request = require('request-promise');

(async () => {
  try {
    const url = 'https://mp.weixin.qq.com/s/VSCJD-1ACSP7NWoV_CI2_Q';
    const html = await request({
      uri: url,
      method: 'GET',
      headers: {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Host': 'mp.weixin.qq.com'
      },
      timeout: 30000
    });

    fs.writeFileSync(path.join(__dirname, 'raw.html'), html, 'utf8');
    console.log('HTML size:', html.length);

    const $ = cheerio.load(html, { decodeEntities: false });

    const title = $('#activity-name').text().trim() || $('meta[property="og:title"]').attr('content') || '';
    const author = $('#js_author_name').text().trim() || $('.rich_media_meta_link_account_nickname').text().trim() || '';
    const accountNickname = $('#js_profile_qrcode > div > p:nth-child(3)').text().trim() ||
                          $('.profile_meta_value').text().trim() ||
                          $('meta[property="og:article:author"]').attr('content') || '';
    const publishTime = $('script').text().match(/var\spublish_time\s*=\s*"?(\d{4}-\d{2}-\d{2}\s*\d{2}:\d{2})"?/);
    const desc = $('meta[name="description"]').attr('content') || '';
    const cover = $('meta[property="og:image"]').attr('content') || '';

    // 提取 js_content 内的文本
    const content = $('#js_content');
    let text = '';
    if (content.length) {
      text = content.text().replace(/\s+/g, '\n').trim();
    }

    const result = {
      title,
      author,
      accountNickname,
      publishTime: publishTime ? publishTime[1] : '',
      desc,
      cover,
      textLength: text.length,
      textPreview: text.substring(0, 2000)
    };

    console.log(JSON.stringify(result, null, 2));
  } catch (e) {
    console.error('ERROR:', e.message);
    console.error(e.stack);
    process.exit(1);
  }
})();
