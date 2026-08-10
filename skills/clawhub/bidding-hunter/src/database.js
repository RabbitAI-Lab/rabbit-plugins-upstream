#!/usr/bin/env node
/**
 * database.js — SQLite storage layer for Bidding Hunter.
 *
 * All data operations go through this module.
 * Uses better-sqlite3 for synchronous, safe access.
 */

const path = require('path');
const fs = require('fs');

let Database;
try {
  Database = require('better-sqlite3');
} catch {
  // Fallback to JSON file if better-sqlite3 not available
  Database = null;
}

const SCHEMA_VERSION = 1;

const SCHEMA = `
CREATE TABLE IF NOT EXISTS meta (
  key   TEXT PRIMARY KEY,
  value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS entries (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  alias         INTEGER NOT NULL UNIQUE,
  title         TEXT NOT NULL,
  url           TEXT NOT NULL UNIQUE,
  site          TEXT NOT NULL,
  region        TEXT DEFAULT '',
  pub_date      TEXT NOT NULL,
  match_level   TEXT DEFAULT '',
  match_kw      TEXT DEFAULT '',
  status        TEXT DEFAULT 'undecided',
  bid_status    TEXT DEFAULT NULL,
  budget        REAL DEFAULT NULL,
  budget_unit   TEXT DEFAULT NULL,
  proc_method   TEXT DEFAULT NULL,
  first_seen    TEXT NOT NULL,
  last_updated  TEXT NOT NULL,
  notes         TEXT DEFAULT '',
  result_won    INTEGER DEFAULT NULL,
  result_url    TEXT DEFAULT NULL,
  raw_json      TEXT DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS deadlines (
  id        INTEGER PRIMARY KEY AUTOINCREMENT,
  entry_id  INTEGER NOT NULL REFERENCES entries(id) ON DELETE CASCADE,
  type      TEXT NOT NULL,
  date      TEXT NOT NULL,
  source    TEXT DEFAULT 'auto',
  UNIQUE(entry_id, type)
);

CREATE TABLE IF NOT EXISTS history (
  id        INTEGER PRIMARY KEY AUTOINCREMENT,
  entry_id  INTEGER NOT NULL REFERENCES entries(id) ON DELETE CASCADE,
  date      TEXT NOT NULL,
  event     TEXT NOT NULL,
  detail    TEXT DEFAULT ''
);

CREATE TABLE IF NOT EXISTS scan_log (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  date        TEXT NOT NULL,
  site        TEXT NOT NULL,
  scanned     INTEGER DEFAULT 0,
  new_matches INTEGER DEFAULT 0,
  status      TEXT DEFAULT 'ok',
  error       TEXT DEFAULT NULL,
  started_at  TEXT NOT NULL,
  ended_at    TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS reported_urls (
  url         TEXT PRIMARY KEY,
  first_seen  TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_entries_status ON entries(status);
CREATE INDEX IF NOT EXISTS idx_entries_site ON entries(site);
CREATE INDEX IF NOT EXISTS idx_entries_pub_date ON entries(pub_date);
CREATE INDEX IF NOT EXISTS idx_entries_alias ON entries(alias);
CREATE INDEX IF NOT EXISTS idx_deadlines_entry ON deadlines(entry_id);
CREATE INDEX IF NOT EXISTS idx_deadlines_date ON deadlines(date);
CREATE INDEX IF NOT EXISTS idx_history_entry ON history(entry_id);
`;

function init(config) {
  if (!Database) {
    return initJsonFallback(config);
  }

  const dbPath = resolvePath(config.database?.path || '~/.bidding-hunter/data.db');
  fs.mkdirSync(path.dirname(dbPath), { recursive: true });

  let db;
  try {
    db = new Database(dbPath);
  } catch {
    // Native binding missing (e.g., npm install --ignore-scripts)
    return initJsonFallback(config);
  }
  db.pragma('journal_mode = WAL');
  db.pragma('foreign_keys = ON');

  // Run schema migration
  db.exec(SCHEMA);

  // Version check / migration
  const versionRow = db.prepare("SELECT value FROM meta WHERE key = 'schema_version'").get();
  const currentVersion = versionRow ? parseInt(versionRow.value) : 0;
  if (currentVersion < SCHEMA_VERSION) {
    db.prepare("INSERT OR REPLACE INTO meta (key, value) VALUES ('schema_version', ?)").run(String(SCHEMA_VERSION));
  }

  return new DatabaseWrapper(db, config);
}

