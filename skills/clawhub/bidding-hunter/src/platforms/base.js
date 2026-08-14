#!/usr/bin/env node
/**
 * base.js — Base platform adapter for Bidding Hunter.
 *
 * Extend this class to create new platform adapters.
 * Provides common utilities: retry goto, pagination, extraction helpers.
 *
 * Minimal adapter needs:
 *   meta: { id, name, url, version }
 *   scan(context, config) → { items: [...], stats?: {...} }
 *
 * Optional overrides:
 *   fetchDetail(context, url) → { ... }
 *   matchTitle(context, title) → { level, keyword } | null
 *   dedupKey(item) → string (defaults to item.url)
 */

class BasePlatformAdapter {
  constructor(meta) {
    this.meta = meta;
  }

  /**
   * Navigate with retry stairs.
   * @param {Page} page - Playwright page
   * @param {string} url - Target URL
   * @param {Array} [stairs] - Retry configuration [{ timeout, waitUntil }]
   * @param {string} [label] - Log label
   * @returns {Promise<boolean>}
   */
  async gotoWithRetry(page, url, stairs, label = '') {
    const retryStairs = stairs || [
      { timeout: 30000, waitUntil: 'domcontentloaded' },
      { timeout: 45000, waitUntil: 'domcontentloaded' },
      { timeout: 60000, waitUntil: 'networkidle' },
    ];

    for (let i = 0; i < retryStairs.length; i++) {
      try {
        await page.goto(url, {
          waitUntil: retryStairs[i].waitUntil || retryStairs[i].wait_until || 'domcontentloaded',
          timeout: retryStairs[i].timeout || 30000,
        });
        return true;
      } catch (e) {
        const sec = retryStairs[i].timeout / 1000;
        console.error(`  ${label} retry ${i + 1}/${retryStairs.length} (${sec}s): ${e.message.split('\n')[0].slice(0, 80)}`);
        if (i < retryStairs.length - 1) {
          await page.waitForTimeout(5000);
          continue;
        }
        return false;
      }
    }
    return false;
  }

  /**
   * Click-based pagination helper.
   * Repeatedly clicks "next page" selector and calls extractFn.
   */
  async paginateByClick(page, extractFn, { maxPages = 15, today, fromDate, nextSelector, delay = 2500 } = {}) {
    const items = [];
    for (let p = 1; p <= maxPages; p++) {
      const ex = await extractFn(page, { today, fromDate, page: p });
      if (ex.length === 0 && p === 1) {
        console.error('  Page 1 has no data');
        break;
      }
      let hasWindow = false;
      for (const i of ex) {
        if (i.date >= fromDate && i.date <= today) {
          hasWindow = true;
          items.push(i);
        }
      }
      if (!hasWindow) {
        console.error('  Date window exhausted, stopping pagination');
        break;
      }
      if (p < maxPages) {
        try {
          const next = await page.$(nextSelector || '.ant-pagination-next:not(.ant-pagination-disabled), a:has-text("下一页"), li.next:not(.disabled) a');
          if (next) {
            await next.click();
            await page.waitForTimeout(delay);
          } else {
            break;
          }
        } catch (e) {
          console.error(`  Pagination failed at page ${p}: ${e.message.split('\n')[0]}`);
          break;
        }
      }
    }
    return items;
  }

  /**
   * URL-based pagination helper.
   * Calls urlFn(pageNum) for each page.
   */
  async paginateByUrl(context, browser, urlFn, extractFn, { maxPages = 15, today, fromDate, retryStairs } = {}) {
    const page = await browser.newContext().then(ctx => ctx.newPage());
    const items = [];
    for (let p = 1; p <= maxPages; p++) {
      const url = urlFn(p);
      const ok = await this.gotoWithRetry(page, url, retryStairs, `Page ${p}`);
      if (!ok) {
        console.error(`  Page ${p} failed after retries`);
        break;
      }
      await page.waitForTimeout(3000);
      const ex = await extractFn(page, { today, fromDate, page: p });
      if (ex.length === 0 && p === 1) {
        console.error('  Page 1 has no data');
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
    await page.close();
    return items;
  }

  /**
   * Default dedup key: URL.
   */
  dedupKey(item) {
    return item.url;
  }

  /**
   * Default title matching: delegate to the matcher engine.
   * Override for platform-specific logic.
   */
  matchTitle(title) {
    return null; // Falls back to global matcher if null
  }

  /**
   * Transform detail page URLs before fetching.
   * Some platforms use different URLs for list vs detail views.
   * Override in platform-specific adapters.
   */
  transformDetailUrl(url) {
    return url;
  }
}

module.exports = BasePlatformAdapter;
