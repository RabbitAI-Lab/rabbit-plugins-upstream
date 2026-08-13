#!/usr/bin/env node
/**
 * matcher.test.js — Tests for the keyword matching engine.
 */

const { describe, it } = require('node:test');
const assert = require('node:assert');
const { matchTitle, matchAll, isBlacklisted, normalizeTitle, quickMatch } = require('../src/matcher');

// Test fixture: typical config
const FIXTURE_CONFIG = {
  tiers: {
    high: { label: 'L1', keywords: ['视频制作', '宣传视频', '宣传片', '动画制作'] },
    medium: { label: 'L2', keywords: ['会务执行', '会议服务', '活动策划'] },
    low: { label: 'L3', keywords: ['文化传媒', '拍摄制作', '后期制作'] },
  },
  blacklist: ['中标', '成交', '废标', '更正', '变更'],
  case_sensitive: false,
};

describe('matchTitle', () => {
  it('matches high-priority keyword', () => {
    const result = matchTitle('工伤预防宣传推广和宣传视频制作项目招标公告', FIXTURE_CONFIG);
    assert.ok(result);
    assert.strictEqual(result.level, 'L1');
    assert.strictEqual(result.keyword, '视频制作');
  });

  it('matches medium-priority keyword', () => {
    const result = matchTitle('青岛即墨街道回迁活动策划执行服务项目公开招标公告', FIXTURE_CONFIG);
    assert.ok(result);
    assert.strictEqual(result.level, 'L2');
    assert.strictEqual(result.keyword, '活动策划');
  });

  it('matches low-priority keyword', () => {
    const result = matchTitle('2026年视频拍摄制作服务项目比选公告', FIXTURE_CONFIG);
    assert.ok(result);
    assert.strictEqual(result.level, 'L3');
    assert.strictEqual(result.keyword, '拍摄制作');
  });

  it('returns null for non-matching title', () => {
    const result = matchTitle('某市道路建设工程施工招标公告', FIXTURE_CONFIG);
    assert.strictEqual(result, null);
  });

  it('returns null for blacklisted title', () => {
    const result = matchTitle('工伤预防宣传视频制作项目中标公告', FIXTURE_CONFIG);
    assert.strictEqual(result, null);
  });

  it('returns null for title containing 废标', () => {
    const result = matchTitle('视频制作项目废标公告', FIXTURE_CONFIG);
    assert.strictEqual(result, null);
  });

  it('returns null for title containing 更正', () => {
    const result = matchTitle('活动策划服务更正公告', FIXTURE_CONFIG);
    assert.strictEqual(result, null);
  });

  it('is case-insensitive by default', () => {
    const result = matchTitle('视频制作项目招标公告'.toUpperCase(), FIXTURE_CONFIG);
    assert.ok(result);
    assert.strictEqual(result.keyword, '视频制作');
  });

  it('handles empty title gracefully', () => {
    assert.strictEqual(matchTitle('', FIXTURE_CONFIG), null);
    assert.strictEqual(matchTitle(null, FIXTURE_CONFIG), null);
  });

  it('handles empty config gracefully', () => {
    assert.strictEqual(matchTitle('视频制作项目', null), null);
    assert.strictEqual(matchTitle('视频制作项目', {}), null);
  });

  it('first-matching tier wins (L1 before L2 before L3)', () => {
    // Title contains both "视频制作" (L1) and "活动策划" (L2)
    // L1 should win
    const result = matchTitle('视频制作和活动策划服务招标公告', FIXTURE_CONFIG);
    assert.ok(result);
    assert.strictEqual(result.level, 'L1');
  });

  it('respects case-sensitive mode', () => {
    const sensitiveConfig = {
      tiers: { high: { label: 'L1', keywords: ['Video Production'] } },
      blacklist: [],
      case_sensitive: true,
    };
    assert.ok(matchTitle('Video Production Project Bid', sensitiveConfig));
    assert.strictEqual(matchTitle('video production project bid', sensitiveConfig), null);
  });
});

describe('matchAll', () => {
  it('filters and annotates all items', () => {
    const items = [
      { title: '视频制作项目招标公告', url: 'http://a.com/1', date: '2026-07-01' },
      { title: '道路工程招标公告', url: 'http://a.com/2', date: '2026-07-01' },
      { title: '活动策划服务公告', url: 'http://a.com/3', date: '2026-07-01' },
      { title: '视频制作项目中标公告', url: 'http://a.com/4', date: '2026-07-01' },
      { title: '拍摄制作服务比选公告', url: 'http://a.com/5', date: '2026-07-01' },
    ];

    const matched = matchAll(items, FIXTURE_CONFIG);
    assert.strictEqual(matched.length, 3); // #1, #3, #5; #2 no match; #4 blacklisted
    assert.strictEqual(matched[0].match.level, 'L1');
    assert.strictEqual(matched[1].match.level, 'L2');
    assert.strictEqual(matched[2].match.level, 'L3');
  });

  it('returns empty array for empty input', () => {
    assert.deepStrictEqual(matchAll([], FIXTURE_CONFIG), []);
    assert.deepStrictEqual(matchAll(null, FIXTURE_CONFIG), []);
  });
});

describe('isBlacklisted', () => {
  it('detects blacklisted words', () => {
    assert.ok(isBlacklisted('视频制作项目中标公告', ['中标', '成交']));
    assert.ok(isBlacklisted('成交结果公示', ['中标', '成交']));
    assert.ok(!isBlacklisted('视频制作项目招标公告', ['中标', '成交']));
  });

  it('handles case-insensitive', () => {
    assert.ok(isBlacklisted('视频制作项目中标公告'.toUpperCase(), ['中标']));
  });
});

describe('normalizeTitle', () => {
  it('collapses whitespace', () => {
    assert.strictEqual(
      normalizeTitle('  工伤预防  宣传视频   制作 项目  '),
      '工伤预防 宣传视频 制作 项目'
    );
  });

  it('handles empty/undefined', () => {
    assert.strictEqual(normalizeTitle(''), '');
    assert.strictEqual(normalizeTitle(null), '');
  });
});

describe('quickMatch', () => {
  it('finds first matching keyword', () => {
    assert.strictEqual(quickMatch('视频制作项目', ['视频制作', '宣传视频']), '视频制作');
    assert.strictEqual(quickMatch('宣传视频项目', ['视频制作', '宣传视频']), '宣传视频');
    assert.strictEqual(quickMatch('道路工程', ['视频制作', '宣传视频']), null);
  });
});

// Run directly: node tests/matcher.test.js
// Or with test runner: node --test tests/matcher.test.js
