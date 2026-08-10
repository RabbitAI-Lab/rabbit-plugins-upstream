#!/usr/bin/env node
/**
 * national.js — 全国公共资源交易平台 adapter.
 *
 * The most complex adapter: 6 data sources within one platform.
 * Uses UI interaction (click filters, fill search, click buttons).
 * Page pooling: 3 Pages handle 6 data sources (2 per page).
 *
 * Data sources:
 *   1 — 省平台 (search mode, uses search queries)
 *   2 — 央企招投标 (browse mode)
 *   6 — 商务部 (browse mode)
 *   3 — 财政部 (browse mode)
 *   4 — 自然资源部 (browse mode)
 *   5 — 国资委 (browse mode)
 */

const BasePlatformAdapter = require('./base');

const adapter = new BasePlatformAdapter({
  id: 'national',
  name: '全国公共资源交易平台',
  url: 'https://www.ggzy.gov.cn/deal/dealList.html',
  version: '1.0.0',
});

/**
 * National platform uses different URLs for list (/a/) vs detail (/b/) pages.
 */
adapter.transformDetailUrl = function (url) {
  if (/\/information\/deal\/html\/a\//.test(url)) {
    return url.replace(/\/a\//, '/b/');
  }
  return url;
};

const MAX_PAGES = 15;
const BASE_URL = 'https://www.ggzy.gov.cn/deal/dealList.html';

// Data sources ordered by UI tab position (left to right).
// Each source opens in its own tab via #choose_source_{id}.
const DATA_SOURCES = [
  { id: 1, name: '省平台', mode: 'search' },
  { id: 2, name: '央企招投标', mode: 'browse' },
  { id: 3, name: '财政部', mode: 'browse' },
  { id: 4, name: '自然资源部', mode: 'browse' },
  { id: 5, name: '国资委', mode: 'browse' },
  { id: 6, name: '商务部', mode: 'browse' },
];

/**
 * Extract items from the current page using .publicont div structure.
 */
async function extractItems(page, { today, fromDate }) {
  return await page.$$eval('.publicont', (divs, { t, f }) => {
    return divs.map(div => {
      const a = div.querySelector('h4 a[href*="/information/deal/html/"]');
      if (!a) return null;
      const title = a.textContent.trim().replace(/\s+/g, ' ');
      if (title.length < 10) return null;

      const dateSpan = div.querySelector('.span_o');
      const dateText = dateSpan ? dateSpan.textContent.trim() : '';
      const dm = dateText.match(/(\d{4}-\d{2}-\d{2})/);
      const date = dm ? dm[1] : '';
      if (date < f || date > t) return null;

      const spans = div.querySelectorAll('.span_on');
      const province = spans.length > 0 ? spans[0].textContent.trim() : '';

      const pTw = div.querySelector('.p_tw');
      const infoTypeMatch = pTw ? pTw.textContent.match(/信息类型：\s*(\S+)/) : null;
      const infoType = infoTypeMatch ? infoTypeMatch[1] : '';

      return {
        site: '全国',
        region: province,
        title: title.substring(0, 150),
        date,
        url: a.href,
        infoType,
      };
    }).filter(Boolean);
  }, { t: today, f: fromDate });
}

/**
 * Scan a single data source with optional keyword.
 */
async function scanSource(page, sourceId, sourceName, keyword, context, config) {
  const { today, fromDate, retryStairs } = context;
  const maxPages = config.platforms?.overrides?.national?.max_pages || MAX_PAGES;
  const allItems = [];
  const seenUrls = new Set();

  try {
    // Navigate to dealList if needed
    const currentUrl = page.url();
    if (!currentUrl || !currentUrl.includes('dealList.html')) {
      const ok = await adapter.gotoWithRetry(page, BASE_URL, retryStairs, `全国/${sourceName}`);
      if (!ok) {
        console.error(`  全国/${sourceName}: page load failed`);
        return allItems;
      }
    }
    await page.waitForTimeout(ctx.politeDelay || 3000);

    // Set time range
    try {
      await page.click('#choose_time_02 a', { timeout: 5000 });
    } catch {
      // May already be set
    }
    await page.waitForTimeout(300);

    // Select data source
    try {
      await page.click(`#choose_source_${sourceId} a`);
    } catch (e) {
      console.error(`  全国/${sourceName}: source switch failed: ${e.message.split('\n')[0].slice(0, 80)}`);
      return allItems;
    }
    await page.waitForTimeout(300);

    // Enter keyword or clear search
    if (keyword) {
      await page.fill('#FINDTXT', keyword);
    } else {
      await page.$eval('#FINDTXT', el => { el.value = ''; });
    }

    // Click search
    await page.click('button:has-text("搜索")');
    await page.waitForTimeout(ctx.politeDelay || 3000);

    // Check for no-data state
    try {
      const noData = await page.$('#noDataShow');
      if (noData) {
        const visible = await noData.evaluate(el => el.style.display !== 'none');
        if (visible) {
          console.error(`  全国/${sourceName}${keyword ? '/' + keyword : ''}: no data`);
          return allItems;
        }
      }
    } catch { /* continue */ }

    // Paginate
    for (let p = 1; p <= maxPages; p++) {
      const items = await extractItems(page, { today, fromDate });

      if (items.length === 0 && p === 1) {
        console.error(`  全国/${sourceName}${keyword ? '/' + keyword : ''} page 1: no data`);
        break;
      }
      if (items.length === 0) break;

      for (const item of items) {
        if (item.date >= fromDate && item.date <= today) {
          if (!seenUrls.has(item.url)) {
            seenUrls.add(item.url);
            allItems.push(item);
          }
        }
      }

      const lastDate = items[items.length - 1]?.date || '';
      if (lastDate && lastDate < fromDate) break;

      if (p < maxPages) {
        try {
          const nextBtn = await page.$('.paging a:has-text("下一页")');
          if (nextBtn) {
            await nextBtn.click();
            await page.waitForTimeout(ctx.politeDelay || 2500);
          } else {
            break;
          }
        } catch {
          break;
        }
      }
    }
  } catch (e) {
    console.error(`  全国/${sourceName}${keyword ? '/' + keyword : ''} error: ${e.message.split('\n')[0]}`);
  }

  return allItems;
}

adapter.scan = async function (context, config) {
  const { browser } = context;
  const queries = config.matching?.search_queries || [];

  // Create page pool (3 pages for 6 sources)
  const pages = [];
  for (let i = 0; i < 3; i++) {
    const ctx = await browser.newContext({ userAgent: context.userAgent });
    pages.push(await ctx.newPage());
  }

  const allItems = [];

  try {
    for (let si = 0; si < DATA_SOURCES.length; si++) {
      const src = DATA_SOURCES[si];
      const pageIdx = Math.floor(si / 2);
      const page = pages[pageIdx];

      console.error(`  全国 → ${src.name} [${src.mode}]`);

      if (src.mode === 'search') {
        // Search mode: iterate through all search queries
        for (const kw of queries) {
          const items = await scanSource(page, src.id, src.name, kw, context, config);
          allItems.push(...items);
          console.error(`  全国/${src.name}/${kw}: ${items.length} items`);
        }
      } else {
        // Browse mode: single pass
        const items = await scanSource(page, src.id, src.name, null, context, config);
        allItems.push(...items);
        console.error(`  全国/${src.name}: ${items.length} items`);
      }
    }
  } finally {
    for (const page of pages) {
      try { await page.context().close(); } catch { /* ok */ }
    }
  }

  return { items: allItems };
};

module.exports = adapter;
