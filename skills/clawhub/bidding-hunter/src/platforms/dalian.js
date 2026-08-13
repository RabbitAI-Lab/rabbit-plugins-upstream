#!/usr/bin/env node
/**
 * dalian.js — 大连市公共资源交易平台 adapter.
 *
 * URL-based pagination through procurement announcement list.
 * Simple <a> tag extraction with URL pattern matching.
 */

const BasePlatformAdapter = require('./base');

const adapter = new BasePlatformAdapter({
  id: 'dalian',
  name: '大连市公共资源交易平台',
  url: 'https://ggzyjy.dl.gov.cn/jyxx/002002/002002001/002002001003/transaction_information.html',
  version: '1.0.0',
});

const MAX_PAGES = 15;

async function extractItems(page, { today, fromDate }) {
  return await page.$$eval('a', (links, { t, f }) => {
    return links
      .map(a => ({ text: a.textContent.trim().replace(/\s+/g, ' '), href: a.href }))
      .filter(a => a.text.length > 15 && a.href.includes('/jyxx/002002/'))
      .map(a => {
        const dm = a.text.match(/(\d{4}-\d{2}-\d{2})/);
        const d = dm ? dm[1] : '';
        let tl = a.text.replace(/\d{4}-\d{2}-\d{2}/, '').trim();
        if (!tl) tl = a.text;
        return {
          site: '大连',
          region: '',
          title: tl.substring(0, 150),
          date: d,
          url: a.href,
        };
      })
      .filter(a => a.date >= f && a.date <= t);
  }, { t: today, f: fromDate });
}

adapter.scan = async function (context, config) {
  const { fromDate, today, retryStairs, browser } = context;
  const maxPages = config.platforms?.overrides?.dalian?.max_pages || MAX_PAGES;

  const page = await browser.newContext({
    userAgent: context.userAgent,
  }).then(ctx => ctx.newPage());

  const items = [];

  try {
    for (let p = 1; p <= maxPages; p++) {
      const url = p === 1
        ? 'https://ggzyjy.dl.gov.cn/jyxx/002002/002002001/002002001003/transaction_information.html'
        : `https://ggzyjy.dl.gov.cn/jyxx/002002/002002001/002002001003/${p}.html`;

      const ok = await this.gotoWithRetry(page, url, retryStairs, `大连 p${p}`);
      if (!ok) {
        console.error(`  大连 p${p} failed after retries`);
        break;
      }

      await page.waitForTimeout(ctx.politeDelay || 5000);
      const ex = await extractItems(page, { today, fromDate });

      if (ex.length === 0 && p === 1) {
        console.error('  大连 page 1: no data');
        break;
      }

      let hasWindow = false;
      for (const i of ex) {
        if (i.date >= fromDate && i.date <= today) {
          hasWindow = true;
          items.push(i);
        }
      }
      if (!hasWindow) break;
    }
  } catch (error) {
    return { items, error: error.message };
  } finally {
    await page.close();
  }

  return { items };
};

module.exports = adapter;
