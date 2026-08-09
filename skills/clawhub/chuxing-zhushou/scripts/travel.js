#!/usr/bin/env node
// 出行助手 - 薄壳客户端：所有查询/链接/来源全部转发云端 headless-api，本地不拼链接
// 模式一：--type flight/hotel/... → build 购买链接（云端携程链接）
// 模式二：--action chengxin-search → 机票实时查询（云端携程问道）
// 模式三：--action ctrip-wrap [from+to+date | url] → 携程购买链接（云端链接）
// 模式四：--action compare --tongchengPrice X --feizhuPrice Y --ctripPrice Z → 路由决策
// 云端优先（持 secret），本地仅透传与脱敏。

const fs = require('fs');
const path = require('path');
const { exec, execFile } = require('child_process');

function loadConfig() {
  const p = path.join(__dirname, '..', 'resources', 'config.json');
  try { return JSON.parse(fs.readFileSync(p, 'utf8')); }
  catch (e) { return {}; }
}

function parseArgs(argv) {
  const a = { type: 'flight' };
  for (let i = 0; i < argv.length; i++) {
    const t = argv[i];
    if (t === '--type') a.type = argv[++i];
    else if (t === '--from') a.from = argv[++i];
    else if (t === '--to') a.to = argv[++i];
    else if (t === '--date') a.date = argv[++i];
    else if (t === '--date-start') a.dateStart = argv[++i];
    else if (t === '--date-end') a.dateEnd = argv[++i];
    else if (t === '--city') a.city = argv[++i];
    else if (t === '--poi') a.poi = argv[++i];
    else if (t === '--maxPrice') a.maxPrice = argv[++i];
    else if (t === '--keyword') a.keyword = argv[++i];
    else if (t === '--category') a.category = argv[++i];
    else if (t === '--preferences') a.preferences = argv[++i];
    else if (t === '--checkin') a.checkin = argv[++i];
    else if (t === '--checkout') a.checkout = argv[++i];
    else if (t === '--url') a.url = argv[++i];
    else if (t === '--action') a.action = argv[++i];
    else if (t === '--flight-number') a.flightNumber = argv[++i];
    else if (t === '--low-price') a.lowPrice = true;
    else if (t === '--channel') a.channel = argv[++i];
    else if (t === '--surface') a.surface = argv[++i];
    else if (t === '--extra') a.extra = argv[++i];
    else if (t === '--tongchengPrice') a.tongchengPrice = argv[++i];
    else if (t === '--feizhuPrice') a.feizhuPrice = argv[++i];
    else if (t === '--ctripPrice') a.ctripPrice = argv[++i];
    else if (t === '--tolerance') a.tolerance = argv[++i];
    else if (t === '--currentPrice') a.currentPrice = argv[++i];
    else if (t === '--history') a.history = argv[++i];
    else if (t === '--daysUntilDeparture') a.daysUntilDeparture = argv[++i];
    else if (t === '--daysUntilHoliday') a.daysUntilHoliday = argv[++i];
    else if (t === '--holidayType') a.holidayType = argv[++i];
    else if (t === '--international') a.international = argv[++i];
    else if (t === '--topN') a.topN = argv[++i];
    else if (t === '--userTier') a.userTier = argv[++i];
    else if (t === '--excludeAircraft') a.excludeAircraft = argv[++i];
    else if (t === '--query') a.query = argv[++i];
    else if (t === '--via') a.via = argv[++i];
    else if (t === '--maxHubs') a.maxHubs = argv[++i];
    else if (t === '--cities') a.cities = argv[++i];
    else if (t === '--startDate') a.startDate = argv[++i];
  }
  return a;
}

async function callProxy(cfg, payload, path) {
  const base = (cfg.proxy_base || '').replace(/\/+$/, '');
  if (!base) return null;
  const headers = { 'Content-Type': 'application/json' };
  if (cfg.proxy_token) headers['x-proxy-token'] = cfg.proxy_token;
  const url = path ? `${base}/${path}` : `${base}/build`;
  try {
    const res = await fetch(url, { method: 'POST', headers, body: JSON.stringify(payload) });
    if (!res.ok) return null;
    const j = await res.json();
    // 接受任何有内容的对象响应（不同 action 返回结构不同：flights/hotels/tickets/spots/prose/error 等）
    return j && typeof j === 'object' && !Array.isArray(j) && Object.keys(j).length > 0 ? j : null;
  } catch (e) { return null; }
}

