#!/usr/bin/env node
/**
 * setup.js - Downloads Seedance 2 prompt library from HuggingFace
 *
 * Usage:
 *   node scripts/setup.js           # Download missing files only
 *   node scripts/setup.js --force   # Force re-download (get latest)
 *   node scripts/setup.js --check   # Auto-update if stale (> 24h)
 */

import { existsSync, mkdirSync, statSync, writeFileSync, readFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const refsDir = join(__dirname, '..', 'references');
const stampFile = join(refsDir, '.last-updated');
const destFile = join(refsDir, 'metadata.jsonl');

const DATA_URL = 'https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/metadata.jsonl';
const STALE_HOURS = 24;

function isStale() {
  if (!existsSync(stampFile)) return true;
  const ts = parseInt(readFileSync(stampFile, 'utf8').trim(), 10);
  return (Date.now() - ts) / 1000 / 3600 > STALE_HOURS;
}

async function fetchText(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`HTTP ${res.status} — ${url}`);
  return res.text();
}

async function setup() {
  const args = process.argv.slice(2);
  const forceMode = args.includes('--force');
  const checkMode = args.includes('--check');

  if (checkMode && !isStale()) {
    return;
  }

  if (!existsSync(refsDir)) mkdirSync(refsDir, { recursive: true });

  const label = forceMode ? 'Updating' : 'Downloading';
  console.log(`[setup] ${label} Seedance 2 prompt library from HuggingFace...`);

  // Check if we need to download
  const needsDownload = forceMode || !existsSync(destFile) || (existsSync(destFile) && statSync(destFile).size < 100);

  if (needsDownload) {
    process.stdout.write(`  → metadata.jsonl (8,000+ prompts) ... `);
    try {
      const text = await fetchText(DATA_URL);
      writeFileSync(destFile, text, 'utf8');
      const lines = text.split('\n').filter(l => l.trim()).length;
      console.log(`✓ (${lines} prompts)`);
      writeFileSync(stampFile, String(Date.now()), 'utf8');
      console.log(`[setup] Done! Library is ready.`);
    } catch (err) {
      console.log(`✗ (${err.message})`);
      console.warn('[setup] Download failed. Check your network connection.');
      process.exit(0);
    }
  } else {
    console.log('[setup] References up to date. Use --force to refresh.');
  }
}

setup().catch(err => {
  console.warn('[setup] Warning (non-fatal):', err.message);
  process.exit(0);
});
