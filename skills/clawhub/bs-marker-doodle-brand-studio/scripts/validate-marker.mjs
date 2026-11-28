#!/usr/bin/env node
/**
 * Validate a generated page for self-containment, sandbox safety, icon
 * discipline, and multi-page routing. Usage:
 *
 *   node scripts/validate-STYLE.mjs path/to/page.html [--allow-replace]
 *
 * Pass --allow-replace only for references/template.html, whose REPLACE
 * comments mark the content slots. Exits non-zero when any check fails.
 * Checks:
 *   1. Single self-contained file: no remote resource URLs, no external scripts.
 *   2. No storage or network APIs (must run in a sandboxed iframe).
 *   3. No emoji / dingbat icons — pictorial marks must be inline SVG.
 *   4. No leftover REPLACE or {{img:…}} placeholders (strict mode).
 *   5. Hash router present; every internal "#/…" link resolves to a page
 *      section, and every page section is reachable from at least one link.
 *   6. Style-specific structure (STYLE_CHECKS below — edit per Skill).
 */
import { readFileSync, statSync } from 'node:fs';

const args = process.argv.slice(2);
const allowReplace = args.includes('--allow-replace');
const file = args.find((a) => !a.startsWith('--'));
if (!file) {
  console.error('usage: node scripts/validate-STYLE.mjs <page.html> [--allow-replace]');
  process.exit(2);
}
let html;
try { html = readFileSync(file, 'utf8'); } catch (err) { console.error(`cannot read ${file}: ${err.message}`); process.exit(2); }

const errors = [];
const warn = [];