function initJsonFallback(config) {
  console.error('[bidding-hunter] better-sqlite3 not available, using JSON fallback (not recommended for production)');
  const dataPath = resolvePath(config.database?.path || '~/.bidding-hunter/data.json');
  fs.mkdirSync(path.dirname(dataPath), { recursive: true });

  let data;
  try {
    data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
  } catch {
    data = { entries: {}, next_alias: 1, history: [], scan_log: [], reported_urls: [] };
  }

  return new JsonDatabaseWrapper(data, dataPath);
}

// ============================================================
// SQLite Wrapper
// ============================================================
class DatabaseWrapper {
  constructor(db, config) {
    this.db = db;
    this.config = config;
    // Prepared statements
    this._prepare();
  }

  _prepare() {
    const db = this.db;
    this.stmts = {
      insertEntry: db.prepare(`
        INSERT INTO entries (alias, title, url, site, region, pub_date, match_level, match_kw,
          status, first_seen, last_updated, raw_json)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'undecided', ?, ?, ?)
      `),
      getEntryByUrl: db.prepare('SELECT * FROM entries WHERE url = ?'),
      getEntryByAlias: db.prepare('SELECT * FROM entries WHERE alias = ?'),
      updateEntry: db.prepare(`
        UPDATE entries SET status = ?, bid_status = ?, notes = ?, last_updated = ?,
        result_won = ?, result_url = ?
        WHERE alias = ?
      `),
      insertDeadline: db.prepare(`
        INSERT OR REPLACE INTO deadlines (entry_id, type, date, source) VALUES (?, ?, ?, ?)
      `),
      insertHistory: db.prepare(`
        INSERT INTO history (entry_id, date, event, detail) VALUES (?, ?, ?, ?)
      `),
      insertScanLog: db.prepare(`
        INSERT INTO scan_log (date, site, scanned, new_matches, status, error, started_at, ended_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
      `),
      getReportedUrls: db.prepare('SELECT url FROM reported_urls'),
      insertReportedUrl: db.prepare('INSERT OR IGNORE INTO reported_urls (url, first_seen) VALUES (?, ?)'),
      getNextAlias: db.prepare("SELECT COALESCE(MAX(alias), 0) + 1 as next FROM entries"),
      getStats: db.prepare(`
        SELECT status, COUNT(*) as count FROM entries GROUP BY status
      `),
      listByStatus: db.prepare('SELECT * FROM entries WHERE status = ? ORDER BY pub_date DESC'),
      getDeadlines: db.prepare('SELECT * FROM deadlines WHERE entry_id = ?'),
      getHistory: db.prepare('SELECT * FROM history WHERE entry_id = ? ORDER BY date DESC'),
      searchEntries: db.prepare(`
        SELECT * FROM entries WHERE title LIKE ? OR site LIKE ? ORDER BY pub_date DESC
      `),
      getAllEntries: db.prepare('SELECT * FROM entries ORDER BY alias'),
    };
  }

  getReportedUrls() {
    try {
      const rows = this.stmts.getReportedUrls.all();
      return new Set(rows.map(r => r.url));
    } catch { return new Set(); }
  }

  getNextAlias() {
    const row = this.stmts.getNextAlias.get();
    return row ? row.next : 1;
  }

  entryExists(url) {
    return Boolean(this.stmts.getEntryByUrl.get(url));
  }

  insertEntry(entry, today) {
    const alias = this.getNextAlias();
    const stmt = this.stmts.insertEntry;
    stmt.run(
      alias,
      entry.title,
      entry.url,
      entry.site || '',
      entry.region || '',
      entry.pub_date || entry.date || today,
      entry.match_level || entry.level || '',
      entry.match_kw || entry.keyword || '',
      entry.first_seen || today,
      today,
      JSON.stringify(entry.raw || {})
    );
    // Add history
    const entryRow = this.stmts.getEntryByAlias.get(alias);
    if (entryRow) {
      this.stmts.insertHistory.run(entryRow.id, today, 'ingested', 'Discovered by scanner');
    }
    return { alias, url: entry.url, title: entry.title };
  }

