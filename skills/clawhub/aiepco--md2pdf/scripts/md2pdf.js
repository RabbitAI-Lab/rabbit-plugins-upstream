#!/usr/bin/env node
/**
 * md2pdf.js — 把 Markdown 以渲染后预览样式导出为 PDF。
 *
 * 零外部依赖：marked.js 已 vendored，Chrome 本机就有。
 * 用法见 SKILL.md。
 */
"use strict";

const fs = require("fs");
const path = require("path");
const os = require("os");
const { execFileSync } = require("child_process");

// ---------- 路径解析 ----------
const SKILL_DIR = path.resolve(__dirname, "..");
const MARKED_JS = path.join(SKILL_DIR, "assets", "marked.min.js");
const STYLE_CSS = path.join(SKILL_DIR, "assets", "style.css");

const CHROME_CANDIDATES = [
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  process.env.CHROME_PATH,
].filter(Boolean);

// ---------- 参数解析 ----------
function parseArgs(argv) {
  const args = {
    input: null,
    output: null,
    css: null,
    paper: "A4",
    stdin: false,
    noHeaderFooter: false,
  };
  const pos = [];
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--stdin") args.stdin = true;
    else if (a === "-o" || a === "--output") args.output = argv[++i];
    else if (a === "--css") args.css = argv[++i];
    else if (a === "--paper") args.paper = argv[++i];
    else if (a === "--no-pdf-header-footer") args.noHeaderFooter = true;
    else if (a === "-h" || a === "--help") { printHelp(); process.exit(0); }
    else if (a.startsWith("-")) { console.error(`未知参数: ${a}`); printHelp(); process.exit(1); }
    else pos.push(a);
  }
  if (!args.stdin) args.input = pos[0] || null;
  if (!args.stdin && !args.input) { console.error("缺少输入：请提供 .md 文件路径，或用 --stdin"); printHelp(); process.exit(1); }
  if (!["A4", "Letter"].includes(args.paper)) { console.error(`--paper 只支持 A4 或 Letter，收到: ${args.paper}`); process.exit(1); }
  return args;
}

function printHelp() {
  console.log(`用法:
  node md2pdf.js <input.md> [选项]
  echo "# 标题" | node md2pdf.js --stdin -o out.pdf

选项:
  --stdin                  从标准输入读 Markdown 文本
  -o, --output <file>      输出 PDF 路径（默认与输入同名 .pdf）
  --css <file>             额外 CSS 覆盖内置样式
  --paper <A4|Letter>      纸张尺寸（默认 A4）
  --no-pdf-header-footer   关闭 Chrome 默认页眉页脚
  -h, --help               帮助`);
}

// ---------- 工具 ----------
function findChrome() {
  for (const c of CHROME_CANDIDATES) {
    if (c && fs.existsSync(c)) return c;
  }
  console.error("❌ 找不到 Google Chrome，请设置 CHROME_PATH 环境变量");
  process.exit(1);
}

// ---------- 主流程 ----------
function main() {
  const args = parseArgs(process.argv.slice(2));

  // 1. 读取 Markdown 内容
  let mdText;
  let inputName;
  if (args.stdin) {
    mdText = fs.readFileSync(0, "utf8");
    inputName = "stdin";
  } else {
    const p = path.resolve(args.input);
    if (!fs.existsSync(p)) { console.error(`❌ 文件不存在: ${args.input}`); process.exit(1); }
    mdText = fs.readFileSync(p, "utf8");
    inputName = path.basename(p, path.extname(p));
  }

  // 2. 用 marked.js 渲染 HTML
  const marked = require(MARKED_JS);
  const parse = marked.parse || (marked.marked && marked.marked.parse);
  const bodyHtml = parse(mdText);

  // 3. 组装完整 HTML（内置样式 + 可选自定义样式）
  let extraCss = "";
  if (args.css) {
    const cp = path.resolve(args.css);
    if (!fs.existsSync(cp)) { console.error(`❌ 自定义 CSS 不存在: ${args.css}`); process.exit(1); }
    extraCss = fs.readFileSync(cp, "utf8");
  }
  const baseCss = fs.readFileSync(STYLE_CSS, "utf8");
  // 纸张尺寸：注入 @page，让 --paper 真正生效
  const pageCss = `@page { size: ${args.paper}; margin: 2cm; }`;
  const html = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>${escapeHtml(inputName)}</title>
<style>
${pageCss}
${baseCss}
${extraCss}
</style>
</head>
<body>
${bodyHtml}
</body>
</html>`;

  // 4. 写临时 HTML
  const tmpHtml = path.join(os.tmpdir(), `md2pdf_${Date.now()}.html`);
  fs.writeFileSync(tmpHtml, html, "utf8");

  // 5. 确定输出路径
  let outPath;
  if (args.output) {
    outPath = path.resolve(args.output);
  } else if (args.stdin) {
    console.error("⚠️ --stdin 模式需指定 -o <output.pdf>");
    process.exit(1);
  } else {
    outPath = path.resolve(path.dirname(args.input), inputName + ".pdf");
  }

  // 6. Chrome headless 打印 PDF
  const chrome = findChrome();
  // 默认关闭页眉页脚（预览导出应干净，不带 URL/日期/页码噪音）
  const pdfArgs = [
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=2000",
    "--print-to-pdf=" + outPath,
    "--no-pdf-header-footer",
  ];
  pdfArgs.push("file://" + tmpHtml);

  try {
    // 用 execFileSync，捕获噪音 stderr 但不判失败
    execFileSync(chrome, pdfArgs, { stdio: ["ignore", "ignore", "pipe"], timeout: 60000 });
  } catch (e) {
    // Chrome 即使在成功时也可能以非零码退出（macOS 噪音），以 PDF 文件为准
    if (!fs.existsSync(outPath) || fs.statSync(outPath).size === 0) {
      console.error("❌ PDF 生成失败:", e.message);
      if (e.stderr) console.error(String(e.stderr).slice(0, 2000));
      fs.rmSync(tmpHtml, { force: true });
      process.exit(1);
    }
  }

  // 7. 清理临时 HTML，校验 PDF 非空
  fs.rmSync(tmpHtml, { force: true });
  if (!fs.existsSync(outPath) || fs.statSync(outPath).size === 0) {
    console.error("❌ 输出 PDF 为空或未生成:", outPath);
    process.exit(1);
  }
  const sizeKb = (fs.statSync(outPath).size / 1024).toFixed(1);
  console.log(`✅ 已生成: ${outPath} (${sizeKb} KB)`);
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
}

main();
