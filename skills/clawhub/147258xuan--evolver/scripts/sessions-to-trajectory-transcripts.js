#!/usr/bin/env node
/**
 * sessions-to-trajectory-transcripts.js — Export OpenClaw sessions as generic-chat
 * transcripts WITH structured tool_use/tool_result pairs, so evolver's distiller can
 * form "complete units".
 *
 * Why this exists (2026-09-29):
 *   - `transcript_events` stores toolCall parts but NO tool results, so a transcript
 *     built from it can never yield paired action→result units → distill returns
 *     `no_eligible_signal` / `unit_too_long`.
 *   - `trajectory_runtime_events` stores tool.call (625) and tool.result (625) paired by
 *     `data.toolCallId`, plus `prompt.submitted` (user text) and `model.completed`
 *     (assistant text) — enough to rebuild a whole session from ONE table.
 *
 * Output is OpenAI chat-completions shape: assistant `tool_calls` + `role:"tool"` results.
 * Field values are truncated so distiller units stay bounded (long units get rejected
 * as `unit_too_long`).
 *
 * NOTE: `trajectory_runtime_events` has NO `event_zstd` column — payload is plain
 * `event_json`. (That column only exists on `transcript_events`.)
 *
 * Usage:
 *   node sessions-to-trajectory-transcripts.js [--limit N] [--min-tools N]
 *                                              [--session-key SUBSTR] [--out-dir DIR]
 *                                              [--db PATH] [--agent main]
 *                                              [--max-args N] [--max-result N] [--max-text N]
 */

const fs = require('fs');
const os = require('os');
const path = require('path');
const zlib = require('zlib');
const { execFileSync } = require('child_process');

function arg(name, dflt) {
  const i = process.argv.indexOf('--' + name);
  return i >= 0 && process.argv[i + 1] ? process.argv[i + 1] : dflt;
}

const AGENT = arg('agent', 'main');
const LIMIT = Number(arg('limit', '3'));
const MIN_TOOLS = Number(arg('min-tools', '5'));
const SESSION_KEY_FILTER = arg('session-key', '');
const OUT_DIR = path.resolve(arg('out-dir', path.join(process.cwd(), 'memory', 'evolution')));
const MAX_ARGS = Number(arg('max-args', '800'));
const MAX_RESULT = Number(arg('max-result', '1500'));
const MAX_TEXT = Number(arg('max-text', '2000'));

function log(m) { console.log(`[sessions-to-trajectory-transcripts] ${m}`); }
function clip(s, n) {
  if (typeof s !== 'string') s = String(s ?? '');
  return s.length > n ? s.slice(0, n) + ` …[+${s.length - n} chars]` : s;
}

function findDb() {
  const explicit = arg('db', '');
  if (explicit) return explicit;
  for (const home of [process.env.OPENCLAW_HOME, path.join(os.homedir(), '.openclaw'),
                      '/mnt/c/Users/Admin/.openclaw'].filter(Boolean)) {
    const p = path.join(home, 'agents', AGENT, 'agent', 'openclaw-agent.sqlite');
    if (fs.existsSync(p)) return p;
  }
  return null;
}

function stageDb(src) {
  const tmp = path.join(os.tmpdir(), `oc-traj-db-${process.pid}.sqlite`);
  fs.copyFileSync(src, tmp);
  return tmp;
}

function query(dbFile, sql, params = []) {
  const script = `
    const { DatabaseSync } = require('node:sqlite');
    const db = new DatabaseSync(process.argv[1], { readOnly: true });
    const rows = db.prepare(process.argv[2]).all(...JSON.parse(process.argv[3]));
    process.stdout.write(JSON.stringify(rows));
  `;
  const out = execFileSync(process.execPath, ['-e', script, dbFile, sql, JSON.stringify(params)], {
    encoding: 'utf8', maxBuffer: 512 * 1024 * 1024,
  });
  return JSON.parse(out || '[]');
}