  updateEntry(alias, updates, today) {
    const entry = this.stmts.getEntryByAlias.get(alias);
    if (!entry) throw new Error(`Entry #${alias} not found`);

    const db = this.db;
    const txn = db.transaction(() => {
      const now = today || new Date().toISOString().slice(0, 10);
      const status = updates.status !== undefined ? updates.status : entry.status;
      const bidStatus = updates.bid_status !== undefined ? updates.bid_status : entry.bid_status;
      const notes = updates.notes !== undefined ? updates.notes : (entry.notes || '');
      const resultWon = updates.result_won !== undefined ? (updates.result_won ? 1 : 0) : entry.result_won;
      const resultUrl = updates.result_url !== undefined ? updates.result_url : (entry.result_url || '');

      this.stmts.updateEntry.run(status, bidStatus, notes, now, resultWon, resultUrl, alias);

      // Log history
      const events = [];
      if (updates.status !== undefined && updates.status !== entry.status) events.push(`status → ${updates.status}`);
      if (updates.bid_status !== undefined && updates.bid_status !== entry.bid_status) events.push(`bid_status → ${updates.bid_status}`);
      if (updates.result_won !== undefined) events.push(`result → ${updates.result_won ? 'won' : 'lost'}`);
      if (updates.notes !== undefined) events.push('notes updated');

      for (const e of events) {
        this.stmts.insertHistory.run(entry.id, now, e, notes);
      }
    });
    txn();
    return this.stmts.getEntryByAlias.get(alias);
  }

  setDeadline(alias, type, date, source = 'auto') {
    const entry = this.stmts.getEntryByAlias.get(alias);
    if (!entry) return;
    this.stmts.insertDeadline.run(entry.id, type, date, source);
  }

  getEntriesNeedingDetails(today, maxAgeDays = 30) {
    const rows = this.db.prepare(`
      SELECT e.* FROM entries e
      WHERE e.status = 'tracked'
      AND e.id NOT IN (SELECT entry_id FROM deadlines)
      AND julianday(?) - julianday(e.first_seen) <= ?
    `).all(today, maxAgeDays);
    return rows;
  }

  getTrackedEntries() {
    return this.db.prepare(`
      SELECT e.*, 
        (SELECT date FROM deadlines WHERE entry_id = e.id AND type = 'bid_submit') as bid_submit,
        (SELECT date FROM deadlines WHERE entry_id = e.id AND type = 'bid_open') as bid_open
      FROM entries e WHERE e.status = 'tracked' ORDER BY e.alias
    `).all();
  }

  getEntriesByDate(today) {
    return this.db.prepare('SELECT * FROM entries WHERE first_seen = ? OR pub_date = ? ORDER BY alias').all(today, today);
  }

  listEntries(filters = {}) {
    let query = 'SELECT * FROM entries WHERE 1=1';
    const params = [];
    if (filters.status) { query += ' AND status = ?'; params.push(filters.status); }
    if (filters.site) { query += ' AND site = ?'; params.push(filters.site); }
    if (filters.level) { query += ' AND match_level = ?'; params.push(filters.level); }
    query += ' ORDER BY alias';
    return this.db.prepare(query).all(...params);
  }

  getStats() {
    const byStatus = {};
    for (const row of this.stmts.getStats.all()) {
      byStatus[row.status] = row.count;
    }
    const totalRow = this.db.prepare('SELECT COUNT(*) as total FROM entries').get();
    return {
      total: totalRow ? totalRow.total : 0,
      byStatus,
      bySite: this._getBySite(),
      byLevel: this._getByLevel(),
    };
  }

  _getBySite() {
    const rows = this.db.prepare('SELECT site, COUNT(*) as count FROM entries GROUP BY site').all();
    const result = {};
    for (const r of rows) result[r.site] = r.count;
    return result;
  }

  _getByLevel() {
    const rows = this.db.prepare('SELECT match_level, COUNT(*) as count FROM entries GROUP BY match_level').all();
    const result = {};
    for (const r of rows) result[r.match_level || 'none'] = r.count;
    return result;
  }

