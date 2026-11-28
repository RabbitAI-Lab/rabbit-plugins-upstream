#!/usr/bin/env node
/**
 * Validate a site built with the tracklane Skill.
 *
 *   node scripts/validate-template.mjs path/to/index.html               # your site (default)
 *   node scripts/validate-template.mjs path/to/index.html --files       # deployed site with images/, fonts/ beside it
 *   node scripts/validate-template.mjs references/template.html --template
 *   node scripts/validate-template.mjs path/to/store-demo.html --demo
 *   node scripts/validate-template.mjs path/to/project-dir              # framework port
 *
 * Modes
 *   (default)   A finished single-file site for a real brief. Strict: zero
 *               remote requests, every image and font inlined as a data URI
 *               (build it with scripts/inline-assets.mjs), size budget, and
 *               it FAILS when the template's sample identity is still in the
 *               page (brand, domain, sample customers, sample people, address,
 *               sample route slug). Case-insensitive; comments count.
 *   --files     Like the default, for a deployed site that keeps its own
 *               images/, fonts/ or assets/ files beside the page: those local
 *               references must exist; remote hosts (including font CDNs)
 *               still fail; sample leftovers still fail; size is not checked.
 *   --template  references/template.html itself: local images/ references and
 *               the fontsource CDN woff2 files inside @font-face src are
 *               allowed. Sample identity is expected here.
 *   --demo      The fictional store demo: strict like the default, but the
 *               sample identity is allowed because the demo is the sample.
 *   directory   Framework ports: walks source files for emoji, remote
 *               resources, missing /images/ files and sample leftovers.
 *
 * Options
 *   --brand <Name>   also fail on this extra string (e.g. a previous brand of
 *                    your own after a second rebrand)
 *   --no-signature   skip the style-signature warnings after a deliberate restyle
 *
 * HTML checks (errors fail the run, warnings do not):
 *   - emoji and Unicode dingbats/arrows used as icons or decoration
 *   - external requests (CDN scripts/styles, remote fonts or images, @import)
 *   - <img> without alt; <img> without width/height or aspect-ratio (warning)
 *   - a prefers-reduced-motion block and :focus-visible styles
 *   - alert/confirm/prompt/window.open, unguarded localStorage/sessionStorage
 *   - native submit buttons inside forms (blocked in sandboxed preview frames)
 *   - em and en dashes in visible copy
 *   - landmarks (header, main, footer), skip link, labelled form controls
 *   - site structure (generic, the route names are yours): with a hash router
 *     ([data-view] views) a home view, a 404 view and at least four other
 *     views; every view has exactly one <h1>; every #/route link resolves to a
 *     ROUTES entry whose view exists; every #id link has a target; the home
 *     view has at least eight sections
 *   - local asset references exist; strict modes require them inlined
 *   - size budget for a single file (target 5 MB, hard cap 8 MB)
 *   - tracklane style signature (tokens, fonts, product hero, bento, cycles
 *     tabs, pricing switch), as warnings
 *   - sample leftovers (default, --files and directory mode)
 */
import { readdirSync, readFileSync, statSync, existsSync } from 'node:fs';
import { join, resolve, dirname, extname } from 'node:path';

const args = process.argv.slice(2);
const flag = (n) => args.includes(n);
const opt = (n) => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : null; };
const brand = opt('--brand');
const templateMode = flag('--template') || flag('--allow-replace');
const demo = flag('--demo') && !templateMode;
const files = flag('--files') && !templateMode && !demo;
const target = args.find((a, i) => !a.startsWith('--') && args[i - 1] !== '--brand');
if (!target) { console.error('Usage: node scripts/validate-template.mjs <index.html|site-dir> [--files | --template | --demo] [--brand Name] [--no-signature]'); process.exit(2); }
const root = resolve(target);
if (!existsSync(root)) { console.error(`Not found: ${root}`); process.exit(2); }

/* The template's sample identity (Tracklane, fictional; sample customer
   workspace Kestova). A buyer's site must not contain any of these; the
   template and the store demo may. Matched case-insensitively against the
   whole file, comments and attribute values included. */
