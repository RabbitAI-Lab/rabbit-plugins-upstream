#!/usr/bin/env node
// Validate a single-file Mint Noir site: icons, palette, self-containment, pages and slots.
// Usage: node scripts/validate-site.mjs <file.html> [--allow-network]
import { readFileSync } from 'node:fs';

const file = process.argv[2];
if (!file) {
  console.error('Usage: node scripts/validate-site.mjs <file.html> [--allow-network]');
  process.exit(2);
}
const allowNetwork = process.argv.includes('--allow-network');
const html = readFileSync(file, 'utf8');
const text = html.replace(/data:[^"')\s]+/g, '');
const errors = [];
const warn = [];

// 1. No emoji or dingbats used as icons.
const emoji = text.match(/[\u{1F000}-\u{1FAFF}\u{2600}-\u{27BF}\u{2B00}-\u{2BFF}\u{2190}-\u{21FF}\u{25A0}-\u{25FF}\u{2700}-\u{27BF}\u{2318}]/gu);
if (emoji) errors.push(`emoji or dingbat characters found: ${[...new Set(emoji)].join(' ')}`);

// 2. No purple / violet.
const hexes = text.match(/#[0-9a-fA-F]{6}\b/g) || [];
for (const hex of new Set(hexes)) {
  const r = parseInt(hex.slice(1, 3), 16), g = parseInt(hex.slice(3, 5), 16), b = parseInt(hex.slice(5, 7), 16);
  const max = Math.max(r, g, b), min = Math.min(r, g, b);
  if (max - min < 40) continue;
  let h = 0;
  if (max === r) h = ((g - b) / (max - min)) * 60;
  else if (max === g) h = (2 + (b - r) / (max - min)) * 60;
  else h = (4 + (r - g) / (max - min)) * 60;
  if (h < 0) h += 360;
  if (h >= 255 && h <= 320) errors.push(`purple/violet colour ${hex}`);
}
if (/\b(purple|violet|indigo|fuchsia)\b/i.test(text.replace(/<symbol[\s\S]*?<\/symbol>/g, ''))) warn.push('colour keyword purple/violet/indigo/fuchsia present');

// 3. Self-contained unless explicitly allowed.
if (!allowNetwork) {
  const ext = text.match(/(?:src|href)\s*=\s*["']https?:\/\/[^"']+/g) || [];
  const cssExt = text.match(/url\(\s*["']?https?:\/\/[^)]+\)/g) || [];
  if (ext.length || cssExt.length) errors.push(`external requests: ${[...ext, ...cssExt].slice(0, 5).join(', ')}`);
  if (/\bfetch\s*\(|XMLHttpRequest|localStorage|sessionStorage|\balert\s*\(/.test(text)) errors.push('network, storage or alert() calls found');
}

// 4. Required pages and shared chrome.
for (const id of ['home', 'pricing', 'resources', 'events', 'changelog']) {
  if (!new RegExp(`data-page=["']${id}["']`).test(html)) warn.push(`page "${id}" missing (fine only if the user dropped it)`);
}
if (!/class=["'][^"']*\bnav\b/.test(html)) errors.push('shared nav missing');
if (!/<footer/.test(html)) errors.push('footer missing');
if (!/#6ee7c8/i.test(html)) errors.push('mint accent #6ee7c8 missing');
if (!/class=["'][^"']*\bserif\b/.test(html)) errors.push('no serif accent word found');

// 5. Unfilled template slots.
const slots = html.match(/<!--\s*REPLACE:[^>]*-->/g);
if (slots) warn.push(`${slots.length} REPLACE slots still present`);

// 6. Images: alt attribute present.
const imgs = html.match(/<img\b[^>]*>/g) || [];
const noAlt = imgs.filter((t) => !/\balt=/.test(t));
if (noAlt.length) errors.push(`${noAlt.length} <img> without alt`);

for (const w of warn) console.log(`WARN  ${w}`);
for (const e of errors) console.log(`FAIL  ${e}`);
if (errors.length) process.exit(1);
console.log(`PASS  ${file}`);
