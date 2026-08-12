#!/usr/bin/env node
/**
 * reporter.js — Report generation for Bidding Hunter.
 *
 * Generates structured reports in multiple formats: text, markdown, JSON.
 */

const dayjs = require('dayjs');

/**
 * Generate a complete report.
 * @param {object} params
 * @param {object} params.config - Full config
 * @param {object} params.scan - Scan results { stats, items }
 * @param {Array} params.added - Newly added entries
 * @param {object} params.reminders - Reminder output { urgent, openResults, missingDates }
 * @param {object} params.db - Database wrapper
 * @param {string} params.today - Date string YYYY-MM-DD
 * @returns {{ text: string, json: object, markdown: string }}
 */
function generate({ config, scan, added, reminders, db, today }) {
  const maxTitleLen = config.report?.max_title_length || 60;
  const showStats = config.report?.show_stats !== false;
  const showReminders = config.report?.show_reminders !== false;
  const showUndecided = config.report?.show_undecided_prompt !== false;

  const stats = scan.stats || {};
  const dbStats = db.getStats ? db.getStats() : { total: 0, byStatus: {} };

  const json = {
    date: today,
    generated_at: new Date().toISOString(),
    scan: { stats, summary: summarizeScan(stats) },
    added: (added || []).map(e => ({
      alias: e.alias,
      level: e.match_level || e.level || '',
      keyword: e.match_kw || e.keyword || '',
      title: e.title,
      region: e.region || e.site || '',
      pub_date: e.pub_date || e.date || '',
      url: e.url,
    })),
    reminders: {
      urgent: (reminders?.urgent || []).map(r => ({
        alias: r.alias || (r.entry?.alias),
        title: r.title || (r.entry?.title),
        deadline: r.deadline || (r.entry?.bid_submit),
        days: r.days,
        status: r.bid_status || (r.entry?.bid_status),
      })),
      openResults: (reminders?.openResults || []).map(r => ({
        alias: r.alias || (r.entry?.alias),
        title: r.title || (r.entry?.title),
      })),
      missingDates: (reminders?.missingDates || []).map(e => ({
        alias: e.alias,
        title: e.title,
      })),
    },
    database: dbStats,
  };

  const text = buildTextReport({ added, reminders, stats, dbStats, today, config, maxTitleLen, showStats, showReminders, showUndecided });
  const markdown = buildMarkdownReport(json, config, maxTitleLen);

  return { text, json, markdown };
}

/**
 * Build the human-readable text report.
 */
