'use strict';
/**
 * _shared/session_result.js — 会话结果收敛与主动回报 (2026-11-13)。
 *
 * 所有「分步会话」型 skill (xhs/dy/ks/b/wb/dcd/zh/sohu/autohome/弹幕/博主主页) 共用:
 * 会话过期 (空闲租约 / 步进卡死兜底) 时服务端只改状态、不推送, 客户端要主动把已采结果
 * 交给用户, 三条路:
 *   1) step 报 3006 → reportEndedSession: 结果塞进错误 JSON 的 data, 退出码 5;
 *   2) watch  → 守候到终态, 自动导出并输出 (过期那一刻);
 *   3) inbox  → 列出「已结束但还没告诉过用户」的会话 (本地 seen 文件去重)。
 *
 * 各平台差异只有 exportPath / csvPrefix / label, 由 createSessionResult 注入。
 * 输出规约: stdout 只 JSON, 提示走 stderr。
 */
const fs = require('fs');
const path = require('path');
const { configPaths, resolveConfig } = require('./config');
const { ApiClient, skillHeaders, warnSkillResponse } = require('./client');
const { UsageError, printOk, parsePositiveNumber, sleep } = require('./output');

const TERMINAL = new Set(['done', 'expired', 'failed']);
const MAX_PAGE = 200;           // 单页拉取上限 (服务端 page_size 最大 100, 兼容降级)
const MAX_PAGES = 200;          // 明细最多翻 200 页, 防异常会话拖死 CLI
const DOWNLOAD_TIMEOUT_MS = 60000;
const SID_RE = /^[0-9a-f]{32}$/;

