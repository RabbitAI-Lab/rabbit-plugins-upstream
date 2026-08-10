#!/usr/bin/env node
/**
 * gen-itinerary-html.js — 出行文档生成器（杂志编辑风 v7 · 绿色定型版）
 *
 * 版式（v7 = v5 绿色杂志风定型 + v6 期间验证过的功能改进；v6 暖陶风已弃用）：
 *  - 顶部山水绿 Hero：省柴柴 logo + kicker + 标题 + 路线胶囊 + 关键信息 chips
 *  - 吸顶 Day 页签（Day N · 地名 + 日期两行）
 *  - 每天：编辑式标题 + 细线小圆点时间线 + 分类标签卡片（交通/景点/美食/住宿）
 *  - 价格自动标红、时间/"提前 N 天开售"标绿（前端 JS，不碰链接）
 *  - 必抢项（name 含 ⚠️ 或 it.warn=true）：浅红描边卡片 + ⚠️ 必抢徽章
 *  - 条目级提醒：items[].tip / items[].tips 渲染在该卡片内（入口按钮上方），
 *    抢票提醒跟高铁卡、限流提醒跟景区卡、锁房提醒跟酒店卡
 *  - 全天通用提醒兜底：itinerary[].tips 渲染在时间线末尾（与卡片同缩进对齐）
 *  - 底部：分享按钮（navigator.share，降级复制文案）+ 省柴柴小程序引流区
 *    （正式小程序码放到 scripts/../assets/省柴柴小程序码.png 会自动 base64 内嵌）
 *  - 入口按钮：统一通用样式（不分平台配色、不显示平台徽标）
 *  - 单文件零依赖：无 CDN，file:// 双击离线可开
 *
 * 文本语气（重要）：每个 items[].text 必须按 references/xiaohongshu-style.md
 * 写成「小红书爆款笔记」——第一人称、情绪钩子、五感细节、具体数字、明确立场，
 * 每项 ≥120 字。禁止"风景优美""值得一去"等空话。
 * 生成器把 text 里的 \n 渲染为 <br>，可自由换行制造呼吸感。
 *
 * 链接契约（本脚本仅作【安全网】二次校验，权威在内部代理层 api/shared/link-contract.js）：
 *  - 链接的"真实平台 + 带渠道来源 + 非中转"由代理层 emitAffiliateLink 唯一保证；
 *    本脚本只做控制台告警（聚合降级/短链提示/缺来源参数提示），不影响渲染。
 *  - 入口按钮不展示平台徽标，但 platform 字段与域名识别仍用于告警判断。
 *
 * 用法：
 *   node gen-itinerary-html.js <行程.json> [-o <输出.html>]
 *   node gen-itinerary-html.js -s '<JSON字符串>' [-o <输出.html>]
 *
 * 行程 JSON 结构：
 * {
 *   "title": "🧳 广州→贵州 · 5天4晚山水人文之旅",
 *   "trip": {
 *     "from": "广州", "to": "贵州", "days": 5, "nights": 4,
 *     "stops": ["广州","贵阳","安顺·黄果树","荔波","西江苗寨","广州"],  // 可选：Hero 路线胶囊
 *     "kicker": "GUIZHOU ROADTRIP · 10.02 – 10.06",                     // 可选：Hero 顶部小字
 *     "chips": ["🚄 高铁合计 ¥1,189/人", "⚠️ 2 张必抢独班车"],           // 可选：Hero 追加 chips
 *     "shareText": "自定义分享文案"                                      // 可选：覆盖默认分享文案
 *   },
 *   "itinerary": [
 *     {
 *       "day": 1, "date": "2026-10-02", "weekday": "周五",
 *       "tab": "Day 1 · 贵阳",                                          // 可选：页签主文案
 *       "title": "出发！高铁直达贵阳，下午开逛",
 *       "weather": "以出行前预报为准",
 *       "intro": "早上高铁出发，中午到贵阳东……",
 *       "items": [
 *         {
 *           "icon": "🚄",
 *           "name": "G3722 广州南 → 贵阳东（07:31→11:34）",
 *           "warn": true,                                               // 可选：必抢警示（或 name 含 ⚠️）
 *           "text": "广州到贵阳最快的一档高铁……",
 *           "tip": "约 9/17 开抢，定闹钟",                              // 可选：卡内提醒（或 tips 数组）
 *           "link": "https://s.ly.com/xxx?refid=xxx",
 *           "linkText": "购票入口"
 *         }
 *       ],
 *       "tips": ["全天通用提醒……"]   // 兜底：仅放不属于任何单条的提醒，优先用条目 tip
 *     }
 *   ],
 *   "notes": ["旧字段：全局提醒，会作为兜底标注放到 Day 1 末尾（建议改用条目 tip）"],
 *   "closing": "一路顺风！玩得开心 ✨"
 * }
 */

