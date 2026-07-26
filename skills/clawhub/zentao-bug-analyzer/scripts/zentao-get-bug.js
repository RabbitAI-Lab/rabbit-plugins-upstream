#!/usr/bin/env node
/**
 * zentao-get-bug.js — 获取禅道 Bug 详情 JSON
 *
 * 用法:
 *   node zentao-get-bug.js --ws=<wsEndpoint> --bug-id=<id> [--zentao-url=http://zentao.gxatek.com:20080]
 *
 * 输出 (stdout):
 *   Bug 详情 JSON 对象
 *
 * 需要先启动 zentao-login.js 获取 WS endpoint。
 */

const { chromium } = require('playwright');

function parseArgs() {
  const args = process.argv.slice(2);
  const config = { wsEndpoint: '', bugId: 0, zentaoUrl: 'http://zentao.gxatek.com:20080' };
  for (const arg of args) {
    if (arg.startsWith('--ws=')) config.wsEndpoint = arg.slice(5);
    if (arg.startsWith('--bug-id=')) config.bugId = parseInt(arg.slice(9), 10);
    if (arg.startsWith('--zentao-url=')) config.zentaoUrl = arg.split('=')[1];
  }
  return config;
}

async function main() {
  const config = parseArgs();

  if (!config.wsEndpoint) {
    console.error('[ERROR] 缺少 --ws 参数（WS endpoint）');
    process.exit(1);
  }
  if (!config.bugId) {
    console.error('[ERROR] 缺少 --bug-id 参数');
    process.exit(1);
  }

  console.error(`[INFO] 连接到浏览器: ${config.wsEndpoint}`);

  const browser = await chromium.connectOverCDP(config.wsEndpoint);

  // 取已有的 context/page（或新建）
  const contexts = browser.contexts();
  const context = contexts.length > 0 ? contexts[0] : await browser.newContext();
  const pages = context.pages();
  const page = pages.length > 0 ? pages[0] : await context.newPage();

  console.error(`[INFO] 获取 Bug #${config.bugId} 详情和操作历史...`);

  // 获取 Bug 详情 + 从 bug-view 页面提取操作历史
  // 注意: 必须在两次独立的 page.evaluate 中进行 (同一 evaluate 中串行 fetch 会导致 HTML 缺少 historyChanges)
  const bugResult = await page.evaluate(async ({ bugId, zentaoUrl }) => {
    const resp = await fetch(`${zentaoUrl}/api.php/v1/bugs/${bugId}`, {
      credentials: 'include',
    });
    if (!resp.ok) {
      return { error: true, status: resp.status, statusText: resp.statusText };
    }
    return await resp.json();
  }, { bugId: config.bugId, zentaoUrl: config.zentaoUrl });

  if (bugResult.error) {
    console.error(`[ERROR] API 请求失败 (HTTP ${bugResult.status}): ${bugResult.statusText}`);
    console.log(JSON.stringify(bugResult));
    process.exit(1);
  }

  // 获取 bug-view 页面的 HTML 并提取 history JSON（独立 evaluate，避免与 API fetch 冲突）
  const historyResult = await page.evaluate(async ({ bugId, zentaoUrl }) => {
    const resp = await fetch(`${zentaoUrl}/bug-view-${bugId}.html`, {
      credentials: 'include',
    });
    if (!resp.ok) {
      return { _fetchError: `bug-view 页面请求失败 (HTTP ${resp.status})` };
    }
    const html = await resp.text();

    // 提取 operation history JSON 数组
    // 注意: page.evaluate 中 fetch 的 HTML 引号为 &quot; 而非 "（实体编码）
    const idx = html.indexOf('&quot;historyChanges&quot;') > 0
      ? html.indexOf('&quot;historyChanges&quot;')
      : html.indexOf('historyChanges');
    if (idx < 0) {
      return [];
    }

    // 向前找 '[' 
    let start = idx;
    while (start > 0 && html[start] !== '[') start--;
    // 括号深度匹配找 ']'
    let depth = 0;
    let end = start;
    for (let i = start; i < html.length; i++) {
      if (html[i] === '[') depth++;
      else if (html[i] === ']') { depth--; if (depth === 0) { end = i + 1; break; } }
    }

    const raw = html.substring(start, end);
    const json = raw.replace(/&quot;/g, '"').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
    try {
      return JSON.parse(json);
    } catch (e) {
      return { _parseError: e.message, _sample: raw.substring(0, 1000) };
    }
  }, { bugId: config.bugId, zentaoUrl: config.zentaoUrl });

  const result = { bug: bugResult, history: historyResult };

  if (result.error) {
    console.error(`[ERROR] 请求失败 (HTTP ${result.status}): ${result.statusText}`);
    console.log(JSON.stringify(result));
    process.exit(1);
  }

  // 分行输出：先输出 bug，再输出 history（避免单次 JSON.stringify 太大导致进程超时）
  console.log('---BUG_START---');
  console.log(JSON.stringify(result.bug));
  console.log('---BUG_END---');
  console.log('---HISTORY_START---');
  console.log(JSON.stringify(result.history));
  console.log('---HISTORY_END---');
}

main().catch((err) => {
  console.error(`[ERROR] ${err.message}`);
  process.exit(1);
});