  saveScanLog(today, stats) {
    const now = new Date().toISOString();
    const stmt = this.stmts.insertScanLog;
    for (const [site, data] of Object.entries(stats)) {
      stmt.run(
        today, site,
        data.scanned || 0, data.new || 0,
        data.error ? 'failed' : 'ok',
        data.error || null,
        now, now
      );
    }
  }

  markReportedUrls(urls, today) {
    const stmt = this.stmts.insertReportedUrl;
    const txn = this.db.transaction(() => {
      for (const url of urls) {
        stmt.run(url, today);
      }
    });
    txn();
  }

  export(format = 'json') {
    const entries = this.stmts.getAllEntries.all();
    if (format === 'csv') {
      const headers = ['alias', 'title', 'url', 'site', 'region', 'pub_date', 'match_level', 'match_kw', 'status', 'bid_status'];
      const lines = [headers.join(',')];
      for (const e of entries) {
        lines.push(headers.map(h => {
          const val = String(e[h] || '').replace(/"/g, '""');
          return `"${val}"`;
        }).join(','));
      }
      return lines.join('\n');
    }
    return JSON.stringify(entries, null, 2);
  }

  /**
   * Ingest matched items into the database.
   * Skips items already in the database (by URL).
   * Updates scan stats with "new" count per site.
   * @param {Array} matched - Items from matchAll() with .match property
   * @param {string} today - Current date
   * @param {object} scanResult - Scanner output { stats }
   * @returns {Array} Newly added entries
   */
  ingest(matched, today, scanResult) {
    const added = [];
    if (!matched || !matched.length) return added;

    for (const item of matched) {
      // Skip if already exists
      if (this.entryExists(item.url)) continue;

      // Map match fields
      const matchLevel = item.match?.level || '';
      const matchKw = item.match?.keyword || '';

      // Insert
      const result = this.insertEntry({
        title: item.title,
        url: item.url,
        site: item.site || '',
        region: item.region || '',
        pub_date: item.pub_date || item.date || today,
        match_level: matchLevel,
        match_kw: matchKw,
        first_seen: today,
      }, today);

      added.push({ ...result, match_level: matchLevel, match_kw: matchKw });

      // Update per-site new count in scan stats
      const site = item.site || 'unknown';
      if (scanResult?.stats?.[site]) {
        scanResult.stats[site].new = (scanResult.stats[site].new || 0) + 1;
      }
    }

    return added;
  }

  close() {
    this.db.close();
  }
}

// ============================================================
// JSON Fallback Wrapper (same interface)
// ============================================================
class JsonDatabaseWrapper {
  constructor(data, filePath) {
    this.data = data;
    this.filePath = filePath;
    this.data.entries = this.data.entries || {};
    this.data.reported_urls = this.data.reported_urls || [];
    this.data.history = this.data.history || [];
    this.data.scan_log = this.data.scan_log || [];
    this.data.next_alias = this.data.next_alias || 1;
  }

  _save() {
    fs.writeFileSync(this.filePath, JSON.stringify(this.data, null, 2));
  }

  getReportedUrls() {
    return new Set(this.data.reported_urls);
  }

  getNextAlias() {
    return this.data.next_alias;
  }

  entryExists(url) {
    return Boolean(this.data.entries[url]);
  }

  insertEntry(entry, today) {
    const alias = this.data.next_alias++;
    this.data.entries[entry.url] = {
      alias,
      title: entry.title,
      url: entry.url,
      site: entry.site || '',
      region: entry.region || '',
      pub_date: entry.pub_date || entry.date || today,
      match_level: entry.match_level || entry.level || '',
      match_kw: entry.match_kw || entry.keyword || '',
      status: 'undecided',
      bid_status: null,
      first_seen: entry.first_seen || today,
      last_updated: today,
      raw_json: JSON.stringify(entry.raw || {}),
    };
    this._save();
    return { alias, url: entry.url, title: entry.title };
  }