'use strict';

const fs = require('fs');
const os = require('os');
const path = require('path');

// ---------- 参数解析 ----------
const args = process.argv.slice(2);
let jsonPath = null, jsonStr = null, outPath = null, showBranding = false;
for (let i = 0; i < args.length; i++) {
  const a = args[i];
  if (a === '-o' || a === '--out') outPath = args[++i];
  else if (a === '-s' || a === '--string') jsonStr = args[++i];
  else if (a === '--branding') showBranding = true;
  else if (a === '-h' || a === '--help') { console.log('用法: node gen-itinerary-html.js <json> [-o out.html] [--branding]'); process.exit(0); }
  else jsonPath = a;
}
if (!jsonStr && !jsonPath) { console.log('用法: node gen-itinerary-html.js <json> [-o out.html]'); process.exit(1); }

let trip;
try {
  trip = jsonStr ? JSON.parse(jsonStr) : JSON.parse(fs.readFileSync(jsonPath, 'utf-8'));
} catch (e) { console.error('读取失败:', e.message); process.exit(1); }
if (!trip?.itinerary?.length) { console.error('缺 itinerary 数组'); process.exit(1); }

if (!outPath) {
  const desk = path.join(os.homedir(), 'Desktop');
  const base = fs.existsSync(desk) ? desk : os.homedir();
  outPath = path.join(base, String(trip.title || '出行文档').replace(/[\\/:*?"<>|]/g, '_') + '.html');
}

// ---------- 工具函数 ----------
function esc(s) {
  return String(s ?? '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
    .replace(/"/g,'&quot;').replace(/\n/g,'<br>');
}

// ---------- 分类（图标 → 分类名/英文/颜色） ----------
const CATS = {
  '🚄': ['交通', 'TRANSIT', '#2563eb'],
  '✈️': ['交通', 'TRANSIT', '#2563eb'],
  '✈': ['交通', 'TRANSIT', '#2563eb'],
  '🚌': ['交通', 'TRANSIT', '#2563eb'],
  '🚗': ['交通', 'TRANSIT', '#2563eb'],
  '🚕': ['交通', 'TRANSIT', '#2563eb'],
  '🚢': ['交通', 'TRANSIT', '#2563eb'],
  '⛰️': ['景点', 'SIGHTS', '#059669'],
  '⛰': ['景点', 'SIGHTS', '#059669'],
  '🏞️': ['景点', 'SIGHTS', '#059669'],
  '🏞': ['景点', 'SIGHTS', '#059669'],
  '🎡': ['景点', 'SIGHTS', '#059669'],
  '🏛️': ['景点', 'SIGHTS', '#059669'],
  '🏛': ['景点', 'SIGHTS', '#059669'],
  '🌊': ['景点', 'SIGHTS', '#059669'],
  '🌉': ['景点', 'SIGHTS', '#059669'],
  '🎫': ['景点', 'SIGHTS', '#059669'],
  '🍜': ['美食', 'FOOD', '#b45309'],
  '🍲': ['美食', 'FOOD', '#b45309'],
  '🍢': ['美食', 'FOOD', '#b45309'],
  '🍡': ['美食', 'FOOD', '#b45309'],
  '☕': ['美食', 'FOOD', '#b45309'],
  '🧋': ['美食', 'FOOD', '#b45309'],
  '🍺': ['美食', 'FOOD', '#b45309'],
  '🐟': ['美食', 'FOOD', '#b45309'],
  '🏨': ['住宿', 'STAY', '#6d28d9'],
  '🏠': ['住宿', 'STAY', '#6d28d9'],
  '🛏️': ['住宿', 'STAY', '#6d28d9'],
  '🛏': ['住宿', 'STAY', '#6d28d9'],
  '🛍️': ['购物', 'SHOPPING', '#be185d'],
  '🛍': ['购物', 'SHOPPING', '#be185d'],
};
const CAT_DEFAULT = ['行程', 'PLAN', '#6b7280'];

function catOf(icon) {
  return CATS[icon] || CAT_DEFAULT;
}

// ---------- 平台映射（仅用于安全网告警；渲染不区分平台） ----------
const PLATFORMS = {
  meituan: '美团', tongcheng: '同程旅行', fliggy: '飞猪', ctrip: '携程',
  taobao: '淘宝', jd: '京东', vip: '唯品会', pdd: '拼多多',
  douyin: '抖音', kuaishou: '快手', other: '链接'
};

// 聚合/内部中转：告警（我们的内部变现层，不应出现在文档里）
const AGGREGATOR_HOSTS = [
  /jutuike\.com$/i,
  /cloudbase\.app$/i,
  /tencentcloudapi\.com$/i,
  /our-proxy/i
];

// 短链服务：仅作提示
const SHORT_LINK_HOSTS = [
  /t\.cn$/i, /url\.cn$/i, /dwz\.cn$/i, /dwz\.win$/i, /suo\.im$/i,
  /tinyurl\.com$/i, /bit\.ly$/i, /tb\.am$/i, /tb\.cn$/i,
  /s\.click\.taobao\.com$/i,
  /u\.meituan\.com$/i, /dpurl\.cn$/i,
  /u\.jd\.com$/i, /t\.vip\.com$/i,
  /mq\.mbd\.baidu\.com$/i,
  /suvmothq\.com$/i
];

const DOMAIN_PLATFORM = [
  [/meituan\./i, 'meituan'], [/dianping\./i, 'meituan'], [/dpurl\.cn$/i, 'meituan'], [/u\.meituan\.com$/i, 'meituan'],
  [/ly\.com$/i, 'tongcheng'], [/tongcheng/i, 'tongcheng'],
  [/fliggy\./i, 'fliggy'], [/router\.feizhu\.com/i, 'fliggy'], [/alitrip\./i, 'fliggy'],
  [/taobao\.com$/i, 'fliggy'], [/s\.click\.taobao\.com$/i, 'fliggy'],
  [/ctrip\.com$/i, 'ctrip'], [/trip\.com$/i, 'ctrip'], [/u\.ctrip\.com$/i, 'ctrip'],
  [/jd\.com$/i, 'jd'], [/u\.jd\.com$/i, 'jd'],
  [/vip\.com$/i, 'vip'], [/t\.vip\.com$/i, 'vip'],
  [/pinduoduo\.com$/i, 'pdd'], [/yangkeduo\.com$/i, 'pdd'],
  [/jinritemai\.com$/i, 'douyin'], [/haohuo/i, 'douyin'],
  [/kuaishou/i, 'kuaishou'], [/kwaixiaodian/i, 'kuaishou']
];

function hostOf(link) {
  try { return new URL(link).hostname; } catch (_) { return ''; }
}

// 安全网：只告警，不影响渲染（入口按钮为统一通用样式）
function checkLink(link) {
  const host = hostOf(link);
  if (!host) return;
  if (AGGREGATOR_HOSTS.some(re => re.test(host))) {
    console.warn(`⚠️ [链接校验] 聚合/内部中转域名出现在文档中：${link}\n   这类是我们的内部变现层，文档里应只放最终真实平台链接。`);
    return;
  }
  let platform = null;
  for (const [re, key] of DOMAIN_PLATFORM) if (re.test(host)) { platform = key; break; }
  if (platform && SHORT_LINK_HOSTS.some(re => re.test(host))) {
    console.warn(`ℹ️ [链接校验] 检测到短链(${host})，已按真实平台(${PLATFORMS[platform]})处理；建议优先用长链以免跳转失效：${link}`);
  }
  if (!platform) {
    console.warn(`ℹ️ [链接校验] 无法识别平台：${link}`);
    return;
  }
  try {
    const u = new URL(link);
    if (!u.search || u.search.length <= 1) {
      console.warn(`⚠️ [收益校验] 平台链接无查询参数，可能缺渠道来源(refid/unionId等)：${link}\n   请确认传入的是推广长链，而非平台首页。`);
    }
  } catch (_) {}
}

// ---------- 省柴柴 logo（assets/logo.jpg 自动内嵌；找不到则用内置兜底） ----------
const LOGO_FALLBACK_B64 = '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';
function loadLogo() {
  const candidates = ['logo.jpg', 'logo.png', 'icon.jpg', 'icon.png']
    .map(f => path.join(__dirname, '..', 'assets', f));
  for (const p of candidates) {
    if (fs.existsSync(p)) {
      const mime = p.endsWith('.png') ? 'image/png' : 'image/jpeg';
      return `data:${mime};base64,` + fs.readFileSync(p).toString('base64');
    }
  }
  return LOGO_FALLBACK_B64 ? 'data:image/jpeg;base64,' + LOGO_FALLBACK_B64 : '';
}
const logoUri = loadLogo();

// ---------- 渲染 ----------
function renderEntry(it) {
  if (!it.link) return '';
  checkLink(it.link);
  return `<a class="entry" href="${esc(it.link)}" target="_blank" rel="noopener">${esc(it.linkText || '查看详情')}<span class="arr">↗</span></a>`;
}

function renderItem(it) {
  const icon = it.icon || '📍';
  const [cat, catEn, color] = catOf(icon);
  const warn = it.warn === true || String(it.name || '').includes('⚠️');
  const name = String(it.name || '').replace(/⚠️/g, '').trim();
  const entries = renderEntry(it);
  return `
      <div class="t-item" style="--cat:${color};">
        <div class="t-dot"></div>
        <div class="t-card${warn ? ' warn' : ''}">
          <div class="t-cat">${esc(icon)} ${esc(cat)} <span class="en">${esc(catEn)}</span></div>
          <div class="t-name">${esc(name)}${warn ? '<span class="t-warn">⚠️ 必抢</span>' : ''}</div>
          <div class="t-desc">${esc(it.text)}</div>
          ${renderItemTips(it)}
          ${entries ? `<div class="t-entries">${entries}</div>` : ''}
        </div>
      </div>`;
}

// 条目级提醒：it.tip（字符串）或 it.tips（数组），渲染在卡片内、入口按钮上方
function renderItemTips(it) {
  const arr = [];
  if (it.tip) arr.push(it.tip);
  if (Array.isArray(it.tips)) arr.push(...it.tips);
  if (!arr.length) return '';
  return arr.map(t => {
    const s = String(t);
    const ic = /^[\u{1F000}-\u{1FAFF}\u{2600}-\u{27BF}]/u.test(s) ? Array.from(s)[0] : '💡';
    const body = (ic === '💡' ? s : s.slice(ic.length)).trim();
    return `<div class="t-tip">${ic} ${esc(body)}</div>`;
  }).join('');
}

function shortDate(d) {
  const m = String(d.date || '').match(/\d{4}-(\d{2})-(\d{2})/);
  return m ? `${Number(m[1])}.${m[2]}` : '';
}

function renderDayTips(tips, header) {
  if (!tips?.length) return '';
  const lis = tips.map(t => {
    const s = String(t);
    const ic = /^[\u{1F000}-\u{1FAFF}\u{2600}-\u{27BF}]/u.test(s) ? Array.from(s)[0] : '•';
    const body = s.slice(ic.length).trim();
    return `<li>${ic} ${esc(body)}</li>`;
  }).join('');
  return `<div class="day-tips"><div class="dt-h">💡 ${esc(header || '本日提醒')}</div><ul>${lis}</ul></div>`;
}

function renderDay(d, idx) {
  const itemsHtml = (d.items || []).map(renderItem).join('');
  // 兜底提醒：优先 d.tips；Day 1 追加旧字段全局 notes（向后兼容）
  const tips = Array.isArray(d.tips) ? d.tips.slice() : [];
  if (idx === 0 && Array.isArray(trip.notes) && trip.notes.length) tips.push(...trip.notes);
  return `
    <section class="day${idx === 0 ? ' active' : ''}" id="day-${idx+1}">
      <div class="day-head">
        <div class="day-no">DAY ${idx+1}${d.tab && d.tab.includes('·') ? ' · ' + esc(d.tab.split('·').pop().trim()) : ''}</div>
        <h2 class="day-title">${esc(d.title || `第 ${idx+1} 天`)}</h2>
        ${d.date ? `<div class="day-meta">${esc(d.date)}${d.weekday ? '  '+esc(d.weekday) : ''}${d.weather ? '  ·  '+esc(d.weather) : ''}</div>` : ''}
        ${d.intro ? `<p class="day-intro">${esc(d.intro)}</p>` : ''}
      </div>
      <div class="timeline">${itemsHtml}${renderDayTips(tips, '本日提醒')}</div>
    </section>`;
}

function renderTabs(arr) {
  return arr.map((d, i) => {
    const main = d.tab || `Day ${i+1}`;
    const sub = [shortDate(d), d.weekday].filter(Boolean).join(' ');
    return `<button class="tab${i===0 ? ' active' : ''}" data-target="day-${i+1}"><span class="t1">${esc(main)}</span>${sub ? `<span class="t2">${esc(sub)}</span>` : ''}</button>`;
  }).join('');
}

// ---------- Hero ----------
const tm = trip.trip || {};
const stops = Array.isArray(tm.stops) && tm.stops.length ? tm.stops : [tm.from, tm.to].filter(Boolean);
const routeHtml = stops.map((s, i) => (i ? '<span class="arr">→</span>' : '') + `<span class="stop">${esc(s)}</span>`).join('');
const autoChips = [];
const userChips = Array.isArray(tm.chips) ? tm.chips : [];
// 天数 chip：用户 chips 里已含"N天M晚"则不重复加
const hasDayChip = userChips.some(c => /天/.test(String(c)) && /晚/.test(String(c)));
if ((tm.days || tm.nights) && !hasDayChip) autoChips.push(`🗓 ${tm.days || ''}天${tm.nights || ''}晚`);
const chips = autoChips.concat(userChips);
const chipsHtml = chips.map(c => `<span>${esc(c)}</span>`).join('');
const kicker = tm.kicker || [tm.from, tm.to].filter(Boolean).join(' → ');

// ---------- 分享 + 小程序引流 ----------
// 正式小程序码：放 scripts/../assets/ 下任一文件名即自动 base64 内嵌
const QR_CANDIDATES = ['省柴柴小程序码.png', 'scc-mp-qr.png'].map(f => path.join(__dirname, '..', 'assets', f));
let qrDataUri = '';
for (const p of QR_CANDIDATES) {
  if (fs.existsSync(p)) {
    qrDataUri = 'data:image/png;base64,' + fs.readFileSync(p).toString('base64');
    break;
  }
}
const qrHtml = qrDataUri
  ? `<img src="${qrDataUri}" alt="省柴柴小程序码">`
  : '<div class="qr-ph">正式小程序码<br>放上后自动显示</div>';

const shareText = tm.shareText ||
  `${String(trip.title || '出行文档').replace(/^[\u{1F000}-\u{1FAFF}\u{2600}-\u{27BF}\s]+/u, '')}：每天怎么玩、票哪天抢都排好了，拿走不谢！`;

// ---------- 组装页面 ----------
const html = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${esc(trip.title || '出行文档')}</title>
<style>
:root{--ink:#1a2029;--sub:#6b7280;--muted:#9ca3af;--border:#e8eae5;--bg:#f4f5f2;--teal:#0f766e;
--shadow:0 1px 2px rgba(16,24,40,.04),0 6px 16px rgba(16,24,40,.05);}
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:-apple-system,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans SC",sans-serif;
background:var(--bg);color:var(--ink);-webkit-font-smoothing:antialiased;}
.wrap{max-width:680px;margin:0 auto;padding:0 16px 56px;}

.hero{position:relative;color:#fff;padding:40px 24px 32px;overflow:hidden;
background:linear-gradient(150deg,#0d5c4d 0%,#0f766e 45%,#14a085 100%);}
.hero::after{content:"";position:absolute;inset:0;pointer-events:none;
background:radial-gradient(420px 200px at 85% -10%,rgba(255,255,255,.18),transparent 60%),
radial-gradient(300px 160px at -5% 110%,rgba(255,255,255,.10),transparent 60%);}
.hero-inner{position:relative;z-index:1;max-width:680px;margin:0 auto;}
.hero-brand{display:flex;align-items:center;gap:12px;margin-bottom:14px;}
.hero-logo{width:52px;height:52px;border-radius:14px;object-fit:cover;flex-shrink:0;
border:2px solid rgba(255,255,255,.55);box-shadow:0 2px 8px rgba(0,0,0,.18);}
.hero-kicker{font-size:11px;letter-spacing:4px;opacity:.85;}
.hero h1{font-family:"Noto Serif SC","Songti SC","SimSun",serif;font-size:27px;font-weight:800;line-height:1.4;letter-spacing:1px;}
.hero-route{display:flex;flex-wrap:wrap;align-items:center;gap:6px;margin:18px 0;font-size:12.5px;}
.hero-route .stop{border:1px solid rgba(255,255,255,.35);padding:3px 11px;border-radius:999px;white-space:nowrap;}
.hero-route .arr{opacity:.6;font-size:11px;}
.hero-chips{display:flex;flex-wrap:wrap;gap:8px;font-size:12px;}
.hero-chips span{background:rgba(0,0,0,.16);border-radius:8px;padding:5px 10px;}

.tabs{position:sticky;top:0;z-index:20;display:flex;gap:8px;overflow-x:auto;padding:12px 16px;
background:rgba(244,245,242,.9);backdrop-filter:blur(10px);scrollbar-width:none;
border-bottom:1px solid var(--border);}
.tabs::-webkit-scrollbar{display:none;}
.tab{flex:0 0 auto;border:none;background:transparent;border-radius:10px;
padding:7px 12px;cursor:pointer;text-align:left;transition:all .18s;line-height:1.3;}
.tab .t1{display:block;font-size:13px;font-weight:700;color:var(--sub);}
.tab .t2{display:block;font-size:10.5px;color:var(--muted);margin-top:1px;}
.tab.active{background:var(--teal);}
.tab.active .t1,.tab.active .t2{color:#fff;}

.day{display:none;padding-top:10px;}
.day.active{display:block;animation:fadeIn .35s ease;}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px);}to{opacity:1;}}
.day-head{margin:12px 2px 20px;}
.day-no{font-size:11px;font-weight:800;letter-spacing:3px;color:var(--teal);}
.day-title{font-family:"Noto Serif SC","Songti SC",serif;font-size:21px;font-weight:800;line-height:1.45;margin:5px 0 5px;}
.day-meta{color:var(--sub);font-size:12px;}
.day-intro{font-size:13.5px;color:#5b6470;line-height:1.9;margin:12px 0 0;
border-left:2px solid var(--teal);padding:2px 0 2px 14px;}

.timeline{position:relative;margin-top:20px;padding-left:26px;}
.timeline::before{content:"";position:absolute;left:5px;top:10px;bottom:24px;width:1px;background:#dfe3dd;}
.t-item{position:relative;margin-bottom:14px;}
.t-dot{position:absolute;left:-26px;top:24px;width:9px;height:9px;border-radius:50%;
background:var(--cat,#999);box-shadow:0 0 0 3px var(--bg),0 0 0 4px #dfe3dd;}
.t-card{background:#fff;border:1px solid var(--border);border-radius:16px;padding:17px 19px 15px;
box-shadow:var(--shadow);}
.t-card.warn{border-color:#f3d2d2;}
.t-cat{font-size:10px;font-weight:800;letter-spacing:2.5px;color:var(--cat,#666);margin-bottom:6px;}
.t-cat .en{opacity:.55;font-weight:700;letter-spacing:1.5px;}
.t-name{font-size:16px;font-weight:700;line-height:1.55;letter-spacing:.2px;}
.t-warn{display:inline-block;font-size:10px;font-weight:800;color:#dc2626;background:#fef2f2;
border:1px solid #fecaca;border-radius:6px;padding:2px 7px;margin-left:7px;vertical-align:2px;letter-spacing:.5px;}
.t-desc{font-size:13.5px;color:#535b67;line-height:1.95;margin-top:9px;text-align:justify;}
.t-desc .price{color:#dc2626;font-weight:800;}
.t-desc .hl{color:var(--teal);font-weight:700;}
.t-entries{display:flex;flex-wrap:wrap;gap:8px;margin-top:13px;}

/* 条目内提醒标注（沿用全天提醒的米色 identity） */
.t-tip{margin-top:11px;background:#fdf9ef;border:1px solid #f0e4c8;border-radius:10px;
padding:8px 12px;font-size:12.5px;color:#6f6046;line-height:1.75;}

.entry{display:inline-flex;align-items:center;gap:6px;text-decoration:none;
border:1px solid #d3e3de;border-radius:999px;padding:6px 14px;background:#f5faf8;
font-size:12px;font-weight:600;color:var(--teal);letter-spacing:.5px;transition:all .15s;}
.entry:hover{background:var(--teal);color:#fff;transform:translateY(-1px);
box-shadow:0 4px 10px rgba(15,118,110,.22);}
.entry:hover .arr{color:#fff;}
.entry .arr{color:#8bb3ac;font-size:12px;}

/* 全天通用提醒兜底（收进时间线缩进，与卡片左对齐） */
.day-tips{margin:6px 0 2px;background:#fdf9ef;border:1px solid #f0e4c8;border-radius:14px;
padding:12px 16px;}
.day-tips .dt-h{font-size:10.5px;font-weight:800;color:#a16207;letter-spacing:2.5px;margin-bottom:6px;}
.day-tips ul{list-style:none;}
.day-tips li{font-size:12.5px;color:#6f6046;line-height:1.85;padding-left:2px;margin-bottom:3px;}
.day-tips li:last-child{margin-bottom:0;}

.share-box{display:flex;gap:18px;align-items:center;background:#fff;border:1px solid var(--border);
border-radius:16px;padding:20px;margin-top:32px;box-shadow:var(--shadow);position:relative;}
.share-close{position:absolute;top:6px;right:10px;background:none;border:none;font-size:20px;
color:var(--sub);cursor:pointer;line-height:1;padding:2px 6px;border-radius:4px;}
.share-close:hover{background:#f0f0f0;color:#666;}
.share-main{flex:1;min-width:0;}
.share-h{font-family:"Noto Serif SC","Songti SC",serif;font-size:17px;font-weight:800;}
.share-p{font-size:12.5px;color:var(--sub);line-height:1.85;margin:7px 0 13px;}
.share-p b{color:var(--teal);}
.share-actions{display:flex;flex-wrap:wrap;gap:8px;}
.share-btn{border:none;border-radius:999px;padding:9px 18px;font-size:13px;font-weight:700;
background:var(--teal);color:#fff;cursor:pointer;letter-spacing:.5px;transition:all .15s;
font-family:inherit;}
.share-btn:hover{transform:translateY(-1px);box-shadow:0 4px 10px rgba(15,118,110,.25);}
.share-btn.ghost{background:#f5faf8;color:var(--teal);border:1px solid #d3e3de;}
.share-qr{flex-shrink:0;text-align:center;}
.share-qr img{width:96px;height:96px;border-radius:10px;display:block;margin:0 auto 6px;}
.qr-ph{width:96px;height:96px;border:1.5px dashed #cfd6d1;border-radius:10px;margin:0 auto 6px;
display:flex;align-items:center;justify-content:center;font-size:10.5px;color:var(--muted);
line-height:1.6;text-align:center;padding:8px;}
.share-qr-t{font-size:10.5px;color:var(--sub);line-height:1.6;}
.toast{position:fixed;left:50%;bottom:32px;transform:translateX(-50%) translateY(20px);
background:rgba(26,32,41,.92);color:#fff;font-size:12.5px;padding:9px 18px;border-radius:999px;
opacity:0;pointer-events:none;transition:all .25s;z-index:99;white-space:nowrap;}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0);}

.closing{text-align:center;font-size:15px;color:var(--teal);margin-top:30px;font-weight:700;}
.foot{margin-top:20px;color:var(--muted);font-size:11px;text-align:center;line-height:1.8;
border-top:1px solid var(--border);padding-top:14px;}
@media (min-width:560px){.hero h1{font-size:31px;}}
@media (max-width:560px){
.hero{padding:28px 18px 26px;}
.hero-logo{width:44px;height:44px;border-radius:12px;}
.hero h1{font-size:22px;}
.day-title{font-size:19px;}
.t-desc{font-size:13.5px;line-height:1.9;}
.share-box{flex-direction:column;text-align:center;}
.share-actions{justify-content:center;}}
</style>
</head>
<body>

  <header class="hero">
    <div class="hero-inner">
      <div class="hero-brand">
        ${logoUri ? `<img src="${logoUri}" alt="省柴柴" class="hero-logo">` : ''}
        <div class="hero-kicker">${esc(kicker)}</div>
      </div>
      <h1>${esc(trip.title || '出行文档')}</h1>
      ${routeHtml ? `<div class="hero-route">${routeHtml}</div>` : ''}
      ${chipsHtml ? `<div class="hero-chips">${chipsHtml}</div>` : ''}
    </div>
  </header>

  <div class="wrap">
    <div class="tabs" id="tabs">${renderTabs(trip.itinerary)}</div>

    ${trip.itinerary.map(renderDay).join('')}

    ${showBranding ? `<div class="share-box" id="shareBox">
      <div class="share-close" id="shareClose" title="关闭推广区">×</div>
      <div class="share-main">
        <div class="share-h">觉得这份行程有用？</div>
        <div class="share-p">分享给同行的朋友一起抄作业。想定制自己的行程、比价订酒店，微信搜索 <b>「省柴柴」</b>小程序，直接跟柴柴说就行。</div>
        <div class="share-actions">
          <button class="share-btn" id="shareBtn">📤 分享给朋友</button>
          <button class="share-btn ghost" id="copyMp">关注小程序「省柴柴」</button>
        </div>
      </div>
      <div class="share-qr">${qrHtml}<div class="share-qr-t">微信扫一扫<br>打开省柴柴小程序</div></div>
    </div>` : ''}

    ${trip.closing ? `<p class="closing">${esc(trip.closing)}</p>` : ''}

    <div class="foot">链接打开后以购买页为准 · 价格与可订性实时变化<br>生成于 ${new Date().toLocaleString('zh-CN')}</div>
  </div>

  <div class="toast" id="toast"></div>

<script>
(function(){
  var tabs=document.querySelectorAll('.tab'),panels=document.querySelectorAll('.day');
  tabs.forEach(function(t){t.addEventListener('click',function(){
    tabs.forEach(function(x){x.classList.remove('active');});
    panels.forEach(function(x){x.classList.remove('active');});
    t.classList.add('active');
    document.getElementById(t.getAttribute('data-target')).classList.add('active');
    window.scrollTo({top:0,behavior:'smooth'});
  });});
  document.querySelectorAll('.t-desc').forEach(function(d){
    var html=d.innerHTML;
    html=html.replace(/(¥[\\d,]+(?:\\.\\d+)?(?:-[¥]?[\\d,]+(?:\\.\\d+)?)?)/g,'<span class="price">$1</span>');
    html=html.replace(/(\\d{1,2}:\\d{2}(?:→\\d{1,2}:\\d{2})?)/g,'<span class="hl">$1</span>');
    html=html.replace(/(提前 \\d+ 天开售)/g,'<span class="hl">$1</span>');
    d.innerHTML=html;
  });
  function toast(msg){var t=document.getElementById('toast');t.textContent=msg;
    t.classList.add('show');setTimeout(function(){t.classList.remove('show');},2400);}
  function copyText(txt,okMsg){
    if(navigator.clipboard&&window.isSecureContext){
      navigator.clipboard.writeText(txt).then(function(){toast(okMsg);},function(){legacy();});
    }else legacy();
    function legacy(){var ta=document.createElement('textarea');ta.value=txt;
      ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);
      ta.select();try{document.execCommand('copy');toast(okMsg);}catch(e){toast('复制失败，请手动长按复制');}
      document.body.removeChild(ta);}
  }
  var shareText=${JSON.stringify(shareText)};
  document.getElementById('shareBtn').addEventListener('click',function(){
    if(navigator.share){navigator.share({title:document.title,text:shareText}).catch(function(){});}
    else copyText(shareText,'已复制分享文案，去微信粘贴给朋友吧');
  });
  document.getElementById('copyMp').addEventListener('click',function(){
    copyText('省柴柴','已复制「省柴柴」，去微信搜索小程序');
  });
  ${showBranding ? `var sb=document.getElementById('shareBox');var sc=document.getElementById('shareClose');
    if(sb&&sc)sc.addEventListener('click',function(){sb.style.display='none';});` : ''}
})();
</script>
</body>
</html>`;

fs.writeFileSync(outPath, html, 'utf-8');
const totalDays = trip.itinerary.length;
const totalItems = trip.itinerary.reduce((n, d) => n + (d.items || []).length, 0);
console.log(`已生成: ${outPath}`);
console.log(`${totalDays}天 | ${totalItems}项 | ${(html.length / 1024).toFixed(1)}KB`);
