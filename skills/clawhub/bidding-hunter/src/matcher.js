#!/usr/bin/env node
/**
 * matcher.js — Keyword matching engine for Bidding Hunter.
 *
 * Matches raw scan results against configurable keyword tiers.
 * Supports case-insensitive matching by default.
 */

/**
 * Match a single title against configured keyword tiers.
 * @param {string} title - The bid announcement title
 * @param {object} matchingConfig - The matching section from config
 * @returns {object|null} { level, keyword } or null if no match
 */
function matchTitle(title, matchingConfig) {
  if (!title || !matchingConfig) return null;

  const caseSensitive = matchingConfig.case_sensitive || false;
  const titleNorm = caseSensitive ? title : title.toLowerCase();

  // Check blacklist first
  const blacklist = matchingConfig.blacklist || [];
  for (const word of blacklist) {
    const wordNorm = caseSensitive ? word : word.toLowerCase();
    if (titleNorm.includes(wordNorm)) {
      return null; // Blacklisted — don't match
    }
  }

  // Check each tier in order
  const tiers = matchingConfig.tiers || {};
  for (const [tierKey, tier] of Object.entries(tiers)) {
    const keywords = tier.keywords || [];
    for (const keyword of keywords) {
      const kwNorm = caseSensitive ? keyword : keyword.toLowerCase();
      if (titleNorm.includes(kwNorm)) {
        return {
          level: tier.label || tierKey,
          keyword,
          tier: tierKey,
        };
      }
    }
  }

  return null;
}

/**
 * Match all items from a scan result.
 * @param {Array} items - Raw scan items with { title, url, ... }
 * @param {object} matchingConfig - The matching section from config
 * @returns {Array} Items with .match property added (or null for non-matching)
 */
function matchAll(items, matchingConfig) {
  if (!items || !items.length) return [];

  return items
    .map(item => ({
      ...item,
      match: matchTitle(item.title, matchingConfig),
    }))
    .filter(item => item.match !== null);
}

/**
 * Check if a title is blacklisted.
 * @param {string} title
 * @param {Array<string>} blacklist
 * @returns {boolean}
 */
function isBlacklisted(title, blacklist = []) {
  if (!title || !blacklist.length) return false;
  const t = title.toLowerCase();
  return blacklist.some(word => t.includes(word.toLowerCase()));
}

/**
 * Normalize a title for display (trim whitespace, collapse spaces).
 */
function normalizeTitle(title) {
  return (title || '').replace(/\s+/g, ' ').trim();
}

/**
 * Shorthand: match with a simple keywords list (no tiers).
 * Useful for quick checks.
 * @param {string} title
 * @param {string[]} keywords
 * @returns {string|null} The first matching keyword
 */
function quickMatch(title, keywords) {
  if (!title || !keywords) return null;
  const t = title.toLowerCase();
  return keywords.find(kw => t.includes(kw.toLowerCase())) || null;
}

module.exports = {
  matchTitle,
  matchAll,
  isBlacklisted,
  normalizeTitle,
  quickMatch,
};
