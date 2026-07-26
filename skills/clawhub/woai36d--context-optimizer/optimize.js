#!/usr/bin/env node
/**
 * Context Optimizer - Daily context optimization script
 * 
 * Run daily to clean up and compress context:
 * 1. Optimize today's daily memory (archive detail, keep summary)
 * 2. Clean historical session memory (archive inactive, keep active)
 * 3. Archive old daily memories (>7 days)
 * 4. Optimize DREAMS.md if bloated
 */

const fs = require('fs');
const path = require('path');

const WORKSPACE = '/Users/andy51/.openclaw/workspace';
const MEMORY_DIR = path.join(WORKSPACE, 'memory');
const ARCHIVE_DIR = path.join(MEMORY_DIR, 'archive');
const SESSION_ARCHIVE_DIR = path.join(ARCHIVE_DIR, 'sessions');
const DREAM_ARCHIVE_DIR = path.join(ARCHIVE_DIR, 'dream-diary');

// Ensure directories exist
[ARCHIVE_DIR, SESSION_ARCHIVE_DIR, DREAM_ARCHIVE_DIR].forEach(dir => {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
});

const NOW = new Date();
const DATE_STR = NOW.toISOString().slice(0, 10);
const SEVEN_DAYS_MS = 7 * 24 * 60 * 60 * 1000;
const FOURTEEN_DAYS_MS = 14 * 24 * 60 * 60 * 1000;

// Stats
const stats = {
  optimized: [],
  archived: [],
  errors: []
};

// Active task markers — files containing these will NOT be archived
const ACTIVE_MARKERS = [
  '⏳',            // 进行中
  'TODO',          // TODO
  '[ ]',           // 未完成复选框
  '进行中',         // 中文标记
  'pending',       // 英文标记
  '⏸',            // 暂停
  '待处理',         // 待处理
];

function hasActiveTasks(content) {
  return ACTIVE_MARKERS.some(marker => content.includes(marker));
}