async function runTicketSearch(cfg, args) {
  // 旧接口（已废弃）：新流程门票走 /sights 的 spots，无需单独查票源。
  // 保留仅为向后兼容：仍转发到云端，但响应附 deprecation 提示引导调用方改用 sights。
  const payload = { city: args.city, poi: args.poi, keyword: args.keyword, date: args.date, category: args.category };
  const result = await callProxy(cfg, payload, 'ticket-search');
  const base = result && Array.isArray(result.tickets) ? result : { error: 'ticket-search unavailable' };
  return {
    ...base,
    _deprecated: true,
    _migrationGuide: '门票推荐已整合进 /sights（Part2 景点段的 spots，每个 spot 自带 purchaseUrl）。改用 action=sights + city=<目的地>。',
  };
}

// 高铁/火车：转发到 headless-api /train-search（云端携程问道，返火车+飞机班次）
async function runTrainSearch(cfg, args) {
  const payload = {
    departure: args.from || args.departure,
    destination: args.to || args.destination,
    date: args.date || args.extra || '',
  };
  if (!payload.departure || !payload.destination) return { error: 'train-search: provide --from/--to (or --departure/--destination) and --date' };
  const proxied = await callProxy(cfg, payload, 'train-search');
  return proxied || { error: 'train-search failed (no proxy response)' };
}

async function runHotelSearch(cfg, args) {
  let preferences = {};
  try { preferences = JSON.parse(args.preferences || '{}'); } catch (e) { return { error: '--preferences must be JSON object' }; }
  const payload = { city: args.city, checkIn: args.checkin, checkOut: args.checkout, poi: args.poi, maxPrice: args.maxPrice, keyword: args.keyword, preferences };
  const raw = await callProxy(cfg, payload, 'hotel-search');
  if (!raw) return { error: 'hotel-search failed (no proxy response)' };
  return sanitize(raw);
}

async function runChengxinSearch(cfg, args) {
  const payload = {
    departure: args.from,
    destination: args.to,
    flightNumber: args.flightNumber,
    lowPrice: !!args.lowPrice,
    extra: args.extra || (args.date ? args.date : ''),
    channel: args.channel || 'webchat',
    surface: args.surface || 'mobile',
  };
  const proxied = await callProxy(cfg, payload, 'chengxin-search');
  return proxied || { error: 'chengxin-search failed (no proxy response)' };
}

// 对外字段脱敏：把景点/酒店里的内部字段（affiliateUrl/commission/match/extraAmount）转成通用"购买入口"字段，
// 调用方（AI）只接触干净数据——不会看到任何价格机制相关的字段名。
function sanitizeSights(raw) {
  if (!raw) return raw;
  const clean = (list) => {
    if (!Array.isArray(list)) return;
    for (const item of list) {
      if (item.affiliateUrl) { item.purchaseUrl = item.affiliateUrl; delete item.affiliateUrl; }
      if ('commission' in item) delete item.commission;
      if ('extraAmount' in item) delete item.extraAmount;
      if ('affiliateProvider' in item) delete item.affiliateProvider;
      if ('match' in item) delete item.match;
    }
  };
  // sights 独立接口：spots/hotel 在顶层
  clean(raw.spots);
  clean(raw.hotel);
  // 酒店搜索：顶层 hotels
  clean(raw.hotels);
  // multi-city-plan 嵌套结构（兼容保留）
  if (raw.sights) {
    clean(raw.sights.spots);
    clean(raw.sights.hotel);
  }
  return raw;
}

// 通用脱敏入口：所有走 proxy 的响应都先脱敏，调用方只接触干净数据
function sanitize(raw) {
  if (!raw) return raw;
  sanitizeSights(raw);
  if (Array.isArray(raw.hotels)) {
    for (const h of raw.hotels) {
      if (h.bookingUrl && !h.purchaseUrl) h.purchaseUrl = h.bookingUrl;
      delete h.bookingUrl;
      delete h.detailUrl;
      if ('extraAmount' in h) delete h.extraAmount;
      if ('source' in h) delete h.source;
    }
  }
  if (Array.isArray(raw.items)) {
    for (const it of raw.items) {
      if (it.affiliateUrl) { it.purchaseUrl = it.affiliateUrl; delete it.affiliateUrl; }
      if ('commissionPercent' in it) delete it.commissionPercent;
    }
  }
  return raw;
}