/* 1. remote resource references are forbidden */
for (const m of html.matchAll(/(?:src|href)\s*=\s*["'](https?:\/\/[^"']+)["']/gi)) errors.push(`external reference not allowed: ${m[1]}`);
if (/url\(\s*["']?https?:\/\//i.test(html)) errors.push('CSS url() references a remote asset');
if (/@import\s+(?:url\(\s*)?["']?https?:\/\//i.test(html)) errors.push('remote CSS @import is not allowed');
// examples/demo.html must inline everything. references/template.html is
// allowed to load the ReUI runtime from the ./reui/ folder shipped beside
// it — a local sibling, not a network dependency.
for (const m of html.matchAll(/<script[^>]+src\s*=\s*["']([^"']+)["']/gi)) {
  const src = m[1];
  const localRuntime = /^\.\/reui\//.test(src);
  if (!localRuntime || !allowReplace) {
    errors.push(`external <script src> is not allowed — inline all JS (${src})`);
  }
}
for (const m of html.matchAll(/<link[^>]+href\s*=\s*["']([^"']+)["'][^>]*rel=["']stylesheet["']|<link[^>]+rel=["']stylesheet["'][^>]*href\s*=\s*["']([^"']+)["']/gi)) {
  const href = m[1] || m[2];
  if (/^https?:/i.test(href)) errors.push(`remote stylesheet is not allowed: ${href}`);
  else if (!/^\.\/reui\//.test(href) && !allowReplace) errors.push(`external stylesheet is not allowed — inline all CSS (${href})`);
}

/* 2. storage / network APIs */
for (const api of ['localStorage', 'sessionStorage', 'document.cookie', 'fetch(', 'XMLHttpRequest', 'WebSocket', 'indexedDB', 'navigator.sendBeacon', 'window.open(']) {
  if (html.includes(api)) errors.push(`forbidden API in a sandboxed demo: ${api}`);
}
if (/target\s*=\s*["']_(?:top|parent)["']/i.test(html)) errors.push('top-level navigation targets are not allowed');

/* 3. emoji / dingbat icons (inline SVG only) */
const emojiRe = /[\u{1F000}-\u{1FAFF}\u{2600}-\u{27BF}\u{2190}-\u{21FF}\u{2B00}-\u{2BFF}\u{FE0F}\u{2713}\u{2714}\u{2716}\u{25A0}-\u{25FF}\u{2605}\u{2606}\u{2731}\u{2726}\u{2727}\u{2794}\u{27A4}\u{2B95}\u{2B50}]/u;
const bodyText = html.replace(/<!--[\s\S]*?-->/g, '').replace(/<svg[\s\S]*?<\/svg>/gi, '').replace(/data:[^"')]+/g, '');
const em = bodyText.match(emojiRe);
if (em) errors.push(`emoji/dingbat character used as an icon: U+${em[0].codePointAt(0).toString(16).toUpperCase()} — replace with an inline SVG`);
if (/font-family\s*:[^;]*(font\s*awesome|material\s*icons|icomoon|ionicons)/i.test(html)) errors.push('icon fonts are not allowed');

/* 4. leftover placeholders */
if (!allowReplace && /<!--\s*REPLACE:/.test(html)) errors.push('leftover REPLACE placeholder comment');
if (/\{\{img:[A-Za-z0-9_-]+\}\}/.test(html)) errors.push('leftover {{img:…}} token — run the build step');
if (/lorem ipsum/i.test(html)) errors.push('lorem ipsum copy is not allowed');

/* 5. hash router + route integrity */
if (!/hashchange/.test(html)) errors.push('no hash router found (expected a hashchange listener)');
const pages = new Set([...html.matchAll(/data-page\s*=\s*["']([^"']+)["']/g)].map((m) => m[1]));
if (pages.size < 4) errors.push(`expected at least 4 routed pages (data-page), found ${pages.size}`);
const links = [...html.matchAll(/href\s*=\s*["']#\/([^"'#?]*)["']/g)].map((m) => m[1]);
const routeOf = (path) => path.replace(/\/$/, '');
const linked = new Set();
for (const l of links) {
  const route = routeOf(l);
  const top = route.split('/')[0];
  const candidates = [route, top, route === '' ? 'home' : route];
  if (!candidates.some((c) => pages.has(c))) errors.push(`link "#/${l}" resolves to no data-page section`);
  else for (const c of candidates) if (pages.has(c)) linked.add(c);
}
for (const p of pages) {
  if (!linked.has(p) && !html.includes(`data-route-child="${p}"`)) {
    // detail pages may be opened by JS (data-open="…") instead of a plain link
    if (!html.includes(`#/${p}`)) warn.push(`page "${p}" is never linked`);
  }
}
if (!/data-nav-toggle|aria-expanded/.test(html)) warn.push('no mobile menu toggle detected');
if (!/prefers-reduced-motion/.test(html)) warn.push('no reduced-motion media query');

/* 6. style-specific structure — EDIT PER SKILL */
const STYLE_CHECKS = [
  ['marker display font stack', /Marker Felt/],
  ['hero blob portrait (clip-path blob)', /id="blob-clip"/],
  ['hero three-line headline with red underline', /class="u-red"/],
  ['intro card with count-up stats', /class="card intro-card[\s\S]*data-count=/],
  ['four colored service cards', /(class="svc c-(blue|yellow|red)[^"]*"[\s\S]*?){4}/],
  ['blue testimonial band', /class="quotes"[\s\S]*class="qgrid"/],
  ['five-step process row', /class="steps"[\s\S]*(class="step reveal[^"]*"[\s\S]*?){5}/],
  ['red CTA band', /class="cta"[\s\S]*class="band/],
  ['black footer with sticker', /class="site-foot"[\s\S]*class="foot-sticker"/],
  ['work filters', /data-reui="toggle-group"/],
  ['FAQ accordion', /class="acc[\s\S]*data-reui="accordion"/],
];
for (const [label, re] of STYLE_CHECKS) if (!re.test(html)) errors.push(`missing structure: ${label}`);

/* size budget */
const bytes = statSync(file).size;
if (bytes > 20 * 1024 * 1024) errors.push(`file is ${(bytes / 1024 / 1024).toFixed(1)} MB (limit 20 MB)`);

for (const w of warn) console.warn(`warn: ${w}`);
if (errors.length) {
  for (const e of errors) console.error(`error: ${e}`);
  console.error(`\n${errors.length} problem(s) in ${file}`);
  process.exit(1);
}
console.log(`ok: ${file} (${pages.size} pages, ${(bytes / 1024).toFixed(0)} KB)`);
