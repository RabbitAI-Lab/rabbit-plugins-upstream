#!/usr/bin/env node
/**
 * detail-fetcher.js — Generic bid detail page fetcher.
 *
 * Opens bid announcement URLs to extract key dates and metadata.
 * Independent from the scanner — can be called separately.
 *
 * Usage (CLI):
 *   node detail-fetcher.js <url>
 *
 * Usage (module):
 *   const { fetchDetail, fetchDetails } = require('./detail-fetcher');
 */

const { chromium } = require('playwright');
const registry = require('./platforms/registry');

// --- Extraction Patterns ---

const BID_SUBMIT_PATTERNS = [
  /投标截止[时间日]/,
  /提交.*?截止[时间日]/,
  /响应文件.*?截止/,
  /递交截止[时间日]/,
  /截止[时间日].*?投标/,
  /投标.*?截止/,
  /响应文件.*?提交.*?截止/,
  /投标文件.*?截止/,
  /获取.*?截止[时间日]/,
];

const BID_OPEN_PATTERNS = [
  /开标[时间日]/,
  /开启[时间日]/,
  /开启.*?时间/,
];

const BUDGET_PATTERNS = [
  /预算[金额]/,
  /采购预算/,
  /最高投标限价/,
  /最高限价/,
  /预算总[金额]/,
  /项目预算/,
  /总预算/,
];

const PROC_METHODS = [
  '公开招标', '竞争性磋商', '竞争性谈判',
  '询价', '单一来源', '邀请招标', '框架协议',
];

const DATE_RE = /(\d{4})\s*[年\-\/\.]\s*(\d{1,2})\s*[月\-\/\.]\s*(\d{1,2})/g;

// --- Helpers ---

function normalizeDate(text) {
  const match = text.match(DATE_RE);
  if (match) {
    return `${match[1]}-${String(parseInt(match[2])).padStart(2, '0')}-${String(parseInt(match[3])).padStart(2, '0')}`;
  }
  return null;
}

function extractDateNearKeyword(text, patterns, windowChars = 200) {
  for (const pattern of patterns) {
    const match = pattern.exec(text);
    if (match) {
      const idx = match.index;
      const start = Math.max(0, idx - windowChars);
      const end = Math.min(text.length, idx + match[0].length + windowChars);
      const snippet = text.substring(start, end);

      const dates = [];
      let dm;
      try {
        while ((dm = DATE_RE.exec(snippet)) !== null) {
          dates.push({
            date: `${dm[1]}-${String(parseInt(dm[2])).padStart(2, '0')}-${String(parseInt(dm[3])).padStart(2, '0')}`,
            pos: dm.index,
          });
        }
      } finally {
        DATE_RE.lastIndex = 0;
      }

      if (dates.length > 0) {
        const kwEndInSnippet = idx - start + match[0].length;
        const after = dates.filter(d => d.pos >= kwEndInSnippet - 10);
        if (after.length > 0) return after[0].date;

        let closest = dates[0];
        for (const d of dates) {
          if (Math.abs(d.pos - kwEndInSnippet) < Math.abs(closest.pos - kwEndInSnippet)) {
            closest = d;
          }
        }
        return closest.date;
      }
    }
  }
  return null;
}

function extractBudget(text) {
  for (const pattern of BUDGET_PATTERNS) {
    const re = new RegExp(pattern.source + '[：:]*[\\s]*(\\d+(?:\\.\\d+)?)\\s*(万元|元|万)', 'i');
    const m = text.match(re);
    if (m) return { amount: parseFloat(m[1]), unit: m[2] };
  }
  const fallbackRe = /(?:总预算|项目预算|采购预算|预算)[^：:\d]{0,10}[：:]?\s*(\d+(?:\.\d+)?)\s*(万元|元|万)/;
  const m2 = text.match(fallbackRe);
  if (m2) return { amount: parseFloat(m2[1]), unit: m2[2] };
  return null;
}

function extractProcurementMethod(text) {
  for (const method of PROC_METHODS) {
    if (text.includes(method)) return method;
  }
  return null;
}