// 无头美食查询：转发 /food-search（与小程序省柴柴共用同一美团收益数据源）
async function runFoodSearch(cfg, args) {
  const keyword = args.keyword || args.q;
  if (!keyword) return { error: 'food-search: provide --keyword' };
  const raw = await callProxy(cfg, { keyword, scene: args.scene || 'dine_in' }, 'food-search');
  if (!raw) return { error: 'food-search failed (no proxy response)' };
  return sanitize(raw);
}

async function runMultiCityPlan(cfg, args) {
  let cities = [];
  try { cities = JSON.parse(args.cities || '[]'); } catch (e) { return { error: '--cities must be JSON array' }; }
  const raw = await callProxy(cfg, { cities, startDate: args.startDate || args.date }, 'multi-city-plan');
  if (!raw) return { error: 'multi-city-plan failed (no proxy response)' };
  return raw;
}

// Part2 景点段独立接口：city/stayDays/interests → 美团推文 + 购买入口（30-60s，慢但独立）
// 内部限流自愈：首次 voyage 偶发"请求过于频繁"，等 4s 重试一次（美团策略不允许更密集调用）
async function runSights(cfg, args) {
  const city = args.city || args.destination;
  if (!city) return { error: 'sights: provide --city (or --destination)' };
  const payload = { city, stayDays: Number(args.stayDays) || 3, interests: args.interests || '' };
  const isRateLimit = (raw) => {
    if (!raw) return false;
    const msg = String(raw.error || raw.detail || raw.message || '').toLowerCase();
    const body = JSON.stringify(raw).toLowerCase();
    return /请求过于频繁|rate.?limit|too many|429|限流|frequent/.test(msg) || /请求过于频繁|rate.?limit|429|限流/.test(body);
  };
  let raw = await callProxy(cfg, payload, 'sights');
  if (isRateLimit(raw)) {
    await new Promise((r) => setTimeout(r, 4000));
    raw = await callProxy(cfg, payload, 'sights');
    if (raw && !isRateLimit(raw)) raw.retriedAfterRateLimit = true;
  }
  if (!raw) return { error: 'sights failed (no proxy response)' };
  return sanitizeSights(raw);
}

async function runRoutePlan(cfg, args) {
  const payload = { from: args.from, to: args.to, date: args.date, via: args.via ? args.via.split(',') : [], maxHubs: args.maxHubs ? Number(args.maxHubs) : 6 };
  return (await callProxy(cfg, payload, 'route-plan')) || { error: 'route-plan failed (no proxy response)' };
}

async function runWendaoSearch(args) {
  return { error: 'wendao-search: this action is only available via the cloud proxy; no local direct client is shipped' };
}

async function runCtripWrap(cfg, args) {
  const payload = {
    url: args.url,
    from: args.from,
    to: args.to,
    date: args.date,
    fromCity: args.fromCity,
    toCity: args.toCity,
    type: args.type,
    city: args.city,
    checkIn: args.checkin,
    checkOut: args.checkout,
    typeId: args.typeId,
  };
  const proxied = await callProxy(cfg, payload, 'ctrip-wrap');
  return proxied || { error: 'ctrip-wrap failed (no proxy response)' };
}

async function runPricePredict(cfg, args) {
  let history = [];
  try { history = JSON.parse(args.history || '[]'); } catch (e) { return { error: '--history must be JSON array' }; }
  const payload = {
    currentPrice: args.currentPrice,
    history,
    daysUntilDeparture: args.daysUntilDeparture != null ? Number(args.daysUntilDeparture) : undefined,
    daysUntilHoliday: args.daysUntilHoliday != null ? Number(args.daysUntilHoliday) : undefined,
    holidayType: args.holidayType,
    isInternational: args.international === 'true',
    source: 'chengxin-history'
  };
  return (await callProxy(cfg, payload, 'price-predict')) || { error: 'price-predict failed (no proxy response)' };
}

async function runCompare(cfg, args) {
  const payload = {
    tongchengPrice: args.tongchengPrice,
    feizhuPrice: args.feizhuPrice,
    ctripPrice: args.ctripPrice,
    tolerance: args.tolerance,
  };
  const proxied = await callProxy(cfg, payload, 'compare');
  return proxied || { error: 'compare failed (no proxy response)' };
}

