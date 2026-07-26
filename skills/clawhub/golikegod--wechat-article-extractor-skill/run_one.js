const { extract } = require('./scripts/extract.js');

const url = 'https://mp.weixin.qq.com/s/MbPJmvGU9wWjb9fTtfuEBQ';

extract(url, {
  shouldReturnContent: true,
  shouldReturnRawMeta: false,
  shouldFollowTransferLink: true,
  shouldExtractMpLinks: false,
})
  .then((result) => {
    // 只输出关键字段，避免 base_resp 之类干扰
    const out = {
      done: result.done,
      code: result.code,
      msg: result.msg,
    };
    if (result.data) {
      out.data = {
        account_name: result.data.account_name,
        account_alias: result.data.account_alias,
        msg_title: result.data.msg_title,
        msg_desc: result.data.msg_desc,
        msg_author: result.data.msg_author,
        msg_publish_time_str: result.data.msg_publish_time_str,
        msg_type: result.data.msg_type,
        msg_cover: result.data.msg_cover,
        msg_source_url: result.data.msg_source_url,
        msg_link: result.data.msg_link,
        content_len: result.data.msg_content ? result.data.msg_content.length : 0,
      };
    }
    console.log(JSON.stringify(out, null, 2));

    // 把正文 HTML 落到文件
    if (result.data && result.data.msg_content) {
      const fs = require('fs');
      fs.writeFileSync(
        'C:/Users/ZWB2016/.openclaw/workspace/skills/wechat-article-extractor-skill/_mbpjmvg.html',
        result.data.msg_content,
        'utf8'
      );
      console.log('\n[HTML saved -> _mbpjmvg.html, length=' + result.data.msg_content.length + ']');
    }
  })
  .catch((e) => {
    console.error('EXTRACT FAILED:', e && e.stack ? e.stack : e);
    process.exit(1);
  });