  updateEntry(alias, updates, today) {
    const now = today || new Date().toISOString().slice(0, 10);
    let found = null;
    for (const [url, entry] of Object.entries(this.data.entries)) {
      if (entry.alias === alias) {
        if (updates.status !== undefined) entry.status = updates.status;
        if (updates.bid_status !== undefined) entry.bid_status = updates.bid_status;
        if (updates.notes !== undefined) entry.notes = updates.notes;
        entry.last_updated = now;
        found = entry;
        break;
      }
    }
    if (!found) throw new Error(`Entry #${alias} not found`);
    this._save();
    return found;
  }

  setDeadline(alias, type, date, source = 'auto') {
    for (const [url, entry] of Object.entries(this.data.entries)) {
      if (entry.alias === alias) {
        entry.deadlines = entry.deadlines || {};
        entry.deadlines[type] = { date, source };
        this._save();
        return;
      }
    }
  }

  getTrackedEntries() {
    return Object.values(this.data.entries).filter(e => e.status === 'tracked');
  }

  getEntriesNeedingDetails(today, maxAge) {
    return this.getTrackedEntries().filter(e => !e.deadlines || Object.keys(e.deadlines).length === 0);
  }

  getEntriesByDate(today) {
    return Object.values(this.data.entries).filter(e => e.first_seen === today || e.pub_date === today);
  }

  listEntries(filters = {}) {
    let entries = Object.values(this.data.entries);
    if (filters.status) entries = entries.filter(e => e.status === filters.status);
    if (filters.site) entries = entries.filter(e => e.site === filters.site);
    if (filters.level) entries = entries.filter(e => e.match_level === filters.level);
    return entries;
  }

  getStats() {
    const byStatus = {};
    const bySite = {};
    const byLevel = {};
    for (const e of Object.values(this.data.entries)) {
      byStatus[e.status] = (byStatus[e.status] || 0) + 1;
      bySite[e.site] = (bySite[e.site] || 0) + 1;
      const lvl = e.match_level || 'none';
      byLevel[lvl] = (byLevel[lvl] || 0) + 1;
    }
    return {
      total: Object.keys(this.data.entries).length,
      byStatus,
      bySite,
      byLevel,
    };
  }

  saveScanLog(today, stats) {
    for (const [site, data] of Object.entries(stats)) {
      this.data.scan_log.push({
        date: today, site,
        scanned: data.scanned || 0,
        new_matches: data.new || 0,
        status: data.error ? 'failed' : 'ok',
        error: data.error || null,
      });
    }
    this._save();
  }

  markReportedUrls(urls, today) {
    for (const url of urls) {
      if (!this.data.reported_urls.includes(url)) {
        this.data.reported_urls.push(url);
      }
    }
    this._save();
  }

  ingest(matched, today, scanResult) {
    const added = [];
    if (!matched || !matched.length) return added;

    for (const item of matched) {
      if (this.data.entries[item.url]) continue;

      const matchLevel = item.match?.level || '';
      const matchKw = item.match?.keyword || '';

      const result = this.insertEntry({
        title: item.title,
        url: item.url,
        site: item.site || '',
        region: item.region || '',
        pub_date: item.pub_date || item.date || today,
        match_level: matchLevel,
        match_kw: matchKw,
        first_seen: today,
      }, today);

      added.push({ ...result, match_level: matchLevel, match_kw: matchKw });

      const site = item.site || 'unknown';
      if (scanResult?.stats?.[site]) {
        scanResult.stats[site].new = (scanResult.stats[site].new || 0) + 1;
      }
    }

    return added;
  }

  export(format = 'json') {
    const entries = Object.values(this.data.entries);
    if (format === 'csv') {
      const headers = ['alias', 'title', 'url', 'site', 'region', 'pub_date', 'match_level', 'match_kw', 'status'];
      const lines = [headers.join(',')];
      for (const e of entries) {
        lines.push(headers.map(h => `"${String(e[h] || '').replace(/"/g, '""')}"`).join(','));
      }
      return lines.join('\n');
    }
    return JSON.stringify(entries, null, 2);
  }

  close() {}
}

// --- Helpers ---

function resolvePath(p) {
  if (p.startsWith('~')) {
    const home = process.env.HOME || path.join('/home', process.env.USER || 'user');
    p = path.join(home, p.slice(1));
  }
  return path.resolve(p);
}

module.exports = { init, resolvePath };
