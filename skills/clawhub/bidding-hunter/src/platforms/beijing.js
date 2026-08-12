#!/usr/bin/env node
/**
 * beijing.js — 北京公共资源交易平台 adapter.
 *
 * URL-based pagination through procurement announcement index pages.
 * Extraction: <a> tags with /jyxxcggg/ in href.
 */

const BasePlatformAdapter = require('./base');

const adapter = new BasePlatformAdapter({
  id: 'beijing',
  name: '北京公共资源交易平台',
  url: 'https://ggzyfw.beijing.gov.cn/jyxxcggg/index.html',
  version: '1.0.0',
});

const MAX_PAGES = 15;

/**
 * Extract items from a list page.
 */
async function extractItems(page, { today, fromDate }) {
  return await page.$$eval('a', (links, opts) => {
    const { t, f } = opts;
    return links
      .map(a => ({ text: a.textContent.trim().replace(/\s+/g, ' '), href: a.href }))
      .filter(a => a.text.length > 20 && a.href.includes('/jyxxcggg/'))
      .map(a => {
        const dm = a.href.match(/\/(\d{8})\//);
        const d = dm ? `${dm[1].slice(0, 4)}-${dm[1].slice(4, 6)}-${dm[1].slice(6, 8)}` : '';
        const rm = a.text.match(/【(.+?)】/);
        return {
          site: '北京',
          region: rm ? rm[1] : '',
          title: a.text.replace(/【.+?】\[.+?\]\s*/, '').trim(),
          date: d,
          url: a.href,
        };
      })
      .filter(a => a.date >= f && a.date <= t);
  }, { t: today, f: fromDate });
}

adapter.scan = async function (context, config) {
  const { fromDate, today, retryStairs, browser } = context;
  const maxPages = config.platforms?.overrides?.beijing?.max_pages || MAX_PAGES;

  const page = await browser.newContext({
    userAgent: context.userAgent,
  }).then(ctx => ctx.newPage());

  const items = [];

  try {
    for (let p = 1; p <= maxPages; p++) {
      const url = p === 1
        ? 'https://ggzyfw.beijing.gov.cn/jyxxcggg/index.html'
        : `https://ggzyfw.beijing.gov.cn/jyxxcggg/index_${p}.html`;

      const ok = await this.gotoWithRetry(page, url, retryStairs, `北京 p${p}`);
      if (!ok) {
        console.error(`  北京 p${p} failed after retries`);
        break;
      }

      await page.waitForTimeout(ctx.politeDelay || 5000);
      const ex = await extractItems(page, { today, fromDate });

      if (ex.length === 0 && p === 1) {
        console.error('  北京 page 1: no data');
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
