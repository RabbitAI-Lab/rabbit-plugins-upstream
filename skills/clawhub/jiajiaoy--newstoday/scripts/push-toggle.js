#!/usr/bin/env node
/**
 * NewsToday — 推送开关（无文件写入版）
 *
 * 档案存放在原生 MEMORY.md 中，由 Agent 维护；本脚本不读写任何文件。
 * 开启推送所需的语言 / 话题 / 渠道由 Agent 从 MEMORY.md 读出后作为参数传入，
 * cron 任务通过 openclaw 运行时协议（__OPENCLAW_CRON_ADD__）创建，运行时负责持久化。
 * lang/topics 被嵌入 cron 命令行，因此 push 脚本运行时无需再读任何文件。
 *
 * 用法:
 *   node push-toggle.js on <userId> [--lang zh|en] [--topics 科技,财经,国际] \
 *        [--channel telegram] [--morning 08:00] [--evening 20:00]
 *   node push-toggle.js off <userId>
 *   node push-toggle.js status <userId>
 */

const path = require('path');

const ALLOWED_TOPICS = new Set(['科技', '财经', '国际', '社会', '娱乐', '体育']);
const ALLOWED_CHANNELS = new Set(['telegram', 'feishu', 'slack', 'discord']);

// 只允许字母、数字、连字符、下划线，最长 128 字符
function sanitizeId(value, label) {
  if (typeof value !== 'string' || !/^[a-zA-Z0-9_-]{1,128}$/.test(value)) {
    console.error(`❌ 无效的 ${label}：只允许字母、数字、- 和 _，长度 1-128`);
    process.exit(1);
  }
  return value;
}

// 校验 HH:MM 格式，返回 { h, m } 整数
function sanitizeTime(value, label) {
  if (typeof value !== 'string' || !/^\d{1,2}:\d{2}$/.test(value)) {
    console.error(`❌ 无效的 ${label}：格式应为 HH:MM，如 08:00`);
    process.exit(1);
  }
  const [h, m] = value.split(':').map(Number);
  if (h < 0 || h > 23 || m < 0 || m > 59) {
    console.error(`❌ 无效的 ${label}：小时 0-23，分钟 0-59`);
    process.exit(1);
  }
  return { h, m };
}

function enablePush(userId, opts = {}) {
  userId = sanitizeId(userId, 'userId');

  // 语言与话题由 Agent 从 MEMORY.md 读出后传入；此处再做白名单过滤，避免不可信数据进入 cron
  const lang = opts.lang === 'en' ? 'en' : 'zh';
  const topics = (opts.topics || '')
    .split(',').map(t => t.trim())
    .filter(t => ALLOWED_TOPICS.has(t))
    .join(',');

  const pushArgs = `--lang ${lang}${topics ? ` --topics ${topics}` : ''}`;

  const { h: mh, m: mm } = sanitizeTime(opts.morning || '08:00', 'morning');
  const { h: eh, m: em } = sanitizeTime(opts.evening || '20:00', 'evening');
  const rawChannel = opts.channel || 'telegram';
  if (!ALLOWED_CHANNELS.has(rawChannel)) {
    console.error(`❌ 不支持的渠道：${rawChannel}。支持：${[...ALLOWED_CHANNELS].join(', ')}`);
    process.exit(1);
  }
  const channel = rawChannel;
  const tz = 'Asia/Shanghai';

  const morningCron = `${mm} ${mh} * * *`;
  const eveningCron = `${em} ${eh} * * *`;
  const sessionKey = `agent:main:${channel}:direct:${userId}`;

  // 早报 cron（lang/topics 已嵌入命令，push 脚本无需再读文件）
  const morningConfig = {
    name: `newstoday-morning-${userId}`,
    cronExpr: morningCron,
    tz,
    session: 'isolated',
    sessionKey,
    channel,
    to: userId,
    announce: true,
    timeoutSeconds: 120,
    message: `node ${path.join(__dirname, 'morning-push.js')} ${pushArgs}`
  };
  console.log(`__OPENCLAW_CRON_ADD__:${JSON.stringify(morningConfig)}`);

  // 晚报 cron
  const eveningConfig = {
    name: `newstoday-evening-${userId}`,
    cronExpr: eveningCron,
    tz,
    session: 'isolated',
    sessionKey,
    channel,
    to: userId,
    announce: true,
    timeoutSeconds: 120,
    message: `node ${path.join(__dirname, 'evening-push.js')} ${pushArgs}`
  };
  console.log(`__OPENCLAW_CRON_ADD__:${JSON.stringify(eveningConfig)}`);

  // 突发新闻检测 cron（每2小时，08:00-22:00）
  const breakingConfig = {
    name: `newstoday-breaking-${userId}`,
    cronExpr: '0 8,10,12,14,16,18,20,22 * * *',
    tz,
    session: 'isolated',
    sessionKey,
    channel,
    to: userId,
    announce: false,
    timeoutSeconds: 60,
    message: `node ${path.join(__dirname, 'breaking-alert.js')} ${pushArgs}`
  };
  console.log(`__OPENCLAW_CRON_ADD__:${JSON.stringify(breakingConfig)}`);

  const morningDisplay = `${String(mh).padStart(2, '0')}:${String(mm).padStart(2, '0')}`;
  const eveningDisplay = `${String(eh).padStart(2, '0')}:${String(em).padStart(2, '0')}`;

  console.log(`
✅ 每日推送已开启

⏰ 早报：每天 ${morningDisplay}（个性化10条要闻 + RSS）
🌙 晚报：每天 ${eveningDisplay}（收官 + 明日预告）
🚨 突发：每2小时检测（08:00-22:00，有重大事件才提醒）
📡 渠道：${channel}${topics ? `\n📌 重点话题：${topics.split(',').join('、')}` : ''}

💡 请在 MEMORY.md 的档案区块记下：推送已开启（${channel}，${morningDisplay}/${eveningDisplay}）。
关闭推送：node scripts/push-toggle.js off ${userId}`);
}