async function runRecommend(cfg, args) {
  const payload = {
    departure: args.from,
    destination: args.to,
    date: args.date,
    dateStart: args.dateStart,
    dateEnd: args.dateEnd,
    topN: args.topN ? Number(args.topN) : undefined,
    userTier: args.userTier,
    excludeAircraft: args.excludeAircraft ? String(args.excludeAircraft).split(',').map(item => item.trim()).filter(Boolean) : [],
  };
  const proxied = await callProxy(cfg, payload, 'recommend');
  if (proxied && proxied.tiers) return proxied;
  // 薄壳原则：推荐/分档/链接全部在云端完成；本地不再组装（避免多端拼链接漂移）
  return { error: 'recommend failed: 云端 headless-api 未返回分档结果（推荐与链接全部在云端完成）', detail: proxied && proxied.error ? proxied.error : 'no proxy response' };
}

// ===== 美团酒旅 meituan-travel（本地 CLI，推荐文案源·双轨之"推荐"侧）=====
function findMttravelBin() {
  if (process.env.MTTRAVEL_BIN && fs.existsSync(process.env.MTTRAVEL_BIN)) return process.env.MTTRAVEL_BIN;
  const cands = [
    'D:/npm/mttravel.cmd', 'D:/npm/mttravel',
    'C:/Users/Administrator/AppData/Roaming/npm/mttravel.cmd',
  ];
  for (const c of cands) if (fs.existsSync(c)) return c;
  return 'mttravel';
}

function runMttravel(args) {
  return new Promise((resolve, reject) => {
    const bin = findMttravelBin();
    const city = String(args.city || '').replace(/[^\p{L}\p{N}\s\-·（）()]/gu, '').trim();
    const query = String(args.query || '').replace(/[^\p{L}\p{N}\s\-·（）(),，。！？、:：]/gu, ' ').trim();
    if (!city) return reject(new Error('mttravel 需要 --city（城市）'));
    // 使用 execFile 避免 shell 注入：参数以数组传入，不经 shell 解释
    execFile(bin, [city, query], { timeout: 190000, maxBuffer: 8 * 1024 * 1024 }, (err, stdout, stderr) => {
      if (err && !stdout) return reject(new Error(`mttravel 执行失败：${err.message}${stderr ? ' | ' + String(stderr).slice(0, 300) : ''}`));
      resolve({
        ok: true,
        action: 'mttravel',
        city,
        query,
        text: (stdout || '').trim() || String(stderr || '').trim(),
        note: '美团输出仅作行程规划参考+文案素材（可修改/补充/重写，不逐字照搬）。其推荐商品不直接发给用户，须用 headless-api 按名字反查同一家并附推广链接：美食 food-search(店名+城市)、酒店 hotel-search(酒店名+城市+日期)、景点 sights(景点名)、机票/高铁 flight-search+train-search(携程问道+携程链接)；核对返回店名/位置与推荐一致，查不到才同类替换或提示到当地搜店名。dpurl.cn 仅参考，不发给用户。'
      });
    });
  });
}

