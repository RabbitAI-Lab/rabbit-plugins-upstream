#!/usr/bin/env node
// grupo-venus helper: people storage, geocoding (city and country sent to
// photon.komoot.io; time zone computed locally), and cached, throttled
// access to grupovenus.com. Node.js 18+, no packages.
//
// Every grupovenus.com request goes through fetchSite(), which takes a
// directory lock (parallel invocations queue instead of running at once),
// waits PAUSE_MS since the previous request, and reads from / writes to the
// local cache. Nothing here registers people on the server.
import { chmodSync, existsSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, rmSync, statSync, utimesSync, writeFileSync } from 'node:fs';
import { homedir, tmpdir } from 'node:os';
import { dirname, join, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import { parseArgs } from 'node:util';

const SKILL = dirname(dirname(fileURLToPath(import.meta.url)));
const LEGACY = join(homedir(), '.openclaw', 'workspace', 'memory');
const HOME = process.env.GRUPO_VENUS_HOME
  ? resolve(process.env.GRUPO_VENUS_HOME.replace(/^~(?=$|\/)/, homedir()))
  : existsSync(join(LEGACY, 'grupo-venus.json')) ? LEGACY : join(homedir(), '.grupo-venus');
const PEOPLE = join(HOME, 'grupo-venus.json');
const EXPORTS = join(HOME, 'exports');
const CACHE = join(HOME, 'grupo-venus-cache');
const BASE = 'https://grupovenus.com';
const PHOTON = 'https://photon.komoot.io/api/';
const UA = 'Mozilla/5.0 (grupo-venus skill)';
const PAUSE_MS = 2000;
const TICKET = 'necesita obtener un Ticket';
const latin1 = new TextDecoder('latin1');
const sleep = ms => new Promise(r => setTimeout(r, ms));
const die = msg => { process.stderr.write(`${msg}\n`); process.exit(1); };
const out = v => process.stdout.write(typeof v === 'string' ? `${v}\n` : `${JSON.stringify(v, null, 1)}\n`);

// ---------- storage ----------

const load = () => existsSync(PEOPLE) ? JSON.parse(readFileSync(PEOPLE, 'utf8')) : { people: {} };
// Birth data is personal: keep the folder and file readable by the owner only.
const save = db => { mkdirSync(HOME, { recursive: true, mode: 0o700 }); writeFileSync(PEOPLE, JSON.stringify(db, null, 2), { mode: 0o600 }); chmodSync(PEOPLE, 0o600); };
const KEY_RE = /^[a-z0-9][a-z0-9-]{0,63}$/;
const slug = name => name.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 64).replace(/-$/, '') || 'person';

function person(key) {
  const people = load().people;
  return people[key] || die(`unknown person '${key}'. Known: ${Object.keys(people).join(', ') || 'none'}`);
}

/** The semicolon person string grupovenus.com uses everywhere. */
const line = p => [p.name, p.birthdate, p.city, p.country, p.sex, '', p.tz_offset, p.lat_dms, p.lon_dms].join(';');

// ---------- coordinates ----------

function toDms(value, pos, neg) {
  let d = Math.trunc(Math.abs(value)), m = Math.round((Math.abs(value) - d) * 60);
  if (m === 60) { d += 1; m = 0; }
  return `${d}${value >= 0 ? pos : neg}${String(m).padStart(2, '0')}`;
}

function fromDms(s) {
  const m = /^(\d+)([NSEW])(\d+)$/.exec(String(s).trim().toUpperCase());
  if (!m) throw new Error(`bad coordinate ${s}`);
  const v = +m[1] + +m[3] / 60;
  return 'SE'.includes(m[2]) ? -v : v; // grupovenus: South negative, West positive
}

const round4 = v => Math.round(v * 1e4) / 1e4;
const record = (name, birthdate, city, country, sex, tz, lat, lon, style = null) => ({
  name, birthdate, city, country, sex, tz_offset: String(tz), lat_dms: lat, lon_dms: lon,
  lat_decimal: round4(fromDms(lat)), lon_decimal: round4(fromDms(lon)), style,
});

// ---------- time zone ----------

