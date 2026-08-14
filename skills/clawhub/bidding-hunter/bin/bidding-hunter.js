#!/usr/bin/env node
/**
 * bidding-hunter — CLI entry point.
 *
 * Commands:
 *   scan        Run full scan pipeline
 *   report      Show report for a date
 *   list        List entries with filters
 *   status      Update entry status
 *   remind      Show reminders
 *   stats       Show database statistics
 *   export      Export database
 *   init        Create initial config
 *   explore     Agent-guided platform exploration
 *   create-adapter  Create platform adapter from template
 *   test-platform   Test a platform adapter
 *   version     Show version
 */

const { program } = require('commander');
const path = require('path');
const fs = require('fs');

const PACKAGE = require('../package.json');
const { loadConfig, validateConfig } = require('../src/config');
const index = require('../src/index');
const registry = require('../src/platforms/registry');

program
  .name('bidding-hunter')
  .description('Automated government procurement bid discovery engine')
  .version(PACKAGE.version)
  .option('-c, --config <path>', 'Path to config file', '~/.bidding-hunter/config.yaml');

// === scan ===
program.command('scan')
  .description('Run the full scan pipeline')
  .option('-d, --dry-run', 'Preview without writing to database')
  .option('-f, --force', 'Force re-scan even if already done today')
  .option('--skip-details', 'Skip detail page fetching')
  .action(async (opts) => {
    const config = loadConfig(program.opts().config);
    const validation = validateConfig(config);
    if (!validation.valid) {
      console.error('Config validation errors:');
      for (const err of validation.errors) console.error(`  - ${err}`);
      process.exit(1);
    }

    if (opts.skipDetails && config.detail_fetch) {
      config.detail_fetch.enabled = false;
    }

    try {
      const result = await index.scan(config, {
        dryRun: opts.dryRun,
        force: opts.force,
      });
      if (result.report) {
        console.log(result.report);
      }
    } catch (error) {
      console.error(`Scan failed: ${error.message}`);
      process.exit(1);
    }
  });

// === report ===
program.command('report')
  .description('Show report for a date')
  .option('-d, --date <date>', 'Date (YYYY-MM-DD), defaults to today')
  .option('-f, --format <format>', 'Output format: text|json|markdown', 'text')
  .action(async (opts) => {
    const config = loadConfig(program.opts().config);
    const date = opts.date || index.localDate();
    const report = index.report(config, date);

    if (opts.format === 'json') {
      console.log(JSON.stringify(report.json, null, 2));
    } else if (opts.format === 'markdown') {
      console.log(report.markdown);
    } else {
      console.log(report.text);
    }
  });

// === list ===
program.command('list')
  .description('List entries')
  .option('-s, --status <status>', 'Filter by status (tracked/undecided/discarded)')
  .option('--site <site>', 'Filter by site')
  .option('--level <level>', 'Filter by match level (L1/L2/L3)')
  .option('--json', 'Output as JSON')
  .action(async (opts) => {
    const config = loadConfig(program.opts().config);
    const entries = index.list(config, {
      status: opts.status,
      site: opts.site,
      level: opts.level,
    });

    if (opts.json) {
      console.log(JSON.stringify(entries, null, 2));
    } else {
      if (!entries.length) {
        console.log('No entries found.');
        return;
      }
      for (const e of entries) {
        const status = e.status || 'undecided';
        const level = e.match_level ? `[${e.match_level}]` : '';
        console.log(`#${e.alias} ${level} ${e.title.substring(0, 60)}`);
        console.log(`   ${e.site} · ${e.pub_date} · ${status} · ${e.bid_status || '-'}`);
        if (e.url) console.log(`   🔗 ${e.url}`);
        console.log('');
      }
    }
  });

// === status ===
program.command('status')
  .description('Update entry status')
  .requiredOption('--id <alias>', 'Entry alias number')
  .requiredOption('-s, --status <value>', 'New status: tracked|undecided|discarded')
  .option('--bid-status <value>', 'Bid progress: watching|docs_purchased|docs_prepared|submitted|opened')
  .option('--note <text>', 'Note to add to history')
  .action(async (opts) => {
    const config = loadConfig(program.opts().config);
    const validStatuses = ['tracked', 'undecided', 'discarded'];
    if (!validStatuses.includes(opts.status)) {
      console.error(`Invalid status. Must be one of: ${validStatuses.join(', ')}`);
      process.exit(1);
    }

    const alias = parseInt(opts.id);
    if (isNaN(alias)) {
      console.error('--id must be a number');
      process.exit(1);
    }

    try {
      const updates = { status: opts.status };
      if (opts.bidStatus) updates.bid_status = opts.bidStatus;
      if (opts.note) updates.notes = opts.note;

      const entry = index.updateStatus(config, alias, updates);
      console.log(`✅ #${entry.alias} → ${entry.status}${entry.bid_status ? ` (${entry.bid_status})` : ''}`);
    } catch (error) {
      console.error(`Error: ${error.message}`);
      process.exit(1);
    }
  });

