#!/usr/bin/env node
/**
 * PPT style catalog for the narrated report workflow.
 *
 *   node scripts/styles.mjs list   [--locale zh] [--json] [--base-url URL] [--refresh]
 *   node scripts/styles.mjs pick   [--locale zh] [--base-url URL] [--no-open] [--timeout 900]
 *   node scripts/styles.mjs choose <slug> [--locale zh] [--base-url URL]
 *   node scripts/styles.mjs prefs
 *   node scripts/styles.mjs locate <slug> [--base-url URL]
 *
 * Styles come from the public Skillry API (GET /api/public/deck-styles, no
 * sign-in). The previously chosen style is listed first. Preferences live in
 * ~/.skillry/audio-ppt/preferences.json and hold slugs only — never keys.
 * Requires Node.js 20 or newer; no packages are installed.
 */
import { spawn } from 'node:child_process';
import { createHash } from 'node:crypto';
import { existsSync, mkdirSync, readFileSync, renameSync, writeFileSync } from 'node:fs';
import { createServer } from 'node:http';
import { homedir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
const DEFAULT_BASE_URL = 'https://skillry.dev';
const STATE_DIR = join(homedir(), '.skillry', 'audio-ppt');
const PREFS_PATH = join(STATE_DIR, 'preferences.json');
const CACHE_TTL_MS = 60 * 60 * 1000;
const LOCALES = ['en', 'zh', 'zh-tw', 'ja', 'ko', 'es', 'pt-br', 'de', 'fr'];
const SKILL_PARENTS = [
  join(homedir(), '.claude', 'skills'),
  join(homedir(), '.agents', 'skills'),
  join(homedir(), '.codex', 'skills'),
  join(homedir(), '.gemini', 'config', 'skills'),
  join(process.cwd(), '.claude', 'skills'),
  join(process.cwd(), '.agents', 'skills'),
  join(process.cwd(), 'skills'),
];

const [command, ...rest] = process.argv.slice(2);
const { flags, positional } = parseArgs(rest);

try {
  if (command === 'list') await listCommand();
  else if (command === 'pick') await pickCommand();
  else if (command === 'choose') await chooseCommand();
  else if (command === 'prefs') console.log(JSON.stringify(readPrefs(), null, 2));
  else if (command === 'locate') await locateCommand();
  else fail('Usage: node styles.mjs <list|pick|choose|prefs|locate> [flags]');
} catch (error) {
  fail(error instanceof Error ? error.message : String(error));
}

// ---------------------------------------------------------------- commands

async function listCommand() {
  const catalog = await loadCatalog();
  const styles = orderStyles(catalog.styles, readPrefs());
  if (flags.json) {
    console.log(JSON.stringify({ ...catalog, styles }, null, 2));
    return;
  }
  console.log(`${styles.length} styles · ${catalog.origin} · ${catalog.locale}`);
  styles.forEach((style, index) => {
    const mark = style.lastSelected ? ' [last used]' : style.previouslySelected ? ' [used before]' : '';
    const tags = style.styleTags.map((tag) => tag.label).join(', ');
    console.log(`${String(index + 1).padStart(2)}. ${style.name} — ${style.slug} (${style.access})${mark}`);
    if (tags) console.log(`    ${tags}`);
  });
}

async function chooseCommand() {
  const slug = positional[0];
  if (!slug) fail('Usage: node styles.mjs choose <slug>');
  const catalog = await loadCatalog();
  const style = catalog.styles.find((item) => item.slug === slug);
  if (!style) fail(`Unknown style "${slug}" in ${catalog.origin}. Run "list" to see the slugs.`);
  rememberChoice(slug, catalog.locale);
  console.log(JSON.stringify(choiceResult(style, catalog), null, 2));
}

async function locateCommand() {
  const slug = positional[0];
  if (!slug || !/^[a-z0-9][a-z0-9-]*$/.test(slug)) fail('Usage: node styles.mjs locate <slug>');
  const found = SKILL_PARENTS.map((parent) => join(parent, slug)).find((dir) =>
    existsSync(join(dir, 'SKILL.md'))
  );
  const base = baseUrl();
  const suffix = base === DEFAULT_BASE_URL ? '' : ` --base-url ${base}`;
  console.log(
    JSON.stringify(
      {
        slug,
        installed: Boolean(found),
        path: found ?? null,
        installCommand: `npx skillry-cli@latest install ${slug}${suffix}`,
      },
      null,
      2
    )
  );
}

async function pickCommand() {
  // Without --locale or a saved preference the page follows the browser language.
  const followBrowser = !flags.locale && !readPrefs().preferredLocale;
  const catalog = await loadCatalog();
  const template = readFileSync(join(HERE, 'style-picker.html'), 'utf8');
  const pagePayload = (current) =>
    JSON.stringify({
      locale: current.locale,
      origin: current.origin,
      locales: LOCALES,
      followBrowser,
      styles: orderStyles(current.styles, readPrefs()),
    }).replace(/</g, '\\u003c');
  const html = template.replace('"__PICKER_DATA__"', () => pagePayload(catalog));
  const token = createHash('sha256').update(`${Math.random()}${Date.now()}`).digest('hex').slice(0, 24);
  const timeoutSeconds = Number(flags.timeout || 900);

  await new Promise((resolvePick, rejectPick) => {
    let settled = false;
    const server = createServer((request, response) => {
      const url = new URL(request.url || '/', 'http://127.0.0.1');
      if (request.method === 'GET' && url.pathname === '/' && url.searchParams.get('t') === token) {
        response.writeHead(200, {
          'Content-Type': 'text/html; charset=utf-8',
          'Cache-Control': 'no-store',
          'Content-Security-Policy':
            "default-src 'none'; img-src https: http://localhost:* http://127.0.0.1:* data:; style-src 'unsafe-inline'; script-src 'unsafe-inline'; connect-src 'self'",
        });
        response.end(html);
        return;
      }
      if (request.method === 'GET' && url.pathname === '/catalog' && url.searchParams.get('t') === token) {
        loadCatalog(url.searchParams.get('locale'))
          .then((current) => {
            response.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' });
            response.end(pagePayload(current));
          })
          .catch((error) => {
            response.writeHead(502, { 'Content-Type': 'application/json' });
            response.end(JSON.stringify({ ok: false, error: error.message }));
          });
        return;
      }
      if (request.method === 'POST' && url.pathname === '/choose' && url.searchParams.get('t') === token) {
        let body = '';
        request.on('data', (chunk) => {
          body += chunk;
          if (body.length > 4096) request.destroy();
        });
        request.on('end', () => {
          let slug = '';
          let locale = catalog.locale;
          try {
            const parsed = JSON.parse(body);
            slug = String(parsed.slug || '');
            locale = resolveLocale(parsed.locale);
          } catch {}
          loadCatalog(locale)
            .catch(() => catalog)
            .then((current) => {
              const style = current.styles.find((item) => item.slug === slug);
              if (!style) {
                response.writeHead(400, { 'Content-Type': 'application/json' });
                response.end('{"ok":false}');
                return;
              }
              rememberChoice(slug, current.locale);
              response.writeHead(200, { 'Content-Type': 'application/json' });
              response.end('{"ok":true}');
              finish(null, choiceResult(style, current));
            });
        });
        return;
      }
      response.writeHead(404);
      response.end();
    });
    const timer = setTimeout(
      () => finish(new Error(`No style was chosen within ${timeoutSeconds} seconds. Run "pick" again or use "list" + "choose".`)),
      timeoutSeconds * 1000
    );
    function finish(error, result) {
      if (settled) return;
      settled = true;
      clearTimeout(timer);
      setTimeout(() => server.close(), 300);
      if (error) rejectPick(error);
      else {
        console.log(JSON.stringify(result, null, 2));
        resolvePick();
      }
    }
    server.listen(Number(flags.port || 0), '127.0.0.1', () => {
      const { port } = server.address();
      const pageUrl = `http://127.0.0.1:${port}/?t=${token}`;
      console.error(`Style picker: ${pageUrl}`);
      if (!flags['no-open']) openBrowser(pageUrl);
    });
  });
}

// ---------------------------------------------------------------- catalog

function baseUrl() {
  const raw = String(flags['base-url'] || process.env.SKILLRY_URL || DEFAULT_BASE_URL);
  const url = new URL(raw);
  if (!['https:', 'http:'].includes(url.protocol)) fail('The base URL must be http(s).');
  if (url.protocol === 'http:' && !['localhost', '127.0.0.1'].includes(url.hostname)) {
    fail('Plain http is only accepted for localhost.');
  }
  return url.origin;
}

function resolveLocale(requested) {
  const raw = String(requested || flags.locale || readPrefs().preferredLocale || 'en')
    .toLowerCase()
    .replace(/_/g, '-');
  if (LOCALES.includes(raw)) return raw;
  if (raw.startsWith('zh')) return /-(tw|hk|mo|hant)/.test(raw) ? 'zh-tw' : 'zh';
  if (raw.startsWith('pt')) return 'pt-br';
  return LOCALES.includes(raw.split('-')[0]) ? raw.split('-')[0] : 'en';
}

async function loadCatalog(requested) {
  const base = baseUrl();
  const locale = resolveLocale(requested);
  const cachePath = join(
    STATE_DIR,
    `styles-${createHash('sha256').update(base).digest('hex').slice(0, 10)}-${locale}.json`
  );
  const cached = readJson(cachePath);
  if (!flags.refresh && cached?.fetchedAt && Date.now() - cached.fetchedAt < CACHE_TTL_MS) {
    return cached.catalog;
  }
  const url = `${base}/api/public/deck-styles?locale=${encodeURIComponent(locale)}`;
  let response;
  try {
    response = await fetch(url, { headers: { Accept: 'application/json' } });
  } catch (error) {
    if (cached?.catalog) return cached.catalog;
    throw new Error(`Could not reach ${url}: ${error.message}`);
  }
  if (!response.ok) {
    if (cached?.catalog) return cached.catalog;
    throw new Error(`${url} answered HTTP ${response.status}.`);
  }
  const catalog = await response.json();
  if (catalog?.schemaVersion !== 1 || !Array.isArray(catalog.styles)) {
    throw new Error('The style API returned an unexpected shape.');
  }
  writeJsonAtomic(cachePath, { fetchedAt: Date.now(), catalog });
  return catalog;
}

/** Last used first, then other styles used before (most often first), then the API order. */
function orderStyles(styles, prefs) {
  const recent = prefs.recentSlugs || [];
  const counts = prefs.selectionCounts || {};
  const used = styles
    .filter((style) => recent.includes(style.slug))
    .sort((a, b) => {
      if (a.slug === prefs.lastSelectedSlug) return -1;
      if (b.slug === prefs.lastSelectedSlug) return 1;
      return (counts[b.slug] || 0) - (counts[a.slug] || 0) || recent.indexOf(a.slug) - recent.indexOf(b.slug);
    });
  const others = styles.filter((style) => !recent.includes(style.slug));
  return [...used, ...others].map((style) => ({
    ...style,
    lastSelected: style.slug === prefs.lastSelectedSlug,
    previouslySelected: recent.includes(style.slug),
  }));
}

function choiceResult(style, catalog) {
  return {
    slug: style.slug,
    name: style.name,
    access: style.access,
    detailUrl: style.detailUrl,
    demoUrl: style.demoUrl,
    installCommand: style.installCommand,
    locale: catalog.locale,
    origin: catalog.origin,
  };
}

// ---------------------------------------------------------------- preferences

function readPrefs() {
  const prefs = readJson(PREFS_PATH) || {};
  return {
    lastSelectedSlug: typeof prefs.lastSelectedSlug === 'string' ? prefs.lastSelectedSlug : null,
    recentSlugs: Array.isArray(prefs.recentSlugs) ? prefs.recentSlugs.filter((s) => typeof s === 'string') : [],
    selectionCounts: prefs.selectionCounts && typeof prefs.selectionCounts === 'object' ? prefs.selectionCounts : {},
    preferredLocale: typeof prefs.preferredLocale === 'string' ? prefs.preferredLocale : null,
    updatedAt: prefs.updatedAt || null,
  };
}

function rememberChoice(slug, locale) {
  const prefs = readPrefs();
  prefs.lastSelectedSlug = slug;
  prefs.recentSlugs = [slug, ...prefs.recentSlugs.filter((item) => item !== slug)].slice(0, 12);
  prefs.selectionCounts = { ...prefs.selectionCounts, [slug]: (prefs.selectionCounts[slug] || 0) + 1 };
  prefs.preferredLocale = locale;
  prefs.updatedAt = new Date().toISOString();
  // The same file holds the voice provider and voices saved by tts.mjs; keep them.
  writeJsonAtomic(PREFS_PATH, { ...(readJson(PREFS_PATH) || {}), ...prefs });
}

// ---------------------------------------------------------------- helpers

function openBrowser(url) {
  const [cmd, args] =
    process.platform === 'darwin'
      ? ['open', [url]]
      : process.platform === 'win32'
        ? ['cmd', ['/c', 'start', '', url]]
        : ['xdg-open', [url]];
  try {
    spawn(cmd, args, { stdio: 'ignore', detached: true }).unref();
  } catch {
    console.error('Open the URL above in a browser.');
  }
}

function parseArgs(args) {
  const out = { flags: {}, positional: [] };
  for (let i = 0; i < args.length; i += 1) {
    const arg = args[i];
    if (!arg.startsWith('--')) {
      out.positional.push(arg);
      continue;
    }
    const key = arg.slice(2);
    const next = args[i + 1];
    if (next === undefined || next.startsWith('--')) out.flags[key] = true;
    else {
      out.flags[key] = next;
      i += 1;
    }
  }
  return out;
}

function readJson(path) {
  try {
    return JSON.parse(readFileSync(path, 'utf8'));
  } catch {
    return null;
  }
}

function writeJsonAtomic(path, value) {
  mkdirSync(dirname(path), { recursive: true });
  const temp = `${path}.${process.pid}.tmp`;
  writeFileSync(temp, `${JSON.stringify(value, null, 2)}\n`);
  renameSync(temp, path);
}

function fail(message) {
  console.error(message);
  process.exit(1);
}