async function gotoWithRetry(page, url, retryConfig) {
  const stairs = retryConfig || [
    { timeout: 30000, waitUntil: 'domcontentloaded' },
    { timeout: 45000, waitUntil: 'domcontentloaded' },
    { timeout: 60000, waitUntil: 'networkidle' },
  ];

  for (let i = 0; i < stairs.length; i++) {
    try {
      await page.goto(url, {
        waitUntil: stairs[i].waitUntil || stairs[i].wait_until || 'domcontentloaded',
        timeout: stairs[i].timeout || 30000,
      });
      return true;
    } catch (e) {
      const sec = stairs[i].timeout / 1000;
      console.error(`  Retry ${i + 1}/${stairs.length} (${sec}s): ${e.message.split('\n')[0].slice(0, 80)}`);
      if (i < stairs.length - 1) {
        await page.waitForTimeout(5000);
        continue;
      }
      return false;
    }
  }
  return false;
}

/**
 * Fetch detail information from a single bid announcement URL.
 * @param {string} url - The bid announcement URL
 * @param {object} [options]
 * @param {Array} [options.retryStairs] - Custom retry configuration
 * @param {object} [options.browser] - Reuse an existing browser instance
 * @returns {Promise<object>} { url, bid_submit, bid_open, budget, procurement_method, raw_text_preview, error }
 */
async function fetchDetail(url, options = {}) {
  // URL validation
  try {
    const parsed = new URL(url);
    if (!['http:', 'https:'].includes(parsed.protocol)) {
      return { url, error: 'Invalid protocol: only http/https allowed', bid_submit: null, bid_open: null, budget: null, procurement_method: null };
    }
  } catch {
    return { url, error: 'Invalid URL format', bid_submit: null, bid_open: null, budget: null, procurement_method: null };
  }

  // Apply platform-specific URL transformation (via adapter hook)
  const transformUrl = options.transformUrl || (url => registry.findTransformDetailUrl({}, url));
  const fetchUrl = transformUrl(url);

  const result = {
    url,
    bid_submit: null,
    bid_open: null,
    budget: null,
    procurement_method: null,
    raw_text_preview: '',
    error: null,
  };

  let browser = options.browser;
  let ownBrowser = false;

  try {
    if (!browser) {
      try {
        browser = await chromium.launch({
          headless: true,
          executablePath: '/snap/bin/chromium',
          args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage'],
        });
      } catch {
        browser = await chromium.launch({
          headless: true,
          args: ['--no-sandbox', '--disable-setuid-sandbox'],
        });
      }
      ownBrowser = true;
    }

    const context = await browser.newContext({
      userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    });
    const page = await context.newPage();

    const ok = await gotoWithRetry(page, fetchUrl, options.retryStairs);
    if (!ok) {
      result.error = 'Page load failed after retries';
      await context.close();
      return result;
    }

    await page.waitForTimeout(1000);

    // Extract body text
    let bodyText = await page.evaluate(() => {
      const body = document.body;
      const removes = body.querySelectorAll('script, style, noscript, nav, footer, .header, .footer, .nav');
      removes.forEach(el => el.remove());
      return body.textContent.replace(/\s+/g, ' ').replace(/ {2,}/g, ' ').trim();
    });

    // Iframe fallback
    if (!bodyText || bodyText.length < 50) {
      await page.waitForTimeout(3000);
      const iframeResult = await page.evaluate(() => {
        const iframes = document.querySelectorAll('iframe');
        const texts = [];
        for (const iframe of iframes) {
          try {
            const doc = iframe.contentDocument || iframe.contentWindow?.document;
            if (doc && doc.body) texts.push(doc.body.textContent);
          } catch { /* cross-origin */ }
        }
        return {
          iframeTexts: texts,
          bodyRetry: document.body.textContent.replace(/\s+/g, ' ').replace(/ {2,}/g, ' ').trim(),
        };
      });

      if (iframeResult.iframeTexts.length > 0) {
        bodyText = iframeResult.iframeTexts.join(' ');
      } else if (iframeResult.bodyRetry && iframeResult.bodyRetry.length >= 50) {
        bodyText = iframeResult.bodyRetry;
      }
    }

    if (!bodyText || bodyText.length < 50) {
      result.error = 'Page text too short (possibly JS-rendered or empty)';
      await context.close();
      return result;
    }

    result.raw_text_preview = bodyText.substring(0, 500);

    // Extract data
    result.bid_submit = extractDateNearKeyword(bodyText, BID_SUBMIT_PATTERNS);
    result.bid_open = extractDateNearKeyword(bodyText, BID_OPEN_PATTERNS);

    if (!result.bid_open) {
      const openMatch = bodyText.match(/开标[^，。；\n]{0,30}?(\d{4}\s*[年\-\/\.]\s*\d{1,2}\s*[月\-\/\.]\s*\d{1,2})/);
      if (openMatch) result.bid_open = normalizeDate(openMatch[0]);
    }

    const budget = extractBudget(bodyText);
    result.budget = budget ? { amount: budget.amount, unit: budget.unit } : null;
    result.procurement_method = extractProcurementMethod(bodyText);

    await context.close();
    return result;
  } catch (e) {
    result.error = e.message.split('\n')[0];
    return result;
  } finally {
    if (ownBrowser && browser) {
      await browser.close();
    }
  }
}

