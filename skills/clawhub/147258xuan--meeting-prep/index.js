// Cycle #0038 — meeting-prep skill entry point
const fs = require('fs');
const path = require('path');

const WORKSPACE = process.env.WORKSPACE_ROOT || process.cwd();
const MEMORY_DIR = path.join(WORKSPACE, 'memory');
const LEARNINGS_DIR = path.join(WORKSPACE, '.learnings');

function readRecentMemories(days = 3) {
  const now = Date.now();
  const cutoff = now - days * 24 * 60 * 60 * 1000;
  const files = fs.readdirSync(MEMORY_DIR).filter(f => f.endsWith('.md'));
  const snippets = [];
  for (const file of files) {
    const full = path.join(MEMORY_DIR, file);
    const stat = fs.statSync(full);
    if (stat.mtimeMs >= cutoff) {
      snippets.push({ file, mtime: stat.mtimeMs, content: fs.readFileSync(full, 'utf8') });
    }
  }
  snippets.sort((a, b) => b.mtime - a.mtime);
  return snippets;
}

function readRecentLearnings(days = 7) {
  if (!fs.existsSync(LEARNINGS_DIR)) return [];
  const now = Date.now();
  const cutoff = now - days * 24 * 60 * 60 * 1000;
  const files = fs.readdirSync(LEARNINGS_DIR).filter(f => f.endsWith('.md'));
  const snippets = [];
  for (const file of files) {
    const full = path.join(LEARNINGS_DIR, file);
    const stat = fs.statSync(full);
    if (stat.mtimeMs >= cutoff) {
      snippets.push({ file, mtime: stat.mtimeMs, content: fs.readFileSync(full, 'utf8') });
    }
  }
  snippets.sort((a, b) => b.mtime - a.mtime);
  return snippets;
}

function extractHighPriority(snippets) {
  const lines = [];
  for (const s of snippets) {
    for (const line of s.content.split('\n')) {
      const trimmed = line.trim();
      if (!trimmed) continue;
      if (/^(#|<!--|\[memory-promotion)/.test(trimmed)) continue;
      if (trimmed.length < 5) continue;
      lines.push({ source: s.file, text: trimmed });
    }
  }
  return lines.slice(0, 40);
}

function buildBrief(snippets) {
  const items = extractHighPriority(snippets);
  const learnings = readRecentLearnings(7);
  const lines = ['# Meeting Prep Brief', '', `Generated: ${new Date().toISOString()}`, '', `Sources: ${snippets.length} recent memory file(s)`];
  if (items.length === 0) {
    lines.push('', '> No recent memory activity found in the last 3 days.');
    return lines.join('\n');
  }
  lines.push('', '## Top Context');
  for (const item of items) {
    lines.push(`- ${item.text}`);
  }
  lines.push('', '## Open Items');
  for (const item of items.filter(i => /TODO|FIXME|pending|open|待办|待确认/.test(i.text))) {
    lines.push(`- ${item.text}`);
  }
  if (learnings.length > 0) {
    lines.push('', '## Recent Learnings');
    for (const l of learnings) {
      const recentLines = l.content.split('\n').filter(ln => ln.trim().startsWith('## ')).slice(0, 3);
      for (const rl of recentLines) {
        lines.push(`- ${rl.replace(/^## /, '')} (${l.file})`);
      }
    }
  }
  return lines.join('\n');
}

function main() {
  const snippets = readRecentMemories(3);
  const brief = buildBrief(snippets);
  console.log(brief);
  return brief;
}

module.exports = { main, readRecentMemories, readRecentLearnings, buildBrief };