function zones() {
  const dm = (s, w) => { const v = +s.slice(1, 1 + w) + +s.slice(1 + w, 3 + w) / 60; return s[0] === '-' ? -v : v; };
  return readFileSync(join(SKILL, 'data', 'zone.tab'), 'utf8').split('\n')
    .filter(r => r && !r.startsWith('#'))
    .map(r => {
      const [cc, coord, tz] = r.split('\t');
      const i = Math.max(coord.lastIndexOf('+'), coord.lastIndexOf('-'));
      return { cc, lat: dm(coord.slice(0, i), 2), lon: dm(coord.slice(i), 3), tz };
    });
}

/** Nearest IANA zone within the country (east-positive lon). */
function zoneFor(lat, lon, cc) {
  const all = zones(), cands = all.filter(z => z.cc === cc.toUpperCase());
  const dist = z => (z.lat - lat) ** 2 + ((z.lon - lon) * Math.cos(lat * Math.PI / 180)) ** 2;
  return (cands.length ? cands : all).reduce((a, b) => dist(a) <= dist(b) ? a : b).tz;
}

function utcOffsetMinutes(zone, utcMs) {
  const name = new Intl.DateTimeFormat('en-US', { timeZone: zone, timeZoneName: 'longOffset' })
    .formatToParts(new Date(utcMs)).find(p => p.type === 'timeZoneName').value;
  const m = /GMT([+-])(\d\d):(\d\d)/.exec(name);
  return m ? (m[1] === '-' ? -1 : 1) * (+m[2] * 60 + +m[3]) : 0;
}

/** grupovenus sign convention: hours WEST of UTC (UTC-3 -> "3"), for a local wall time. */
function serverOffset(zone, y, mo, d, h, mi) {
  const wall = Date.UTC(y, mo - 1, d, h, mi);
  let off = utcOffsetMinutes(zone, wall);
  off = utcOffsetMinutes(zone, wall - off * 60000);
  return String(-off / 60);
}

// ---------- network ----------

/** application/x-www-form-urlencoded in ISO-8859-1, which the site expects. */
function formLatin1(params) {
  const enc = s => [...String(s)].map(ch => {
    const c = ch.codePointAt(0);
    if (/[A-Za-z0-9*\-._]/.test(ch)) return ch;
    if (ch === ' ') return '+';
    return c < 256 ? `%${c.toString(16).toUpperCase().padStart(2, '0')}` : '%3F';
  }).join('');
  return Object.entries(params).map(([k, v]) => `${enc(k)}=${enc(v)}`).join('&');
}

async function httpGet(url, body) {
  const res = await fetch(url, {
    method: body ? 'POST' : 'GET', body,
    headers: { 'User-Agent': UA, ...(body ? { 'Content-Type': 'application/x-www-form-urlencoded' } : {}) },
  });
  if (!res.ok) die(`HTTP ${res.status} from ${new URL(url).host}`);
  return Buffer.from(await res.arrayBuffer());
}

async function withLock(fn) {
  const lock = join(CACHE, '.lock');
  for (;;) {
    try { mkdirSync(lock); break; } catch (e) {
      if (e.code !== 'EEXIST') throw e;
      try { if (Date.now() - statSync(lock).mtimeMs > 120000) rmSync(lock, { recursive: true, force: true }); } catch {}
      await sleep(200);
    }
  }
  try { return await fn(); } finally { rmSync(lock, { recursive: true, force: true }); }
}

/** One grupovenus.com request: cached, serialized, paced. */
async function fetchSite(path, { params, post, cacheKey }) {
  mkdirSync(CACHE, { recursive: true, mode: 0o700 });
  const file = cacheKey ? resolve(CACHE, cacheKey) : null;
  if (file && !file.startsWith(CACHE + sep)) die('refusing a cache path outside the cache folder');
  if (file && existsSync(file)) return readFileSync(file);
  return withLock(async () => {
    if (file && existsSync(file)) return readFileSync(file);
    const stamp = join(CACHE, '.last');
    const wait = PAUSE_MS - (Date.now() - (existsSync(stamp) ? statSync(stamp).mtimeMs : 0));
    if (wait > 0) await sleep(wait);
    let data;
    try {
      data = await httpGet(`${BASE}/${path}${params ? `?${formLatin1(params)}` : ''}`, post ? formLatin1(post) : undefined);
    } finally {
      writeFileSync(stamp, ''); const now = new Date(); utimesSync(stamp, now, now);
    }
    const text = latin1.decode(data);
    if (file && data.length > 1000 && !text.includes(TICKET) && !text.includes('caducado')) {
      mkdirSync(dirname(file), { recursive: true });
      writeFileSync(file, data);
    }
    return data;
  });
}

