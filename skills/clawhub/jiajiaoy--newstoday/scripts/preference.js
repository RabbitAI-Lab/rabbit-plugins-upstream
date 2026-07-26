#!/usr/bin/env node
/**
 * NewsToday — 话题偏好管理（无文件写入版）
 *
 * 档案存于原生 MEMORY.md，由 Agent 维护；本脚本不读写任何文件。
 * 它是一个纯计算助手：接收当前权重（由 Agent 从 MEMORY.md 读出后传入），
 * 应用一次修改，然后打印更新后的权重表 + 一段 <!-- newstoday:profile:<userId> -->
 * 区块，供 Agent 写回 MEMORY.md。
 *
 * 用法:
 *   node preference.js show <userId>  [--weights '{"科技":0.9,...}']
 *   node preference.js set  <userId> <话题> <权重0-1> [--weights '{...}'] [--lang zh] [--channel telegram]
 *   node preference.js reset <userId> [--lang zh] [--channel telegram]
 *
 * 说明:
 *   --weights  当前话题权重 JSON（从 MEMORY.md 读出）。缺省时以默认权重为基础。
 *   --lang / --channel  写回区块时保留档案的语言与渠道（缺省 zh / telegram）。
 *
 * 话题: 科技 财经 国际 社会 娱乐 体育
 * 权重: 0.0（不感兴趣）~ 1.0（最感兴趣）
 */

const ALLOWED_TOPICS = ['科技', '财经', '国际', '社会', '娱乐', '体育'];
const TOPIC_MAP = { tech: '科技', finance: '财经', international: '国际', society: '社会', entertainment: '娱乐', sports: '体育' };
const DEFAULT_TOPICS = { 科技: 0.8, 财经: 0.8, 国际: 0.7, 社会: 0.6, 娱乐: 0.3, 体育: 0.3 };

function sanitizeId(value) {
  if (typeof value !== 'string' || !/^[a-zA-Z0-9_-]{1,128}$/.test(value)) {
    console.error('❌ 无效的 userId');
    process.exit(1);
  }
  return value;
}

function flag(args, name) {
  const i = args.indexOf(name);
  return (i !== -1 && args[i + 1]) ? args[i + 1] : undefined;
}

/** 解析 --weights JSON，仅保留白名单话题的合法数值权重，其余用默认值补齐 */
function parseWeights(raw) {
  const weights = { ...DEFAULT_TOPICS };
  if (raw) {
    let parsed = null;
    try { parsed = JSON.parse(raw); } catch (_) {
      console.error('❌ --weights 不是合法 JSON');
      process.exit(1);
    }
    if (parsed && typeof parsed === 'object') {
      for (const [k, v] of Object.entries(parsed)) {
        const t = TOPIC_MAP[k] || k;
        if (ALLOWED_TOPICS.includes(t) && typeof v === 'number' && v >= 0 && v <= 1) {
          weights[t] = v;
        }
      }
    }
  }
  return weights;
}

function bar(weight) {
  const filled = Math.round(weight * 10);
  return '█'.repeat(filled) + '░'.repeat(10 - filled);
}

function renderMemoryBlock(userId, weights, lang, channel) {
  const topicLine = ALLOWED_TOPICS
    .map(t => `${t} ${(weights[t] ?? 0.5).toFixed(1)}`)
    .join(' · ');
  return `<!-- newstoday:profile:${userId} -->
## 新闻档案 · ${userId}
- userId: ${userId}
- 语言: ${lang}
- 话题权重: ${topicLine}
- 渠道: ${channel}
<!-- /newstoday:profile -->`;
}

function printTable(userId, weights, lang, channel) {
  console.log(`\n📌 话题偏好 — ${userId}\n${'━'.repeat(30)}`);
  for (const t of ALLOWED_TOPICS) {
    const w = weights[t] ?? 0.5;
    console.log(`  ${t.padEnd(4)}  ${bar(w)}  ${(w * 10).toFixed(0)}/10`);
  }
  console.log('━'.repeat(30));
  console.log(`语言：${lang === 'en' ? 'English' : '中文'}  渠道：${channel}`);
  console.log('\n📇 请把更新后的档案区块写回 MEMORY.md：');
  console.log('```markdown');
  console.log(renderMemoryBlock(userId, weights, lang, channel));
  console.log('```');
}

const args = process.argv.slice(2);
const command = args[0];
const userId  = args[1] ? sanitizeId(args[1]) : null;

if (!command || !userId) {
  console.log(`用法:
  node preference.js show <userId>  [--weights '{"科技":0.9,...}']
  node preference.js set  <userId> <话题> <权重0-1> [--weights '{...}'] [--lang zh] [--channel telegram]
  node preference.js reset <userId> [--lang zh] [--channel telegram]

说明: 档案存于 MEMORY.md，本脚本不落盘。当前权重经 --weights 传入，
      脚本打印更新后的权重表和 <!-- newstoday:profile --> 区块供写回。`);
  process.exit(1);
}

const lang = (flag(args, '--lang') === 'en') ? 'en' : 'zh';
const channel = flag(args, '--channel') || 'telegram';

switch (command) {
  case 'show': {
    const weights = parseWeights(flag(args, '--weights'));
    printTable(userId, weights, lang, channel);
    break;
  }

  case 'set': {
    const rawTopic = args[2];
    const rawWeight = args[3];
    if (!rawTopic || rawWeight === undefined || rawWeight.startsWith('--')) {
      console.error('用法: node preference.js set <userId> <话题> <权重0-1> [--weights ...]');
      process.exit(1);
    }
    const topic = TOPIC_MAP[rawTopic] || rawTopic;
    if (!ALLOWED_TOPICS.includes(topic)) {
      console.error(`❌ 无效话题：${rawTopic}。可用：${ALLOWED_TOPICS.join(', ')}`);
      process.exit(1);
    }
    const weight = parseFloat(rawWeight);
    if (isNaN(weight) || weight < 0 || weight > 1) {
      console.error('❌ 权重须在 0.0 ~ 1.0 之间');
      process.exit(1);
    }
    const weights = parseWeights(flag(args, '--weights'));
    weights[topic] = weight;
    console.log(`✅ 已设置「${topic}」权重为 ${weight.toFixed(1)}`);
    printTable(userId, weights, lang, channel);
    break;
  }

  case 'reset': {
    const weights = { ...DEFAULT_TOPICS };
    console.log(`✅ 话题偏好已重置为默认值`);
    printTable(userId, weights, lang, channel);
    break;
  }

  default:
    console.error(`❌ 未知命令: ${command}`);
    process.exit(1);
}

module.exports = { renderMemoryBlock, parseWeights };
