#!/usr/bin/env node
// xhs-product-trend-fit — 小红书商品宣传方向 / 近2周热度 / 爆款素材分析
// 架构分工（源自探索 SUMMARY §2）：
//   子会话（wc3-code.mjs）：步骤1 方向识别+候选词；步骤5 宣传方向组织+爆款选择+建议
//   代码：搜索页导航、卡片提取、note_id 日期解码/点赞换算/14天窗口、点卡片进详情、详情提取、
//         热度评级、HTML 报告 / res.json / data.md 渲染
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { spawn } from 'node:child_process';
import { join, isAbsolute } from 'node:path';
import { tmpdir } from 'node:os';

/* ------------------------- 常量 ------------------------- */

const RELAY_URL = 'http://127.0.0.1:3459';
const GROUP_NAME = 'xhs-trend-fit';
const TMP = join(tmpdir(), 'skill-run-' + process.pid);
const WC3_CODE = join(import.meta.dirname, 'wc3-code.mjs');

// 时序常量（SUMMARY §3c 实测值）
const SEARCH_WAIT_MS = 6500;        // 搜索页 SPA 加载（tab.create 返回 url/title 为空属正常）
const BETWEEN_SEARCH_MS = 4000;     // 搜索词之间间隔（防验证码墙，实测 >=3.5s）
const CLICK_WAIT_MS = 6000;         // 点卡片后等详情
const DETAIL_POLL_ROUNDS = 4;       // 详情轮询上限
const DETAIL_POLL_MS = 3000;        // 详情轮询间隔
const CARD_POLL_ROUNDS = 3;         // 搜索页卡片补抓轮次
const SCROLL_ROUNDS = 3;            // 目标卡片懒加载补抓轮次
const SCROLL_WAIT_MS = 2500;        // 滚动后等待
const RELAY_TIMEOUT = 45000;

// 业务常量
const HEAT_WINDOW_DAYS = 14;        // 用户口径：近 2 周
const HALF_YEAR_DAYS = 180;         // 素材参考最远窗口：近 6 个月（超过忽略）
const MIN_CARDS_PER_KW = 5;         // 每词有效卡片底线（不足标 partial）
const VIRAL_LIKE_MIN = 100;         // 爆款点赞底线（筛选笔记用）
const LIKE_ACC_MIN = 1000;          // 热度证据：点赞累计门槛（趋势按累加）
const COLLECT_ACC_MIN = 1000;       // 热度证据：收藏累计门槛（趋势按累加）
const MAX_VIRAL_NOTES = 3;          // 素材参考最多 3 篇（2 篇近 14 天 + 1 篇近 6 个月）
const MAX_VIRAL_RECENT = 2;         // 其中近 14 天最多 2 篇
const MAX_KEYWORDS = 6;             // 候选词上限

const SEARCH_URL = (kw) =>
  `https://www.xiaohongshu.com/search_result_ai?keyword=${encodeURIComponent(kw)}`;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

/* ------------------------- Relay 封装（Extension Relay HTTP API，端口 3459） ------------------------- */

async function relayCall(op, params = {}, timeout = RELAY_TIMEOUT) {
  const res = await fetch(`${RELAY_URL}/api/call`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ op, params, timeout }),
  });
  const data = await res.json();
  if (data.error) throw new Error(data.error);
  return data.result;
}

async function ensureRelay() {
  try {
    const status = await (await fetch(`${RELAY_URL}/api/status`)).json();
    if (!status.extensionConnected) throw new Error('Extension not connected');
  } catch (e) {
    throw new Error(`Relay not available at ${RELAY_URL}: ${e.message}`);
  }
}

function pageEval(tabId, code, groupId) {
  return relayCall('page.eval', { tabId, code, groupId });
}

/* ------------------------- 页面 eval 代码（SUMMARY §3a/b 实测选择器） ------------------------- */

// 搜索结果卡片提取（占位行过滤在 Node 侧 cleanCards 做）
const CARD_CODE = `(() => {
  const cards = [...document.querySelectorAll("section.note-item[data-note-id]")];
  const out = cards.map(c => {
    const id = c.getAttribute("data-note-id");
    const titleEl = c.querySelector(".title");
    const authorEl = c.querySelector(".author .name");
    const likeEl = c.querySelector(".like-wrapper .count");
    const imgEl = c.querySelector("a.cover img");
    const linkEl = c.querySelector("a[href*=xsec_token]");
    return { id, title: titleEl ? titleEl.textContent.trim() : "", author: authorEl ? authorEl.textContent.trim() : "",
             like: likeEl ? likeEl.textContent.trim() : "", cover: imgEl ? (imgEl.currentSrc || imgEl.src) : "",
             href: linkEl ? linkEl.getAttribute("href") : "" };
  });
  return JSON.stringify(out);
})()`;

// 定位并点击目标爆款卡片（必须走搜索结果页点卡片进详情，不能独立 explore 直开）
// 选择器用 a.cover.mask, a.cover 兜底：单用 a.cover 首次点击可能弹层不打开（SUMMARY §4）
const CLICK_CODE = (id) => `(() => {
  const a = document.querySelector("section.note-item[data-note-id=\\"${id}\\"] a.cover.mask, section.note-item[data-note-id=\\"${id}\\"] a.cover");
  if (!a) return "NO_CARD";
  a.click();
  return "clicked";
})()`;

// 笔记详情提取（所有字段限定 .note-container 内，避免命中背景推荐流——SUMMARY §4 实测坑）
const DETAIL_CODE = `(() => {
  const c = document.querySelector(".note-container");
  if (!c) return JSON.stringify({loaded:false});
  const title = c.querySelector("#detail-title, .title");
  const authorEl = c.querySelector(".author-wrapper .name, .name-time-wrapper .name, .author .name");
  // 互动数：用具体 wrapper 选择器拿 like/collect/comment 三个独立值（避免 .engage-bar-container 内全量 .count 漏项/错位）
  const likeEl = c.querySelector(".engage-bar-container .like-wrapper .count");
  const collectEl = c.querySelector(".engage-bar-container .collect-wrapper .count");
  const commentEl = c.querySelector(".engage-bar-container .chat-wrapper .count");
  // 粉丝数（尽力）：详情区作者信息附近的粉丝数，拿不到置空
  const fanEl = c.querySelector(".author-wrapper .fans, .author-wrapper [class*=fans], .fans-count, [class*=follower]");
  const desc = c.querySelector("#detail-desc, .desc");
  const coverImgs = [...c.querySelectorAll("img")].map(i => i.currentSrc || i.src).filter(u => u && u.includes("sns-webpic-qc"));
  const comments = [...c.querySelectorAll(".parent-comment")].slice(0, 12).map(p => {
    const content = p.querySelector(".content");
    const likeEl2 = p.querySelector("[class*=like] .count, .like .count");
    return { text: content ? content.textContent.trim() : "", like: likeEl2 ? likeEl2.textContent.trim() : "" };
  });
  return JSON.stringify({loaded:true, title: title ? title.textContent.trim() : "", author: authorEl ? authorEl.textContent.trim() : "",
    like: likeEl ? likeEl.textContent.trim() : "", collect: collectEl ? collectEl.textContent.trim() : "",
    comment: commentEl ? commentEl.textContent.trim() : "", fans: fanEl ? fanEl.textContent.trim() : "",
    desc: desc ? desc.textContent.trim() : "", coverImgs: coverImgs.slice(0,4), comments});
})()`;

// 评论区懒加载滚动（独立滚动容器，window 滚动不触发评论懒加载）
const SCROLL_COMMENTS_CODE = `(() => {
  const scrollers = [...document.querySelectorAll(".note-scroller, .comments-container, .interaction-container")];
  scrollers.forEach(s => { s.scrollTop = s.scrollHeight; });
  window.scrollTo(0, document.body.scrollHeight);
  return "ok";
})()`;