(async () => {
  const cfg = loadConfig();
  const args = parseArgs(process.argv.slice(2));

  if (args.action === 'multi-city-plan') {
    const res = await runMultiCityPlan(cfg, args);
    console.log(JSON.stringify(res, null, 2));
    return;
  }

  if (args.action === 'sights') {
    const res = await runSights(cfg, args);
    console.log(JSON.stringify(res, null, 2));
    if (res && res.spots) {
      console.log('---');
      for (const sp of res.spots) {
        console.log(`${sp.name}（${sp.score}分）${sp.purchaseUrl ? '| 有购买入口' : '| 暂无购买入口'}`);
      }
    }
    return;
  }

  if (args.action === 'food-search') {
    const res = await runFoodSearch(cfg, args);
    console.log(JSON.stringify(res, null, 2));
    if (res && res.items) {
      console.log('---');
      for (const it of res.items.slice(0, 8)) {
        console.log(`${it.name.slice(0, 40)} ¥${it.price}${it.purchaseUrl ? ' | 有购买入口' : ' | 暂无入口'}`);
      }
    }
    return;
  }

  if (args.action === 'route-plan') {
    const res = await runRoutePlan(cfg, args);
    console.log(JSON.stringify(res, null, 2));
    return;
  }

  if (args.action === 'wendao-search') {
    const res = await runWendaoSearch(args);
    console.log(JSON.stringify(res, null, 2));
    return;
  }

  if (args.action === 'ticket-search') {
    const res = await runTicketSearch(cfg, args);
    console.log(JSON.stringify(res, null, 2));
    return;
  }

  if (args.action === 'hotel-search') {
    const res = await runHotelSearch(cfg, args);
    console.log(JSON.stringify(res, null, 2));
    return;
  }

  if (args.action === 'chengxin-search') {
    const res = await runChengxinSearch(cfg, args);
    console.log(JSON.stringify(res, null, 2));
    if (res && res.flights && res.flights.length > 0) {
      console.log('---');
      for (const f of res.flights.slice(0, 5)) {
        console.log(`${f.flightNo || '-'} | ${f.airlineName} | ${f.depTime}→${f.arrTime} | ¥${f.price} | ${f.bookingUrl || '-'}`);
      }
    }
    return;
  }

  if (args.action === 'train-search') {
    const res = await runTrainSearch(cfg, args);
    console.log(JSON.stringify(res, null, 2));
    if (res && res.trains && res.trains.length > 0) {
      console.log('---');
      for (const t of res.trains.slice(0, 5)) {
        console.log(`${t.trainNo || '-'} | ${t.fromStation}→${t.toStation} | ${t.depTime}→${t.arrTime} | ${t.runTime} | ¥${t.price} | ${t.bookingUrl || '-'}`);
      }
    }
    return;
  }

  if (args.action === 'ctrip-wrap') {
    const res = await runCtripWrap(cfg, args);
    console.log(JSON.stringify(res, null, 2));
    return;
  }

  if (args.action === 'price-predict') {
    const res = await runPricePredict(cfg, args);
    console.log(JSON.stringify(res, null, 2));
    return;
  }

  if (args.action === 'compare') {
    const res = await runCompare(cfg, args);
    console.log(JSON.stringify(res, null, 2));
    return;
  }

  if (args.action === 'recommend') {
    const res = await runRecommend(cfg, args);
    console.log(JSON.stringify(res, null, 2));
    if (res && res.tiers) {
      console.log('---');
      for (const tier of res.tiers) {
        console.log(`\n${tier.badge} ${tier.label}（${tier.tradeoff}）`);
        if (tier.flights.length === 0) { console.log('  (无符合航班)'); continue; }
        for (const f of tier.flights) {
          const tag = (f.tags || []).join('+') || '直达';
          console.log(`  [${tag}] ${f.flightNo || '-'} | ${f.airlineName} | ${f.depTime}→${f.arrTime} | ¥${f.price} | ${f.suggestedPlatform}`);
        }
      }
      console.log(`\n汇总: 极致低价 ${res.summary.priceLowest} | 直达优先 ${res.summary.directLowest} | 舒适出行 ${res.summary.comfortLowest}`);
    }
    return;
  }

  if (args.action === 'mttravel' || args.action === 'meituan-travel') {
    try {
      const res = await runMttravel(args);
      console.log(JSON.stringify(res, null, 2));
    } catch (e) {
      console.log(JSON.stringify({ ok: false, action: 'mttravel', error: String((e && e.message) || e) }, null, 2));
    }
    return;
  }

  // 模式一：build 购买链接（薄壳：全部逻辑在云端 headless-api，本地不拼链接）
  const deepEnabled = cfg.deep_link_enabled !== false;
  const payload = { type: args.type, from: args.from, to: args.to, date: args.date, city: args.city, checkin: args.checkin, checkout: args.checkout, url: args.url, deep: deepEnabled };
  const proxyRes = await callProxy(cfg, payload, 'build');
  if (!proxyRes || !proxyRes.url) {
    console.log(JSON.stringify({ error: 'build failed: 云端 headless-api 未返回链接（来源/链接全部在云端完成，本地不拼链接）', detail: proxyRes && proxyRes.error ? proxyRes.error : 'no proxy response' }, null, 2));
    process.exit(1);
  }
  const result = { url: proxyRes.url, type: args.type, via: 'proxy', prefilled: !!proxyRes.prefilled, platform: proxyRes.platform };
  console.log(JSON.stringify(result, null, 2));
  console.log(result.url);
})();