async function geocode(city, country) {
  const q = query => `${PHOTON}?${new URLSearchParams({ q: query, limit: '5', layer: 'city' })}`;
  let feats = JSON.parse(await httpGet(q(`${city}, ${country}`))).features;
  // Abbreviations like "USA" can confuse Photon; retry on the city alone.
  if (!feats.length) feats = JSON.parse(await httpGet(q(city))).features;
  if (!feats.length) die(`no city found for ${city}, ${country}`);
  const c = country.toLowerCase();
  const fits = f => (f.properties.country || '').toLowerCase().includes(c) || (f.properties.countrycode || '').toLowerCase() === c;
  return [...feats.filter(fits), ...feats.filter(f => !fits(f))];
}

// ---------- commands ----------

async function cmdAdd(o) {
  for (const k of ['name', 'date', 'time', 'city', 'country', 'sex']) if (!o[k]) die(`missing --${k}`);
  if (!['V', 'H'].includes(o.sex)) die('--sex must be V (male) or H (female)');
  const [y, mo, d] = o.date.split('-').map(Number), [h, mi] = o.time.split(':').map(Number);
  if (![y, mo, d, h, mi].every(Number.isFinite)) die('use --date YYYY-MM-DD and --time HH:MM');
  const feats = await geocode(o.city, o.country), pick = Number(o.pick || 0), f = feats[pick] || die(`no match ${pick}`);
  const [lon, lat] = f.geometry.coordinates, pr = f.properties;
  const zone = zoneFor(lat, lon, pr.countrycode || '');
  const h12 = h % 12 || 12, ampm = h < 12 ? 'AM' : 'PM';
  const birth = `${mo}/${d}/${y} ${h12}:${String(mi).padStart(2, '0')}:00 ${ampm}`;
  const p = record(o.name, birth, pr.name || o.city, o.country, o.sex, serverOffset(zone, y, mo, d, h, mi),
    toDms(lat, 'N', 'S'), toDms(-lon, 'W', 'E'), o.style || null);
  const key = o.key || slug(o.name);
  if (o.save) { const db = load(); db.people[key] = p; save(db); }
  const label = x => [x.properties.name, x.properties.state, x.properties.country].filter(Boolean).join(', ');
  out({
    saved: !!o.save, key: o.save ? key : null, sent_to: ['photon.komoot.io (city and country only)'], zone, picked: pick,
    matches: Object.fromEntries(feats.map((x, i) => [i, label(x)])), person: p, line: line(p),
    next: o.save ? `use KEY ${key}` : 'not saved: pass --line with the line above to chart/transits; nothing about this person is written to disk',
  });
}

