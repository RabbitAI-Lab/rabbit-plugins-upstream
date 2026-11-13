#!/usr/bin/env node
const https = require('https');
const iconv = require('iconv-lite');
const fs = require('fs');
const path = require('path');

const WATCHLIST_FILE = path.join(__dirname, '..', 'watchlist.json');

function loadWatchlists() {
  try { return JSON.parse(fs.readFileSync(WATCHLIST_FILE, 'utf8')); } catch (e) { return {}; }
}
function saveWatchlists(data) {
  fs.writeFileSync(WATCHLIST_FILE, JSON.stringify(data, null, 2), 'utf8');
}

function fetch(url) {
  return new Promise((resolve, reject) => {
    https.get(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://finance.qq.com/',
        'Accept': '*/*',
        'Connection': 'close'
      }
    }, res => {
      const chunks = [];
      res.on('data', c => chunks.push(c));
      res.on('end', () => {
        const buf = Buffer.concat(chunks);
        const text = iconv.decode(buf, 'gbk');
        resolve(text);
      });
      res.on('error', reject);
    }).on('error', reject);
  });
}

function parseLine(raw) {
  const cleaned = raw.replace(/\s*;?\s*$/, '');
  const m = cleaned.match(/^v_(\w{2})(\d{6})="(.+)"$/);
  if (!m) return null;
  const f = m[3].split('~');
  const g = i => { const v = f[i]; if (!v || v === '-') return null; const n = Number(v); return Number.isNaN(n) ? v : n; };
  return {
    market: m[1], code: m[2],
    name: String(g(1) || '').replace(/\s+/g, '').trim(),
    price: g(3), prev_close: g(4), open: g(5),
    volume: g(6),
    change: g(31), change_pct: g(32),
    high: g(33), low: g(34),
    turnover: g(37) ? g(37) * 10000 : null,
    turnover_rate: g(38),
    pe: g(39), pb: g(66),
    volume_ratio: g(43),
    market_cap: g(45) ? g(45) * 1e8 : null,
    circ_mcap: g(44) ? g(44) * 1e8 : null,
  };
}

async function fetchStocks(codes) {
  const out = [];
  for (let i = 0; i < codes.length; i += 50) {
    const batch = codes.slice(i, i + 50);
    const body = await fetch('https://qt.gtimg.cn/q=' + batch.join(','));
    for (const raw of body.split('\n')) {
      const s = parseLine(raw.trim());
      if (s && s.price != null) out.push(s);
    }
  }
  return out;
}

function inRange(val, s) {
  if (val == null || isNaN(val)) return false;
  const n = Number(val);
  if (s.startsWith('<=')) return n <= +s.slice(2);
  if (s.startsWith('>=')) return n >= +s.slice(2);
  if (s.startsWith('<')) return n < +s.slice(1);
  if (s.startsWith('>')) return n > +s.slice(1);
  const p = s.split('-').map(Number);
  if (p.length === 2) return n >= p[0] && n <= p[1];
  return Math.abs(n - +s) < 1e-9;
}

