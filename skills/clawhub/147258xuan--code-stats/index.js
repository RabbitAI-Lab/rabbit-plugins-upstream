const fs = require('fs');
const path = require('path');

const SKIP_DIRS = new Set(['node_modules', '.git', '.next', 'dist', 'build', '__pycache__', '.cache', '.openclaw']);
const TEXT_EXTS = new Set(['.js', '.ts', '.jsx', '.tsx', '.py', '.rb', '.go', '.rs', '.java', '.c', '.cpp', '.h', '.hpp', '.cs', '.php', '.html', '.css', '.scss', '.less', '.json', '.yaml', '.yml', '.toml', '.xml', '.md', '.txt', '.sh', '.bat', '.ps1', '.vue', '.svelte']);

function walkDir(dir, files) {
  files = files || [];
  let entries;
  try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch (e) { return files; }
  for (const entry of entries) {
    if (SKIP_DIRS.has(entry.name)) continue;
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walkDir(fullPath, files);
    } else if (entry.isFile()) {
      files.push(fullPath);
    }
  }
  return files;
}

function analyze(dir) {
  dir = path.resolve(dir);
  const files = walkDir(dir);
  const filesByExt = {};
  const linesByExt = {};
  let totalFiles = 0;
  let totalLines = 0;

  for (const f of files) {
    const ext = path.extname(f).toLowerCase() || '(no ext)';
    filesByExt[ext] = (filesByExt[ext] || 0) + 1;
    totalFiles++;

    if (TEXT_EXTS.has(ext)) {
      try {
        const content = fs.readFileSync(f, 'utf8');
        const lines = content.split('\n').length;
        linesByExt[ext] = (linesByExt[ext] || 0) + lines;
        totalLines += lines;
      } catch (e) { /* skip binary or unreadable */ }
    }
  }

  // Language breakdown
  const languageBreakdown = {};
  const langMap = {
    '.js': 'JavaScript', '.jsx': 'JavaScript', '.ts': 'TypeScript', '.tsx': 'TypeScript',
    '.py': 'Python', '.rb': 'Ruby', '.go': 'Go', '.rs': 'Rust', '.java': 'Java',
    '.c': 'C', '.cpp': 'C++', '.h': 'C/C++', '.hpp': 'C++', '.cs': 'C#',
    '.php': 'PHP', '.html': 'HTML', '.css': 'CSS', '.scss': 'SCSS',
    '.json': 'JSON', '.yaml': 'YAML', '.yml': 'YAML', '.md': 'Markdown',
    '.sh': 'Shell', '.bat': 'Batch', '.ps1': 'PowerShell', '.vue': 'Vue', '.svelte': 'Svelte'
  };

  for (const [ext, count] of Object.entries(linesByExt)) {
    const lang = langMap[ext] || ext;
    languageBreakdown[lang] = (languageBreakdown[lang] || 0) + count;
  }

  // Sort by lines descending
  const sorted = Object.entries(languageBreakdown).sort((a, b) => b[1] - a[1]);
  const sortedBreakdown = {};
  for (const [lang, lines] of sorted) {
    sortedBreakdown[lang] = totalLines > 0 ? ((lines / totalLines) * 100).toFixed(1) + '%' : '0%';
  }

  return { dir, filesByExt, linesByExt, totalFiles, totalLines, languageBreakdown: sortedBreakdown };
}

function countTodos(dir) {
  dir = path.resolve(dir);
  const files = walkDir(dir);
  const todoPattern = /\b(TODO|FIXME|HACK|XXX)\b[\s:：]*(.*)/gi;
  let count = 0;
  const details = [];

  for (const f of files) {
    const ext = path.extname(f).toLowerCase();
    if (!TEXT_EXTS.has(ext)) continue;
    try {
      const content = fs.readFileSync(f, 'utf8');
      const lines = content.split('\n');
      for (let i = 0; i < lines.length; i++) {
        const matches = lines[i].match(todoPattern);
        if (matches) {
          count += matches.length;
          details.push({ file: path.relative(dir, f), line: i + 1, text: lines[i].trim().substring(0, 120) });
        }
      }
    } catch (e) { /* skip */ }
  }

  return { count, details };
}

function report(stats) {
  const lines = [];
  lines.push('=== Code Stats ===');
  lines.push('Directory: ' + stats.dir);
  lines.push('Total files: ' + stats.totalFiles);
  lines.push('Total lines: ' + stats.totalLines);
  lines.push('');
  lines.push('Language breakdown:');
  for (const [lang, pct] of Object.entries(stats.languageBreakdown)) {
    lines.push('  ' + lang + ': ' + pct);
  }
  lines.push('');
  lines.push('Top extensions by file count:');
  const sortedExts = Object.entries(stats.filesByExt).sort((a, b) => b[1] - a[1]).slice(0, 10);
  for (const [ext, count] of sortedExts) {
    lines.push('  ' + ext + ': ' + count + ' files');
  }
  return lines.join('\n');
}

module.exports = { analyze, countTodos, report };
