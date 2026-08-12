#!/usr/bin/env node
/**
 * reminder.js — Reminder / alert engine for Bidding Hunter.
 *
 * Scans tracked entries for upcoming deadlines, awaiting results,
 * and entries missing key dates.
 */

const { ENTRY_STATUS, BID_STATUS, ACTIVE_BID_STATUSES } = require('./constants');

/**
 * Build reminder lists from the database.
 * @param {object} db - Database wrapper
 * @param {object} config - Full config
 * @param {string} today - Current date YYYY-MM-DD
 * @returns {{ urgent: Array, openResults: Array, missingDates: Array, semanticQueue: Array }}
 */
function build(db, config, today) {
  const urgentDays = config.reminders?.urgent_days || 7;
  const includeYesterday = config.reminders?.include_yesterday !== false;
  const minDays = includeYesterday ? -1 : 0;

  const entries = db.getTrackedEntries();
  const urgent = [];
  const openResults = [];
  const missingDates = [];
  const semanticQueue = [];

  const activeBidStatuses = ACTIVE_BID_STATUSES;

  for (const entry of entries) {
    const submitDate = entry.bid_submit || entry.deadlines?.bid_submit?.date;
    const openDate = entry.bid_open || entry.deadlines?.bid_open?.date;

    // Urgent: deadline approaching
    if (activeBidStatuses.has(entry.bid_status) && submitDate) {
      const days = daysBetween(today, submitDate);
      if (days >= minDays && days <= urgentDays) {
        urgent.push({ entry: decorateEntry(entry), days });
      }
    }

    // Open results: recently opened, awaiting results
    if (entry.bid_status === BID_STATUS.SUBMITTED && openDate) {
      const days = daysBetween(openDate, today);
      if (days >= 0 && days <= 1) {
        openResults.push({ entry: decorateEntry(entry), days });
      }
      if (days >= 0 && entry.result_won === null) {
        semanticQueue.push({
          alias: entry.alias,
          title: entry.title,
          site: entry.site,
          url: entry.url,
          bid_open: openDate,
        });
      }
    }

    // Missing dates: tracking but no deadline info
    if (entry.bid_status === BID_STATUS.WATCHING && !submitDate && !openDate) {
      const firstSeenAge = daysBetween(entry.first_seen, today);
      if (firstSeenAge > 1) {
        missingDates.push(decorateEntry(entry));
      }
    }
  }

  // Sort urgent by deadline (closest first)
  urgent.sort((a, b) => {
    const dA = a.entry.bid_submit || a.entry.deadlines?.bid_submit?.date || '';
    const dB = b.entry.bid_submit || b.entry.deadlines?.bid_submit?.date || '';
    return dA.localeCompare(dB);
  });

  return { urgent, openResults, missingDates, semanticQueue };
}

/**
 * Decorate entry with flat fields for easier access in templates.
 */
function decorateEntry(entry) {
  return {
    ...entry,
    deadlines: entry.deadlines || {
      ...(entry.bid_submit ? { bid_submit: { date: entry.bid_submit } } : {}),
      ...(entry.bid_open ? { bid_open: { date: entry.bid_open } } : {}),
    },
  };
}

/**
 * Calculate days between two date strings (YYYY-MM-DD).
 */
function daysBetween(from, to) {
  if (!from || !to) return Infinity;
  const a = new Date(`${from}T00:00:00`);
  const b = new Date(`${to}T00:00:00`);
  return Math.round((b.getTime() - a.getTime()) / 86400000);
}

module.exports = { build, daysBetween };