async function screen(args) {
  // Watchlist management commands
  if (args['list-watchlists']) {
    const wl = loadWatchlists();
    const names = Object.keys(wl);
    if (names.length === 0) { console.log('No watchlists saved.'); return; }
    console.log('Saved watchlists:');
    names.forEach(n => console.log(`  ${n}: ${wl[n].codes.join(',')}`));
    return;
  }
  if (args['save-watchlist']) {
    const wl = loadWatchlists();
    const name = args['save-watchlist'];
    const codes = args.codes ? args.codes.split(',').map(c => c.trim()).filter(Boolean) : [
      'sh600519','sz000858','sh601318','sz000333','sh600036',
      'sz002594','sh601899','sz000001','sh600000','sz002714',
      'sh600276','sz000651','sh601012','sz002475','sh600585',
      'sz300750','sh601398','sz000568','sh600030','sz002415',
      'sh601166','sz002304','sh601857','sz000725','sh600887',
    ];
    wl[name] = { codes, createdAt: new Date().toISOString() };
    saveWatchlists(wl);
    console.log(`Watchlist "${name}" saved with ${codes.length} codes.`);
    return;
  }
  if (args['delete-watchlist']) {
    const wl = loadWatchlists();
    const name = args['delete-watchlist'];
    if (!wl[name]) { console.log(`Watchlist "${name}" not found.`); return; }
    delete wl[name];
    saveWatchlists(wl);
    console.log(`Watchlist "${name}" deleted.`);
    return;
  }

  let codes;
  if (args.codes) {
    codes = args.codes.split(',').map(c => c.trim()).filter(Boolean);
  } else if (args['codes-file']) {
    try {
      const content = require('fs').readFileSync(args['codes-file'], 'utf8');
      codes = content.split(/[\n,;\s]+/).map(c => c.trim()).filter(Boolean);
      console.log(`Loaded ${codes.length} codes from ${args['codes-file']}`);
    } catch (e) { console.error(`Failed to read codes file: ${e.message}`); process.exit(1); }
  } else if (args['builtin']) {
    codes = [
      'sh600519','sz000858','sh601318','sz000333','sh600036',
      'sz002594','sh601899','sz000001','sh600000','sz002714',
      'sh600276','sz000651','sh601012','sz002475','sh600585',
      'sz300750','sh601398','sz000568','sh600030','sz002415',
      'sh601166','sz002304','sh601857','sz000725','sh600887',
    ];
    console.log('Using built-in stock list (25 stocks)');
  } else {
    // Try to load full A-share market list
    try {
      const allPath = require('path').join(__dirname, '..', 'all_a_shares.json');
      const allStocks = JSON.parse(require('fs').readFileSync(allPath, 'utf8'));
      codes = allStocks.map(s => s.code);
      console.log(`Loaded ${codes.length} stocks from all_a_shares.json (full A-share market)`);
    } catch (e) {
      // Fall back to built-in list
      codes = [
        'sh600519','sz000858','sh601318','sz000333','sh600036',
        'sz002594','sh601899','sz000001','sh600000','sz002714',
        'sh600276','sz000651','sh601012','sz002475','sh600585',
        'sz300750','sh601398','sz000568','sh600030','sz002415',
        'sh601166','sz002304','sh601857','sz000725','sh600887',
      ];
      console.log('Using built-in stock list (25 stocks). Run update_stock_list.py to get full market data.');
    }
  }

  if (args.preset) {
    const presets = {
      value: { pe: '0-20', pb: '0-3', volume_ratio: '>1' },
      growth: { pe: '20-50', volume_ratio: '>2', change_pct: '>0' },
      dividend: { pe: '0-15', pb: '0-2', turnover_rate: '0.5-5' },
      momentum: { volume_ratio: '>2', change_pct: '>1', turnover_rate: '1-10' },
    };
    const p = presets[args.preset];
    if (!p) { console.error(`Unknown preset: ${args.preset}. Available: ${Object.keys(presets).join(', ')}`); process.exit(1); }
    Object.entries(p).forEach(([k, v]) => { if (!(k in args)) args[k] = v; });
    console.log(`Using preset: ${args.preset}`);
  }
  if (args.watchlist) {
    const wl = loadWatchlists();
    const name = args.watchlist;
    if (!wl[name]) { console.error(`Watchlist "${name}" not found. Use --list-watchlists to see saved lists.`); process.exit(1); }
    codes = wl[name].codes;
    console.log(`Loaded watchlist "${name}" (${codes.length} codes)`);
  }
  let limit = args.limit || 20;
  let stocks = await fetchStocks(codes);

  if (args.pe) stocks = stocks.filter(s => inRange(s.pe, args.pe));
  if (args.pb) stocks = stocks.filter(s => inRange(s.pb, args.pb));
  if (args.turnover_rate) stocks = stocks.filter(s => inRange(s.turnover_rate, args.turnover_rate));
  if (args.change_pct) stocks = stocks.filter(s => inRange(s.change_pct, args.change_pct));
  if (args.volume_ratio) stocks = stocks.filter(s => inRange(s.volume_ratio, args.volume_ratio));
  if (args.market_cap) stocks = stocks.filter(s => inRange(s.market_cap ? s.market_cap / 1e8 : null, args.market_cap));
  if (args['min-price']) stocks = stocks.filter(s => s.price != null && s.price >= Number(args['min-price']));
  if (args['max-price']) stocks = stocks.filter(s => s.price != null && s.price <= Number(args['max-price']));

  // Technical indicator filters (two-stage: only analyze stocks passing basic filters)
  const techFilters = ['ma-bullish','ma-bearish','macd-golden','macd-death','rsi-overbought','rsi-oversold','boll-breakout','boll-breakdown','limit-up','limit-down'];
  const hasTechFilter = techFilters.some(f => args[f]);
  if (hasTechFilter && stocks.length > 0) {
    const MAX_TECH_ANALYSIS = 100;
    if (stocks.length > MAX_TECH_ANALYSIS) {
      console.log(`Too many stocks (${stocks.length}) for technical analysis. Limiting to top ${MAX_TECH_ANALYSIS} by ${args.sort_by || 'volume_ratio'}.`);
      const sortKey = args.sort_by || 'volume_ratio';
      stocks.sort((a, b) => { const va=a[sortKey], vb=b[sortKey]; if (va==null) return 1; if (vb==null) return -1; return vb-va; });
      stocks = stocks.slice(0, MAX_TECH_ANALYSIS);
    }
    const techInput = require('path').join(__dirname, '..', '_tech_input.json');
    const techOutput = require('path').join(__dirname, '..', '_tech_output.json');
    const pyScript = require('path').join(__dirname, 'analyze_technical.py');
    const pyBin = 'python3';
    // Write stocks to temp file for Python analysis
    require('fs').writeFileSync(techInput, JSON.stringify(stocks.map(s => ({code: s.market + s.code, name: s.name}))), 'utf8');
    console.log(`Running technical analysis on ${stocks.length} stocks...`);
    const { execSync } = require('child_process');
    try {
      execSync(`"${pyBin}" "${pyScript}" "${techInput}" "${techOutput}"`, { timeout: 600000, stdio: ['pipe','pipe','pipe'] });
      const techResults = JSON.parse(require('fs').readFileSync(techOutput, 'utf8'));
      const techMap = new Map(techResults.map(r => [r.code, r]));
      stocks = stocks.map(s => ({ ...s, _tech: techMap.get(s.market + s.code) })).filter(s => {
        const t = s._tech;
        if (!t || t.error) return false;
        if (args['ma-bullish'] && !t.ma_bullish) return false;
        if (args['ma-bearish'] && !t.ma_bearish) return false;
        if (args['macd-golden'] && !t.macd_golden) return false;
        if (args['macd-death'] && !t.macd_death) return false;
        if (args['rsi-overbought'] && !t.rsi_overbought) return false;
        if (args['rsi-oversold'] && !t.rsi_oversold) return false;
        if (args['boll-breakout'] && !t.boll_breakout) return false;
        if (args['boll-breakdown'] && !t.boll_breakdown) return false;
        if (args['limit-up'] && !t.limit_up) return false;
        if (args['limit-down'] && !t.limit_down) return false;
        return true;
      }).map(s => ({ ...s, _rsi: s._tech?.rsi ?? null, _macd: s._tech?.macd ?? null }));
      try { require('fs').unlinkSync(techInput); require('fs').unlinkSync(techOutput); } catch(e) {}
      console.log(`After technical filters: ${stocks.length} stocks`);
    } catch (e) {
      console.error('Technical analysis failed:', e.message);
      try { require('fs').unlinkSync(techInput); } catch(e2) {}
    }
  }

  const sm = { pe:'pe', pb:'pb', change_pct:'change_pct', turnover_rate:'turnover_rate', market_cap:'market_cap', price:'price', name:'name' };
  const k = sm[args.sort_by];
  if (k) stocks.sort((a, b) => { const va=a[k], vb=b[k]; if (va==null) return 1; if (vb==null) return -1; if (typeof va==='string') return args.sort_asc ? va.localeCompare(vb) : vb.localeCompare(va); return args.sort_asc ? va-vb : vb-va; });

  const r = stocks.slice(0, limit);
  if (args.output === 'json') return console.log(JSON.stringify(r, null, 2));
  if (args.output === 'csv') {
    const hdr = 'code,name,price,change_pct,turnover_rate,volume_ratio,pe,pb,rsi,macd,market_cap';
    const rows = r.map(s => [s.code, s.name, s.price??'', s.change_pct??'', s.turnover_rate??'', s.volume_ratio??'', s.pe??'', s.pb??'', s._rsi ?? '', s._macd ?? '', s.market_cap ? (s.market_cap/1e8).toFixed(0) : ''].join(','));
    const out = [hdr, ...rows].join('\n');
    if (args.file) { require('fs').writeFileSync(args.file, out, 'utf8'); console.log(`Saved ${r.length} rows to ${args.file}`); } else console.log(out);
    return;
  }
  if (args.output === 'markdown') {
    let md = '';
    md += '| 代码 | 名称 | 最新价 | 涨跌幅 | 换手率 | 量比 | PE | PB | RSI | MACD | 市值(亿) |\n';
    md += '|------|------|--------|--------|--------|------|----|----|-----|-------|----------|\n';
    r.forEach(s => { const c = s.market_cap ? (s.market_cap/1e8).toFixed(0) : '-'; const rsi = s._rsi ?? '-'; const macd = s._macd ?? '-'; md += `| ${s.code} | ${s.name} | ${s.price??'-'} | ${s.change_pct??'-'}% | ${s.turnover_rate??'-'}% | ${s.volume_ratio??'-'} | ${s.pe??'-'} | ${s.pb??'-'} | ${rsi} | ${macd} | ${c} |\n`; });
    if (args.file) { require('fs').writeFileSync(args.file, md, 'utf8'); console.log(`Saved ${r.length} rows to ${args.file}`); } else console.log(md);
    return;
  }
  console.log(`筛选结果（共 ${r.length} 条）:\n`);
  r.forEach((s, i) => { const c = s.market_cap ? `${(s.market_cap/1e8).toFixed(0)}亿` : '-'; const rsi = s._rsi ?? '-'; const macd = s._macd ?? '-'; console.log(`[${i+1}] ${s.name} ${s.code}  价格:${s.price??'-'}  涨跌幅:${s.change_pct??'-'}%  换手率:${s.turnover_rate??'-'}%  量比:${s.volume_ratio??'-'}  PE:${s.pe??'-'}  PB:${s.pb??'-'}  RSI:${rsi}  MACD:${macd}  市值:${c}`); });
}

function main() {
  const args = require('minimist')(process.argv.slice(2));
  screen(args).catch(e => { console.error('ERROR:', e.message); process.exit(1); });
}

if (require.main === module) main();
module.exports = { screen, fetchStocks, parseLine };
