'use strict';

const fs = require('fs');
const path = require('path');

const DEFAULT_IGNORE = ['node_modules', '.git', 'dist', 'build', '.next', 'coverage', 'todos.json'];
const DEFAULT_EXTENSIONS = ['.js', '.ts', '.py', '.md', '.json', '.yaml', '.yml', '.sh', '.ps1'];
const TAG_PATTERN = /\b(TODO|FIXME|HACK|XXX)\b[\s:：]*(.*)/i;
const DESCRIPTIVE_TAG_LIST = /(TODO|FIXME|HACK|XXX)[/\\s,]+(TODO|FIXME|HACK|XXX)/i;

function collectFiles(dir, extensions, ignore, results) {
  results = results || [];
  let entries;
  try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch (_) { return results; }
  for (const entry of entries) {
    if (ignore.includes(entry.name)) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) { collectFiles(full, extensions, ignore, results); }
    else if (extensions.includes(path.extname(entry.name).toLowerCase())) { results.push(full); }
  }
  return results;
}

function scanFile(filePath) {
  let content;
  try { content = fs.readFileSync(filePath, 'utf8'); } catch (_) { return []; }
  const lines = content.split('\n');
  const todos = [];
  for (let i = 0; i < lines.length; i++) {
    const match = TAG_PATTERN.exec(lines[i]);
    if (match) {
      // Skip lines that list tags as part of a description (e.g. "TODO/FIXME/HACK comments")
      if (DESCRIPTIVE_TAG_LIST.test(lines[i])) continue;
      todos.push({ file: filePath, line: i + 1, column: match.index + 1, tag: match[1].toUpperCase(), text: match[2].trim(), context: lines[i].trim() });
    }
  }
  return todos;
}

function scanTodos(rootDir, options) {
  rootDir = rootDir || '.';
  const ext = (options && options.extensions) || DEFAULT_EXTENSIONS;
  const ign = (options && options.ignore) || DEFAULT_IGNORE;
  const files = collectFiles(path.resolve(rootDir), ext, ign);
  const all = [];
  for (const f of files) { all.push(...scanFile(f)); }
  return all;
}

function formatReport(todos) {
  if (!todos || todos.length === 0) return 'No TODOs found.';
  const groups = {};
  for (const t of todos) { (groups[t.tag] = groups[t.tag] || []).push(t); }
  const lines = [];
  for (const [tag, items] of Object.entries(groups).sort()) {
    lines.push('\n## ' + tag + ' (' + items.length + ')');
    for (const item of items) { lines.push('  ' + item.file + ':' + item.line + ' — ' + (item.text || item.context)); }
  }
  return lines.join('\n');
}

function saveTodos(todos, outputPath) {
  outputPath = outputPath || 'memory/todos.json';
  const dir = path.dirname(outputPath);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(outputPath, JSON.stringify(todos, null, 2), 'utf8');
  return outputPath;
}

function getSummary(todos) {
  if (!todos || todos.length === 0) return { total: 0, byTag: {} };
  const byTag = {};
  for (const t of todos) { byTag[t.tag] = (byTag[t.tag] || 0) + 1; }
  return { total: todos.length, byTag };
}

/**
 * Filter todos by a specific tag.
 */
function filterByTag(todos, tag) {
  if (!todos) return [];
  return todos.filter(function(t) { return t.tag === tag.toUpperCase(); });
}

/**
 * Filter todos by file extension.
 */
function filterByExtension(todos, ext) {
  if (!todos) return [];
  const normalized = ext.toLowerCase().replace(/^\./, '');
  return todos.filter(function(t) {
    const fileExt = path.extname(t.file).toLowerCase().replace(/^\./, '');
    return fileExt === normalized;
  });
}

module.exports = { scanTodos, formatReport, saveTodos, scanFile, collectFiles, getSummary, filterByTag };
