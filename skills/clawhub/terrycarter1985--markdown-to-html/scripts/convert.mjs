#!/usr/bin/env node
/**
 * Markdown to HTML Converter
 * Converts Markdown files to standalone styled HTML.
 */

import { readFileSync, writeFileSync, existsSync } from "fs";
import { resolve, basename } from "path";

// --- Minimal Markdown Parser (no external deps) ---

function escapeHtml(str) {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function parseInline(text) {
  // Code first to avoid conflicts
  text = text.replace(/`([^`]+)`/g, '<code>$1</code>');
  // Bold
  text = text.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
  // Italic
  text = text.replace(/\*(.+?)\*/g, "<em>$1</em>");
  // Links [text](url)
  text = text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
  // Images ![alt](url)
  text = text.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, '<img alt="$1" src="$2" />');
  // Strikethrough
  text = text.replace(/~~(.+?)~~/g, "<del>$1</del>");
  return text;
}

function parseMarkdown(md) {
  const lines = md.split("\n");
  const html = [];
  const toc = [];
  let inCodeBlock = false;
  let codeLang = "";
  let codeContent = [];
  let inList = false;
  let listType = ""; // ul or ol
  let inBlockquote = false;
  let inTable = false;
  let tableRows = [];

  function closeList() {
    if (inList) {
      html.push(`</${listType}>`);
      inList = false;
      listType = "";
    }
  }

  function closeBlockquote() {
    if (inBlockquote) {
      html.push("</blockquote>");
      inBlockquote = false;
    }
  }

  function flushTable() {
    if (inTable && tableRows.length > 0) {
      html.push('<table>');
      // Header
      html.push("<thead><tr>");
      tableRows[0].forEach((cell) => {
        html.push(`<th>${parseInline(cell)}</th>`);
      });
      html.push("</tr></thead>");
      // Body
      if (tableRows.length > 1) {
        html.push("<tbody>");
        for (let i = 1; i < tableRows.length; i++) {
          html.push("<tr>");
          tableRows[i].forEach((cell) => {
            html.push(`<td>${parseInline(cell)}</td>`);
          });
          html.push("</tr>");
        }
        html.push("</tbody>");
      }
      html.push("</table>");
      inTable = false;
      tableRows = [];
    }
  }

  let idCounter = 0;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    // Code block handling
    if (line.startsWith("```")) {
      if (!inCodeBlock) {
        closeList();
        closeBlockquote();
        flushTable();
        inCodeBlock = true;
        codeLang = line.slice(3).trim();
        codeContent = [];
      } else {
        const langClass = codeLang ? ` class="language-${codeLang}"` : ' class="language-text"';
        html.push(`<pre><code${langClass}>${escapeHtml(codeContent.join("\n"))}</code></pre>`);
        inCodeBlock = false;
        codeLang = "";
      }
      continue;
    }

    if (inCodeBlock) {
      codeContent.push(line);
      continue;
    }

    // Horizontal rule
    if (/^---+$/.test(line.trim())) {
      closeList();
      closeBlockquote();
      flushTable();
      html.push("<hr />");
      continue;
    }

    // Headings
    const headingMatch = line.match(/^(#{1,6})\s+(.+)/);
    if (headingMatch) {
      closeList();
      closeBlockquote();
      flushTable();
      const level = headingMatch[1].length;
      const text = headingMatch[2];
      const id = `sec-${idCounter++}`;
      html.push(`<h${level} id="${id}">${parseInline(text)}</h${level}>`);
      if (level <= 3) {
        toc.push({ level, text, id });
      }
      continue;
    }

    // Table
    if (line.includes("|") && line.trim().startsWith("|")) {
      const cells = line.split("|").slice(1, -1).map((c) => c.trim());
      // Skip separator row (---|---)
      if (cells.every((c) => /^[-:]+$/.test(c))) continue;
      if (!inTable) {
        closeList();
        closeBlockquote();
        inTable = true;
        tableRows = [];
      }
      tableRows.push(cells);
      continue;
    } else {
      flushTable();
    }

    // Blockquote
    if (line.startsWith(">")) {
      closeList();
      if (!inBlockquote) {
        html.push("<blockquote>");
        inBlockquote = true;
      }
      html.push(`<p>${parseInline(line.replace(/^>\s?/, ""))}</p>`);
      continue;
    } else {
      closeBlockquote();
    }

    // Unordered list
    const ulMatch = line.match(/^[-*+]\s+(.+)/);
    if (ulMatch) {
      if (!inList || listType !== "ul") {
        closeList();
        html.push("<ul>");
        inList = true;
        listType = "ul";
      }
      html.push(`<li>${parseInline(ulMatch[1])}</li>`);
      continue;
    }

    // Ordered list
    const olMatch = line.match(/^\d+\.\s+(.+)/);
    if (olMatch) {
      if (!inList || listType !== "ol") {
        closeList();
        html.push("<ol>");
        inList = true;
        listType = "ol";
      }
      html.push(`<li>${parseInline(olMatch[1])}</li>`);
      continue;
    }

    closeList();

    // Empty line
    if (line.trim() === "") continue;

    // Paragraph (collect consecutive non-empty lines)
    let para = line;
    while (i + 1 < lines.length && lines[i + 1].trim() !== "" && !lines[i + 1].match(/^(#{1,6}\s|```|[-*+]\s|\d+\.\s|>\s|\|)/)) {
      i++;
      para += " " + lines[i].trim();
    }
    html.push(`<p>${parseInline(para)}</p>`);
  }

  closeList();
  closeBlockquote();
  flushTable();

  return { body: html.join("\n"), toc };
}

// --- CSS Themes ---

const themes = {
  light: `
    :root { --bg: #ffffff; --fg: #1a1a2e; --muted: #666; --accent: #4361ee; --code-bg: #f5f5f5; --border: #e0e0e0; --table-header: #f0f4ff; }
    body { background: var(--bg); color: var(--fg); }
    a { color: var(--accent); }
    code { background: var(--code-bg); }
    pre { background: var(--code-bg); }
    th { background: var(--table-header); }
    blockquote { border-left: 4px solid var(--accent); }
    hr { border-color: var(--border); }
  `,
  dark: `
    :root { --bg: #1a1a2e; --fg: #e0e0e0; --muted: #999; --accent: #4cc9f0; --code-bg: #16213e; --border: #333; --table-header: #16213e; }
    body { background: var(--bg); color: var(--fg); }
    a { color: var(--accent); }
    code { background: var(--code-bg); }
    pre { background: var(--code-bg); }
    th { background: var(--table-header); }
    blockquote { border-left: 4px solid var(--accent); }
    hr { border-color: var(--border); }
  `,
  classic: `
    :root { --bg: #fefae0; --fg: #283618; --muted: #606c38; --accent: #bc6c25; --code-bg: #dda15e; --border: #dda15e; --table-header: #dda15e; }
    body { background: var(--bg); color: var(--fg); font-family: Georgia, serif; }
    a { color: var(--accent); }
    code { background: var(--code-bg); }
    pre { background: var(--code-bg); }
    th { background: var(--table-header); }
    blockquote { border-left: 4px solid var(--accent); }
    hr { border-color: var(--border); }
  `,
};

const baseStyle = `
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    max-width: 800px; margin: 2rem auto; padding: 0 1rem;
    line-height: 1.7; font-size: 16px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  }
  h1 { font-size: 2em; margin: 1.5em 0 0.5em; border-bottom: 2px solid var(--border); padding-bottom: 0.3em; }
  h2 { font-size: 1.5em; margin: 1.5em 0 0.5em; border-bottom: 1px solid var(--border); padding-bottom: 0.2em; }
  h3 { font-size: 1.25em; margin: 1.2em 0 0.4em; }
  h4, h5, h6 { margin: 1em 0 0.3em; }
  p { margin: 0.8em 0; }
  a { text-decoration: none; }
  a:hover { text-decoration: underline; }
  code { padding: 0.15em 0.4em; border-radius: 3px; font-size: 0.9em; font-family: 'SF Mono', Consolas, monospace; }
  pre { padding: 1em; border-radius: 6px; overflow-x: auto; margin: 1em 0; }
  pre code { background: none; padding: 0; }
  blockquote { padding: 0.5em 1em; margin: 1em 0; background: rgba(0,0,0,0.03); border-radius: 0 4px 4px 0; }
  blockquote p { margin: 0.3em 0; }
  ul, ol { margin: 0.8em 0; padding-left: 2em; }
  li { margin: 0.3em 0; }
  table { width: 100%; border-collapse: collapse; margin: 1em 0; }
  th, td { border: 1px solid var(--border); padding: 0.5em 0.8em; text-align: left; }
  img { max-width: 100%; height: auto; border-radius: 4px; }
  hr { margin: 2em 0; border: none; border-top: 1px solid var(--border); }
  .toc { background: rgba(0,0,0,0.03); padding: 1em 1.5em; border-radius: 6px; margin: 1em 0; }
  .toc h2 { border: none; margin: 0 0 0.5em; font-size: 1.1em; }
  .toc ul { list-style: none; padding-left: 1em; }
  .toc ul ul { padding-left: 1.5em; }
  .toc a { color: var(--accent); }
  @media (max-width: 600px) {
    body { font-size: 15px; margin: 1rem auto; }
    pre { padding: 0.8em; }
  }
  @media print {
    body { max-width: 100%; margin: 0; }
    pre { overflow: hidden; }
  }
`;

// --- CLI ---

function parseArgs(argv) {
  const args = { output: null, title: null, toc: false, theme: "light", highlight: true };
  const positional = [];
  for (let i = 2; i < argv.length; i++) {
    switch (argv[i]) {
      case "-o":
      case "--output":
        args.output = argv[++i];
        break;
      case "-t":
      case "--title":
        args.title = argv[++i];
        break;
      case "--toc":
        args.toc = true;
        break;
      case "--theme":
        args.theme = argv[++i] || "light";
        break;
      case "--no-highlight":
        args.highlight = false;
        break;
      default:
        if (!argv[i].startsWith("-")) positional.push(argv[i]);
    }
  }
  args.input = positional[0];
  return args;
}

function generateHtml(inputPath, options) {
  if (!inputPath || !existsSync(inputPath)) {
    console.error(`Error: Input file not found: ${inputPath}`);
    process.exit(1);
  }

  const md = readFileSync(inputPath, "utf-8");
  const { body, toc } = parseMarkdown(md);
  const title = options.title || basename(inputPath, ".md");
  const theme = themes[options.theme] || themes.light;

  let tocHtml = "";
  if (options.toc && toc.length > 0) {
    tocHtml = `<nav class="toc"><h2>Table of Contents</h2><ul>`;
    let prevLevel = toc[0].level;
    toc.forEach((item) => {
      if (item.level > prevLevel) {
        tocHtml += "<ul>".repeat(item.level - prevLevel);
      } else if (item.level < prevLevel) {
        tocHtml += "</ul>".repeat(prevLevel - item.level);
      }
      tocHtml += `<li><a href="#${item.id}">${escapeHtml(item.text)}</a></li>`;
      prevLevel = item.level;
    });
    tocHtml += "</ul></nav>";
  }

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>${escapeHtml(title)}</title>
  <style>
    ${theme}
    ${baseStyle}
    ${options.highlight ? '/* Syntax highlighting */ code { background: var(--code-bg); } pre { background: var(--code-bg); }' : ''}
  </style>
</head>
<body>
${tocHtml}
<article>
${body}
</article>
</body>
</html>`;
}

// --- Main ---

const args = parseArgs(process.argv);
if (!args.input) {
  console.log("Usage: node convert.mjs <input.md> [options]");
  console.log("");
  console.log("Options:");
  console.log("  -o, --output <path>   Output HTML file path");
  console.log("  -t, --title <text>    Page title");
  console.log("  --toc                 Include table of contents");
  console.log("  --theme <name>        Theme: light, dark, classic (default: light)");
  console.log("  --no-highlight        Disable syntax highlighting");
  process.exit(0);
}

const outputPath = args.output || args.input.replace(/\.md$/, ".html");
const html = generateHtml(resolve(args.input), args);
writeFileSync(resolve(outputPath), html, "utf-8");
console.log(`✅ Converted: ${outputPath}`);
