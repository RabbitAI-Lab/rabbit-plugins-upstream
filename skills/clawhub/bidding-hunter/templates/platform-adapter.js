#!/usr/bin/env node
/**
 * {{PLATFORM_ID}}.js — Platform adapter template.
 *
 * Replace {{PLATFORM_ID}} and {{PLATFORM_NAME}} with your values.
 * Implement the scan() method — that's the only required method.
 *
 * The adapter will be auto-discovered from:
 *   ~/.bidding-hunter/platforms/
 *
 * Interface:
 *   meta: { id, name, url, version }
 *   scan(context, config) → { items: [...], stats?: {...}, error?: string }
 *
 * Context provided:
 *   context.browser     — Shared Playwright Browser instance
 *   context.reportedUrls — Set of already-processed URLs
 *   context.logger      — { info, warn, error } functions
 *   context.today       — "YYYY-MM-DD" today
 *   context.fromDate    — "YYYY-MM-DD" window start
 *   context.retryStairs — [{ timeout, waitUntil }] for gotoWithRetry
 *   context.userAgent   — User agent string
 */

const BasePlatformAdapter = require('bidding-hunter/src/platforms/base');

const adapter = new BasePlatformAdapter({
  id: '{{PLATFORM_ID}}',
  name: '{{PLATFORM_NAME}}',
  url: 'https://example.gov.cn/',  // ← Replace with actual URL
  version: '1.0.0',
});

// ============================================================
// Item Extraction Function
// ============================================================
// Extract bid announcement items from the current page.
// 
// MUST return Array<{ site, region, title, date, url }>
// - site:  string, platform name (e.g., '四川')
// - region: string, province/city (or empty string)
// - title:  string, announcement title
// - date:   string, "YYYY-MM-DD"
// - url:    string, full URL to detail page
//
// Use page.$$eval() to extract from DOM. Example:
//
// async function extractItems(page, { today, fromDate }) {
//   return await page.$$eval('.result-item', (items, { t, f }) => {
//     return items.map(item => {
//       const link = item.querySelector('a.title');
//       const dateEl = item.querySelector('.date');
//       if (!link || !dateEl) return null;
//       
//       const title = link.textContent.trim();
//       const url = link.href;
//       const dateText = dateEl.textContent.trim();
//       const dateMatch = dateText.match(/(\d{4}-\d{2}-\d{2})/);
//       const date = dateMatch ? dateMatch[1] : '';
//       
//       if (date < f || date > t) return null;
//       
//       return {
//         site: '四川',
//         region: '',
//         title: title.substring(0, 150),
//         date,
//         url,
//       };
//     }).filter(Boolean);
//   }, { t: today, f: fromDate });
// }

async function extractItems(page, { today, fromDate }) {
  // TODO: Implement your extraction logic here
  // See examples in bidding-hunter/src/platforms/
  
  return await page.$$eval('a', (links, { t, f }) => {
    // Simple fallback: extract all links with enough text
    // Replace this with your platform-specific selector
    return links
      .map(a => ({ text: a.textContent.trim().replace(/\s+/g, ' '), href: a.href }))
      .filter(a => a.text.length > 15)
      .map(a => {
        const dm = a.text.match(/(\d{4}-\d{2}-\d{2})/);
        const d = dm ? dm[1] : '';
        return {
          site: '{{PLATFORM_NAME}}',
          region: '',
          title: a.text.substring(0, 150),
          date: d,
          url: a.href,
        };
      })
      .filter(a => a.date >= f && a.date <= t);
  }, { t: today, f: fromDate });
}

// ============================================================
// Scan Method (REQUIRED)
// ============================================================
// This is the main entry point called by the scanner.
// It should:
//   1. Open a browser context + page
//   2. Navigate to the listing page (with retry)
//   3. Extract items (using extractItems or inline logic)
//   4. Handle pagination
//   5. Return { items: [...] }
//
// For search-based platforms, iterate through config.matching.search_queries.
//
// See beijing.js (URL pagination) and hebei.js (search-based) for examples.

adapter.scan = async function (context, config) {
  const { fromDate, today, retryStairs, browser } = context;

  // Create a new page for this scan
  const pageCtx = await browser.newContext({ userAgent: context.userAgent });
  const page = await pageCtx.newPage();

  const items = [];

  try {
    // --- Navigate to listing page ---
    // URL-BASED pagination example:
    // for (let p = 1; p <= maxPages; p++) {
    //   const url = p === 1 ? BASE_URL : `${BASE_URL}?page=${p}`;
    //   const ok = await this.gotoWithRetry(page, url, retryStairs, `Page ${p}`);
    //   if (!ok) break;
    //   await page.waitForTimeout(3000);
    //   const ex = await extractItems(page, { today, fromDate });
    //   if (ex.length === 0 && p === 1) break;
    //   for (const i of ex) items.push(i);
    // }

    // SEARCH-BASED example:
    // const queries = config.matching?.search_queries || ['关键词'];
    // for (const kw of queries) {
    //   await page.fill('#searchInput', kw);
    //   await page.click('button.search-btn');
    //   await page.waitForTimeout(3000);
    //   const ex = await extractItems(page, { today, fromDate });
    //   for (const i of ex) items.push(i);
    // }

    // --- TODO: Replace with your actual scanning logic ---
    console.error('  Template adapter — replace scan() with actual logic');

  } catch (error) {
    return { items, error: error.message };
  } finally {
    await pageCtx.close();
  }

  return { items };
};

// ============================================================
// Optional Methods (uncomment and implement as needed)
// ============================================================

// Custom detail fetching (if platform needs special handling)
// adapter.fetchDetail = async function (context, url) {
//   // Return { bid_submit, bid_open, budget, procurement_method }
//   return {};
// };

// Custom matching (if platform needs special title matching)
// adapter.matchTitle = function (context, title) {
//   // Return { level, keyword } or null
//   return null;
// };

// Custom dedup key (if URL alone is not sufficient)
// adapter.dedupKey = function (item) {
//   return item.url + '|' + item.title;
// };

module.exports = adapter;