// === remind ===
program.command('remind')
  .description('Show pending reminders')
  .action(async (opts) => {
    const config = loadConfig(program.opts().config);
    const today = index.localDate();
    const report = index.report(config, today);

    if (report.json.reminders.urgent.length === 0 &&
        report.json.reminders.openResults.length === 0 &&
        report.json.reminders.missingDates.length === 0) {
      console.log('✅ No pending reminders.');
      return;
    }

    for (const r of report.json.reminders.urgent) {
      const label = r.days === 0 ? 'TODAY' : r.days === -1 ? 'YESTERDAY' : `${r.days}d`;
      console.log(`🔴 #${r.alias} ${r.title} — ${label} — ${r.status || ''}`);
    }
    for (const r of report.json.reminders.openResults) {
      console.log(`🔵 #${r.alias} ${r.title} — awaiting results`);
    }
    for (const e of report.json.reminders.missingDates) {
      console.log(`🟡 #${e.alias} ${e.title} — no deadline set`);
    }
  });

// === stats ===
program.command('stats')
  .description('Show database statistics')
  .action(async (opts) => {
    const config = loadConfig(program.opts().config);
    const stats = index.stats(config);

    console.log(`📊 Database Statistics`);
    console.log(`   Total entries: ${stats.total}`);
    console.log(`   By status:`);
    for (const [status, count] of Object.entries(stats.byStatus || {})) {
      console.log(`     ${status}: ${count}`);
    }
    if (stats.bySite) {
      console.log(`   By site:`);
      for (const [site, count] of Object.entries(stats.bySite)) {
        console.log(`     ${site}: ${count}`);
      }
    }
    if (stats.byLevel) {
      console.log(`   By level:`);
      for (const [level, count] of Object.entries(stats.byLevel)) {
        console.log(`     ${level}: ${count}`);
      }
    }
  });

// === export ===
program.command('export')
  .description('Export database')
  .option('-f, --format <format>', 'Export format: json|csv', 'json')
  .option('-o, --output <path>', 'Output file (default: stdout)')
  .action(async (opts) => {
    const config = loadConfig(program.opts().config);
    const data = index.exportDb(config, opts.format);

    if (opts.output) {
      fs.writeFileSync(opts.output, data, 'utf8');
      console.log(`Exported to ${opts.output}`);
    } else {
      console.log(data);
    }
  });

// === init ===
program.command('init')
  .description('Create initial config file')
  .option('-f, --force', 'Overwrite existing config')
  .action(async (opts) => {
    const configPath = path.resolve(
      (program.opts().config || '~/.bidding-hunter/config.yaml').replace(/^~/, process.env.HOME || '/home/$USER')
    );

    if (fs.existsSync(configPath) && !opts.force) {
      console.error(`Config already exists at ${configPath}`);
      console.error('Use --force to overwrite, or edit manually.');
      process.exit(1);
    }

    const defaultConfig = fs.readFileSync(
      path.join(__dirname, '..', 'config', 'default.yaml'),
      'utf8'
    );

    fs.mkdirSync(path.dirname(configPath), { recursive: true });
    fs.writeFileSync(configPath, defaultConfig, 'utf8');
    console.log(`✅ Config created at ${configPath}`);
    console.log('Edit this file to configure keywords, platforms, and notifications.');
  });