const ENTITIES = {
  amp: '&', lt: '<', gt: '>', quot: '"', apos: "'", nbsp: ' ', deg: '°', laquo: '«', raquo: '»', iquest: '¿', iexcl: '¡', ordf: 'ª', ordm: 'º',
  ...Object.fromEntries(['aacute á', 'eacute é', 'iacute í', 'oacute ó', 'uacute ú', 'ntilde ñ', 'uuml ü']
    .flatMap(s => { const [n, c] = s.split(' '); return [[n, c], [n[0].toUpperCase() + n.slice(1), c.toUpperCase()]]; })),
};
const decodeEntities = s => s.replace(/&(#x[0-9a-f]+|#\d+|\w+);/gi, (m, e) => e[0] === '#'
  ? String.fromCodePoint(e[1].toLowerCase() === 'x' ? parseInt(e.slice(2), 16) : +e.slice(1))
  : ENTITIES[e] ?? m);

function parseList(text) {
  const m = /<textarea[^>]*>([\s\S]*?)<\/textarea>/i.exec(text);
  return decodeEntities(m ? m[1] : text).split(/\r?\n/).map(r => r.split(';').map(x => x.trim()))
    .filter(p => p.length >= 9 && p[0])
    .map(([name, bdate, city, country, sex, , tz, lat, lon]) => record(name, bdate, city, country, sex, tz, lat, lon));
}

function cmdImport(file) {
  if (!file) die('usage: import FILE');
  const raw = readFileSync(resolve(file));
  let text = new TextDecoder('utf-8', { fatal: true });
  try { text = text.decode(raw); } catch { text = latin1.decode(raw); }
  const db = load(), imported = [];
  for (const p of parseList(text)) {
    const key = slug(p.name);
    p.style = db.people[key]?.style ?? null;
    db.people[key] = p; imported.push(key);
  }
  save(db); out({ imported });
}

function cmdExport(file) {
  const people = Object.values(load().people), n = people.length;
  const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const doc = `<html><head><title>Grupo Venus - Lista de personas</title>`
    + `<meta http-equiv="Content-Type" content="text/html;charset=iso-8859-1"></head><body><center>`
    + `<form ACTION="${BASE}/perso2.asp" METHOD="POST"><input type="hidden" name="desti" value="modi">`
    + `<p>Lista de ${n} personas.</p><textarea NAME="lista" ROWS="15" COLS="84" WRAP=OFF>\r\n`
    + people.map(p => esc(line(p))).join('\r\n')
    + `\r\n</textarea><br><br>Al pulsar Modificar se reemplaza la Lista de personas guardada en este navegador. `
    + `<INPUT TYPE="submit" VALUE="Modificar" name="modif"></form></center></body></html>`;
  mkdirSync(EXPORTS, { recursive: true, mode: 0o700 });
  const target = file ? resolve(file) : join(EXPORTS, `Lista de ${n} Personas.html`);
  writeFileSync(target, Buffer.from([...doc].map(c => c.codePointAt(0) < 256 ? c.codePointAt(0) : 63)), { mode: 0o600 });
  out({ file: target, note: target.startsWith(EXPORTS + sep) ? 'inside the data folder; forget deletes it' : 'outside the data folder; forget does not delete it' });
}

/** Delete a person and every cached file made from their data. */
function cmdRemove(key, o) {
  if (!o.yes) die('remove deletes data: confirm with the user, then pass --yes');
  const db = load(); person(key); delete db.people[key]; save(db);
  let files = 0;
  for (const dir of ['chart', 'transits']) {
    const d = join(CACHE, dir);
    if (!existsSync(d)) continue;
    for (const f of readdirSync(d)) if (f.startsWith(`${key}-`)) { rmSync(join(d, f)); files++; }
  }
  out({ removed: key, cached_files_deleted: files });
}

/** Delete everything this skill stored: people and cache. */
function cmdForget(o) {
  if (!o.yes) die('forget deletes all people, the cache and exports: confirm with the user, then pass --yes');
  for (const p of [PEOPLE, CACHE, EXPORTS]) rmSync(p, { recursive: true, force: true });
  out({ deleted: [PEOPLE, CACHE, EXPORTS] });
}

function cmdStyle(key, style) {
  if (!['casual', 'deep', 'practical'].includes(style)) die('style must be casual, deep or practical');
  const db = load(); person(key); db.people[key].style = style; save(db); out('ok');
}

/** A stored person by KEY, or an unsaved one from --line (never cached to disk). */
function subject(key, o) {
  if (o.line) {
    const [p] = parseList(o.line);
    return { p: p || die('--line must be a full person line from add'), key: null };
  }
  return { p: person(key || die('give a KEY or --line')), key };
}

async function cmdChart(arg, o) {
  const { p, key } = subject(arg, o), cacheKey = key && `chart/${key}-${o.zodiac}-${o.lang}.png`;
  const data = await fetchSite('dibujo.aspx', {
    cacheKey, params: {
      fec: p.birthdate, aju: p.tz_offset, ciu: p.city, pais: p.country, lat: p.lat_decimal, lon: p.lon_decimal,
      nom: p.name, bot: 'atras', idioma: o.lang, CASASPRO: '', zodi: o.zodiac,
    },
  });
  if (!data.subarray(0, 4).equals(Buffer.from([0x89, 0x50, 0x4e, 0x47]))) die('error: not a PNG');
  if (cacheKey) return out(join(CACHE, cacheKey));
  const tmp = join(mkdtempSync(join(tmpdir(), 'grupo-venus-')), 'chart.png');
  writeFileSync(tmp, data, { mode: 0o600 });
  out({ file: tmp, note: 'temporary file for this conversation; delete it when done' });
}

async function report(nombre, rid, start, o, cacheKey) {
  const now = new Date(), pad = n => String(n).padStart(2, '0');
  const data = await fetchSite('informes3.asp', {
    cacheKey, post: {
      nombre, urldestino: 'informes3.asp', INFORMEDESEADO: rid,
      DIA1: start.getUTCDate(), MES1: start.getUTCMonth() + 1, ANO1: start.getUTCFullYear(),
      HORA1: pad(now.getHours()), MINU1: pad(now.getMinutes()), tipzod: o.zodiac, TIC: '', idiomas: o.lang,
    },
  });
  const text = latin1.decode(data);
  if (text.includes(TICKET)) die('ticket required: this report or date is not in the free tier');
  return text;
}

function parseBars(doc) {
  const by = {};
  for (const [, title, h] of doc.matchAll(/<img class="barras"[^>]*title="([^"]*)"[^>]*height=(\d+)/g)) {
    const m = /^(r )?(\w+) (\d+)\/(\d+)\/(\d+) [\d:]+ orbe: (\d+)\D+(\d+)/.exec(decodeEntities(title));
    if (!m) continue;
    const code = m[2].toUpperCase();
    (by[code] ||= []).push({ retro: !!m[1], date: new Date(Date.UTC(+m[5], +m[4] - 1, +m[3])), orb: `${m[6]}°${m[7]}'`, height: +h });
  }
  const iso = d => d.toISOString().slice(0, 10);
  return Object.entries(by).map(([code, ps]) => {
    ps.sort((a, b) => a.date - b.date);
    const peak = ps.reduce((a, b) => b.height > a.height ? b : a);
    const wins = [[ps[0]]];
    for (const p of ps.slice(1)) {
      const cur = wins.at(-1);
      if ((p.date - cur.at(-1).date) / 864e5 <= 4) cur.push(p); else wins.push([p]);
    }
    return {
      code, peak_height: peak.height, peak_date: iso(peak.date), peak_orb: peak.orb, intensity: Math.round(peak.height / 55 * 100) / 100,
      windows: wins.map(w => ({ from: iso(w[0].date), to: iso(w.at(-1).date), retro: w.some(p => p.retro) })),
    };
  }).sort((a, b) => b.peak_height - a.peak_height);
}