const SAMPLE = {
  brand: ['Tracklane', 'tracklane.dev'],
  customers: ['Kestova', 'kestova.com', 'Vantri', 'Halcyra', 'Orrelby', 'Pellmar', 'Druvo', 'Sennet', 'Ilvara'],
  people: ['Rhea Kapoor', 'Jonas Wexler', 'Amara Diallo', 'Kenji Morita', 'Lucía Ferraro', 'Tobi Adeyemi', 'Mara Lindqvist', 'Daniel Cho', 'Noor Haddad', 'Felix Brandt', 'Ingrid Solberg', 'Owen Pryce', 'Amaya Brooks'],
  address: ['NW Couch Street', 'OR 97209'],
  slugs: ['customers/vantri'],
  firstNames: ['Rhea', 'Jonas', 'Amara', 'Kenji', 'Tobi', 'Mara', 'Noor', 'Felix', 'Lucía'],
};
const checkLeftovers = !templateMode && !demo;

const errors = [], warnings = [];
const EMOJI = /[\u{1F000}-\u{1FAFF}\u{2600}-\u{27BF}\u{2B00}-\u{2BFF}\u{2190}-\u{21FF}\u{2300}-\u{23FF}\u{25A0}-\u{25FF}\u{2700}-\u{27BF}\u{FE0F}\u{2022}\u{2026}\u{2605}\u{2713}\u{2714}\u{2717}\u{2726}]/u;
const stripData = (s) => s.replace(/data:[a-z0-9.+\/-]+;base64,[A-Za-z0-9+/=]+/gi, 'data:');
const lineOf = (text, idx) => text.slice(0, idx).split('\n').length;
const CDN_FONT = /url\(\s*(["']?)https:\/\/cdn\.jsdelivr\.net\/fontsource\/fonts\/[^)"'\s]+\.woff2\1\s*\)/g;
const normalize = (s) => s
  .replace(/&iacute;|&#237;|&#xed;/gi, 'í').replace(/&rsquo;|&#8217;|&#x2019;|’|&#39;|&apos;/g, "'").replace(/&amp;/g, '&').replace(/&nbsp;|\s+/g, ' ')
  .toLowerCase();

function leftovers(text, where) {
  const t = normalize(text);
  const found = [];
  for (const [kind, terms] of Object.entries(SAMPLE)) {
    if (kind === 'firstNames') continue;
    for (const term of terms) if (t.includes(term.toLowerCase())) found.push(`${term} (${kind})`);
  }
  if (brand && t.includes(brand.toLowerCase())) found.push(`${brand} (--brand)`);
  if (found.length) errors.push(`${where}: sample identity from the template is still in the page: ${found.join(', ')}`);
  return found.length;
}

function checkHtml(file, inDir = false) {
  const raw = readFileSync(file, 'utf8');
  const html = stripData(raw);
  const template = templateMode && !inDir;
  const strict = !template && !files && !inDir; /* everything inlined */
  const rel = file.replace(process.cwd() + '/', '');
  const scripts = [...html.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/gi)].map((m) => m[1]).join('\n');
  const markup = html.replace(/<script\b[\s\S]*?<\/script>/gi, '').replace(/<style\b[\s\S]*?<\/style>/gi, '');

  // 1. emoji / dingbats anywhere (markup, CSS content, JS strings)
  html.split('\n').forEach((line, i) => { const m = line.match(EMOJI); if (m) errors.push(`${rel}:${i + 1} emoji/dingbat ${JSON.stringify(m[0])} (use an inline SVG icon)`); });

  // 2. external requests (template mode: fontsource CDN fonts inside @font-face only)
  const net = template ? html.replace(/@font-face\s*\{[^}]*\}/g, (block) => block.replace(CDN_FONT, 'url()')) : html;
  const ext = [
    ...net.matchAll(/<(?:script|img|source|video|audio|iframe)\b[^>]*\ssrc=["'](https?:)?\/\/[^"']+/gi),
    ...net.matchAll(/<link\b[^>]*href=["'](https?:)?\/\/[^"']+["'][^>]*>/gi),
    ...net.matchAll(/url\(\s*["']?(https?:)?\/\/[^)"']+/gi),
    ...net.matchAll(/@import\s+(url\()?["']?(https?:)?\/\//gi),
  ];
  for (const m of ext) {
    if (/<link\b/i.test(m[0]) && !/rel=["'](stylesheet|preload|icon|modulepreload|preconnect|dns-prefetch)/i.test(m[0])) continue;
    const inFontFace = /@font-face\s*\{[^}]*$/.test(net.slice(Math.max(0, m.index - 600), m.index));
    const hint = !inFontFace ? '' : template
      ? ' (only https://cdn.jsdelivr.net/fontsource/fonts/...woff2 is allowed in @font-face)'
      : files ? ' (download the woff2 into fonts/ beside the page and point src at it)'
      : inDir ? ' (use the @fontsource-variable packages or next/font)'
      : ' (build with scripts/inline-assets.mjs, which embeds the fontsource woff2 files)';
    errors.push(`${rel}:${lineOf(net, m.index)} external request ${m[0].slice(0, 90)}${hint}`);
  }

  // 3. images
  for (const m of html.matchAll(/<img\b[^>]*>/gi)) {
    const tag = m[0];
    if (!/\salt=/.test(tag)) errors.push(`${rel}:${lineOf(html, m.index)} <img> without alt`);
    if (!/\swidth=/.test(tag) && !/aspect-ratio/.test(tag)) warnings.push(`${rel}:${lineOf(html, m.index)} <img> without width/height`);
  }

  // 4. motion + focus
  if (!/prefers-reduced-motion\s*:\s*reduce/.test(html)) errors.push(`${rel} has no @media (prefers-reduced-motion: reduce) block`);
  if (!/:focus-visible/.test(html)) errors.push(`${rel} has no :focus-visible styles`);

  // 5. sandbox-hostile APIs
  for (const api of ['alert(', 'confirm(', 'prompt(', 'window.open(']) {
    if (new RegExp('(^|[^.\\w])' + api.replace(/[.(]/g, '\\$&')).test(scripts)) errors.push(`${rel} calls ${api.slice(0, -1)}() (blocked in sandboxed previews)`);
  }
  for (const m of scripts.matchAll(/\b(localStorage|sessionStorage)\b/g)) {
    const before = scripts.slice(Math.max(0, m.index - 120), m.index);
    if (!/try\s*\{[^}]*$/.test(before)) errors.push(`${rel} ${m[1]} access outside try/catch`);
  }

  // 6. native submit buttons
  for (const f of html.matchAll(/<form\b[\s\S]*?<\/form>/gi)) {
    const bad = f[0].match(/<button\b(?![^>]*type=["'](button|reset)["'])[^>]*>|<input\b[^>]*type=["']submit["'][^>]*>/i);
    if (bad) errors.push(`${rel}:${lineOf(html, f.index)} native submit control in a form (use type="button" + a click/Enter handler)`);
  }

  // 7. dashes in visible copy
  const visible = markup.replace(/<!--[\s\S]*?-->/g, '').replace(/<[^>]+>/g, ' ');
  const dash = visible.match(/[–—]|&mdash;|&ndash;/g);
  if (dash) errors.push(`${rel} contains ${dash.length} em/en dash(es) in visible copy (use a hyphen, comma or period)`);
  const jsDash = scripts.match(/[–—]/g);
  if (jsDash) warnings.push(`${rel} has ${jsDash.length} em/en dash(es) inside scripts (check rendered strings)`);
  if (/lorem ipsum|dolor sit amet/i.test(visible)) errors.push(`${rel} contains lorem ipsum copy`);
  if (/\b(John|Jane) Doe\b|\bYour Company\b|\bACME\b|\bAcme\b/.test(visible)) errors.push(`${rel} contains generic placeholder names (Acme, Your Company, John/Jane Doe)`);

  // 8. landmarks, skip link, labelled controls
  if (!inDir) {
    for (const tag of ['header', 'main', 'footer']) if (!new RegExp(`<${tag}\\b`).test(markup)) errors.push(`${rel} has no <${tag}> landmark`);
    if (!/class="skip"/.test(markup)) warnings.push(`${rel} has no skip link (class="skip")`);
  }
  for (const m of markup.matchAll(/<(input|select|textarea)\b([^>]*)>/gi)) {
    const attrs = m[2];
    if (/type\s*=\s*["'](hidden|radio|checkbox|button|submit|reset)["']/.test(attrs)) continue;
    if (/aria-label(ledby)?\s*=/.test(attrs)) continue;
    const id = (attrs.match(/\bid\s*=\s*["']([^"']+)["']/) || [])[1];
    if (!id || !new RegExp(`for\\s*=\\s*["']${id}["']`).test(markup)) errors.push(`${rel}:${lineOf(markup, m.index)} form control without a <label for> or aria-label: ${m[0].slice(0, 70)}`);
  }

  // 9. site structure: views, h1, routes and in-page links (names are yours)
  const views = [...html.matchAll(/<(div|section|main)\b[^>]*data-view=["']([^"']+)["'][^>]*>/gi)];
  const viewNames = new Set(views.map((v) => v[2]));
  if (views.length) {
    views.forEach((v, i) => {
      const end = i + 1 < views.length ? views[i + 1].index : html.length;
      const n = (html.slice(v.index, end).match(/<h1\b/gi) || []).length;
      if (n !== 1) errors.push(`${rel} view "${v[2]}" has ${n} <h1> (expected 1)`);
    });
    if (!viewNames.has('home')) errors.push(`${rel} has no data-view="home"`);
    if (!viewNames.has('404')) errors.push(`${rel} has no data-view="404" (unknown routes must land on a not-found view)`);
    const others = [...viewNames].filter((n) => n !== 'home' && n !== '404');
    if (others.length < 4) errors.push(`${rel} has ${others.length} views besides home and 404 (expected at least 4: e.g. pricing, sign-in or sign-up, security or company, legal)`);
    const homeIdx = views.findIndex((v) => v[2] === 'home');
    if (homeIdx >= 0) {
      const homeEnd = homeIdx + 1 < views.length ? views[homeIdx + 1].index : html.length;
      const sections = (html.slice(views[homeIdx].index, homeEnd).match(/<section\b/gi) || []).length;
      if (sections < 8) errors.push(`${rel} home view has ${sections} <section> elements (expected at least 8 layout families)`);
    }
    const routesSrc = (scripts.match(/\bROUTES\s*=\s*\{([\s\S]*?)\}/) || [])[1];
    const routes = new Map();
    if (routesSrc) for (const m of routesSrc.matchAll(/['"]([^'"]*)['"]\s*:\s*['"]([^'"]+)['"]/g)) routes.set(m[1], m[2]);
    if (!routesSrc) warnings.push(`${rel} has views but no ROUTES object: route links were not checked`);
    for (const [path, view] of routes) if (!viewNames.has(view)) errors.push(`${rel} ROUTES maps "${path}" to missing view "${view}"`);
    const ids = new Set([...html.matchAll(/\sid=["']([^"']+)["']/g)].map((m) => m[1]));
    const seen = new Set();
    for (const m of markup.matchAll(/<a\b[^>]*\shref=["']#([^"']*)["']/gi)) {
      const h = m[1];
      if (!h || seen.has(h)) continue; seen.add(h);
      if (h.startsWith('/')) { if (routesSrc && !routes.has(h.replace(/\/+$/, '') || '/')) errors.push(`${rel} link "#${h}" has no ROUTES entry (it would show the 404 view)`); }
      else if (!ids.has(h)) errors.push(`${rel} link "#${h}" has no element with id="${h}"`);
    }
  } else {
    const n = (html.match(/<h1\b/gi) || []).length;
    if (n !== 1) errors.push(`${rel} has ${n} <h1> (expected 1)`);
  }

  // 10. local assets
  const refs = [...new Set([...raw.matchAll(/["'(]((?:\.\/)?(?:images|fonts|assets)\/[A-Za-z0-9._\/-]+\.(?:webp|png|jpe?g|svg|avif|woff2?|mp4))["')]/g)].map((m) => m[1]))];
  if (strict) { if (refs.length) errors.push(`${rel} still references ${refs.length} local asset(s), e.g. ${refs[0]} (build with scripts/inline-assets.mjs, or validate a deployed site with --files)`); }
  else for (const r of refs) if (!existsSync(join(dirname(file), r))) errors.push(`${rel} references missing asset ${r}`);

  if (strict) {
    const mb = statSync(file).size / 1048576;
    if (mb > 8) errors.push(`${rel} is ${mb.toFixed(2)} MB (hard cap 8 MB; inline-assets.mjs embeds each repeated image once)`);
    else if (mb > 5) warnings.push(`${rel} is ${mb.toFixed(2)} MB (target 5 MB)`);
  }

  // 11. style signature
  if (!flag('--no-signature')) {
    const sig = [
      [/--bg:\s*#F5F2EC/i, 'warm sand ground token --bg'],
      [/--mint:\s*#/i, 'mint band token --mint'],
      [/font-family:\s*"Inter Tight"/i, 'Inter Tight display face'],
      [/letter-spacing:\s*-\.0[3-5]\d*em/, 'tracking-tight display headlines'],
      [/class="app"/, 'product window hero (.app)'],
      [/role="tablist"[^>]*aria-label="Product views"/, 'hero view tabs (three product views)'],
      [/class="bento"/, 'workspace bento'],
      [/class="ctabs/, 'tabbed cycles section'],
      [/data-billing=/, 'pricing billing switch'],
      [/class="marquee/, 'customer wordmark marquee'],
    ];
    for (const [re, what] of sig) if (!re.test(raw)) warnings.push(`${rel} style signature missing: ${what}`);
  }

  // 12. sample leftovers (a buyer's page must not ship the template's identity)
  if (checkLeftovers) {
    leftovers(html, rel);
    for (const n of SAMPLE.firstNames) if (new RegExp(`(^|[^\\p{L}])${n}([^\\p{L}]|$)`, 'u').test(visible)) warnings.push(`${rel} sample first name "${n}" appears: confirm it is a real person from this brief`);
    const placeholder = [...new Set(html.match(/\b[a-z0-9-]+(?:\.[a-z0-9-]+)*\.example\b/gi) || [])];
    if (placeholder.length) warnings.push(`${rel} placeholder domain(s) ${placeholder.join(', ')}: list them for the buyer to replace with the real domain`);
  }
  return 1;
}

function checkDir(dir) {
  const SRC = /\.(tsx?|jsx?|mjs|css|html|md|mdx|json|astro|svelte|vue|svg)$/;
  let n = 0;
  (function walk(d) {
    for (const name of readdirSync(d)) {
      if (name === 'node_modules' || name.startsWith('.') || name === 'dist' || name === 'build' || /^package-lock\.json$|^pnpm-lock|^yarn\.lock$/.test(name)) continue;
      const p = join(d, name);
      if (statSync(p).isDirectory()) { walk(p); continue; }
      if (checkLeftovers && /tracklane|kestova|vantri/i.test(name)) errors.push(`${p}: file name still carries the sample identity`);
      if (extname(p) === '.html') { checkHtml(p, true); n++; continue; }
      if (!SRC.test(p)) continue;
      n++;
      const text = readFileSync(p, 'utf8');
      text.split('\n').forEach((line, i) => {
        const m = line.match(EMOJI); if (m) errors.push(`${p}:${i + 1} emoji/dingbat ${JSON.stringify(m[0])}`);
        if (/(src|href)=["']https?:\/\/[^"']+\.(js|css|woff2?)/.test(line) || /url\(\s*["']?https?:\/\/[^)"']+\.woff2?/.test(line) || /fonts\.googleapis\.com/.test(line)) errors.push(`${p}:${i + 1} external resource`);
      });
      if (checkLeftovers) leftovers(text, p);
      for (const m of text.matchAll(/['"(](\/(?:images|fonts|favicon)\/[^'")\s]+\.(?:webp|svg|png|jpe?g|ico|woff2))['")]/g)) {
        if (!existsSync(join(dir, 'public', m[1]))) errors.push(`${p} references missing asset ${m[1]}`);
      }
    }
  })(dir);
  return n;
}

const isDir = statSync(root).isDirectory();
const count = isDir ? checkDir(root) : checkHtml(root);
const mode = isDir ? 'directory mode' : templateMode ? 'template mode' : demo ? 'demo mode' : files ? 'site mode, local files' : 'site mode';
for (const w of warnings) console.warn('WARN ' + w);
if (errors.length) {
  console.error(`FAIL ${errors.length} issue(s) [${mode}]:`);
  for (const e of errors.slice(0, 80)) console.error('  - ' + e);
  process.exit(1);
}
console.log(`PASS ${count} file(s) checked in ${root} (${mode})${warnings.length ? ` (${warnings.length} warning(s))` : ''}`);