// 当前页卡片 id 列表（懒加载兜底用）
const IDS_CODE = `(() => {
  const ids = [...document.querySelectorAll("section.note-item[data-note-id]")].map(c => c.getAttribute("data-note-id"));
  return JSON.stringify(ids);
})()`;

const SCROLL_BOTTOM_CODE = `(() => { window.scrollTo(0, document.body.scrollHeight); return "ok"; })()`;

/* ------------------------- 数据工具（SUMMARY §3a 步骤4：note_id 解码 + 点赞换算 + 14 天窗口） ------------------------- */

// 有效 note_id：16 位以上纯十六进制；占位行（空 id / UUID 带 #时间戳）在 ID_RE 之外被滤掉
const ID_RE = /^[0-9a-f]{16,}$/;

function likeNum(s) {
  if (!s) return 0;
  s = String(s).trim();
  if (!s || s === '赞') return 0;
  if (s.includes('万')) return Math.round(parseFloat(s) * 10000);
  const n = parseFloat(s);
  return isNaN(n) ? 0 : n;
}

function decodeNoteDate(id) {
  if (!ID_RE.test(id)) return null;
  const ts = parseInt(id.slice(0, 8), 16) * 1000;
  return {
    ts,
    date: new Date(ts).toISOString().slice(0, 10),
    ageDays: Math.round((Date.now() - ts) / 86400000),
  };
}

// 卡片清洗 + 装饰：过滤占位行、补 likeNum/日期/14 天窗口
function cleanCards(cards, kw) {
  return cards
    .filter((c) => c && ID_RE.test(c.id))
    .map((c) => {
      const d = decodeNoteDate(c.id);
      return {
        id: c.id,
        kw,
        title: c.title || '',
        author: c.author || '',
        like: c.like || '',
        likeNum: likeNum(c.like),
        cover: (c.cover || '').startsWith('http') ? c.cover : '',
        href: c.href || '',
        date: d ? d.date : null,
        ageDays: d ? d.ageDays : null,
        in14d: d ? d.ageDays <= HEAT_WINDOW_DAYS : false,
      };
    });
}

/* ------------------------- 子会话调用（subsession-api 封装） ------------------------- */

function callClaudeWithFile(promptContent, promptFile, outputFile, opts = {}) {
  writeFileSync(promptFile, promptContent, 'utf-8');
  return new Promise((resolve, reject) => {
    const args = ['--prompt-file', promptFile, '--output', outputFile];
    if (opts.timeout) args.push('--timeout', String(opts.timeout));
    if (opts.schema) args.push('--schema', opts.schema);
    const child = spawn('node', [WC3_CODE, ...args], { stdio: ['ignore', 'ignore', 'pipe'] });
    let stderr = '';
    child.stderr.on('data', (d) => { stderr += d; });
    child.on('close', (code) => {
      if (code !== 0) return reject(new Error(`wc3-code exit ${code}: ${stderr.slice(0, 300)}`));
      try { resolve(JSON.parse(readFileSync(outputFile, 'utf-8'))); }
      catch { resolve(readFileSync(outputFile, 'utf-8')); }
    });
    child.on('error', reject);
  });
}