const todayUTC = () => { const n = new Date(); return new Date(Date.UTC(n.getFullYear(), n.getMonth(), n.getDate())); };

/** Reuse a 1-year report from the last 14 days instead of requesting a new one. */
function cachedStart(key, rid, today) {
  if (!['8', '7', '6'].includes(rid)) return today;
  for (let back = 0; back < 15; back++) {
    const s = new Date(today - back * 864e5);
    if (existsSync(join(CACHE, 'transits', `${key}-${rid}-${s.toISOString().slice(0, 10)}.html`))) return s;
  }
  return today;
}

async function cmdTransits(arg, o) {
  const { p, key } = subject(arg, o);
  const start = o.start ? new Date(`${o.start}T00:00:00Z`) : key ? cachedStart(key, o.report, todayUTC()) : todayUTC();
  const day = start.toISOString().slice(0, 10);
  const doc = await report(line(p), o.report, start, o, key && `transits/${key}-${o.report}-${day}.html`);
  out({ report: o.report, start: day, transits: parseBars(doc).slice(0, Number(o.top || 40)) });
}

function textOf(doc) {
  const parts = [...doc.matchAll(/<p class="interp">([\s\S]*?)(?:<\/p>|<\/font>)/gi)].map(m => m[1]);
  let t = (parts.length ? parts.join('\n') : doc).replace(/<(script|style)[\s\S]*?<\/\1>/gi, '');
  t = decodeEntities(t.replace(/<br\s*\/?>|<\/p>/gi, '\n').replace(/<[^>]+>/g, ''));
  return t.replace(/[ \t]+/g, ' ').replace(/\n\s*\n+/g, '\n\n').replace(/([^\n])\n(?!\n)/g, '$1 ').replace(/ +/g, ' ').trim();
}

