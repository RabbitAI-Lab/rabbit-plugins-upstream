#!/usr/bin/env node
/**
 * zentao-build-comment.js — 将分析报告 Markdown 转为禅道兼容 HTML
 *
 * 用法:
 *   node zentao-build-comment.js <report.md> [--out <output.html>]
 *
 *   不指定 --out 则输出到 stdout。
 *   输出末尾自动追加来源标记。
 *
 * 转换规则（与 SKILL.md 步骤 5 一致）:
 *   ### xxx      → <h3>xxx</h3>
 *   #### xxx     → <h4>xxx</h4>
 *   **xxx**      → <b>xxx</b>
 *   `xxx`        → <code>xxx</code>
 *   - xxx        → <p>- xxx</p>
 *   代码块       → <pre><code>...</code></pre>
 *   普通段落     → <p>xxx</p>
 *   空行         → <br>
 *   末尾自动附加 <p><i>— Bug终结者 · 自动分析</i></p>
 */

const fs = require('fs');
const path = require('path');

function parseArgs() {
  const args = process.argv.slice(2);
  const config = { input: '', output: '' };
  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--out' && i + 1 < args.length) {
      config.output = args[++i];
    } else if (!config.input && !args[i].startsWith('--')) {
      config.input = args[i];
    }
  }
  return config;
}

function escapeHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

function buildComment(markdown) {
  const lines = markdown.split(/\r?\n/);
  let result = '';
  let inCodeBlock = false;

  for (let i = 0; i < lines.length; i++) {
    let line = lines[i];

    // Code block fence
    if (line.trim().startsWith('```')) {
      if (inCodeBlock) {
        result += '</code></pre>\n';
        inCodeBlock = false;
      } else {
        result += '<pre><code>';
        inCodeBlock = true;
      }
      continue;
    }

    if (inCodeBlock) {
      result += escapeHtml(line) + '\n';
      continue;
    }

    // Empty line → <br>
    if (line.trim() === '') {
      result += '<br>\n';
      continue;
    }

    // Headings
    if (line.startsWith('### ')) {
      result += '<h3>' + line.substring(4).trim() + '</h3>\n';
      continue;
    }
    if (line.startsWith('#### ')) {
      result += '<h4>' + line.substring(5).trim() + '</h4>\n';
      continue;
    }

    // Escape HTML entities first, then apply inline formatting
    let formatted = escapeHtml(line.trim());

    // **bold** → <b>bold</b>
    formatted = formatted.replace(/\*\*(.+?)\*\*/g, '<b>$1</b>');

    // `code` → <code>code</code>
    formatted = formatted.replace(/`([^`]+)`/g, '<code>$1</code>');

    // Table row: | col1 | col2 | → <p>| col1 | col2 |</p>
    if (/^\|.+\|$/.test(formatted)) {
      result += '<p>' + formatted + '</p>\n';
      continue;
    }

    // List item: - xxx
    if (formatted.startsWith('- ')) {
      result += '<p>' + formatted + '</p>\n';
      continue;
    }

    // Numbered list: 1. xxx
    if (/^\d+\.\s/.test(formatted)) {
      result += '<p>' + formatted + '</p>\n';
      continue;
    }

    // Regular paragraph
    result += '<p>' + formatted + '</p>\n';
  }

  // Close any unclosed code block
  if (inCodeBlock) {
    result += '</code></pre>\n';
  }

  // Append source footer
  result += '<p><i>— Bug终结者 · 自动分析</i></p>\n';

  return result.trim();
}

function main() {
  const config = parseArgs();

  if (!config.input) {
    console.error('[ERROR] 缺少输入文件参数');
    console.error('用法: node zentao-build-comment.js <report.md> [--out <output.html>]');
    process.exit(1);
  }

  if (!fs.existsSync(config.input)) {
    console.error('[ERROR] 文件不存在: ' + config.input);
    process.exit(1);
  }

  const markdown = fs.readFileSync(config.input, 'utf-8');
  const html = buildComment(markdown);

  if (config.output) {
    fs.writeFileSync(config.output, html, 'utf-8');
    console.error('[INFO] HTML 已写入: ' + config.output);
    console.log('OK');
  } else {
    process.stdout.write(html);
  }
}

main();