// 递归解析子会话返回值（{type:'result'} 壳、代码块包裹、字符串化 JSON 逐层解开）
function extractJson(v) {
  if (typeof v === 'string') {
    const t = v.trim();
    const fence = t.match(/```(?:json)?\s*([\s\S]*?)```/);
    const s = fence ? fence[1] : t;
    try {
      const o = JSON.parse(s);
      if (o && typeof o === 'object') {
        if (o.type === 'result' || 'result' in o) return extractJson(o.result);
        return o;
      }
      return o;
    } catch {}
    const start = s.search(/[\[{]/);
    if (start !== -1) {
      const stack = [];
      for (let i = start; i < s.length; i++) {
        const ch = s[i];
        if (ch === '[' || ch === '{') stack.push(ch);
        else if (ch === ']' || ch === '}') {
          stack.pop();
          if (stack.length === 0) {
            try { return JSON.parse(s.slice(start, i + 1)); } catch {}
            break;
          }
        }
      }
    }
    return null;
  }
  if (v && typeof v === 'object') {
    if (v.type === 'result' || 'result' in v) return extractJson(v.result);
    return v;
  }
  return null;
}

/* ------------------------- 子会话 1：方向识别 + 候选词（SUMMARY §2 步骤1） ------------------------- */

const STEP1_SCHEMA = {
  type: 'object',
  required: ['direction_desc', 'keywords'],
  properties: {
    direction_desc: { type: 'string' },
    keywords: { type: 'array', items: { type: 'string' } },
  },
};

function step1Prompt(productDesc, productImage) {
  return `你是小红书商品方向识别助手。根据商品信息，识别商品关联的「方向」（品类/风格/场景），并生成用于小红书搜索的候选词。

【商品介绍文字】
${productDesc || '（未提供）'}

${productImage ? `【商品图片路径】
${productImage}
（可用 Read 工具读取该图片文件辅助识别；若图片无法读取或路径无效，仅凭上面的介绍文字识别即可，不要失败。）` : ''}

【识别要求】
1. direction_desc：一句话描述商品的品类/风格/场景方向。格式如"<品类/单品>，<风格>风格，场景为<场景>，面向<人群>"（按商品实际情况填写，不要照抄此格式示例的具体内容）。
2. keywords：3~6 个小红书可搜候选词，按 主品类/风格/单品/场景 四维展开。硬规则：
   - 优先给「场景词」（场景词热度通常高于单品词）；
   - 每个词必须带品类限定词避免歧义（如"<风格>+<品类>"组合词；禁止只写"<品类>餐厅"这类可能被理解成餐饮推荐的裸场景词）；
   - 避免过短泛词（如"餐桌""家居"这类宽泛词）。
3. 只输出一个 JSON 对象，格式如下，不要输出其他内容：
{"direction_desc": "方向描述", "keywords": ["词1", "词2", "词3"]}`;
}

async function step1Identify(productDesc, productImage) {
  const schemaFile = join(TMP, 'step1_schema.json');
  writeFileSync(schemaFile, JSON.stringify(STEP1_SCHEMA));
  const raw = await callClaudeWithFile(
    step1Prompt(productDesc, productImage),
    join(TMP, 'step1_prompt.md'),
    join(TMP, 'step1_out.json'),
    { schema: schemaFile }
  );
  const obj = extractJson(raw);
  if (!obj || typeof obj !== 'object') throw new Error('方向识别子会话返回无法解析');
  const directionDesc = String(obj.direction_desc || '').trim();
  const keywords = Array.isArray(obj.keywords)
    ? obj.keywords.map((k) => String(k).trim()).filter(Boolean)
    : [];
  if (!directionDesc) throw new Error('方向识别子会话未返回 direction_desc');
  if (keywords.length < 1) throw new Error('方向识别子会话未返回候选词');
  return { direction_desc: directionDesc, keywords };
}

/* ------------------------- 子会话 5：宣传方向组织 + 爆款选择 + 建议（SUMMARY §2 步骤5） ------------------------- */

const STEP5_SCHEMA = {
  type: 'object',
  required: ['direction', 'viral_notes'],
  properties: {
    direction: { type: 'string' },
    viral_notes: { type: 'array', items: { type: 'string' } },
  },
  additionalProperties: true, // forms 等扩展字段不参与 schema 校验，代码侧防御式读取
};

function step5Prompt(directionDesc, kwGroups) {
  const lines = kwGroups.map((g) => {
    const head = `【候选词：${g.kw}】（有效卡片 ${g.cards.length} 张${g.partial ? '，结果量少' : ''}）`;
    // 控制 prompt 体量：按点赞降序取前 25，再补上未入选的近 14 天新帖（新爆款信号不能丢）
    const sorted = g.cards.slice().sort((a, b) => b.likeNum - a.likeNum);
    const top = sorted.slice(0, 25);
    for (const c of sorted) {
      if (top.length >= 35) break;
      if (c.in14d && !top.includes(c)) top.push(c);
    }
    const rows = top
      .map((c) => {
        const new14 = c.in14d ? ' [NEW14D]' : '';
        const title = (c.title || '').slice(0, 50);
        return `- ${c.id} | ${c.likeNum}赞${new14} | ${c.date || '日期未知'} | ${(c.author || '').slice(0, 20)} | ${title}`;
      })
      .join('\n');
    return `${head}\n${rows}`;
  });
  return `你是小红书商品宣传策划。以下是一个商品在某几个候选搜索词下的小红书搜索结果（全部为公开可见的真实数据）。请基于这些结果完成 3 件事。

【商品方向（上一步识别）】
${directionDesc}

【各候选词搜索结果】
${lines.join('\n\n')}

【任务】
1. 归纳 1 个明确的「宣传方向」direction（不是搜索词本身，而是一句话描述这个商品在小红书应该怎么定位/宣传。格式如"<风格/品类>·场景化种草：把商品放进真实使用场景种草，主打<氛围/风格/可抄作业>，而非单品白底图展示"——按下方真实数据归纳，不要照抄格式示例的具体内容）。
2. 选出 2~3 篇支撑该方向的爆款笔记 viral_notes（数组存 note_id）：
   - 必须是上方数据中真实出现的 note_id；
   - 点赞数 >= ${VIRAL_LIKE_MIN}；
   - 题材与商品方向匹配；
   - 剔除：官方号/品牌号（作者名含"旗舰店/官方/家居薯"等）、卖课引流贴（标题含"训练营/0.1元/保姆级"等且互动异常）、词义错位帖（标题与商品方向无关）；
   - 时间要求：优先选近 14 天新爆款（最多 2 篇，上方标 [NEW14D] 的）；再补 1 篇近 6 个月（180 天）内的历史爆款；**超过 6 个月（180 天）的笔记一律不选**；
   - 若所有词都无赞>=${VIRAL_LIKE_MIN} 的匹配笔记，viral_notes 返回空数组 []。
3. 给每篇入选爆款标注 forms（对象：note_id -> 简短形态描述，如"Roomtour 沉浸式参观"/"装修干货·抄作业清单"/"设计案例·氛围感审美"等，报告不展示，仅供内部参考）。

只输出一个 JSON 对象，格式如下，不要输出其他内容：
{"direction": "宣传方向", "viral_notes": ["note_id", ...], "forms": {"note_id": "形态"}}`;
}

async function step5Plan(directionDesc, kwGroups) {
  const schemaFile = join(TMP, 'step5_schema.json');
  writeFileSync(schemaFile, JSON.stringify(STEP5_SCHEMA));
  const raw = await callClaudeWithFile(
    step5Prompt(directionDesc, kwGroups),
    join(TMP, 'step5_prompt.md'),
    join(TMP, 'step5_out.json'),
    { schema: schemaFile }
  );
  const obj = extractJson(raw);
  if (!obj || typeof obj !== 'object') throw new Error('方向组织子会话返回无法解析');
  const direction = String(obj.direction || '').trim();
  if (!direction) throw new Error('方向组织子会话未返回 direction');
  const viral_notes = Array.isArray(obj.viral_notes) ? obj.viral_notes.map((x) => String(x).trim()).filter(Boolean) : [];
  const forms = obj.forms && typeof obj.forms === 'object' ? obj.forms : {};
  return { direction, viral_notes, forms };
}

/* ------------------------- 子会话 6：爆款分析（为什么这篇能爆） ------------------------- */

const STEP6_SCHEMA = {
  type: 'object',
  required: ['fans', 'titleHook', 'coverWhy', 'contentStruct', 'userPoint'],
  properties: {
    fans: { type: 'string' },
    titleHook: { type: 'string' },
    coverWhy: { type: 'string' },
    contentStruct: { type: 'string' },
    userPoint: { type: 'string' },
  },
};

function step6Prompt(note) {
  const comments = (note.comments || []).slice(0, 6).map((c) => `- ${c.text || ''}`.slice(0, 80)).join('\n');
  return `你是小红书爆款内容分析师。以下是一篇真实的小红书爆款笔记（公开可见数据）。请分析它**为什么能爆**——不是复述它写了什么，而是拆解它抓中了用户的什么心理/需求、用对了什么手法。

【笔记信息】
- 标题：${note.title || '（未获取）'}
- 作者：${note.author || '未知'}
- 作者粉丝数：${note.fans || '（未获取）'}
- 点赞：${note.likeText || '未知'} ｜ 收藏：${note.collectText || '未知'} ｜ 评论：${note.commentText || '未知'}
- 发布日期：${note.date || '未知'}
- 正文（节选）：${(note.descText || '').slice(0, 300) || '（正文较薄）'}

【评论区（节选）】
${comments || '（无）'}

【分析要求】从以下 5 个角度分别分析，**每个角度输出为一个独立字段，各 1~2 句，不要合并成一段**：
1. fans（粉丝基础）：作者粉丝量级对爆款的影响（粉丝数未知则从内容风格推断账号阶段，并注明"粉丝数未知"）
2. titleHook（标题钩子）：标题用了什么钩子（数字/反差/悬念/情绪词/人群标签）
3. coverWhy（首图/封面）：首图为什么抓人（从正文与标题推断画面呈现方式）
4. contentStruct（内容结构）：正文怎么组织（清单/步骤/对比/沉浸叙事），信息密度如何
5. userPoint（抓用户什么点）：戳中了用户的什么心理（抄作业/省钱/避坑/情绪共鸣/身份认同）

只输出一个 JSON 对象，格式如下，不要输出其他内容：
{"fans": "粉丝基础分析", "titleHook": "标题钩子分析", "coverWhy": "首图分析", "contentStruct": "内容结构分析", "userPoint": "抓用户什么点分析"}`;
}

async function step6Analyze(note) {
  const schemaFile = join(TMP, 'step6_schema.json');
  writeFileSync(schemaFile, JSON.stringify(STEP6_SCHEMA));
  const raw = await callClaudeWithFile(
    step6Prompt(note),
    join(TMP, 'step6_prompt.md'),
    join(TMP, 'step6_out.json'),
    { schema: schemaFile }
  );
  const obj = extractJson(raw);
  if (!obj || typeof obj !== 'object') throw new Error('爆款分析子会话返回无法解析');
  return {
    fans: String(obj.fans || '').trim(),
    titleHook: String(obj.titleHook || '').trim(),
    coverWhy: String(obj.coverWhy || '').trim(),
    contentStruct: String(obj.contentStruct || '').trim(),
    userPoint: String(obj.userPoint || '').trim(),
  };
}

/* ------------------------- 搜索与提取（代码步骤 2/3/6/7） ------------------------- */

// 单个候选词搜索：直连 AI 搜索页（SUMMARY §4：首页搜索框真人输入路径会被 Vue 清空，不可用）
async function searchKeyword(kw, groupId) {
  const url = SEARCH_URL(kw);
  const tab = await relayCall('tab.create', { url, active: true, groupId });
  const tabId = tab.id;
  try {
    await sleep(SEARCH_WAIT_MS);
    let cards = [];
    for (let i = 0; i < CARD_POLL_ROUNDS; i++) {
      try {
        const r = await pageEval(tabId, CARD_CODE, groupId);
        const parsed = JSON.parse(r);
        if (Array.isArray(parsed)) cards = parsed;
      } catch {}
      if (cards.length >= 30) break;
      await pageEval(tabId, SCROLL_BOTTOM_CODE, groupId).catch(() => {});
      await sleep(SCROLL_WAIT_MS);
    }
    return { kw, cards: cleanCards(cards, kw) };
  } finally {
    await relayCall('tab.close', { tabId, groupId }).catch(() => {});
  }
}

// 检查目标卡片是否在当前搜索页，可滚动懒加载补抓（SUMMARY §3c：目标卡片可能不在首屏/换页后消失）
async function findCard(tabId, noteId, groupId) {
  for (let round = 0; round <= SCROLL_ROUNDS; round++) {
    try {
      const r = await pageEval(tabId, IDS_CODE, groupId);
      const ids = JSON.parse(r);
      if (Array.isArray(ids) && ids.includes(noteId)) return true;
    } catch {}
    if (round < SCROLL_ROUNDS) {
      await pageEval(tabId, SCROLL_BOTTOM_CODE, groupId).catch(() => {});
      await sleep(SCROLL_WAIT_MS);
    }
  }
  return false;
}

// 详情提取 + 评论懒加载补抓（去重合并；互动数 engage-bar 渲染慢于 note-container，须轮询到 like/collect 非空）
async function extractDetail(tabId, groupId) {
  let detail = null;
  for (let i = 0; i < DETAIL_POLL_ROUNDS + 2; i++) {
    try {
      const r = await pageEval(tabId, DETAIL_CODE, groupId);
      const d = JSON.parse(r);
      if (d && d.loaded) {
        detail = d;
        // 互动数齐全（like/collect 任一非空）即视为渲染完成，提前 break
        if (d.like || d.collect || d.comment) break;
      }
    } catch {}
    await sleep(DETAIL_POLL_MS);
  }
  if (!detail) return null;
  try {
    await pageEval(tabId, SCROLL_COMMENTS_CODE, groupId);
    await sleep(3000);
    const r2 = await pageEval(tabId, DETAIL_CODE, groupId);
    const d2 = JSON.parse(r2);
    if (d2 && d2.loaded) {
      const seen = new Set((detail.comments || []).map((c) => c.text));
      for (const c of d2.comments || []) {
        if (!seen.has(c.text)) detail.comments.push(c);
        seen.add(c.text);
      }
      if (!detail.title && d2.title) detail.title = d2.title;
      if (!detail.desc && d2.desc) detail.desc = d2.desc;
      if (!detail.like && d2.like) detail.like = d2.like;
      if (!detail.collect && d2.collect) detail.collect = d2.collect;
      if (!detail.comment && d2.comment) detail.comment = d2.comment;
      if (!detail.fans && d2.fans) detail.fans = d2.fans;
    }
  } catch {}
  return detail;
}

// 单篇爆款深挖：在搜索结果页定位并点卡片进详情（SUMMARY §4：不能独立打开 explore 详情 URL，会落推荐流）
// 目标卡片可能不在首屏/换页后消失 → id 存在性检查 + 滚动补抓 + 换备用候选词重试（不同 keyword 卡片集合有差异）
async function deepDive(note, kwCandidates, groupId) {
  const attempts = [...new Set([note.kw, ...kwCandidates])];
  for (const kw of attempts) {
    const url = SEARCH_URL(kw);
    let tab;
    try {
      tab = await relayCall('tab.create', { url, active: true, groupId });
      await sleep(SEARCH_WAIT_MS);
      const found = await findCard(tab.id, note.id, groupId);
      if (!found) {
        await relayCall('tab.close', { tabId: tab.id, groupId }).catch(() => {});
        tab = null;
        await sleep(BETWEEN_SEARCH_MS);
        continue;
      }
      await pageEval(tab.id, CLICK_CODE(note.id), groupId).catch(() => {});
      await sleep(CLICK_WAIT_MS);
      const detail = await extractDetail(tab.id, groupId);
      await relayCall('tab.close', { tabId: tab.id, groupId }).catch(() => {});
      tab = null;
      if (detail) return { ...note, detail };
    } catch (e) {
      console.error(`[deepdive] ${note.id} ${kw} err: ${e.message}`);
    } finally {
      if (tab) await relayCall('tab.close', { tabId: tab.id, groupId }).catch(() => {});
    }
    await sleep(BETWEEN_SEARCH_MS);
  }
  return null;
}

/* ------------------------- 热度评级（代码步骤 8，SUMMARY §3a 规则，累计口径） ------------------------- */

// 热度证据按「趋势累加」口径：点赞累计 >= 1000、收藏累计 >= 1000 各自独立成行
function rateHeat(allCards, kwStats, materialNotes) {
  const total = allCards.length;
  const newIn = allCards.filter((c) => c.in14d);
  // 点赞累计证据：近 2 周新帖中点赞 >= 1000 的（趋势信号强）
  const likeAcc = newIn.filter((c) => c.likeNum >= LIKE_ACC_MIN);
  // 收藏累计证据：素材深挖笔记中收藏 >= 1000 的（收藏数只在详情弹层可得）
  const collectNum = (s) => {
    const t = String(s || '').trim();
    if (!t || t === '—' || t === '-') return 0;
    if (t.includes('万')) return Math.round(parseFloat(t) * 10000);
    const n = parseFloat(t);
    return isNaN(n) ? 0 : n;
  };
  const collectAcc = (materialNotes || []).filter((m) => collectNum(m.collectText) >= COLLECT_ACC_MIN);
  // 头部最高赞只统计近 6 个月（180 天）内，超过的忽略（用户口径：整体过滤时间）
  const halfYearCards = allCards.filter((c) => c.ageDays == null || c.ageDays <= HALF_YEAR_DAYS);
  const maxLike = halfYearCards.length ? Math.max(...halfYearCards.map((c) => c.likeNum)) : 0;
  const maxNew = newIn.length ? Math.max(...newIn.map((c) => c.likeNum)) : 0;
  const allKwThin = kwStats && kwStats.length && kwStats.every((s) => s.total < MIN_CARDS_PER_KW);
  let level;
  if (allKwThin || total < MIN_CARDS_PER_KW) level = '无';
  else if (likeAcc.length >= 1 || collectAcc.length >= 1) level = '高';
  else if (newIn.some((c) => c.likeNum >= 100 && c.likeNum <= 999)) level = '中';
  else if (newIn.length >= 2 && maxNew >= 100) level = '中';
  else level = '低';
  return {
    level,
    total,
    newInCount: newIn.length,
    likeAcc: likeAcc.map((v) => ({ title: v.title, author: v.author, likeNum: v.likeNum, date: v.date, id: v.id })),
    collectAcc: collectAcc.map((v) => ({ title: v.title, author: v.author, collectText: v.collectText, date: v.date, id: v.id })),
    maxLike,
    maxNew,
  };
}

function heatEvidenceText(heat) {
  const parts = [];
  if (heat.likeAcc.length) {
    parts.push(
      `近 2 周点赞累计≥${LIKE_ACC_MIN} 的笔记 ${heat.likeAcc.length} 篇：` +
        heat.likeAcc.map((v) => `《${(v.title || '').slice(0, 20)}》+${v.likeNum}赞（${v.date}）`).join('、')
    );
  } else {
    parts.push(`近 2 周无点赞累计≥${LIKE_ACC_MIN} 的新笔记`);
  }
  if (heat.collectAcc.length) {
    parts.push(
      `素材参考中收藏累计≥${COLLECT_ACC_MIN} 的笔记 ${heat.collectAcc.length} 篇：` +
        heat.collectAcc.map((v) => `《${(v.title || '').slice(0, 20)}》${v.collectText}收藏（${v.date}）`).join('、')
    );
  } else {
    parts.push(`素材参考笔记无收藏累计≥${COLLECT_ACC_MIN}`);
  }
  return parts.join('；');
}

/* ------------------------- 素材整理（代码，含确定性信号提取） ------------------------- */

function classifyForm(title) {
  const t = title || '';
  if (/roomtour|沉浸式参观|带逛|参观/i.test(t)) return 'Roomtour 沉浸式参观（视频）';
  if (/抄作业|清单|照着装/i.test(t)) return '装修干货·抄作业清单';
  if (/避坑|指南|教程|干货|一篇讲清楚|攻略/i.test(t)) return '干货教程·避坑指南';
  if (/合集|灵感|风格/i.test(t)) return '风格合集/灵感';
  if (/测评|开箱|单品/i.test(t)) return '单品测评/展示';
  return '家居种草展示';
}

function descSummary(desc) {
  if (!desc) return { text: '（无正文或正文较薄，视频帖常见）', tags: [] };
  const lines = desc.split('\n').map((s) => s.trim()).filter(Boolean);
  const tags = lines.filter((l) => l.startsWith('#') || l.startsWith('@'));
  const body = lines.filter((l) => !l.startsWith('#') && !l.startsWith('@'));
  const text = body.join(' ').slice(0, 120) || '（正文仅标签）';
  return { text, tags: tags.slice(0, 10) };
}

function commentSignals(comments) {
  const texts = (comments || []).map((c) => c.text || '').filter(Boolean);
  if (!texts.length) return '（评论较少或无显著信号）';
  const signals = [];
  const buy = texts.filter((t) => /链接|多少钱|价格|哪里买|在哪买|求购|同款|tb|淘宝/.test(t));
  const spec = texts.filter((t) => /尺寸|多大|参数|规格|长度|宽度|材质/.test(t));
  const color = texts.filter((t) => /颜色|色号|搭配|怎么配/.test(t));
  if (buy.length) signals.push(`高频求链接/询价（${buy.length} 条）`);
  if (spec.length) signals.push(`问尺寸/参数/材质（${spec.length} 条）`);
  if (color.length) signals.push(`问颜色/搭配（${color.length} 条）`);
  const sample = texts.slice(0, 3).map((t) => t.slice(0, 30)).join('｜');
  return (signals.length ? signals.join('；') + '。' : '') + `示例评论：${sample}`;
}

/* ------------------------- 报告渲染（代码步骤 9） ------------------------- */

function esc(s) {
  return String(s ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function renderHtml(d) {
  const kwRows = d.kwStats
    .map(
      (s) => `<tr><td>${esc(s.kw)}</td><td>${s.total}</td><td>${s.newInWindow}</td><td>${s.newViralCount}</td><td>${s.maxLike}</td></tr>`
    )
    .join('\n');

  const noteCards = d.materialNotes
    .map((m, i) => {
      const cover = m.cover
        ? `<img class="cover" src="${esc(m.cover)}" alt="封面图" onerror="this.style.display='none'">`
        : '<p class="form">（封面图未获取）</p>';
      // 爆款分析：5 个维度分块展示（子会话结构化输出；旧数据/失败时降级为正文要点）
      const a = m.analysis && typeof m.analysis === 'object' ? m.analysis : null;
      const dims = a
        ? [
            ['粉丝基础', a.fans],
            ['标题钩子', a.titleHook],
            ['首图/封面', a.coverWhy],
            ['内容结构', a.contentStruct],
            ['抓用户什么点', a.userPoint],
          ]
        : [];
      const analysisBlocks = dims
        .filter(([, v]) => v)
        .map(([label, v]) => `<div class="dim"><span class="dim-label">${label}</span><span class="dim-text">${esc(v)}</span></div>`)
        .join('\n');
      const analysisHtml = analysisBlocks
        ? `<div class="analysis"><div class="analysis-title">爆款分析</div>${analysisBlocks}</div>`
        : `<div class="form"><b>正文要点：</b>${esc(m.descText || '（分析未生成）')}</div>`;
      return `<div class="note-card">
  <h3>${i + 1}. ${esc(m.title || '(标题未获取)')}</h3>
  <div class="meta">作者：${esc(m.author || '未知')} ｜ 发布：${m.date || '未知'} ｜ 搜索词：${esc(m.kw)} ｜ 粉丝：${esc(m.fans || '未知')}</div>
  <div><span class="stat">❤ 点赞 ${esc(m.likeText)}</span><span class="stat">⭐ 收藏 ${esc(m.collectText)}</span><span class="stat">💬 评论 ${esc(m.commentText)}</span></div>
  ${cover}
  ${analysisHtml}
</div>`;
    })
    .join('\n');

  const heatBadgeClass = d.heatLevel === '高' ? 'high' : d.heatLevel === '中' ? 'mid' : d.heatLevel === '低' ? 'low' : 'none';

  const productImg = d.productImageDataUri
    ? `<img class="product-img" src="${d.productImageDataUri}" alt="商品图片">`
    : '<p class="form">（商品图片未获取）</p>';

  return `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>小红书商品宣传分析报告 · ${esc(d.productDesc.slice(0, 30))}</title>
<style>
  :root { --primary:#4cc9a5; --primary-dark:#2da584; --bg:#f3fbf8; --card:#ffffff; --text:#1f2d2a; --muted:#7a8f88; --accent:#ff8a5c; --line:#dff2ea; }
  * { box-sizing:border-box; margin:0; padding:0; }
  body { font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif; background:var(--bg); color:var(--text); line-height:1.7; }
  .wrap { max-width:980px; margin:0 auto; padding:32px 20px 64px; }
  header.hero { background:linear-gradient(135deg,#56cc9d,#2da584 55%,#1f8a6d); color:#fff; border-radius:16px; padding:36px 40px; margin-bottom:28px; box-shadow:0 6px 24px rgba(45,165,132,.25); }
  header.hero h1 { font-size:26px; margin-bottom:8px; }
  header.hero p { opacity:.95; font-size:14px; }
  .badge { display:inline-block; background:rgba(255,255,255,.2); border:1px solid rgba(255,255,255,.4); padding:2px 12px; border-radius:20px; font-size:12px; margin-right:6px; }
  section { background:var(--card); border-radius:14px; padding:28px 32px; margin-bottom:22px; box-shadow:0 2px 12px rgba(76,201,165,.1); }
  h2 { font-size:20px; color:var(--primary-dark); margin-bottom:16px; padding-left:12px; border-left:5px solid var(--primary); }
  h3 { font-size:16px; margin:18px 0 8px; color:var(--primary-dark); }
  table { width:100%; border-collapse:collapse; font-size:14px; margin:12px 0; }
  th,td { border:1px solid var(--line); padding:9px 12px; text-align:left; vertical-align:top; }
  th { background:#eefaf5; color:var(--primary-dark); font-weight:600; }
  .heat { display:inline-block; color:#fff; font-weight:700; font-size:15px; padding:3px 14px; border-radius:20px; }
  .heat.high { background:#ff8a5c; } .heat.mid { background:#ffb74d; } .heat.low { background:#90a4ae; } .heat.none { background:#b0bec5; }
  .note-card { border:1px solid var(--line); border-radius:12px; padding:18px; margin-bottom:18px; background:#fff; }
  .note-card .cover { width:100%; border-radius:8px; margin:10px 0; max-height:300px; object-fit:cover; }
  .note-card .meta { font-size:13px; color:var(--muted); margin-bottom:6px; }
  .note-card .stat { display:inline-block; background:#eefaf5; border-radius:6px; padding:2px 10px; font-size:13px; margin-right:8px; color:var(--primary-dark); }
  .analysis { font-size:14px; color:var(--text); background:#f6fdfa; border-left:3px solid var(--primary); border-radius:6px; padding:12px 14px; margin-top:10px; line-height:1.8; }
  .analysis-title { font-weight:700; color:var(--primary-dark); margin-bottom:8px; font-size:14px; }
  .dim { display:flex; gap:8px; margin-bottom:6px; }
  .dim-label { flex:0 0 76px; background:var(--primary); color:#fff; font-size:12px; border-radius:10px; padding:1px 8px; text-align:center; height:fit-content; margin-top:3px; }
  .dim-text { flex:1; font-size:13px; }
  .product-img { width:100%; max-width:420px; border-radius:12px; margin:10px 0; display:block; }
  .form { font-size:13px; color:var(--muted); background:#f6fdfa; border-radius:8px; padding:12px 14px; margin-top:8px; }
  footer { text-align:center; color:var(--muted); font-size:12px; margin-top:28px; }
</style>
</head>
<body>
<div class="wrap">

<header class="hero">
  <h1>小红书商品宣传分析报告</h1>
  <p>商品：${esc(d.productDesc)}</p>
  <p style="margin-top:10px;">
    <span class="badge">分析日期 ${d.date}</span>
    <span class="badge">热度窗口：近 2 周（累计口径）</span>
    <span class="badge">数据源：小红书真实搜索 + 笔记详情（公开可见）</span>
  </p>
</header>

<section>
  <h2>一、商品方向</h2>
  ${productImg}
  <p><b>商品介绍：</b>${esc(d.productDesc)}</p>
  <h3>识别出的方向</h3>
  <p>${esc(d.directionDesc)}</p>
  <h3>候选搜索词（${d.kwStats.length} 个，按 主品类/风格/单品/场景 四维展开）</h3>
  <table>
    <tr><th>候选词</th><th>笔记数</th><th>近14天新帖</th><th>近14天新爆款(≥${VIRAL_LIKE_MIN})</th><th>头部最高赞(近6个月)</th></tr>
    ${kwRows}
  </table>
  <p class="form">识别依据：候选词覆盖主品类/风格/单品/场景四维，且每个词均在小红书返回足量笔记（标题/作者/点赞/封面均来自搜索结果页公开数据）。</p>
</section>

<section>
  <h2>二、热度趋势判断（按宣传方向）</h2>
  <h3>宣传方向（1 个）</h3>
  <p><b>「${esc(d.direction)}」</b></p>
  <h3>热度结论：<span class="heat ${heatBadgeClass}">${d.heatLevel}</span></h3>
  ${d.heatNote ? `<p class="form"><b>说明：</b>${esc(d.heatNote)}</p>` : ''}
  <table>
    <tr><th>证据维度</th><th>支撑证据</th></tr>
    <tr><td>近 2 周点赞累计≥${LIKE_ACC_MIN}</td><td>${esc(d.heatLikeAccText)}</td></tr>
    <tr><td>素材参考收藏累计≥${COLLECT_ACC_MIN}</td><td>${esc(d.heatCollectAccText)}</td></tr>
    <tr><td>近 2 周新帖数量</td><td>${d.heatNewInCount} 篇</td></tr>
    <tr><td>头部互动水平（近 6 个月）</td><td>最高 ${d.heatMaxLike} 赞</td></tr>
  </table>
  <p class="form"><b>结论：</b>${esc(d.heatConclusion)}</p>
</section>

<section>
  <h2>三、素材参考（爆款笔记详解 · ${d.materialNotes.length} 篇）</h2>
  ${d.materialNoteNone ? `<p class="form">${esc(d.materialNoteNone)}</p>` : ''}
  ${noteCards}
</section>

<footer>数据来源：小红书 Web 搜索结果页 + 笔记详情弹层（全部为公开可见信息，未抓取登录后可见数据）。热度按累计口径：点赞/收藏各自累计≥1000 独立成证据。</footer>
</div>
</body>
</html>`;
}

function renderDataMd(d) {
  const kwRows = d.kwStats
    .map(
      (s) =>
        `| ${s.kw} | ${s.total} | ${s.newInWindow} | ${s.newViralCount} | ${s.maxLike} |`
    )
    .join('\n');

  const noteCards = d.materialNotes
    .map((m, i) => {
      // 爆款分析：5 个维度分块展示（结构化输出；失败/旧数据降级为正文要点）
      const a = m.analysis && typeof m.analysis === 'object' ? m.analysis : null;
      const dims = a
        ? [
            ['粉丝基础', a.fans],
            ['标题钩子', a.titleHook],
            ['首图/封面', a.coverWhy],
            ['内容结构', a.contentStruct],
            ['抓用户什么点', a.userPoint],
          ].filter(([, v]) => v)
        : [];
      const analysisMd = dims.length
        ? dims.map(([label, v]) => `  - **${label}**：${v}`).join('\n')
        : `  - （分析未生成）${m.descText ? `正文要点：${m.descText}` : ''}`;
      return `### 笔记 ${i + 1}：${m.title || '(标题未获取)'}

- **作者**：${m.author || '未知'}（粉丝 ${m.fans || '未知'}）
- **互动**：点赞 ${m.likeText} ｜ 收藏 ${m.collectText} ｜ 评论 ${m.commentText}
- **发布日期**：${m.date || '未知'}
- **搜索词**：${m.kw}
- **封面图 URL**：${m.cover || '（未获取）'}
- **爆款分析**：
${analysisMd}`;
    })
    .join('\n\n');

  return `# 小红书商品宣传分析 · 数据明细（data.md）

> 商品：${d.productDesc}
> 分析日期：${d.date} ｜ 热度窗口：近 2 周（${d.windowStart} ~ ${d.windowEnd}），累计口径
> 数据来源：小红书 Web 搜索结果页 + 笔记详情弹层（全部公开可见信息，未抓取登录后可见数据）

---

## 一、商品方向识别

- **商品介绍**：${d.productDesc}
- **识别结果**：${d.directionDesc}
- **候选搜索词（${d.kwStats.length} 个）**：

| 候选词 | 笔记数 | 近14天新帖 | 近14天新爆款(≥${VIRAL_LIKE_MIN}) | 头部最高赞(近6个月) |
|--------|--------|-----------|-------------------|-----------|
${kwRows}

---

## 二、热度趋势判断（按宣传方向）

- **宣传方向（1 个）**：${d.direction}
- **热度评级**：${d.heatLevel}
${d.heatNote ? `- **说明**：${d.heatNote}` : ''}
- **支撑证据**：
  - 近 2 周点赞累计≥${LIKE_ACC_MIN}：${d.heatLikeAccText}
  - 素材参考收藏累计≥${COLLECT_ACC_MIN}：${d.heatCollectAccText}
  - 近 2 周新帖数量：${d.heatNewInCount} 篇
  - 头部互动水平（近 6 个月）：最高 ${d.heatMaxLike} 赞
- **结论**：${d.heatConclusion}

---

## 三、素材参考（爆款笔记详解，${d.materialNotes.length} 篇）

${d.materialNoteNone ? `> ${d.materialNoteNone}\n` : ''}
${noteCards}

---

## 附：热度统计规则（代码可验证）

- 点赞换算：含"万"→ 数字×10000；"赞"占位或空 → 0
- note_id 前 8 位 = hex 编码 Unix 时间戳 → 解码发布日期；ageDays <= 14 记为近 2 周新帖
- 热度按累计口径：近 2 周点赞累计≥1000、素材参考收藏累计≥1000，各自独立成证据行
- 素材参考最多 3 篇：2 篇近 14 天新爆款 + 1 篇近 6 个月历史爆款；超过 6 个月（180 天）忽略
`;
}

/* ------------------------- 入口 ------------------------- */

function readInput() {
  let input = {};
  const inputPath = process.argv[2];
  if (inputPath) {
    input = JSON.parse(readFileSync(inputPath, 'utf-8'));
  } else {
    try {
      input = JSON.parse(readFileSync('input.json', 'utf-8'));
    } catch {}
  }
  return input;
}

async function main() {
  const input = readInput();
  const productDesc = String(input.product_desc || '').trim();
  const productImage = String(input.product_image || '').trim();
  if (!productDesc && !productImage) {
    throw new Error('product_desc 与 product_image 均为空，无法识别商品方向');
  }

  // 产出路径全部来自入参 output_dir / output_files，绝不写裸相对路径（避免 CWD 漂移）
  const outputDir = input.output_dir || process.cwd();
  const outFiles = input.output_files || {};
  const resultFile = join(outputDir, outFiles.result || 'res.json');
  const dataFile = join(outputDir, outFiles.data || 'data.md');

  const now = new Date();
  const pad = (n) => String(n).padStart(2, '0');
  const dateStr = `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())}`;
  const windowStart = new Date(now.getTime() - HEAT_WINDOW_DAYS * 86400000);
  const windowStartStr = `${windowStart.getFullYear()}-${pad(windowStart.getMonth() + 1)}-${pad(windowStart.getDate())}`;

  const defaultReport = join(outputDir, `小红书商品宣传分析报告_${dateStr}.html`);
  const reportPath = input.report_path
    ? (isAbsolute(input.report_path) ? input.report_path : join(outputDir, input.report_path))
    : defaultReport;

  mkdirSync(outputDir, { recursive: true });
  mkdirSync(TMP, { recursive: true });

  const warnings = [];
  let status = 'success';
  let groupId = null;
  try {
    await ensureRelay();

    const g = await relayCall('group.create', { name: GROUP_NAME });
    groupId = Number(g.groupId); // groupId 必须是 Number，传字符串会报 Group not found（SUMMARY §4）

    // ---- 步骤 1（子会话）：方向识别 + 候选词 ----
    let step1;
    try {
      step1 = await step1Identify(productDesc, productImage);
    } catch (e) {
      throw new Error(`商品方向识别失败（图片/文字不可读）：${e.message}`);
    }
    const keywords = step1.keywords.slice(0, MAX_KEYWORDS);
    if (keywords.length < 3) {
      status = 'partial';
      warnings.push(`候选词不足 3 个（实际 ${keywords.length} 个）`);
    }
    console.error(`[step1] 方向=${step1.direction_desc} 候选词=${keywords.length} 个`);

    // ---- 步骤 2/3/4（代码）：逐个搜索 + 提取卡片 + 日期/点赞/14 天窗口 ----
    const kwResults = [];
    for (let i = 0; i < keywords.length; i++) {
      const kw = keywords[i];
      try {
        const r = await searchKeyword(kw, groupId);
        kwResults.push(r);
        console.error(`[search ${i + 1}/${keywords.length}] ${kw} -> 有效卡片 ${r.cards.length}`);
        if (r.cards.length < MIN_CARDS_PER_KW) {
          status = 'partial';
          warnings.push(`候选词「${kw}」结果量少（${r.cards.length} 张 < ${MIN_CARDS_PER_KW}）`);
        }
      } catch (e) {
        status = 'partial';
        warnings.push(`候选词「${kw}」搜索失败：${e.message}`);
        kwResults.push({ kw, cards: [] });
      }
      // 搜索词之间串行，间隔 >= 4s 防验证码墙（SUMMARY §3c）
      if (i < keywords.length - 1) await sleep(BETWEEN_SEARCH_MS);
    }

    const allCards = kwResults.flatMap((r) => r.cards);
    if (!allCards.length) throw new Error('所有候选词搜索均无有效卡片（可能触发风控或词无结果）');

    const kwStats = kwResults.map((r) => {
      const newIn = r.cards.filter((c) => c.in14d);
      const newVirals = newIn.filter((c) => c.likeNum >= VIRAL_LIKE_MIN);
      // 头部最高赞只统计近 6 个月（180 天）内，超过的忽略（用户口径：整体过滤时间）
      const halfYear = r.cards.filter((c) => c.ageDays == null || c.ageDays <= HALF_YEAR_DAYS);
      const maxLike = halfYear.length ? Math.max(...halfYear.map((c) => c.likeNum)) : 0;
      return {
        kw: r.kw,
        total: r.cards.length,
        partial: r.cards.length < MIN_CARDS_PER_KW,
        newInWindow: newIn.length,
        newViralCount: newVirals.length,
        maxLike,
      };
    });

    // ---- 步骤 5（子会话）：宣传方向组织 + 爆款选择 + 建议 ----
    const kwGroups = kwResults.map((r) => ({
      kw: r.kw,
      cards: r.cards,
      partial: r.cards.length < MIN_CARDS_PER_KW,
    }));
    let plan = null;
    try {
      plan = await step5Plan(step1.direction_desc, kwGroups);
    } catch (e) {
      status = 'partial';
      warnings.push(`方向组织子会话失败：${e.message}，使用确定性兜底`);
    }

    // 兜底方向/爆款（子会话失败或未选够时）：按时间窗口取赞高的卡片
    const byId = new Map(allCards.map((c) => [c.id, c]));
    // 素材笔记的时间过滤：近 14 天优先（最多 2 篇），再补近 6 个月（最多 1 篇），超过 180 天忽略
    const selectViral = (ids) => {
      const recent = [];
      const halfYear = [];
      for (const id of ids) {
        const c = byId.get(id);
        if (!c || !c.likeNum || c.likeNum < VIRAL_LIKE_MIN) continue;
        if (c.ageDays != null && c.ageDays > HALF_YEAR_DAYS) continue; // 超过 6 个月忽略
        if (c.in14d) recent.push(id);
        else halfYear.push(id);
      }
      // 近 14 天最多 2 篇 + 近 6 个月最多 1 篇
      return [...recent.slice(0, MAX_VIRAL_RECENT), ...halfYear.slice(0, MAX_VIRAL_NOTES - MAX_VIRAL_RECENT)].slice(0, MAX_VIRAL_NOTES);
    };
    let viralNotes = [];
    let usedHeadFallback = false;
    if (plan && plan.viral_notes.length) {
      viralNotes = selectViral(plan.viral_notes);
    }
    if (!viralNotes.length) {
      // 子会话未选出合格爆款 → 按时间窗口取赞高的（近 14 天优先）
      const candidates = allCards
        .filter((c) => c.likeNum >= VIRAL_LIKE_MIN && (c.ageDays == null || c.ageDays <= HALF_YEAR_DAYS))
        .sort((a, b) => (b.in14d ? 1 : 0) - (a.in14d ? 1 : 0) || b.likeNum - a.likeNum);
      viralNotes = selectViral(candidates.map((c) => c.id));
      if (!viralNotes.length) {
        usedHeadFallback = true;
        const head = [...allCards]
          .filter((c) => c.ageDays == null || c.ageDays <= HALF_YEAR_DAYS)
          .sort((a, b) => (b.in14d ? 1 : 0) - (a.in14d ? 1 : 0) || b.likeNum - a.likeNum)
          .slice(0, MAX_VIRAL_NOTES);
        viralNotes = head.map((c) => c.id);
      }
    }
    const direction = plan && plan.direction ? plan.direction : `${step1.direction_desc} · 场景化种草`;
    const forms = plan && plan.forms && typeof plan.forms === 'object' ? plan.forms : {};

    if (usedHeadFallback) {
      status = 'partial';
      warnings.push('近 6 个月内无赞≥100 的爆款笔记，素材参考改用头部卡片');
    }

    // ---- 步骤 6/7（代码）：逐个深挖爆款笔记 ----
    // 为什么串行深挖：每次深挖都需新开搜索页，连续高频搜索会触发验证码墙（SUMMARY §3c），
    // 故不复用 pMap 并发，串行并保持 4s 间隔（并发开搜索页的风险高于收益）
    const kwCandidates = keywords;
    const materialNotes = [];
    const deepFail = [];
    for (const id of viralNotes) {
      const note = byId.get(id);
      if (!note) continue;
      const d = await deepDive(note, kwCandidates, groupId);
      if (d && d.detail) {
        const likeText = d.detail.like || note.like || String(note.likeNum);
        const collectText = d.detail.collect || '—';
        const commentText = d.detail.comment || '—';
        const fans = d.detail.fans || '';
        const ds = descSummary(d.detail.desc);
        const analysisNote = {
          id,
          kw: note.kw,
          title: d.detail.title || note.title,
          author: d.detail.author || note.author,
          date: note.date,
          cover: note.cover || (d.detail.coverImgs && d.detail.coverImgs[0]) || '',
          likeText: String(likeText),
          collectText: String(collectText),
          commentText: String(commentText),
          fans: String(fans),
          descText: ds.text,
          tags: ds.tags,
          comments: d.detail.comments || [],
        };
        // 爆款分析（子会话）：为什么这篇能爆——粉丝/标题/首图/内容/抓用户什么点（结构化 5 字段）
        let analysis = null;
        try {
          analysis = await step6Analyze(analysisNote);
        } catch (e) {
          console.error(`[analysis] ${id} err: ${e.message}`);
          analysis = null;
        }
        materialNotes.push({ ...analysisNote, analysis });
      } else {
        deepFail.push(id);
        materialNotes.push({
          id,
          kw: note.kw,
          title: note.title,
          author: note.author,
          date: note.date,
          cover: note.cover,
          likeText: note.like || String(note.likeNum),
          collectText: '—',
          commentText: '—',
          fans: '',
          descText: '（详情深挖失败，保留搜索结果卡片信息）',
          tags: [],
          analysis: null,
          comments: [],
        });
      }
      await sleep(BETWEEN_SEARCH_MS);
    }
    if (deepFail.length) {
      status = 'partial';
      warnings.push(`${deepFail.length} 篇爆款笔记详情深挖失败`);
    }

    // ---- 步骤 8（代码）：热度评级（累计口径） ----
    const heat = rateHeat(allCards, kwStats, materialNotes);
    // 若该方向没有近 6 个月内赞>=100 的爆款支撑（素材参考只能给头部卡片），如实标注热度低
    if (usedHeadFallback && heat.level !== '无') {
      heat.level = '低';
    }

    const heatLikeAccText = heat.likeAcc.length
      ? heat.likeAcc.map((v) => `《${(v.title || '').slice(0, 30)}》+${v.likeNum}赞（${v.date} 发布，作者 ${v.author}）`).join('、')
      : '无（近 2 周无点赞累计≥1000 的新笔记）';
    const heatCollectAccText = heat.collectAcc.length
      ? heat.collectAcc.map((v) => `《${(v.title || '').slice(0, 30)}》${v.collectText}收藏（${v.date} 发布，作者 ${v.author}）`).join('、')
      : '无（素材参考笔记无收藏累计≥1000）';
    const heatConclusion = (() => {
      if (heat.level === '无') return '该方向当前小红书结果量严重不足，无法判定热度。';
      if (heat.level === '低') return '该方向当前小红书热度低（近 2 周无点赞累计≥1000 的新笔记）。仍有头部历史笔记可参考，但近期缺乏内容供给，宣传需谨慎评估投入。';
      if (heat.level === '中') return '该方向有中等热度：近 2 周存在点赞累计 100~999 的笔记，可入局但需在标题与封面上下功夫。';
      return `该方向热度高：近 2 周存在点赞累计≥1000 的笔记 ${heat.likeAcc.length} 篇，叠加素材参考收藏累计≥1000 的 ${heat.collectAcc.length} 篇，内容供给充足。`;
    })();

    // 商品图片转 base64 data URI 供 HTML 直接展示（读取失败不阻塞）
    let productImageDataUri = '';
    if (productImage) {
      try {
        const b64 = readFileSync(productImage).toString('base64');
        const ext = (productImage.match(/\.(\w+)$/) || [])[1] || 'jpg';
        const mime = ext === 'png' ? 'image/png' : ext === 'gif' ? 'image/gif' : 'image/jpeg';
        productImageDataUri = `data:${mime};base64,${b64}`;
      } catch (e) {
        console.error(`[img] 商品图片读取失败: ${e.message}`);
      }
    }

    // ---- 步骤 9（代码）：渲染输出 ----
    const reportData = {
      productImage,
      productImageDataUri,
      productDesc,
      directionDesc: step1.direction_desc,
      kwStats,
      direction,
      heatLevel: heat.level,
      heatNote: usedHeadFallback
        ? '该方向近 6 个月无赞≥100 的爆款笔记，热度如实标注为低。素材参考仅用头部卡片，仅作形式参考，不代表该方向当前有爆款。'
        : null,
      heatLikeAccText,
      heatCollectAccText,
      heatNewInCount: heat.newInCount,
      heatMaxLike: heat.maxLike,
      heatConclusion,
      materialNotes,
      materialNoteNone: usedHeadFallback
        ? '该方向近 6 个月无赞≥100 的爆款笔记，以下为头部卡片素材参考，热度如实标注为低。'
        : null,
      date: dateStr,
      windowStart: windowStartStr,
      windowEnd: dateStr,
    };

    const html = renderHtml(reportData);
    writeFileSync(reportPath, html, 'utf-8');
    const md = renderDataMd(reportData);
    writeFileSync(dataFile, md, 'utf-8');

    const baseSummary = `方向「${direction}」，候选词 ${keywords.length} 个，热度 ${heat.level}，素材参考 ${materialNotes.length} 篇爆款笔记`;
    const summary = status === 'success' ? baseSummary : `${baseSummary}；${warnings.join('；')}`;
    const result = {
      status,
      summary,
      direction,
      heat: heat.level,
      report_path: reportPath,
    };
    writeFileSync(resultFile, JSON.stringify(result, null, 2));
    console.log(JSON.stringify({ status, summary, output_dir: outputDir }));
  } catch (e) {
    const err = String((e && e.message) || e);
    const summary = warnings.length ? `${warnings.join('；')}；${err}` : err;
    const result = { status: 'failed', summary, direction: '', heat: '', report_path: '' };
    try { writeFileSync(resultFile, JSON.stringify(result, null, 2)); } catch {}
    console.log(JSON.stringify({ status: 'failed', summary: err, output_dir: outputDir }));
  } finally {
    // 统一收尾：关闭任务分组，不残留 tab（SUMMARY §3c）
    if (groupId) await relayCall('group.close', { groupId }).catch(() => {});
  }
}

main().catch((e) => {
  console.error(`[xhs-product-trend-fit] fatal: ${e && e.stack ? e.stack : e}`);
  console.log(JSON.stringify({ status: 'failed', error: String((e && e.message) || e) }));
  process.exit(0);
});
