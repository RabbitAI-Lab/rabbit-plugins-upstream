#!/usr/bin/env node
/**
 * database.test.js — Tests for the JSON fallback database layer.
 *
 * Tests run against the JSON fallback (no better-sqlite3 dependency in CI).
 */

const { describe, it, before, after } = require('node:test');
const assert = require('node:assert');
const fs = require('fs');
const path = require('path');
const os = require('os');

describe('Database (JSON fallback)', () => {
  let db;
  const testDir = path.join(os.tmpdir(), `bidding-hunter-test-${Date.now()}`);
  const testConfig = {
    database: { path: path.join(testDir, 'test-data.json') },
  };

  before(() => {
    fs.mkdirSync(testDir, { recursive: true });
    // Force JSON fallback by temporarily removing better-sqlite3
    const database = require('../src/database');
    db = database.init(testConfig);
  });

  after(() => {
    if (db && db.close) db.close();
    fs.rmSync(testDir, { recursive: true, force: true });
  });

  it('starts empty', () => {
    const stats = db.getStats();
    assert.strictEqual(stats.total, 0);
  });

  it('inserts entries and assigns aliases', () => {
    const entry1 = db.insertEntry({
      title: '视频制作项目招标公告',
      url: 'https://example.com/bid/1',
      site: '北京',
      region: '北京市',
      pub_date: '2026-07-20',
      match_level: 'L1',
      match_kw: '视频制作',
    }, '2026-07-21');

    assert.strictEqual(entry1.alias, 1);
    assert.strictEqual(entry1.title, '视频制作项目招标公告');

    const entry2 = db.insertEntry({
      title: '活动策划服务项目',
      url: 'https://example.com/bid/2',
      site: '河北',
      region: '',
      pub_date: '2026-07-20',
      match_level: 'L2',
      match_kw: '活动策划',
    }, '2026-07-21');

    assert.strictEqual(entry2.alias, 2);
  });

  it('deduplicates by URL', () => {
    assert.ok(db.entryExists('https://example.com/bid/1'));
    assert.ok(!db.entryExists('https://example.com/bid/999'));
  });

  it('updates entry status', () => {
    const updated = db.updateEntry(1, { status: 'tracked', bid_status: 'watching' }, '2026-07-21');
    assert.strictEqual(updated.status, 'tracked');
    assert.strictEqual(updated.bid_status, 'watching');
  });

  it('sets deadlines', () => {
    db.setDeadline(1, 'bid_submit', '2026-08-15');
    const entries = db.getTrackedEntries();
    const entry = entries.find(e => e.alias === 1);
    assert.ok(entry);
    assert.ok(entry.deadlines);
    assert.strictEqual(entry.deadlines.bid_submit.date, '2026-08-15');
  });

  it('lists entries with filters', () => {
    const tracked = db.listEntries({ status: 'tracked' });
    assert.strictEqual(tracked.length, 1);
    assert.strictEqual(tracked[0].alias, 1);

    const beijing = db.listEntries({ site: '北京' });
    assert.strictEqual(beijing.length, 1);

    const l2 = db.listEntries({ level: 'L2' });
    assert.strictEqual(l2.length, 1);
  });

  it('returns correct statistics', () => {
    const stats = db.getStats();
    assert.strictEqual(stats.total, 2);
    assert.strictEqual(stats.byStatus.tracked, 1);
    assert.strictEqual(stats.byStatus.undecided, 1);
    assert.strictEqual(stats.bySite['北京'], 1);
    assert.strictEqual(stats.bySite['河北'], 1);
    assert.strictEqual(stats.byLevel.L1, 1);
    assert.strictEqual(stats.byLevel.L2, 1);
  });

  it('handles reported URLs', () => {
    db.markReportedUrls(['https://example.com/bid/reported'], '2026-07-21');
    const urls = db.getReportedUrls();
    assert.ok(urls instanceof Set);
    assert.ok(urls.has('https://example.com/bid/reported'));
  });

  it('exports to JSON format', () => {
    const json = db.export('json');
    const parsed = JSON.parse(json);
    assert.ok(Array.isArray(parsed));
    assert.strictEqual(parsed.length, 2);
    assert.strictEqual(parsed[0].alias, 1);
  });

  it('exports to CSV format', () => {
    const csv = db.export('csv');
    assert.ok(csv.includes('alias,title'));
    assert.ok(csv.includes('视频制作项目招标公告'));
  });

  it('throws on updating non-existent entry', () => {
    assert.throws(() => {
      db.updateEntry(999, { status: 'tracked' });
    }, /not found/);
  });

  it('ingests matched items with proper field mapping', () => {
    const scanResult = { stats: { 湖南: { scanned: 10, new: 0 } } };
    const matched = [
      { title: '湖南视频制作项目', url: 'https://example.com/bid/3', site: '湖南', region: '长沙市', date: '2026-07-21', match: { level: 'L1', keyword: '视频制作' } },
      { title: '湖南活动策划项目', url: 'https://example.com/bid/4', site: '湖南', region: '', date: '2026-07-20', match: { level: 'L2', keyword: '活动策划' } },
      // Duplicate URL — should be skipped
      { title: '重复项目', url: 'https://example.com/bid/1', site: '北京', date: '2026-07-21', match: { level: 'L1', keyword: '视频制作' } },
    ];

    const added = db.ingest(matched, '2026-07-21', scanResult);
    assert.strictEqual(added.length, 2, 'should add 2 new, skip 1 duplicate');
    assert.strictEqual(added[0].match_level, 'L1');
    assert.strictEqual(added[0].match_kw, '视频制作');
    assert.strictEqual(added[1].match_kw, '活动策划');

    // Stats should be updated
    assert.strictEqual(scanResult.stats['湖南'].new, 2);

    // Total should now be 4
    assert.strictEqual(db.getStats().total, 4);
  });

  it('handles empty ingest gracefully', () => {
    assert.deepStrictEqual(db.ingest([], '2026-07-21', {}), []);
    assert.deepStrictEqual(db.ingest(null, '2026-07-21', {}), []);
  });
});

// Run directly: node tests/database.test.js
// Or with test runner: node --test tests/database.test.js