// === explore ===
program.command('explore')
  .description('Agent-guided platform exploration (use with AI assistant)')
  .requiredOption('-u, --url <url>', 'Platform homepage URL')
  .option('-n, --name <name>', 'Platform name (human-readable)')
  .action(async (opts) => {
    const config = loadConfig(program.opts().config);
    const { explorePlatform } = require('../scripts/explore-platform');

    console.log(`🔍 Exploring platform: ${opts.name || opts.url}`);
    console.log(`   URL: ${opts.url}`);
    console.log('');
    console.log('This is an AI-assisted exploration. The agent will:');
    console.log('  1. Navigate to the platform');
    console.log('  2. Identify the procurement listing page');
    console.log('  3. Find pagination controls');
    console.log('  4. Determine extraction selectors');
    console.log('  5. Generate a platform adapter');
    console.log('');
    console.log('Run this with an AI agent that can control a browser.');
    console.log('Or use the following prompt with your AI assistant:');
    console.log('');
    console.log(`Please explore ${opts.url} and help me create a Bidding Hunter platform adapter.`);
    console.log('Find the procurement announcement listing page, identify how to:');
    console.log('  1. Navigate to the listing (URL or search flow)');
    console.log('  2. Extract titles, dates, and URLs from result items');
    console.log('  3. Navigate to next pages (pagination)');
    console.log('  4. Handle any filters or search boxes');
    console.log('');
    console.log('Then create the adapter using:');
    console.log('  bidding-hunter create-adapter --name <id>');
    console.log('And fill in the extraction logic.');
  });

// === create-adapter ===
program.command('create-adapter')
  .description('Create a platform adapter from template')
  .requiredOption('-n, --name <id>', 'Platform identifier (e.g., sichuan)')
  .action(async (opts) => {
    const template = fs.readFileSync(
      path.join(__dirname, '..', 'templates', 'platform-adapter.js'),
      'utf8'
    );

    const userDir = path.join(process.env.HOME || '/tmp', '.bidding-hunter', 'platforms');
    fs.mkdirSync(userDir, { recursive: true });

    const filePath = path.join(userDir, `${opts.name}.js`);
    if (fs.existsSync(filePath)) {
      console.error(`Adapter already exists: ${filePath}`);
      process.exit(1);
    }

    const content = template
      .replace(/\{\{PLATFORM_ID\}\}/g, opts.name)
      .replace(/\{\{PLATFORM_NAME\}\}/g, opts.name);

    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`✅ Adapter created at ${filePath}`);
    console.log('');
    console.log('Next steps:');
    console.log(`  1. Edit the adapter: vim ${filePath}`);
    console.log('  2. Implement the scan() method');
    console.log('  3. Test: bidding-hunter test-platform --name ' + opts.name);
  });

// === test-platform ===
program.command('test-platform')
  .description('Test a platform adapter')
  .requiredOption('-n, --name <id>', 'Platform identifier')
  .option('--url <url>', 'Test a specific URL instead of scanning')
  .action(async (opts) => {
    const config = loadConfig(program.opts().config);
    const adapter = registry.get(config, opts.name);

    if (!adapter) {
      console.error(`Platform '${opts.name}' not found.`);
      console.error('Available platforms: ' + registry.list(config).map(p => p.id).join(', '));
      process.exit(1);
    }

    console.log(`Testing platform: ${adapter.meta.name} (${adapter.meta.id})`);

    if (opts.url) {
      // Test detail fetching
      const { fetchDetail } = require('../src/detail-fetcher');
      console.log(`Fetching detail from: ${opts.url}`);
      const result = await fetchDetail(opts.url);
      console.log(JSON.stringify(result, null, 2));
    } else {
      // Test scan
      try {
        console.log('Running test scan (dry run)...');
        console.log('(This will open a browser. Press Ctrl+C to abort.)');
        const { chromium } = require('playwright');
        const today = index.localDate();
        const yesterday = index.localDate(-1);

        const browser = await chromium.launch({
          headless: true,
          args: ['--no-sandbox', '--disable-setuid-sandbox'],
        });

        const context = {
          browser,
          reportedUrls: new Set(),
          logger: { info: console.error, warn: console.error, error: console.error },
          today,
          fromDate: yesterday,
          dateWindow: 2,
          retryStairs: [
            { timeout: 30000, waitUntil: 'domcontentloaded' },
            { timeout: 45000, waitUntil: 'domcontentloaded' },
            { timeout: 60000, waitUntil: 'networkidle' },
          ],
          userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        };

        const result = await adapter.scan(context, config);
        await browser.close();

        console.log(`\n✅ Scan complete: ${result.items?.length || 0} items returned`);
        if (result.error) console.log(`⚠️  Error: ${result.error}`);
        if (result.items?.length > 0) {
          console.log('\nSample items:');
          for (const item of result.items.slice(0, 5)) {
            console.log(`  - ${item.title?.substring(0, 60)} | ${item.date} | ${item.url?.substring(0, 60)}`);
          }
        }
      } catch (error) {
        console.error(`Test failed: ${error.message}`);
        process.exit(1);
      }
    }
  });

program.parse();
