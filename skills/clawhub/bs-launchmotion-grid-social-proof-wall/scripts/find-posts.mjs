#!/usr/bin/env node
// Find public social posts that mention a product, for the user to confirm before recording.
// Usage: node scripts/find-posts.mjs --product "Name" [--keywords "extra words"] [--platforms tiktok,instagram,threads,x,youtube]
//        [--max 24] [--out posts.json]
// Searches each platform through DuckDuckGo (site: queries) and YouTube Shorts search in a headless
// Chrome. Results are candidates only: open or probe each one before it goes on the wall.
import fs from 'node:fs';
import { openBrowser, args, platformOf } from './lib/browser.mjs';

const opt = args(process.argv.slice(2));
if (!opt.product) {
  console.error('Usage: node scripts/find-posts.mjs --product "Name" [--keywords "..."] [--platforms tiktok,instagram,threads,x,youtube] [--max 24] [--out posts.json]');
  process.exit(1);
}
const product = opt.product.trim();
const platforms = (opt.platforms || 'tiktok,instagram,threads,x,youtube').split(',').map((s) => s.trim());
const max = Number(opt.max || 24);
const SITES = {
  tiktok: 'tiktok.com',
  instagram: 'instagram.com',
  threads: 'threads.com',
  x: 'x.com',
  youtube: 'youtube.com/shorts',
  linkedin: 'linkedin.com/posts',
};
const POST = /tiktok\.com\/@[^/]+\/(video|photo)\/\d+|instagram\.com\/(reel|reels|p)\/[\w-]+|threads\.(net|com)\/@[^/]+\/post\/[\w-]+|(x|twitter)\.com\/\w+\/status\/\d+|youtube\.com\/shorts\/[\w-]{6,}|linkedin\.com\/posts\/[\w-]+/;

function clean(url) {
  const u = new URL(url);
  u.search = '';
  u.hash = '';
  return u.toString().replace(/\/$/, '');
}

const { browser, page } = await openBrowser({ width: 1280, height: 900, scale: 1 });
const found = new Map();
const query = `"${product}"${opt.keywords ? ` ${opt.keywords}` : ''}`;

async function ddg(platform) {
  const q = `${query} site:${SITES[platform]}`;
  await page.goto(`https://html.duckduckgo.com/html/?q=${encodeURIComponent(q)}`, { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForTimeout(1500);
  return page.evaluate(() => [...document.querySelectorAll('.result')].map((r) => {
    const a = r.querySelector('a.result__a');
    if (!a) return null;
    let href = a.href;
    const m = href.match(/[?&]uddg=([^&]+)/);
    if (m) href = decodeURIComponent(m[1]);
    return { url: href, title: a.innerText.trim(), snippet: (r.querySelector('.result__snippet')?.innerText || '').trim() };
  }).filter(Boolean));
}

async function youtubeShorts() {
  await page.goto(`https://www.youtube.com/results?search_query=${encodeURIComponent(query)}&sp=EgIYAQ%253D%253D`, { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForTimeout(4000);
  return page.evaluate(() => [...document.querySelectorAll('a[href*="/shorts/"]')].map((a) => ({
    url: a.href,
    title: (a.getAttribute('title') || a.closest('ytm-shorts-lockup-view-model, ytd-video-renderer, ytd-reel-item-renderer')?.innerText || a.innerText || '').trim().split('\n')[0],
    snippet: '',
  })));
}

for (const platform of platforms) {
  if (!SITES[platform]) { console.error(`Skipping unknown platform "${platform}"`); continue; }
  let rows = [];
  try { rows = await ddg(platform); } catch (e) { console.error(`${platform}: search failed (${e.message.split('\n')[0]})`); }
  if (platform === 'youtube') {
    try { rows = rows.concat(await youtubeShorts()); } catch (e) { console.error(`youtube: search failed (${e.message.split('\n')[0]})`); }
  }
  let n = 0;
  for (const r of rows) {
    if (!POST.test(r.url)) continue;
    const url = clean(r.url);
    if (found.has(url)) continue;
    const text = `${r.title} ${r.snippet}`.toLowerCase();
    found.set(url, { platform: platformOf(url), url, title: r.title, snippet: r.snippet, mentions: text.includes(product.toLowerCase()) });
    n += 1;
  }
  console.error(`${platform}: ${n} post(s)`);
}
await browser.close();

const list = [...found.values()].sort((a, b) => Number(b.mentions) - Number(a.mentions)).slice(0, max);
const json = JSON.stringify(list, null, 2);
if (opt.out) fs.writeFileSync(opt.out, json + '\n');
console.log(json);
if (!list.length) {
  console.error('No posts found. Try --keywords with the product category or the site domain, or ask the user for post links.');
  process.exit(2);
}
