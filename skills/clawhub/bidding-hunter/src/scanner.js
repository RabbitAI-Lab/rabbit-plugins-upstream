#!/usr/bin/env node
/**
 * scanner.js — Bidding Hunter scanner orchestrator.
 *
 * Coordinates platform adapters, manages browser lifecycle,
 * handles concurrency, deduplication, and checkpointing.
 */

const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const registry = require('./platforms/registry');

const RETRY_STAIRS_DEFAULT = [
  { timeout: 30000, waitUntil: 'domcontentloaded' },
  { timeout: 45000, waitUntil: 'domcontentloaded' },
  { timeout: 60000, waitUntil: 'networkidle' },
];

/**
 * Run the full scan pipeline.
 * @param {object} opts
 * @param {object} opts.config - Full config
 * @param {Set} opts.reportedUrls - Previously reported URLs
 * @param {object} opts.db - Database wrapper
 * @param {object} opts.logger - Logger
 * @param {boolean} opts.force - Force re-scan
 * @param {boolean} opts.dryRun - Dry run mode
 * @returns {Promise<{ items: Array, stats: object }>}
 */
async function run({ config, reportedUrls, db, logger, force = false, dryRun = false }) {
  const today = localDate();
  const yesterday = localDate(-1);
  const dateWindow = config.scan?.date_window || 2;
  const fromDate = localDate(-(dateWindow - 1));

  // Get enabled platform IDs
  const enabledIds = config.platforms?.enabled || [];
  if (!enabledIds.length) {
    logger.warn('No platforms enabled. Add platform IDs to config.platforms.enabled');
    return { items: [], stats: {} };
  }

  // Load adapters
  const adapters = registry.loadAll(config);
  const toScan = enabledIds.filter(id => {
    if (!adapters[id]) {
      logger.warn(`Platform '${id}' not found — skipping`);
      return false;
    }
    return true;
  });

  logger.info(`Platforms to scan: ${toScan.join(', ')}`);
  logger.info(`Date window: ${fromDate} ~ ${today}`);

  // Check checkpoints
  const scanState = loadScanState(config);
  const toScanFiltered = [];
  for (const id of toScan) {
    if (!force && scanState[id] === today) {
      logger.info(`  ${id}: already scanned today, skipping (use --force to override)`);
      continue;
    }
    toScanFiltered.push(id);
  }

  if (!toScanFiltered.length) {
    logger.info('All platforms already scanned today');
    return { items: [], stats: {} };
  }

  // Launch browser
  let browser;
  try {
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

    const retryStairs = config.scan?.retry_stairs || RETRY_STAIRS_DEFAULT;
    const userAgent = config.scan?.user_agent || 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36';

    // Build context for adapters
    const adapterContext = {
      browser,
      reportedUrls,
      logger,
      today,
      fromDate,
      dateWindow,
      retryStairs,
      userAgent,
      politeDelay: config.scan?.polite_delay || 2500,
    };

    // Run all platforms with concurrency limit
    const concurrency = config.scan?.concurrency || 3;
    const allItems = [];
    const stats = {};

    for (let i = 0; i < toScanFiltered.length; i += concurrency) {
      const batch = toScanFiltered.slice(i, i + concurrency);
      logger.info(`Scanning batch: ${batch.join(', ')}`);

      const batchResults = await Promise.allSettled(
        batch.map(async (id) => {
          const adapter = adapters[id];
          logger.info(`  ${id}: starting scan...`);
          const startTime = Date.now();

          try {
            const result = await adapter.scan(adapterContext, config);
            const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);

            if (result.error) {
              logger.error(`  ${id}: failed after ${elapsed}s — ${result.error}`);
              stats[id] = { scanned: 0, new: 0, error: result.error };
            } else {
              const scanned = result.items?.length || 0;
              logger.info(`  ${id}: ${scanned} items in ${elapsed}s`);
              stats[id] = { scanned, new: 0 }; // new count updated after matching
            }

            return { id, result };
          } catch (error) {
            logger.error(`  ${id}: exception — ${error.message.split('\n')[0]}`);
            stats[id] = { scanned: 0, new: 0, error: error.message };
            return { id, result: { items: [], error: error.message } };
          }
        })
      );

      for (const r of batchResults) {
        if (r.status === 'fulfilled' && r.value?.result?.items) {
          const items = r.value.result.items;
          const nullCount = items.filter(i => !i).length;
          const valid = items.filter(Boolean);
          if (nullCount > 0) {
            logger.warn(`${r.value.id}: ${nullCount} null items filtered (possible selector mismatch)`);
          }
          allItems.push(...valid);
        }
      }
    }

    // Deduplicate by URL
    const deduped = deduplicate(allItems, reportedUrls);
    logger.info(`Total: ${allItems.length} raw items, ${deduped.length} after dedup`);

    // Save scan state
    if (!dryRun) {
      for (const id of toScanFiltered) {
        if (!stats[id]?.error) {
          scanState[id] = today;
        }
      }
      saveScanState(config, scanState);

      // Save raw results
      saveScanResults(config, today, { items: deduped, stats });
    }

    // Mark URLs as reported
    if (!dryRun) {
      const urls = deduped.map(item => item.url).filter(Boolean);
      db.markReportedUrls(urls, today);
    }

    return { items: deduped, stats };
  } finally {
    if (browser) await browser.close();
  }
}

/**
 * Deduplicate items by URL, respecting already-reported set.
 */
function deduplicate(items, reportedUrls) {
  const seen = new Set();
  const result = [];
  for (const item of items) {
    if (!item.url) continue;
    if (seen.has(item.url)) continue;
    if (reportedUrls && reportedUrls.has(item.url)) continue;
    seen.add(item.url);
    result.push(item);
  }
  return result;
}

// --- State Management ---

function statePath(config) {
  const resultsDir = config.scan?.results_dir || '~/.bidding-hunter/scan_results';
  return path.join(resolvePath(resultsDir), 'scan_state.json');
}

function loadScanState(config) {
  try {
    return JSON.parse(fs.readFileSync(statePath(config), 'utf8'));
  } catch {
    return {};
  }
}

function saveScanState(config, state) {
  const file = statePath(config);
  fs.mkdirSync(path.dirname(file), { recursive: true });
  const tmp = `${file}.tmp-${process.pid}`;
  fs.writeFileSync(tmp, JSON.stringify(state, null, 2));
  fs.renameSync(tmp, file);
}

function saveScanResults(config, today, data) {
  const resultsDir = resolvePath(config.scan?.results_dir || '~/.bidding-hunter/scan_results');
  const dateDir = path.join(resultsDir, today);
  fs.mkdirSync(dateDir, { recursive: true });

  const manifestPath = path.join(dateDir, '_manifest.json');
  const manifestTmp = `${manifestPath}.tmp`;
  fs.writeFileSync(manifestTmp, JSON.stringify({
    date: today,
    scanned_at: new Date().toISOString(),
    stats: data.stats,
    total_items: data.items.length,
  }, null, 2));
  fs.renameSync(manifestTmp, manifestPath);
}

// --- Helpers ---

function localDate(offsetDays = 0) {
  const d = new Date(Date.now() + offsetDays * 86400000);
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
}

function resolvePath(p) {
  if (p.startsWith('~')) {
    p = path.join(process.env.HOME || `/home/${process.env.USER || 'user'}`, p.slice(1));
  }
  return path.resolve(p);
}

module.exports = { run };