function disablePush(userId) {
  userId = sanitizeId(userId, 'userId');
  // cron 名称可由 userId 推导，无需读取档案
  console.log(`__OPENCLAW_CRON_RM__:newstoday-morning-${userId}`);
  console.log(`__OPENCLAW_CRON_RM__:newstoday-evening-${userId}`);
  console.log(`__OPENCLAW_CRON_RM__:newstoday-breaking-${userId}`);
  console.log(`
✅ 推送已关闭（已请求删除 ${userId} 的早报/晚报/突发定时任务）
💡 请在 MEMORY.md 的档案区块记下：推送已关闭。`);
}

function showStatus(userId) {
  userId = sanitizeId(userId, 'userId');
  console.log(`
📡 推送状态由 MEMORY.md 档案记录 —— 请读取 MEMORY.md 中
   <!-- newstoday:profile:${userId} --> 区块查看开启状态 / 时间 / 渠道 / 话题。

如需重新开启：
   node scripts/push-toggle.js on ${userId} --lang <zh|en> --topics <话题> --channel <渠道>`);
}

module.exports = { enablePush, disablePush, showStatus };

if (require.main !== module) return;

const args = process.argv.slice(2);
const command = args[0];
const userId = args[1];

function flag(name) {
  const i = args.indexOf(name);
  return (i !== -1 && args[i + 1]) ? args[i + 1] : undefined;
}

if (!command || !userId) {
  console.log(`用法:
  node push-toggle.js on <userId> [--lang zh|en] [--topics 科技,财经,国际] \\
       [--channel telegram] [--morning 08:00] [--evening 20:00]
  node push-toggle.js off <userId>
  node push-toggle.js status <userId>

说明:
  档案存于原生 MEMORY.md，由 Agent 维护并在开启推送时把语言/话题/渠道作为参数传入。
  开启后创建三个定时任务：早报、晚报、每2小时突发检测。`);
  process.exit(1);
}

const opts = {
  lang: flag('--lang'),
  topics: flag('--topics'),
  channel: flag('--channel'),
  morning: flag('--morning'),
  evening: flag('--evening'),
};

switch (command) {
  case 'on':     enablePush(userId, opts); break;
  case 'off':    disablePush(userId); break;
  case 'status': showStatus(userId); break;
  default:
    console.log(`❌ 未知命令: ${command}`);
    process.exit(1);
}