function buildTextReport({ added, reminders, stats, dbStats, today, config, maxTitleLen, showStats, showReminders, showUndecided }) {
  const lines = [];
  const title = config.report?.title || '📋 Bid Intelligence Report';
  lines.push(`${title} | ${today}`, '');

  // New matches
  if (added && added.length > 0) {
    lines.push(`🆕 New Matches: ${added.length}`, '');
    for (const entry of added) {
      const level = entry.match_level || entry.level || '';
      const kw = entry.match_kw || entry.keyword || '';
      const levelStr = level ? `[${level}${kw ? ` · ${kw}` : ''}] ` : '';
      lines.push(`#${entry.alias} ${levelStr}${truncate(entry.title, maxTitleLen)}`);
      const region = entry.region || entry.site || '';
      const date = entry.pub_date || entry.date || '';
      lines.push(`   ${region} · ${date} · undecided`);
      lines.push(`   🔗 ${entry.url}`, '');
    }
  }

  // Scan stats
  if (showStats) {
    const statParts = [];
    for (const [site, data] of Object.entries(stats)) {
      if (data.error) {
        statParts.push(`${site}(❌)`);
      } else {
        statParts.push(`${site}(${data.scanned || 0})`);
      }
    }
    if (statParts.length > 0) {
      lines.push(`⏱️ Scan: ${statParts.join(' ')}`);
    }
  }

  // Reminders
  if (showReminders && reminders) {
    const hasReminders = (reminders.urgent?.length || 0) +
      (reminders.openResults?.length || 0) +
      (reminders.missingDates?.length || 0) > 0;

    if (hasReminders) {
      lines.push('', '─'.repeat(20), '', '📌 Reminders', '');

      if (reminders.urgent && reminders.urgent.length > 0) {
        lines.push(`🔴 Deadline Approaching (${reminders.urgent.length})`);
        for (const { entry, days } of reminders.urgent) {
          if (!entry) continue;
          const label = days === 0 ? 'TODAY' : days === -1 ? 'YESTERDAY' : `${days}d remaining`;
          lines.push(`   #${entry.alias} [${entry.match_level || ''}] ${truncate(entry.title, maxTitleLen)}`);
          lines.push(`       Deadline: ${entry.bid_submit || entry.deadlines?.bid_submit?.date} · ${label} · ${entry.bid_status || ''}`);
        }
        lines.push('');
      }

      if (reminders.openResults && reminders.openResults.length > 0) {
        lines.push(`🔵 Awaiting Bid Results (${reminders.openResults.length})`);
        for (const { entry } of reminders.openResults) {
          if (!entry) continue;
          lines.push(`   #${entry.alias} [${entry.match_level || ''}] ${truncate(entry.title, maxTitleLen)}`);
        }
        lines.push('');
      }

      if (reminders.missingDates && reminders.missingDates.length > 0) {
        lines.push(`🟡 Tracking — No Due Date (${reminders.missingDates.length})`);
        for (const entry of reminders.missingDates) {
          lines.push(`   #${entry.alias} [${entry.match_level || ''}] ${truncate(entry.title, maxTitleLen)}`);
        }
        lines.push('');
      }
    }
  }

  // Undecided prompt
  const pending = dbStats.byStatus?.undecided || 0;
  if (showUndecided && pending > 0) {
    lines.push(`⭕ ${pending} entries undecided — review and set status: tracked / discarded`);
  }

  // Summary
  const tracked = dbStats.byStatus?.tracked || 0;
  const discarded = dbStats.byStatus?.discarded || 0;
  lines.push(`📊 Total: ${dbStats.total || 0} | Tracked: ${tracked} | Undecided: ${pending} | Discarded: ${discarded}`);

  return lines.join('\n');
}

/**
 * Build a Markdown-formatted report (GitHub-compatible).
 */
function buildMarkdownReport(json, config, maxTitleLen) {
  const lines = [];
  lines.push(`# 📋 Bid Intelligence Report — ${json.date}`, '');

  if (json.added.length > 0) {
    lines.push(`## 🆕 New Matches (${json.added.length})`, '');
    lines.push('| # | Level | Title | Region | Date |');
    lines.push('|---|-------|-------|--------|------|');
    for (const e of json.added) {
      const kw = e.keyword ? `·${e.keyword}` : '';
      lines.push(`| #${e.alias} | ${e.level}${kw} | ${escapeMd(truncate(e.title, maxTitleLen))} | ${e.region} | ${e.pub_date} |`);
    }
    lines.push('');
  }

  lines.push('## ⏱️ Scan Stats', '');
  for (const [site, data] of Object.entries(json.scan.stats)) {
    const emoji = data.error ? '❌' : '✅';
    lines.push(`- ${emoji} **${site}**: ${data.scanned || 0} scanned, ${data.new || 0} new`);
  }
  lines.push('');

  // Reminders
  if (json.reminders.urgent.length > 0 || json.reminders.openResults.length > 0) {
    lines.push('## 📌 Reminders', '');
    for (const r of json.reminders.urgent) {
      const label = r.days === 0 ? '**TODAY**' : `${r.days}d`;
      lines.push(`- 🔴 #${r.alias} ${r.title} — ${label} — ${r.status || ''}`);
    }
    for (const r of json.reminders.openResults) {
      lines.push(`- 🔵 #${r.alias} ${r.title} — awaiting results`);
    }
    lines.push('');
  }

  lines.push(`## 📊 Database Summary`, '');
  lines.push(`- Total: ${json.database.total}`);
  for (const [status, count] of Object.entries(json.database.byStatus || {})) {
    lines.push(`- ${status}: ${count}`);
  }
  lines.push('');

  return lines.join('\n');
}

// --- Helpers ---

function truncate(text, max) {
  if (!text) return '';
  return text.length <= max ? text : text.slice(0, max) + '...';
}

function escapeMd(text) {
  return (text || '').replace(/[|\\]/g, '\\$&');
}

function summarizeScan(stats) {
  const summary = {};
  for (const [site, data] of Object.entries(stats)) {
    summary[site] = data.error ? 'failed' : `${data.scanned || 0} scanned`;
  }
  return summary;
}

module.exports = { generate };
