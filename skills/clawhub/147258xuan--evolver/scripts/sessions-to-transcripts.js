#!/usr/bin/env node
/**
 * sessions-to-transcripts.js — Convert OpenClaw session jsonl → generic-chat transcript
 * for evolver V2 material ingestion.
 *
 * Usage: node skills/evolver/scripts/sessions-to-transcripts.js [--session <id>] [--min-turns N] [--out-dir <dir>]
 *
 * Converts the most recent (or specified) OpenClaw session log into a
 * *.transcript.jsonl file (OpenAI chat-completions message shape) that
 * `evolver ingest` understands as generic-chat material.
 */

const fs = require('fs');
const path = require('path');

const SESSIONS_DIR = path.join(process.env.OPENCLAW_HOME || path.join(require('os').homedir(), '.openclaw'), 'agents', 'main', 'sessions');
const OUT_DIR = process.argv.includes('--out-dir')
  ? path.resolve(process.argv[process.argv.indexOf('--out-dir') + 1])
  : path.join(process.cwd(), 'memory', 'evolution');
const MIN_TURNS = Number(process.argv.includes('--min-turns')
  ? process.argv[process.argv.indexOf('--min-turns') + 1] : 6);

function log(msg) { console.log(`[sessions-to-transcripts] ${msg}`); }

function contentToText(content) {
  if (typeof content === 'string') return content;
  if (!Array.isArray(content)) return '';
  return content
    .filter((p) => p && typeof p === 'object' && p.type === 'text' && typeof p.text === 'string')
    .map((p) => p.text)
    .join('\n')
    .trim();
}

function contentToThinking(content) {
  if (!Array.isArray(content)) return '';
  return content
    .filter((p) => p && typeof p === 'object' && p.type === 'thinking' && typeof p.thinking === 'string')
    .map((p) => p.thinking)
    .join('\n')
    .trim();
}

function toolCallsToText(content) {
  if (!Array.isArray(content)) return [];
  return content
    .filter((p) => p && typeof p === 'object' && p.type === 'toolCall' && p.name)
    .map((p) => `[tool:${p.name}] ${typeof p.arguments === 'string' ? p.arguments : JSON.stringify(p.arguments || {})}`);
}

function toolResultsToText(msg) {
  if (!msg || typeof msg !== 'object') return '';
  const content = msg.content;
  if (typeof content === 'string') return content;
  if (Array.isArray(content)) {
    return content
      .filter((p) => p && typeof p === 'object' && p.type === 'text' && typeof p.text === 'string')
      .map((p) => p.text)
      .join('\n')
      .trim();
  }
  return '';
}

function convertSession(filePath, sessionId) {
  const lines = fs.readFileSync(filePath, 'utf-8').split('\n').filter(Boolean);
  const out = [];
  let turnCount = 0;
  let systemSeen = false;

  for (const line of lines) {
    let rec;
    try { rec = JSON.parse(line); } catch { continue; }
    if (rec.type !== 'message' || !rec.message || !rec.message.role) continue;

    const role = rec.message.role;
    const m = rec.message;

    if (role === 'system') {
      const text = contentToText(m.content);
      if (text && !systemSeen) { out.push({ role: 'system', content: text }); systemSeen = true; }
      continue;
    }

    if (role === 'user') {
      const text = contentToText(m.content);
      // Skip pure heartbeat polls and system-only wrappers
      if (!text || /^\[(OpenClaw )?(heartbeat poll|System)\]/.test(text)) continue;
      if (text.length < 2) continue;
      out.push({ role: 'user', content: text });
      turnCount++;
      continue;
    }

    if (role === 'assistant') {
      const thinking = contentToThinking(m.content);
      const text = contentToText(m.content);
      const tools = toolCallsToText(m.content);
      const parts = [];
      if (thinking) parts.push(`[thinking] ${thinking}`);
      if (text) parts.push(text);
      if (tools.length) parts.push(tools.join('\n'));
      const content = parts.join('\n\n').trim();
      if (!content) continue;
      out.push({ role: 'assistant', content });
      turnCount++;
      continue;
    }

    if (role === 'toolResult' || role === 'tool') {
      const text = toolResultsToText(m);
      if (!text || text === '(no output)') continue;
      // Attach tool result to previous assistant message for context
      const last = out[out.length - 1];
      if (last && last.role === 'assistant') {
        last.content += `\n[result]\n${text.slice(0, 1500)}`;
      }
      continue;
    }
  }

  if (turnCount < MIN_TURNS) {
    log(`skip ${sessionId}: only ${turnCount} user+assistant turns (< ${MIN_TURNS})`);
    return null;
  }

  const outFile = path.join(OUT_DIR, `session_${sessionId}.transcript.jsonl`);
  fs.mkdirSync(OUT_DIR, { recursive: true });
  fs.writeFileSync(outFile, out.map((r) => JSON.stringify(r)).join('\n') + '\n', 'utf-8');
  log(`wrote ${outFile} (${out.length} messages, ${turnCount} turns)`);
  return outFile;
}

function main() {
  const explicit = process.argv.includes('--session')
    ? process.argv[process.argv.indexOf('--session') + 1]
    : null;

  if (!fs.existsSync(SESSIONS_DIR)) {
    log(`ERROR: sessions dir not found: ${SESSIONS_DIR}`);
    process.exit(1);
  }

  const files = fs.readdirSync(SESSIONS_DIR)
    .filter((f) => f.endsWith('.jsonl') && !f.includes('.trajectory'))
    .map((f) => ({ name: f, stat: fs.statSync(path.join(SESSIONS_DIR, f)) }))
    .sort((a, b) => b.stat.mtimeMs - a.stat.mtimeMs);

  if (files.length === 0) {
    log('ERROR: no session jsonl files found');
    process.exit(1);
  }

  let target;
  if (explicit) {
    target = files.find((f) => f.name.startsWith(explicit));
    if (!target) { log(`ERROR: session ${explicit} not found`); process.exit(1); }
  } else {
    target = files[0]; // most recent
  }

  log(`converting: ${target.name} (${target.stat.size} bytes)`);
  const outFile = convertSession(path.join(SESSIONS_DIR, target.name), target.name.replace('.jsonl', ''));
  if (outFile) {
    log('Done. Next: evolver ingest "' + outFile + '" --dry-run');
  } else {
    process.exit(1);
  }
}

main();
