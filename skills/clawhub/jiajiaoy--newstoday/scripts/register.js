#!/usr/bin/env node
/**
 * NewsToday — 用户注册 / 偏好设置（无文件写入版）
 *
 * 档案存放在原生 MEMORY.md 中，由 Agent 维护；本脚本不读写任何文件。
 * 它只做校验 + 话题权重计算，然后输出一段 <!-- newstoday:profile:<userId> --> 区块，
 * 由 Agent 写入 MEMORY.md（跨会话保留）。
 *
 * 用法:
 *   node register.js <userId> [language] [topics] [channel]
 *
 * 参数:
 *   userId    必填，字母/数字/-/_，1-128 字符
 *   language  可选，zh（默认）或 en
 *   topics    可选，逗号分隔的偏好话题（如 科技,财经,国际）
 *             可选值: 科技 财经 国际 社会 娱乐 体育
 *   channel   可选，telegram/feishu/slack/discord（默认 telegram）
 *
 * 示例:
 *   node register.js alice
 *   node register.js bob zh 科技,财经,国际
 *   node register.js carol en tech,finance,international telegram
 */

const ALLOWED_TOPICS_ZH = ['科技', '财经', '国际', '社会', '娱乐', '体育'];
const ALLOWED_TOPICS_EN = ['tech', 'finance', 'international', 'society', 'entertainment', 'sports'];
const TOPIC_MAP = { tech: '科技', finance: '财经', international: '国际', society: '社会', entertainment: '娱乐', sports: '体育' };
const ALLOWED_CHANNELS = new Set(['telegram', 'feishu', 'slack', 'discord']);

const DEFAULT_TOPICS = { 科技: 0.8, 财经: 0.8, 国际: 0.7, 社会: 0.6, 娱乐: 0.3, 体育: 0.3 };

function sanitizeId(value) {
  if (typeof value !== 'string' || !/^[a-zA-Z0-9_-]{1,128}$/.test(value)) {
    console.error('❌ 无效的 userId：只允许字母、数字、- 和 _，长度 1-128');
    process.exit(1);
  }
  return value;
}

function sanitizeLanguage(value) {
  if (value !== 'zh' && value !== 'en') {
    console.error('❌ 无效的语言：请使用 zh 或 en');
    process.exit(1);
  }
  return value;
}

function sanitizeTopics(value, language) {
  const raw = value.split(',').map(t => t.trim()).filter(Boolean);
  const weights = {};
  for (const t of raw) {
    const mapped = TOPIC_MAP[t] || t;
    if (!ALLOWED_TOPICS_ZH.includes(mapped)) {
      console.error(`❌ 无效的话题：${t}。可用值：${[...ALLOWED_TOPICS_ZH, ...ALLOWED_TOPICS_EN].join(', ')}`);
      process.exit(1);
    }
    weights[mapped] = 1.0;
  }
  // 未指定的话题给默认权重 0.5
  for (const t of ALLOWED_TOPICS_ZH) {
    if (!(t in weights)) weights[t] = 0.5;
  }
  return weights;
}

/**
 * 渲染档案为 MEMORY.md 区块（供 Agent 写入原生记忆，脚本本身不落盘）
 */
function renderMemoryBlock(profile) {
  const topicLine = ALLOWED_TOPICS_ZH
    .map(t => `${t} ${(profile.topics[t] ?? 0.5).toFixed(1)}`)
    .join(' · ');
  const pushLine = profile.push?.enabled
    ? `已开启 ${profile.channel} ${profile.push.morningTime || '08:00'}/${profile.push.eveningTime || '20:00'}`
    : '未开启';
  return `<!-- newstoday:profile:${profile.userId} -->
## 新闻档案 · ${profile.userId}
- userId: ${profile.userId}
- 语言: ${profile.language}
- 话题权重: ${topicLine}
- 渠道: ${profile.channel}
- 推送: ${pushLine}
<!-- /newstoday:profile -->`;
}

const args = process.argv.slice(2);
if (!args[0]) {
  console.log(`用法:
  node register.js <userId> [language] [topics] [channel]

参数:
  userId    字母/数字/-/_，1-128 字符
  language  zh（默认）或 en
  topics    逗号分隔偏好话题（如 科技,财经,国际）
  channel   telegram/feishu/slack/discord（默认 telegram）

示例:
  node register.js alice
  node register.js bob zh 科技,财经,国际
  node register.js carol en tech,finance,international`);
  process.exit(1);
}

const userId   = sanitizeId(args[0]);
const language = args[1] ? sanitizeLanguage(args[1]) : 'zh';
const topics   = args[2] ? sanitizeTopics(args[2], language) : { ...DEFAULT_TOPICS };
const rawCh    = args[3] || 'telegram';
if (!ALLOWED_CHANNELS.has(rawCh)) {
  console.error(`❌ 无效渠道：${rawCh}。支持：${[...ALLOWED_CHANNELS].join(', ')}`);
  process.exit(1);
}
const channel = rawCh;

const profile = {
  userId,
  language,
  topics,
  channel,
  push: { enabled: false }
};

const topList = Object.entries(topics).filter(([, w]) => w >= 0.7).map(([t]) => t).join('、');
const topTopicsCsv = Object.entries(topics).filter(([, w]) => w >= 0.7).map(([t]) => t).join(',');

console.log(`
✅ 档案已生成（纯计算，未写入任何文件）

👤 用户：${userId}
🌐 语言：${language === 'zh' ? '中文' : 'English'}
📌 重点话题：${topList || '默认'}
📡 推送渠道：${channel}
`);

// 输出 MEMORY.md 区块，供 Agent 写入原生记忆（脚本不落盘，符合 clawhub 无文件写入规范）
console.log('📇 请将以下档案写入 MEMORY.md（原生记忆，跨会话保留）：');
console.log('```markdown');
console.log(renderMemoryBlock(profile));
console.log('```');
console.log('');
console.log('下一步：');
console.log(`  调整话题偏好：node scripts/preference.js set ${userId} <话题> <权重0-1> [--topics "${topTopicsCsv || '科技,财经'}"]`);
console.log(`  开启每日推送（从 MEMORY.md 读出语言/话题作为参数）：`);
console.log(`    node scripts/push-toggle.js on ${userId} --lang ${language} --topics "${topTopicsCsv || '科技,财经'}" --channel ${channel}`);
console.log(`  获取今日早报：node scripts/morning-push.js --lang ${language} --topics "${topTopicsCsv || '科技,财经'}"`);

module.exports = { renderMemoryBlock, sanitizeTopics };
