#!/usr/bin/env node
/**
 * sessions-to-transcripts-sqlite.js — Export OpenClaw sessions from the agent SQLite
 * store into generic-chat transcripts for evolver V2 material ingestion.
 *
 * Replaces the jsonl path in sessions-to-transcripts.js, which stopped working after
 * OpenClaw 2026.8.1 migrated live sessions from jsonl files into SQLite.
 *
 * Usage:
 *   node sessions-to-transcripts-sqlite.js [--limit N] [--min-turns M]
 *                                          [--session-key SUBSTR] [--out-dir DIR]
 *                                          [--db PATH] [--agent main]
 *
 * Chain: session_nodes -> session_windows -> session_transcript_active_events
 *        -> transcript_event_identities (event_type) -> transcript_events (payload)
 *
 * Writes <session_id>.transcript.jsonl, one {"role","content"} per line.
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
const MIN_TURNS = Number(arg('min-turns', '4'));
const SESSION_KEY_FILTER = arg('session-key', '');
const OUT_DIR = path.resolve(arg('out-dir', path.join(process.cwd(), 'memory', 'evolution')));

function log(m) { console.log(`[sessions-to-transcripts-sqlite] ${m}`); }

// ---- locate the agent sqlite ----
function findDb() {
  const explicit = arg('db', '');
  if (explicit) return explicit;
  const homes = [
    process.env.OPENCLAW_HOME,
    path.join(os.homedir(), '.openclaw'),
    '/mnt/c/Users/Admin/.openclaw',
  ].filter(Boolean);
  for (const home of homes) {
    const p = path.join(home, 'agents', AGENT, 'agent', 'openclaw-agent.sqlite');
    if (fs.existsSync(p)) return p;
  }
  return null;
}

// ---- copy off /mnt/c: sqlite locking fails on the Windows mount ----
function stageDb(src) {
  const tmp = path.join(os.tmpdir(), `oc-agent-db-${process.pid}.sqlite`);
  fs.copyFileSync(src, tmp);
  return tmp;
}

// ---- sqlite access via the node -e child (keeps this file dependency-free) ----
function query(dbFile, sql, params = []) {
  const script = `
    const { DatabaseSync } = require('node:sqlite');
    const db = new DatabaseSync(process.argv[1], { readOnly: true });
    const stmt = db.prepare(process.argv[2]);
    const rows = stmt.all(...JSON.parse(process.argv[3]));
    process.stdout.write(JSON.stringify(rows));
  `;
  const out = execFileSync(process.execPath, ['-e', script, dbFile, sql, JSON.stringify(params)], {
    encoding: 'utf8', maxBuffer: 256 * 1024 * 1024,
  });
  return JSON.parse(out || '[]');
}

function decodeEvent(row) {
  if (row.event_json) return row.event_json;
  if (row.event_zstd) {
    const buf = zlib.zstdDecompressSync(Buffer.from(row.event_zstd));
    return buf.toString('utf8');
  }
  return null;
}

function contentToText(content) {
  if (typeof content === 'string') return content;
  if (!Array.isArray(content)) return '';
  const chunks = [];
  for (const p of content) {
    if (!p || typeof p !== 'object') continue;
    if (p.type === 'text' && typeof p.text === 'string') chunks.push(p.text);
    else if (p.type === 'thinking' && typeof p.thinking === 'string') chunks.push(`[thinking] ${p.thinking}`);
    else if (p.type === 'toolCall' && p.name) {
      const a = typeof p.arguments === 'string' ? p.arguments : JSON.stringify(p.arguments ?? {});
      chunks.push(`[tool:${p.name}] ${a}`);
    }
  }
  return chunks.join('\n').trim();
}

function main() {
  const db = findDb();
  if (!db) { log('FATAL: could not locate openclaw-agent.sqlite'); process.exit(1); }
  log(`db: ${db}`);

  const staged = stageDb(db);
  log(`staged copy: ${staged} (sqlite on /mnt/c cannot lock)`);

  try {
    const sessions = query(staged, `
      SELECT session_key, current_session_id, last_activity_at, status
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
        SELECT e.event_json, e.event_zstd, i.event_type
        FROM session_transcript_active_events a
        JOIN transcript_event_identities i
          ON i.session_id = a.session_id AND i.seq = a.event_seq
        JOIN transcript_events e
          ON e.session_id = a.session_id AND e.seq = a.event_seq
        WHERE a.session_id = ?
        ORDER BY a.active_position`, [s.current_session_id]);

      const out = [];
      for (const r of rows) {
        if (r.event_type !== 'message') continue;
        let obj;
        try { obj = JSON.parse(decodeEvent(r) || 'null'); } catch { continue; }
        if (!obj || obj.type !== 'message' || !obj.message) continue;
        const role = obj.message.role;
        if (role !== 'user' && role !== 'assistant') continue;
        const text = contentToText(obj.message.content);
        if (!text) continue;
        out.push({ role, content: text });
      }

      const turns = out.filter(m => m.role === 'user').length;
      if (turns < MIN_TURNS) {
        log(`skip ${s.session_key} (user turns ${turns} < ${MIN_TURNS})`);
        skipped++;
        continue;
      }

      const dest = path.join(OUT_DIR, `${s.current_session_id}.transcript.jsonl`);
      fs.writeFileSync(dest, out.map(m => JSON.stringify(m)).join('\n') + '\n', 'utf8');
      log(`WROTE ${path.basename(dest)}  msgs=${out.length} userTurns=${turns}  key=${s.session_key}`);
      written++;
    }

    log(`done: written=${written} skipped=${skipped} outDir=${OUT_DIR}`);
  } finally {
    try { fs.unlinkSync(staged); } catch {}
  }
}

main();
