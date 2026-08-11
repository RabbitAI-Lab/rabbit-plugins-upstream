#!/usr/bin/env node
/**
 * index.js — Bidding Hunter main exports
 *
 * Usage:
 *   const hunter = require('bidding-hunter');
 *   await hunter.scan(config);
 *   await hunter.report(config, '2026-07-22');
 *
 * Or use the CLI:
 *   bidding-hunter scan --config ~/.bidding-hunter/config.yaml
 */

const scanner = require('./scanner');
const matcher = require('./matcher');
const database = require('./database');
const reporter = require('./reporter');
const detailFetcher = require('./detail-fetcher');
const reminder = require('./reminder');
const notifier = require('./notifier');
const lock = require('./lock');
const { loadConfig, resolvePath } = require('./config');

/**
 * Run the full scan pipeline.
 * @param {object} config - Merged config object
 * @param {object} [options]
 * @param {boolean} [options.dryRun] - Don't write to database
 * @param {boolean} [options.force] - Force re-scan even if already done today
 * @returns {Promise<object>} { report, stats, added }
 */
async function scan(config, options = {}) {
  const { dryRun = false, force = false } = options;
  const today = localDate();
  const logger = createLogger(config);

  // 1. Acquire lock
  if (!dryRun) {
    lock.acquire(config);
  }

  try {
    // 2. Initialize database
    const db = database.init(config);

    // 3. Load reported URLs for dedup
    const reportedUrls = db.getReportedUrls();

    // 4. Run scan
    logger.info(`Starting scan for ${today}`);
    const scanResults = await scanner.run({
      config,
      reportedUrls,
      db,
      logger,
      force,
      dryRun,
    });

    // 5. Match keywords
    logger.info('Matching keywords...');
    const matched = matcher.matchAll(scanResults.items, config.matching);

    // 6. Ingest into database
    if (!dryRun) {
      logger.info('Ingesting into database...');
      const added = db.ingest(matched, today, scanResults);
      logger.info(`Ingested ${added.length} new entries`);

      // 7. Fetch details for tracked entries
      if (config.detail_fetch?.enabled) {
        logger.info('Fetching details...');
        await detailFetcher.fetchDetails(db, config, today, logger);
      }

      // 8. Build reminders
      const reminders = reminder.build(db, config, today);

      // 9. Generate report
      const report = reporter.generate({
        config,
        scan: scanResults,
        added,
        reminders,
        db,
        today,
      });

      // 10. Dispatch notifications
      await notifier.dispatch(report, config);

      // 11. Save scan state
      db.saveScanLog(today, scanResults.stats);

      logger.info('Scan complete');

      return {
        report: report.text,
        reportJson: report.json,
        stats: scanResults.stats,
        added: added.length,
        reminders,
      };
    } else {
      // Dry run: just return the report
      const report = reporter.generate({
        config,
        scan: scanResults,
        added: matched,
        reminders: [],
        db: { getStats: () => ({ total: 0, byStatus: {} }) },
        today,
      });
      return {
        report: report.text,
        reportJson: report.json,
        stats: scanResults.stats,
        added: matched.length,
        reminders: [],
      };
    }
  } finally {
    if (!dryRun) {
      lock.release(config);
    }
  }
}

/**
 * Generate a report for a specific date.
 */
function report(config, date) {
  const db = database.init(config);
  const today = date || localDate();
  const entries = db.getEntriesByDate(today);
  const stats = db.getStats();
  const reminders = reminder.build(db, config, today);

  return reporter.generate({
    config,
    scan: { stats: {}, items: entries },
    added: entries,
    reminders,
    db,
    today,
  });
}

/**
 * List tracked entries.
 */
function list(config, filters = {}) {
  const db = database.init(config);
  return db.listEntries(filters);
}

/**
 * Update entry status.
 */
function updateStatus(config, alias, updates) {
  const db = database.init(config);
  return db.updateEntry(alias, updates);
}

/**
 * Show statistics.
 */
function stats(config) {
  const db = database.init(config);
  return db.getStats();
}

/**
 * Export database.
 */
function exportDb(config, format = 'json') {
  const db = database.init(config);
  return db.export(format);
}

// --- Helpers ---

function localDate(offsetDays = 0) {
  const d = new Date(Date.now() + offsetDays * 86400000);
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
}

function createLogger(config) {
  const level = config.logging?.level || 'info';
  const file = config.logging?.file;
  return {
    debug: (msg) => log('debug', msg, level, file),
    info: (msg) => log('info', msg, level, file),
    warn: (msg) => log('warn', msg, level, file),
    error: (msg) => log('error', msg, level, file),
  };
}

function log(level, msg, configLevel, file) {
  const levels = { debug: 0, info: 1, warn: 2, error: 3 };
  if (levels[level] < levels[configLevel]) return;
  const line = `[${new Date().toISOString()}] [${level.toUpperCase()}] ${msg}`;
  if (file) {
    const fs = require('fs');
    fs.appendFileSync(resolvePath(file), line + '\n');
  }
  // stderr by default so stdout is for structured output
  if (level === 'error') console.error(line);
  else process.stderr.write(line + '\n');
}

module.exports = {
  scan,
  report,
  list,
  updateStatus,
  stats,
  exportDb,
  loadConfig,
  resolvePath,
  localDate,
};