async function cmdInterp(code, o) {
  if (!code) die('usage: interp CODE [--style transiaw|tratsp|starsolues]');
  if (!['transiaw', 'tratsp', 'starsolues'].includes(o.style)) die('style must be transiaw, tratsp or starsolues');
  const cla = code.toUpperCase();
  const data = await fetchSite('sacainter.asp', {
    params: { tabla: o.style, cla, orb: o.style === 'tratsp' ? '0' : '99' }, cacheKey: `interp/${o.style}-${cla}.html`,
  });
  out(textOf(latin1.decode(data)));
}

const HELP = `Usage: node gv.mjs COMMAND [options]

  add --name N --date YYYY-MM-DD --time HH:MM --city C --country K --sex V|H
      [--save] [--style casual|deep|practical] [--key KEY] [--pick N]
                          build a person line; city and country go to photon.komoot.io
                          (no grupovenus request). Written to disk only with --save.
  import FILE             import a grupovenus "Lista de personas" file
  export [FILE]           write a "Lista de personas" file (default: data folder/exports)
  list                    show stored people
  remove KEY --yes        delete a person and their cached charts and forecasts
  forget --yes            delete all people, the cache and exports
  style KEY STYLE         save a reading style
  chart KEY|--line L      natal chart PNG path        [--lang E|I|F] [--zodiac T|S1..S5]
  transits KEY|--line L   parsed forecast graph       [--report=8|-1|0|1] [--start YYYY-MM-DD] [--top N]
                          --line uses an unsaved person and caches nothing about them
  interp CODE             interpretation text         [--style transiaw|tratsp|starsolues]

Data folder: ${HOME} (set GRUPO_VENUS_HOME to change it)`;

async function main() {
  const { values: o, positionals: [cmd, ...args] } = parseArgs({
    allowPositionals: true, options: {
      name: { type: 'string' }, date: { type: 'string' }, time: { type: 'string' }, city: { type: 'string' },
      country: { type: 'string' }, sex: { type: 'string' }, style: { type: 'string' }, key: { type: 'string' },
      pick: { type: 'string' }, lang: { type: 'string', default: 'E' }, zodiac: { type: 'string', default: 'T' },
      report: { type: 'string', default: '8' }, start: { type: 'string' }, top: { type: 'string' },
      line: { type: 'string' }, save: { type: 'boolean' }, yes: { type: 'boolean' },
      help: { type: 'boolean', short: 'h' },
    },
  });
  if (o.help || !cmd) return out(HELP);
  // Every option that reaches a request or a file name is checked against a closed set.
  const check = (ok, msg) => ok || die(msg);
  check(['E', 'I', 'F'].includes(o.lang), '--lang must be E, I or F');
  check(/^(T|S[1-5])$/.test(o.zodiac), '--zodiac must be T or S1..S5');
  check(['8', '-1', '0', '1', '7', '6', '4'].includes(o.report), '--report must be 8, -1, 0, 1, 7, 6 or 4');
  check(!o.start || /^\d{4}-\d{2}-\d{2}$/.test(o.start), '--start must be YYYY-MM-DD');
  check(!o.top || /^\d{1,3}$/.test(o.top), '--top must be a number');
  check(!o.pick || /^\d$/.test(o.pick), '--pick must be 0-9');
  check(!o.key || KEY_RE.test(o.key), '--key must be lowercase letters, digits and hyphens');
  if (['chart', 'transits', 'remove', 'style'].includes(cmd) && args[0]) check(KEY_RE.test(args[0]), `bad KEY ${args[0]}`);
  if (cmd === 'interp' && args[0]) check(/^[A-Za-z]{5,12}$/.test(args[0]), 'CODE looks like SATCUAASC');
  switch (cmd) {
    case 'add': return cmdAdd(o);
    case 'import': return cmdImport(args[0]);
    case 'export': return cmdExport(args[0]);
    case 'list': return out(load().people);
    case 'remove': return cmdRemove(args[0] || die('usage: remove KEY --yes'), o);
    case 'forget': return cmdForget(o);
    case 'style': return cmdStyle(args[0], args[1]);
    case 'chart': return cmdChart(args[0], o);
    case 'transits': return cmdTransits(args[0], o);
    case 'interp': return cmdInterp(args[0], { ...o, style: o.style || 'transiaw' });
    default: die(`unknown command ${cmd}\n\n${HELP}`);
  }
}

main().catch(e => die(e.message));