function createSessionResult({ exportPath, csvPrefix = 'session', label = '会话',
                               itemsKey = 'comments', itemsCmd = 'comments',
                               methods = {} } = {}) {
  if (!exportPath) throw new Error('session_result: exportPath 必填');
  // client 方法名: 评论类 skill 统一为 CommentSession; 博主主页(profile)另有 ProfileSession
  const M = {
    get: methods.get || 'getCommentSession',
    list: methods.list || 'listCommentSessions',
    items: methods.items || 'listSessionComments',
  };

  /** 会话 id 校验 (各平台均为 uuid4().hex)。 */
  function requireSid(opts) {
    const sid = opts && opts.session;
    if (!sid || !SID_RE.test(sid)) {
      throw new UsageError('需要 --session <32位会话id>（由 start 命令返回）');
    }
    return sid;
  }

  function makeClient(opts) {
    const cfg = resolveConfig(opts);
    if (!cfg.token) {
      const err = new Error('未登录：缺少 token');
      err.name = 'BizError';
      err.code = 1002;
      throw err;
    }
    return { cfg, client: new ApiClient({ baseUrl: cfg.baseUrl, token: cfg.token }) };
  }

  function defaultCsvName(sessionId) {
    return `${csvPrefix}_${String(sessionId).slice(0, 8)}.csv`;
  }

  /** 全量拉取本会话已落库明细 (分页到不足一页为止)。 */
  async function collectAllComments(client, sessionId) {
    let items = [];
    let pageSize = MAX_PAGE;
    for (let page = 1; page <= MAX_PAGES; page += 1) {
      const d = await client[M.items](sessionId, page, pageSize);
      const batch = (d && d.items) || [];
      pageSize = Number(d && d.page_size) || pageSize;
      items = items.concat(batch);
      if (batch.length < pageSize) break;
    }
    return items;
  }

  /** 下载会话 CSV (与 export 命令同一接口)。失败返回 null, 不阻断回报。 */
  async function downloadExport(cfg, sessionId, outPath) {
    const ctrl = new AbortController();
    const timer = setTimeout(() => ctrl.abort(), DOWNLOAD_TIMEOUT_MS);
    try {
      const res = await fetch(
        `${cfg.baseUrl}${exportPath}/${encodeURIComponent(sessionId)}/export`,
        { headers: { Authorization: `Bearer ${cfg.token}`, ...skillHeaders() }, signal: ctrl.signal });
      warnSkillResponse(res);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const buf = Buffer.from(await res.arrayBuffer());
      const out = outPath || defaultCsvName(sessionId);
      fs.mkdirSync(path.dirname(path.resolve(out)), { recursive: true });
      fs.writeFileSync(out, buf);
      process.stderr.write(`[expired] 已导出已采${label}数据: ${out}\n`);
      return { file: out, size: buf.length };
    } catch (e) {
      process.stderr.write(`[expired] CSV 导出失败 (结果仍可用 comments 拉取): ${e && e.message}\n`);
      return null;
    } finally {
      clearTimeout(timer);
    }
  }

  /** 会话进度统一提取: 各平台 _public_session 字段名不同 (mains/subs/notes/danmakus)。 */
  function pickCollected(s) {
    const out = {};
    for (const [k, v] of Object.entries(s || {})) {
      if (k.endsWith('_collected') || k === 'charged_steps') out[k] = v;
    }
    return out;
  }

  /** 收敛一个会话的最终结果: 状态 + 进度 + 明细条数 + 前 5 条预览 (+ CSV)。 */
  async function buildOutcome(cfg, client, sessionId, opts = {}) {
    const s = await client[M.get](sessionId);
    const items = await collectAllComments(client, sessionId);
    const csv = (opts.exportCsv === false || items.length === 0)
      ? null
      : await downloadExport(cfg, sessionId, opts.out);
    return {
      session_id: sessionId,
      note_id: s.note_id || s.content_id || '',
      title: s.title || '',
      status: s.status || 'unknown',
      is_terminal: TERMINAL.has(s.status),
      expired_reason: s.fail_reason || '',
      metrics: s.metrics || {},
      collected: pickCollected(s),
      // 字段名随内容类型 (评论 comments_* / 笔记 notes_* / 弹幕 danmakus_*)
      [`${itemsKey}_count`]: items.length,
      [`${itemsKey}_preview`]: items.slice(0, 5),
      csv_path: csv ? csv.file : null,
      csv_size: csv ? csv.size : 0,
    };
  }

  // ── inbox: 已结束但未播报过的会话 ───────────────────────────────────────────

  function seenPath() {
    return path.join(path.dirname(configPaths.configPath), 'session_inbox_seen.json');
  }

  function readSeen() {
    try {
      const data = JSON.parse(fs.readFileSync(seenPath(), 'utf8'));
      return new Set(Array.isArray(data) ? data : []);
    } catch {
      return new Set();
    }
  }

  function markSeen(sessionIds) {
    try {
      const seen = readSeen();
      sessionIds.forEach((id) => seen.add(id));
      fs.mkdirSync(path.dirname(seenPath()), { recursive: true });
      fs.writeFileSync(seenPath(), JSON.stringify(Array.from(seen).slice(-500)), 'utf8');
    } catch { /* 写失败只影响去重 */ }
  }

  /** 拉最近 N 天的已结束会话, 过滤掉本地已播报的。 */
  async function listUnreported(client, { days = 7, limit = 10 } = {}) {
    const seen = readSeen();
    const deadline = Date.now() - days * 24 * 3600 * 1000;
    const out = [];
    for (let page = 1; page <= 3 && out.length < limit; page += 1) {
      const d = await client[M.list](page, 100, '');
      const rows = (d && d.items) || [];
      for (const s of rows) {
        if (!TERMINAL.has(s.status) || seen.has(s.session_id)) continue;
        const ts = Date.parse(String(s.created_at || '').replace(' ', 'T'));
        if (Number.isFinite(ts) && ts < deadline) continue;
        out.push(s);
        if (out.length >= limit) break;
      }
      if (rows.length < 100) break;
    }
    return out;
  }

  // ── 对外命令 ────────────────────────────────────────────────────────────────

  /**
   * step 撞上 3006 时把已采结果一并带回, 返回 true 表示已处理并退出进程。
   * 过期不是失败: 已采数据仍然有效, 必须交给用户而不是只报「会话已结束」。
   */
  async function reportEndedSession(err, opts = {}) {
    if (!err || err.name !== 'BizError' || err.code !== 3006) return false;
    const sessionId = opts.session;
    if (!sessionId || !SID_RE.test(sessionId)) return false;
    const { cfg, client } = makeClient(opts);
    let outcome;
    try {
      outcome = await buildOutcome(cfg, client, sessionId, { out: opts.out });
    } catch (e) {
      process.stderr.write(`[session] 会话已结束, 但已采结果读取失败: ${e && e.message}\n`);
      return false;
    }
    markSeen([sessionId]);
    if (outcome.status === 'active') {
      // 3006 已判定不可用, 但读状态可能赶上「刚结束」的竞态 → 按 expired 展示
      outcome.status = 'expired';
      outcome.is_terminal = true;
      outcome.expired_reason = outcome.expired_reason || '会话已结束 (服务端已释放, 已采数据仍有效)';
    }
    const pages = outcome.collected.pages_collected || 0;
    process.stderr.write(
      `会话已结束 (status=${outcome.status})。` +
      (outcome.expired_reason ? `${outcome.expired_reason}。` : '') +
      `已采 ${pages} 页 / ${outcome[`${itemsKey}_count`]} 条${label}，` +
      (outcome.csv_path ? `CSV: ${outcome.csv_path}。` : `可用 ${itemsCmd} 命令继续拉取。`) +
      '请把这份结果告知用户；要继续采集需重新 start 建新会话。\n');
    process.stdout.write(JSON.stringify({
      ok: false, code: err.code, message: err.message,
      data: { ended: true, ...outcome },
    }) + '\n');
    process.exit(5);
    return true;
  }

  /**
   * watch — 守候到终态 (过期/结束/失败) 后自动收敛并导出。
   * 唯一能「在过期那一刻」交出结果的形态: 用户说要离开/等待时由 agent 执行。
   */
  async function cmdWatch(opts) {
    const sessionId = requireSid(opts);
    const { cfg, client } = makeClient(opts);
    const interval = Math.max(3, parsePositiveNumber(opts.interval, 'interval', 10));
    const maxWait = parsePositiveNumber(opts.maxWait, 'max-wait', 1800);
    const startedAt = Date.now();
    let lastStatus = '';
    process.stderr.write(
      `开始守候会话 ${sessionId}（每 ${interval}s 查一次，最多 ${maxWait}s）；` +
      `会话空闲 180s 会自动结束，届时自动整理已采${label}结果。\n`);
    for (;;) {
      const s = await client[M.get](sessionId);
      if (s.status !== lastStatus) {
        const col = pickCollected(s);
        const detail = Object.entries(col)
          .filter(([k]) => k !== 'charged_steps')
          .map(([k, v]) => `${k}=${v}`).join(' ');
        process.stderr.write(`[watch] status=${s.status} ${detail}\n`);
        lastStatus = s.status;
      }
      if (TERMINAL.has(s.status)) {
        const outcome = await buildOutcome(cfg, client, sessionId,
          { exportCsv: opts.noExport !== true, out: opts.out });
        markSeen([sessionId]);
        process.stderr.write(`[watch] 会话已结束 (${s.status})，结果已收敛。\n`);
        printOk({ ...outcome, watched_seconds: Math.round((Date.now() - startedAt) / 1000) });
        return;
      }
      if ((Date.now() - startedAt) / 1000 >= maxWait) {
        printOk({
          session_id: sessionId, status: s.status, watching_timeout: true,
          collected: pickCollected(s),
          message: `守候 ${maxWait}s 仍未结束，会话仍在进行；可再次 watch 或直接 step 继续`,
        });
        return;
      }
      await sleep(interval * 1000);
    }
  }

  /**
   * inbox — 列出「已结束但还没告诉过用户」的会话 (本地 seen 文件去重)。
   */
  async function cmdInbox(opts) {
    const { cfg, client } = makeClient(opts);
    const days = parsePositiveNumber(opts.days, 'days', 7);
    const rows = await listUnreported(client, { days, limit: 10 });
    const items = [];
    for (const s of rows) {
      try {
        items.push(await buildOutcome(cfg, client, s.session_id,
          { exportCsv: opts.noExport !== true, out: opts.out }));
      } catch (e) {
        items.push({ session_id: s.session_id, status: s.status, error: e && e.message });
      }
    }
    markSeen(items.map((i) => i.session_id));
    if (items.length) {
      process.stderr.write(
        `有 ${items.length} 个已结束的${label}会话结果待告知用户（近 ${days} 天，未播报过）。` +
        '请把每个会话的标题/状态/已采条数/CSV 路径整理后告诉用户。\n');
    } else {
      process.stderr.write(`近 ${days} 天没有新的已结束${label}会话结果。\n`);
    }
    printOk({ total: items.length, days, items });
  }

  return {
    TERMINAL, defaultCsvName, collectAllComments, downloadExport, buildOutcome,
    listUnreported, markSeen, reportEndedSession, cmdWatch, cmdInbox,
  };
}

module.exports = { createSessionResult, TERMINAL };
