// Shared headless browser setup. Uses an installed Google Chrome (it plays the H.264 video that
// social platforms serve); set CHROME_PATH to point at another Chrome or Chromium build.
import fs from 'node:fs';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);

export const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36';

const CANDIDATES = [
  process.env.CHROME_PATH,
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/usr/bin/google-chrome',
  '/usr/bin/google-chrome-stable',
  '/usr/bin/chromium',
  '/usr/bin/chromium-browser',
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
].filter(Boolean);

function loadPlaywright() {
  try { return require('playwright-core'); } catch {
    console.error('playwright-core is missing. Run once: npm install --prefix <skill>/scripts');
    process.exit(1);
  }
}

export async function openBrowser({ width = 1280, height = 860, scale = 2, colorScheme = 'dark' } = {}) {
  const { chromium } = loadPlaywright();
  const executablePath = CANDIDATES.find((p) => fs.existsSync(p));
  if (!executablePath) {
    console.error('No Chrome found. Install Google Chrome or set CHROME_PATH.');
    process.exit(1);
  }
  const browser = await chromium.launch({ executablePath, headless: true, args: ['--autoplay-policy=no-user-gesture-required', '--hide-scrollbars', '--mute-audio'] });
  const context = await browser.newContext({ viewport: { width, height }, deviceScaleFactor: scale, locale: 'en-US', userAgent: UA, colorScheme });
  return { browser, context, page: await context.newPage() };
}

export function args(argv, flags = []) {
  const out = { _: [] };
  for (let i = 0; i < argv.length; i += 1) {
    const a = argv[i];
    if (!a.startsWith('--')) { out._.push(a); continue; }
    const key = a.slice(2);
    if (flags.includes(key)) { out[key] = true; continue; }
    out[key] = argv[i + 1];
    i += 1;
  }
  return out;
}

export function platformOf(url) {
  const h = new URL(url).hostname.replace(/^www\./, '');
  if (h.endsWith('tiktok.com')) return 'tiktok';
  if (h.endsWith('instagram.com')) return 'instagram';
  if (h.startsWith('threads.')) return 'threads';
  if (h === 'x.com' || h === 'twitter.com') return 'x';
  if (h.endsWith('youtube.com') || h === 'youtu.be') return 'youtube';
  if (h.endsWith('linkedin.com')) return 'linkedin';
  return 'web';
}
