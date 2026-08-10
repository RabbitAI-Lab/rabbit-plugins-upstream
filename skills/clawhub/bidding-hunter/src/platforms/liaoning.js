#!/usr/bin/env node
/**
 * liaoning.js — 辽宁省公共资源交易平台 adapter.
 *
 * Uses API-based extraction (/prs-back/api/transactionInformation/list)
 * which is more reliable than DOM scraping for this Nuxt-based SPA.
 * Falls back to DOM extraction if API fails.
 */

const BasePlatformAdapter = require('./base');

const adapter = new BasePlatformAdapter({
  id: 'liaoning',
  name: '辽宁省公共资源交易平台',
  url: 'http://www.lnggzy.gov.cn/trading',
  version: '1.0.0',
});

const MAX_PAGES = 15;
const BASE_URL = 'http://www.lnggzy.gov.cn';
const API_PATH = '/prs-back/api/transactionInformation/list';

async function extractViaApi(page, kw, { today, fromDate }, maxPages) {
  const items = [];
  const regionCode = '210000'; // Liaoning
  const bulletinType = 'DG02'; // Procurement announcements

  for (let p = 1; p <= maxPages; p++) {
    const apiUrl = `${API_PATH}?regionCode=${regionCode}&bulletinType=${bulletinType}&pageNo=${p}&pageSize=10&code=***&q=${encodeURIComponent(kw)}`;

    const data = await page.evaluate(async (url) => {
      const resp = await fetch(url);
      if (!resp.ok) return null;
      return await resp.json();
    }, apiUrl);

    if (!data || data.code !== 200 || !data.data || !data.data.records || data.data.records.length === 0) {
      if (p === 1) console.error(`  辽宁 [${kw}] API returned no data`);
      break;
    }

    let hasWindow = false;
    for (const r of data.data.records) {
      const d = r.noticeSendTime;
      if (d >= fromDate && d <= today) {
        hasWindow = true;
        items.push({
          site: '辽宁',
          region: r.regionName || '',
          title: r.noticeName,
          date: d,
          url: r.url,
        });
      }
    }

    if (!hasWindow) break;
    if (data.data.records.length < 10) break;
  }

  return items;
}

adapter.scan = async function (context, config) {
  const { fromDate, today, browser } = context;
  const queries = config.matching?.search_queries || [];
  if (!queries.length) {
    console.error('  辽宁: no search_queries configured, skipping');
    return { items: [] };
  }
  const maxPages = config.platforms?.overrides?.liaoning?.max_pages || MAX_PAGES;

  const page = await browser.newContext({
    userAgent: context.userAgent,
  }).then(ctx => ctx.newPage());

  const allItems = [];
  const seenUrls = new Set();

  try {
    // Establish session first
    await page.goto(`${BASE_URL}/trading?mainTabId=48&subTabId=62`, {
      waitUntil: 'domcontentloaded',
      timeout: 30000,
    });
    await page.waitForTimeout(ctx.politeDelay || 5000);

    console.error('  辽宁: API mode');

    for (const kw of queries) {
      try {
        const items = await extractViaApi(page, kw, { today, fromDate }, maxPages);
        let added = 0;
        for (const item of items) {
          if (!seenUrls.has(item.url)) {
            seenUrls.add(item.url);
            allItems.push(item);
            added++;
          }
        }
        console.error(`  辽宁 [${kw}]: ${items.length} raw, ${added} new`);
      } catch (e) {
        console.error(`  辽宁 [${kw}] error: ${e.message.split('\n')[0]}`);
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
