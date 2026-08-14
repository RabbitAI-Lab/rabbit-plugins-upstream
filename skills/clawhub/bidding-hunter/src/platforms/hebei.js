#!/usr/bin/env node
/**
 * hebei.js — 河北省招标投标公共服务平台 adapter.
 *
 * Uses fullsearch.html URL-based search with each query keyword.
 * Filters results by clicking "河北省服务平台" to get only procurement listings.
 * Extraction: li.search-row with data-infourl attribute.
 */

const BasePlatformAdapter = require('./base');

const adapter = new BasePlatformAdapter({
  id: 'hebei',
  name: '河北省招标投标公共服务平台',
  url: 'https://szj.hebei.gov.cn/hbggfwpt/search/fullsearch.html',
  version: '1.0.0',
});

const MAX_PAGES = 15;
const SEARCH_BASE = 'https://szj.hebei.gov.cn/hbggfwpt/search/fullsearch.html';

/**
 * Extract items from a search results page.
 */
async function extractItems(page, { today, fromDate }) {
  return await page.$$eval('li.search-row', (rows, { t, f }) => {
    return rows.map(row => {
      const a = row.querySelector('a.mya');
      const dateSpan = row.querySelector('.content-date');
      if (!a || !dateSpan) return null;
      const infoUrl = a.getAttribute('data-infourl');
      if (!infoUrl) return null;
      const title = a.textContent.trim().replace(/\s+/g, ' ');
      const date = dateSpan.textContent.trim().substring(0, 10);
      if (date < f || date > t) return null;
      return {
        site: '河北',
        region: '',
        title: title.length > 150 ? title.substring(0, 150) : title,
        date,
        url: 'https://szj.hebei.gov.cn' + infoUrl,
      };
    }).filter(Boolean);
  }, { t: today, f: fromDate });
}

adapter.scan = async function (context, config) {
  const { fromDate, today, retryStairs, browser } = context;
  const queries = config.matching?.search_queries || [];
  if (!queries.length) {
    console.error('  河北: no search_queries configured, skipping');
    return { items: [] };
  }
  const maxPages = config.platforms?.overrides?.hebei?.max_pages || MAX_PAGES;

  const page = await browser.newContext({
    userAgent: context.userAgent,
  }).then(ctx => ctx.newPage());

  const allItems = [];
  const seenUrls = new Set();

  try {
    for (const kw of queries) {
      try {
        const url = SEARCH_BASE + '?wd=' + encodeURIComponent(kw);
        await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
        await page.waitForTimeout(ctx.politeDelay || 3000);

        // Click "河北省服务平台" filter for procurement-only results
        try {
          await page.evaluate(() => {
            const items = document.querySelectorAll('.category-list li');
            for (const li of items) {
              if (li.textContent.trim() === '河北省服务平台') {
                li.click();
                return;
              }
            }
          });
          await page.waitForTimeout(ctx.politeDelay || 3000);
        } catch (e) {
          console.error(`  河北 [${kw}] filter click failed: ${e.message.split('\n')[0]}`);
        }

        let kwHits = 0;
        for (let p = 1; p <= maxPages; p++) {
          const items = await extractItems(page, { today, fromDate });
          if (items.length === 0 && p === 1) {
            console.error(`  河北 [${kw}] page 1: no data`);
            break;
          }

          let hasWindow = false;
          for (const i of items) {
            if (i.date >= fromDate && i.date <= today) {
              hasWindow = true;
              if (!seenUrls.has(i.url)) {
                seenUrls.add(i.url);
                allItems.push(i);
              }
            }
          }

          kwHits += items.length;
          if (!hasWindow) break;
          if (items.length < 10) break;

          try {
            const next = await page.$('.m-pagination-page a:has-text("下一页")');
            if (next) {
              await next.click();
              await page.waitForTimeout(ctx.politeDelay || 2500);
            } else {
              break;
            }
          } catch {
            break;
          }
        }
        console.error(`  河北 [${kw}]: ${kwHits} raw`);
      } catch (e) {
        console.error(`  河北 [${kw}] error: ${e.message.split('\n')[0]}`);
      }
    }
  } catch (error) {
    return { items: allItems, error: error.message };
  } finally {
    await page.close();
  }

  return { items: allItems };
};

module.exports = adapter;