// 1. Optimize Today's Daily Memory
function optimizeDailyMemory() {
  const dailyFile = path.join(MEMORY_DIR, `${DATE_STR}.md`);
  if (!fs.existsSync(dailyFile)) return;

  const content = fs.readFileSync(dailyFile, 'utf8');
  const size = content.length;

  if (size < 1024) return;

  // Extract ## sections
  const lines = content.split('\n');
  const sections = [];
  let currentSection = [];
  let inSection = false;

  for (const line of lines) {
    if (line.match(/^##\s+/)) {
      if (currentSection.length > 0) sections.push(currentSection.join('\n'));
      currentSection = [line];
      inSection = true;
    } else if (inSection) {
      currentSection.push(line);
    }
  }
  if (currentSection.length > 0) sections.push(currentSection.join('\n'));

  // Archive original
  const archiveFile = path.join(ARCHIVE_DIR, `${DATE_STR}-detail.md`);
  fs.writeFileSync(archiveFile, content);

  // Write optimized version
  const optimized = `# ${DATE_STR} Daily Log\n\n${sections.join('\n\n')}\n\n> 详细日志: archive/${DATE_STR}-detail.md\n`;
  fs.writeFileSync(dailyFile, optimized);

  stats.optimized.push({
    file: `${DATE_STR}.md`,
    before: size,
    after: optimized.length,
    saved: size - optimized.length
  });
}

// 2. Archive Historical Session Memories (ALL dates, not just today)
function cleanHistoricalSessionMemory() {
  const files = fs.readdirSync(MEMORY_DIR);

  // Match: YYYY-MM-DD-description.md (session memories with description or timestamp)
  // Excludes: YYYY-MM-DD.md (daily memories), non-date topic files
  const sessionPattern = /^\d{4}-\d{2}-\d{2}-.+\.md$/;

  for (const file of files) {
    if (!sessionPattern.test(file)) continue;

    // Skip today's session memories (they might still be active)
    if (file.startsWith(DATE_STR)) continue;

    const filePath = path.join(MEMORY_DIR, file);
    let content;
    try {
      content = fs.readFileSync(filePath, 'utf8');
    } catch (e) {
      stats.errors.push(`Failed to read: ${file}`);
      continue;
    }

    // Parse file date
    const fileDateStr = file.slice(0, 10);
    const fileDate = new Date(fileDateStr);
    if (isNaN(fileDate.getTime())) continue;

    // Files older than 14 days: archive regardless of active markers
    const isStale = (NOW - fileDate > FOURTEEN_DAYS_MS);

    // Preserve files with active tasks (unless too old)
    if (!isStale && hasActiveTasks(content)) continue;

    // Archive
    const archivePath = path.join(SESSION_ARCHIVE_DIR, file);
    try {
      fs.renameSync(filePath, archivePath);
      stats.archived.push({ file, size: content.length });
    } catch (e) {
      stats.errors.push(`Failed to archive: ${file}`);
    }
  }
}

// 3. Archive Old Daily Memories (>7 days old, >1KB)
function cleanOldDailyMemories() {
  const files = fs.readdirSync(MEMORY_DIR);
  // Match: YYYY-MM-DD.md (daily memories only)
  const dailyPattern = /^\d{4}-\d{2}-\d{2}\.md$/;

  for (const file of files) {
    if (!dailyPattern.test(file)) continue;

    // Skip today
    if (file === `${DATE_STR}.md`) continue;

    // Parse date from filename
    const fileDateStr = file.replace('.md', '');
    const fileDate = new Date(fileDateStr);
    if (isNaN(fileDate.getTime())) continue;

    // Skip files newer than 7 days
    if (NOW - fileDate < SEVEN_DAYS_MS) continue;

    const filePath = path.join(MEMORY_DIR, file);
    let content;
    try {
      content = fs.readFileSync(filePath, 'utf8');
    } catch (e) {
      stats.errors.push(`Failed to read: ${file}`);
      continue;
    }

    // Skip small files (already optimized)
    if (content.length < 1024) continue;

    // Files older than 14 days: archive regardless of active markers
    const isStale = (NOW - fileDate > FOURTEEN_DAYS_MS);

    // Preserve files with active tasks (unless too old)
    if (!isStale && hasActiveTasks(content)) continue;

    // Archive
    const archivePath = path.join(ARCHIVE_DIR, file);
    try {
      fs.renameSync(filePath, archivePath);
      stats.archived.push({ file, size: content.length });
    } catch (e) {
      stats.errors.push(`Failed to archive: ${file}`);
    }
  }
}

// 4. Optimize DREAMS.md if bloated
function optimizeDreams() {
  const dreamsFile = path.join(WORKSPACE, 'DREAMS.md');
  if (!fs.existsSync(dreamsFile)) return;

  const content = fs.readFileSync(dreamsFile, 'utf8');
  const size = content.length;

  if (size < 1024) return;

  // Archive with timestamp to avoid overwriting
  const timestamp = Date.now();
  const archiveFile = path.join(DREAM_ARCHIVE_DIR, `${DATE_STR}-${timestamp}.md`);
  fs.writeFileSync(archiveFile, content);

  // Write summary version
  const summary = `# Dream Summary\n\n## 核心主题\n- 技术学习、项目开发、系统维护\n\n## 关键决策\n- 详见 archive/dream-diary/${DATE_STR}-${timestamp}.md\n\n## 生成规则\n> 由 memory-core dreaming 任务自动生成\n> 详细日记已归档到 memory/archive/dream-diary/\n`;
  fs.writeFileSync(dreamsFile, summary);

  stats.optimized.push({
    file: 'DREAMS.md',
    before: size,
    after: summary.length,
    saved: size - summary.length
  });
}

// ===== MAIN =====
console.log(`[${DATE_STR}] Starting context optimization...\n`);

try {
  // Step 1: Optimize today's daily memory
  console.log('Step 1: Optimize daily memory...');
  optimizeDailyMemory();

  // Step 2: Archive historical session memories (all dates, not just today)
  console.log('Step 2: Archive historical session memories...');
  cleanHistoricalSessionMemory();

  // Step 3: Archive old daily memories (>7 days, >1KB, no active tasks)
  console.log('Step 3: Archive old daily memories...');
  cleanOldDailyMemories();

  // Step 4: Optimize DREAMS.md
  console.log('Step 4: Optimize DREAMS.md...');
  optimizeDreams();

  // Report
  const totalSaved = stats.optimized.reduce((sum, item) => sum + item.saved, 0);
  const totalArchived = stats.archived.reduce((sum, item) => sum + item.size, 0);

  console.log('\n=== Optimization Report ===');
  console.log(`Date: ${DATE_STR}`);

  if (stats.optimized.length > 0) {
    console.log(`\nOptimized: ${stats.optimized.length} file(s)`);
    stats.optimized.forEach(item => {
      console.log(`  - ${item.file}: ${item.before}B → ${item.after}B (saved ${item.saved}B)`);
    });
  }

  if (stats.archived.length > 0) {
    console.log(`\nArchived: ${stats.archived.length} file(s) → archive/`);
    stats.archived.forEach(item => {
      console.log(`  - ${item.file}: ${item.size}B`);
    });
  }

  console.log(`\nSummary:`);
  console.log(`  Optimized bytes: ${totalSaved}B (${Math.round(totalSaved/1024)}KB)`);
  console.log(`  Archived bytes:  ${totalArchived}B (${Math.round(totalArchived/1024)}KB)`);

  if (stats.errors.length > 0) {
    console.log(`\n⚠️  Errors: ${stats.errors.length}`);
    stats.errors.forEach(err => console.log(`  - ${err}`));
  }

} catch (error) {
  console.error('Optimization failed:', error);
  process.exit(1);
}

console.log('\n✅ Optimization complete!');