function buildMessages(events) {
  const msgs = [];
  let toolPairs = 0;
  for (const ev of events) {
    const d = ev.data || {};
    switch (ev.type) {
      case 'prompt.submitted': {
        const p = clip(d.prompt, MAX_TEXT).trim();
        if (p) msgs.push({ role: 'user', content: p });
        break;
      }
      case 'model.completed': {
        const texts = Array.isArray(d.assistantTexts) ? d.assistantTexts : [];
        const body = clip(texts.join('\n').trim(), MAX_TEXT);
        if (body) msgs.push({ role: 'assistant', content: body });
        break;
      }
      case 'tool.call': {
        if (!d.toolCallId || !d.name) break;
        toolPairs++;
        msgs.push({
          role: 'assistant',
          content: '',
          tool_calls: [{
            id: d.toolCallId,
            type: 'function',
            function: { name: d.name, arguments: clip(JSON.stringify(d.args ?? {}), MAX_ARGS) },
          }],
        });
        break;
      }
      case 'tool.result': {
        if (!d.toolCallId) break;
        const inner = d.result || {};
        const parts = Array.isArray(inner.content) ? inner.content : [];
        const text = clip(parts.map(p => (p && typeof p.text === 'string' ? p.text : '')).join('\n').trim()
                          || (typeof inner === 'string' ? inner : JSON.stringify(inner)), MAX_RESULT);
        msgs.push({ role: 'tool', tool_call_id: d.toolCallId, content: text, success: d.success !== false });
        break;
      }
    }
  }
  return { msgs, toolPairs };
}

function main() {
  const db = findDb();
  if (!db) { log('FATAL: could not locate openclaw-agent.sqlite'); process.exit(1); }
  log(`db: ${db}`);

  const staged = stageDb(db);
  log(`staged copy: ${staged}`);

  try {
    const sessions = query(staged, `
      SELECT session_key, current_session_id
      FROM session_nodes
      WHERE current_session_id IS NOT NULL
      ${SESSION_KEY_FILTER ? 'AND session_key LIKE ?' : ''}
      ORDER BY COALESCE(last_activity_at, 0) DESC
      LIMIT ?`, SESSION_KEY_FILTER ? [`%${SESSION_KEY_FILTER}%`, LIMIT] : [LIMIT]);

    if (!sessions.length) { log('no sessions matched'); return; }
    log(`candidate sessions: ${sessions.length}`);

    fs.mkdirSync(OUT_DIR, { recursive: true });
    let written = 0, skipped = 0;

    for (const s of sessions) {
      const rows = query(staged, `
        SELECT event_json FROM trajectory_runtime_events
        WHERE session_id = ? ORDER BY seq`, [s.current_session_id]);

      const events = [];
      for (const r of rows) {
        // trajectory_runtime_events stores plain event_json only (no event_zstd column)
        if (!r.event_json) continue;
        try { events.push(JSON.parse(r.event_json)); } catch { /* skip malformed */ }
      }

      const { msgs, toolPairs } = buildMessages(events);
      if (toolPairs < MIN_TOOLS) {
        log(`skip ${s.session_key} (tool pairs ${toolPairs} < ${MIN_TOOLS})`);
        skipped++;
        continue;
      }

      const dest = path.join(OUT_DIR, `${s.current_session_id}.trajectory.transcript.jsonl`);
      fs.writeFileSync(dest, msgs.map(m => JSON.stringify(m)).join('\n') + '\n', 'utf8');
      const users = msgs.filter(m => m.role === 'user').length;
      log(`WROTE ${path.basename(dest)}  msgs=${msgs.length} userTurns=${users} toolPairs=${toolPairs}  key=${s.session_key}`);
      written++;
    }

    log(`done: written=${written} skipped=${skipped} outDir=${OUT_DIR}`);
  } finally {
    try { fs.unlinkSync(staged); } catch { /* best effort */ }
  }
}

main();
