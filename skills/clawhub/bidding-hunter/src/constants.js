#!/usr/bin/env node
/**
 * constants.js — Shared constants for Bidding Hunter.
 *
 * Centralizes status labels, bid progress states, and other
 * configurable-but-stable values to avoid magic strings.
 */

// Top-level entry statuses
const ENTRY_STATUS = {
  UNDECIDED: 'undecided',
  TRACKED: 'tracked',
  DISCARDED: 'discarded',
};

// Bid progress states (ordered lifecycle)
const BID_STATUS = {
  WATCHING: 'watching',
  DOCS_PURCHASED: 'docs_purchased',
  DOCS_PREPARED: 'docs_prepared',
  SUBMITTED: 'submitted',
  OPENED: 'opened',
  WON: 'won',
  LOST: 'lost',
};

// Bid statuses that are considered "active" (pre-submission)
const ACTIVE_BID_STATUSES = new Set([
  BID_STATUS.WATCHING,
  BID_STATUS.DOCS_PURCHASED,
  BID_STATUS.DOCS_PREPARED,
]);

// Default status labels (localizable)
const DEFAULT_STATUS_LABELS = {
  undecided: '待定',
  tracked: '关注',
  discarded: '放弃',
  watching: '仅关注',
  docs_purchased: '已购标书',
  docs_prepared: '已制作文件',
  submitted: '已投标',
  opened: '已开标',
  won: '中标',
  lost: '未中标',
};

// Blacklist defaults (commonly filtered terms in Chinese procurement)
const DEFAULT_BLACKLIST = [
  '中标', '成交', '废标', '更正', '变更',
  '流标', '终止', '异常', '合同',
];

// Retry configuration defaults
const DEFAULT_RETRY_STAIRS = [
  { timeout: 30000, waitUntil: 'domcontentloaded' },
  { timeout: 45000, waitUntil: 'domcontentloaded' },
  { timeout: 60000, waitUntil: 'networkidle' },
];

// Default scan limits
const DEFAULT_MAX_PAGES = 15;
const DEFAULT_DATE_WINDOW = 2;
const DEFAULT_CONCURRENCY = 3;

module.exports = {
  ENTRY_STATUS,
  BID_STATUS,
  ACTIVE_BID_STATUSES,
  DEFAULT_STATUS_LABELS,
  DEFAULT_BLACKLIST,
  DEFAULT_RETRY_STAIRS,
  DEFAULT_MAX_PAGES,
  DEFAULT_DATE_WINDOW,
  DEFAULT_CONCURRENCY,
};