/**
 * Fetch details for all entries in the database that need them.
 * @param {object} db - Database wrapper
 * @param {object} config - Full config
 * @param {string} today - Current date
 * @param {object} logger - Logger instance
 * @returns {Promise<Array>} Results per entry
 */
async function fetchDetails(db, config, today, logger) {
  const maxAge = config.detail_fetch?.max_age_days || 30;
  const concurrency = config.detail_fetch?.concurrency || 2;
  const retryStairs = config.scan?.retry_stairs;

  const entries = db.getEntriesNeedingDetails(today, maxAge);
  if (!entries.length) {
    logger.info('No entries need detail fetching');
    return [];
  }

  logger.info(`Fetching details for ${entries.length} entries (concurrency=${concurrency})`);

  // Launch shared browser
  let browser;
  try {
    browser = await chromium.launch({
      headless: true,
      executablePath: '/snap/bin/chromium',
      args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage'],
    });
  } catch {
    browser = await chromium.launch({
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox'],
    });
  }

  try {
    // Build URL transform closure once (avoid O(n×m) adapter loading)
    const allAdapters = registry.loadAll(config);
    const transformUrl = (url) => {
      for (const a of Object.values(allAdapters)) {
        if (typeof a.transformDetailUrl === 'function') {
          const t = a.transformDetailUrl(url);
          if (t !== url) return t;
        }
      }
      return url;
    };

    const results = [];
    // Process in batches
    for (let i = 0; i < entries.length; i += concurrency) {
      const batch = entries.slice(i, i + concurrency);
      const batchResults = await Promise.allSettled(
        batch.map(entry => fetchDetail(entry.url, {
          browser,
          retryStairs,
          transformUrl,
        }))
      );

      for (let j = 0; j < batch.length; j++) {
        const entry = batch[j];
        const detail = batchResults[j].status === 'fulfilled' ? batchResults[j].value : { error: batchResults[j].reason?.message };
        results.push({ alias: entry.alias, url: entry.url, detail });

        // Save to database
        if (!detail.error) {
          if (detail.bid_submit) {
            db.setDeadline(entry.alias, 'bid_submit', detail.bid_submit);
          }
          if (detail.bid_open) {
            db.setDeadline(entry.alias, 'bid_open', detail.bid_open);
          }
          if (detail.budget) {
            // Update budget in entry
            db.updateEntry(entry.alias, {
              notes: `Budget: ${detail.budget.amount}${detail.budget.unit}, Method: ${detail.procurement_method || 'unknown'}`,
            }, today);
          }
        }
      }
    }

    logger.info(`Detail fetch complete: ${results.filter(r => !r.detail.error).length} ok / ${results.filter(r => r.detail.error).length} failed`);
    return results;
  } finally {
    await browser.close();
  }
}

// --- CLI ---
if (require.main === module) {
  const url = process.argv[2];
  if (!url) {
    console.error('Usage: node detail-fetcher.js <url>');
    process.exit(1);
  }

  fetchDetail(url).then(result => {
    console.log(JSON.stringify(result));
    process.exit(result.error ? 1 : 0);
  }).catch(err => {
    console.error(err);
    process.exit(1);
  });
}

module.exports = { fetchDetail, fetchDetails };
