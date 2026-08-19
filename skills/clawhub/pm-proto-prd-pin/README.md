# 📌 pm-proto-prd-pin: In-situ Prototype PRD Pinning & Multi-Version Spec System

> **A zero-dependency, plug-and-play interactive PRD annotation and multi-version specification framework for any HTML prototype.**
> **Supports Multi-Language Architecture: 🇺🇸 English | 🇨🇳 简体中文 | 🇯🇵 日本語 | 🇰🇷 한국어.**

---

## 🌐 Language Selector / 语言导航
- [🇺🇸 English Documentation (Default)](#-english-documentation)
- [🇨🇳 中文说明文档](#-中文说明文档)

---

# 🇺🇸 English Documentation

## 🌟 Key Features Overview

| Feature Module | Capabilities | Pain Points Solved |
|---|---|---|
| **📊 Visual Table Editor** | Direct in-cell typing, `Shift+Enter` for line breaks, `Enter/Tab` smart cell jumping & auto row creation, bidirectional Markdown serialization | Eliminates tedious `| col |` pipe syntax; works as intuitively as Excel/Notion |
| **✍️ Line-by-Line Live WYSIWYG** | Typora/Obsidian-grade inline editing: active line is raw markdown input, all other lines render instant rich text | No need to toggle between preview and edit modes; seamless document writing |
| **🏷️ Strict Version Isolation** | 100% physical version isolation (pins from different versions are strictly hidden from each other), default clean blank version creation, multi-strategy import conflict resolution | Manages multi-iteration requirements cleanly without cross-version data contamination |
| **🔄 Pure White Mermaid Engine** | Elegant pure white card container for flowcharts, dynamic `viewBox` height compensation (+28px) | Removes messy dark code blocks; complex multi-level flowcharts never cut off |
| **🔍 Fuzzy Title Search** | Case-insensitive substring, multi-keyword split, and character sequence fuzzy matching across drawer cards and screen pin badges | Instantly pinpoints target specs among dozens of pins |
| **🔒 Reorder & Safety Lock Mode** | Default browsing mode prevents accidental drags/deletions; unlock management mode to drag-to-sort, jump by index number (`🔢 Move to`), or delete | Prevents accidental modifications during standard walkthroughs |
| **🎯 Frame-Rate Tracking Locator** | `position: fixed` absolute coordinate alignment + 800ms smooth scroll continuous tracking glow box | Eliminates all vertical and horizontal scroll offset drift bugs |
| **📑 Full PRD Screen & PDF Export** | Fixed TOC outline tree, `↗️ Open in New Tab` standalone presentation, and `Ctrl+P / Cmd+P` delivery-grade PDF export | Delivers polished, ready-to-share product requirement documentation |
| **🌐 Native Multi-Language (i18n)** | Built-in 4-language support (English, 简体中文, 日本語, 한국어) with real-time UI switching and persistence | Seamless global team collaboration across diverse engineering environments |

---

## 📸 Real Usage Screenshots

### 1. 📋 Prototype Pin Markers & Right Drawer Overview
Annotate any UI component interactively. The right drawer stays readily accessible with version switching and fuzzy search.

![Right Drawer & Pin Overview](assets/images/screenshot_drawer_overview.png)

---

### 2. 📊 Visual Table Direct Editing & Borderless Canvas
Tables are rendered as clean, formatted tables. Click cells directly to type, insert/delete rows & columns, and create line breaks with `Shift+Enter`.

![Visual Table Direct Editing](assets/images/screenshot_visual_table_editor.png)

---

### 3. 🔄 Pure White Mermaid Flowcharts with Anti-Clipping Engine
Flowcharts are displayed inside clean white cards with full SVG viewBox compensation, ensuring no bottom nodes are truncated.

![Pure White Mermaid Flowcharts](assets/images/screenshot_mermaid_render.png)

---

### 4. 📑 Fullscreen PRD Document Screen with Outline TOC
Open the full PRD screen with left-side TOC navigation, standalone new-tab opening, and instant print to PDF.

![Fullscreen PRD Document View](assets/images/screenshot_full_prd_document.png)

---

## 🛠️ Project Directory Structure

```text
my-prototype-project/
├── admin.html               # Admin console prototype
├── mall.html                # Marketplace frontend prototype
├── merchant.html            # Merchant console prototype
├── h5.html                  # Buyer mobile H5 prototype
├── server.js                # Local persistence backend (Zero-dependency Node.js)
├── start.sh                 # One-click startup script
└── assets/
    └── js/
        ├── prd-pin-tool.js  # Core engine (i18n / WYSIWYG / Visual Table / Isolation)
        ├── prd-data-admin.js# Page-specific PRD data file
        ├── prd-data-mall.js # Page-specific PRD data file
        └── prd-data-merchant.js
```

---

## 🚀 Quick Start Guide

### Step 1: Include Scripts in Prototype HTML

Before the closing `</body>` tag of any HTML prototype, include the page data file and the core pinning tool:

```html
  <!-- Include page PRD data and core pinning engine -->
  <script src="assets/js/prd-data-mall.js"></script>
  <script src="assets/js/prd-pin-tool.js"></script>
</body>
</html>
```

To set the default language programmatically:
```html
<script>
  window.PRD_DEFAULT_LANG = 'en'; // 'en' | 'zh-CN' | 'ja' | 'ko'
</script>
```

---

### Step 2: Configure Lightweight Persistence Server (`server.js`)

A native Node.js HTTP server supporting disk persistence via `/api/save-prd` and static asset hosting:

```javascript
const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = process.env.PORT || 3000;
let BASE_DIR = __dirname;
if (fs.existsSync(path.join(__dirname, 'platform'))) {
  BASE_DIR = path.join(__dirname, 'platform');
}

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.svg': 'image/svg+xml'
};

const server = http.createServer((req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  const parsedUrl = new URL(req.url, `http://${req.headers.host}`);
  const pathname = decodeURIComponent(parsedUrl.pathname);

  // 1. Multi-version PRD disk persistence
  if (pathname === '/api/save-prd' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', () => {
      try {
        const payload = JSON.parse(body);
        const { page, data, versionRegistry } = payload;
        const cleanPageName = page.replace('.html', '').replace(/^prd-data-/, '');
        const jsDir = path.join(BASE_DIR, 'assets', 'js');
        const pageFilePath = path.join(jsDir, `prd-data-${cleanPageName}.js`);

        const fileContent = `/**\n * PRD Specification Data - ${cleanPageName}\n * Saved at: ${new Date().toLocaleString()}\n */\nwindow.INITIAL_PRD_DATA = ${JSON.stringify(data || [], null, 2)};\n${versionRegistry ? `window.PRD_VERSION_REGISTRY = ${JSON.stringify(versionRegistry, null, 2)};\n` : ''}`;

        fs.mkdirSync(jsDir, { recursive: true });
        fs.writeFileSync(pageFilePath, fileContent, 'utf-8');

        res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
        res.end(JSON.stringify({ success: true, message: `Written to ${pageFilePath}` }));
      } catch (err) {
        res.writeHead(500, { 'Content-Type': 'application/json; charset=utf-8' });
        res.end(JSON.stringify({ success: false, error: err.message }));
      }
    });
    return;
  }

  // 2. Static file serving
  let filePath = path.join(BASE_DIR, pathname);
  if (filePath.endsWith('/') || filePath === BASE_DIR) {
    filePath = path.join(BASE_DIR, 'mall.html');
  }

  const ext = path.extname(filePath).toLowerCase();
  const contentType = MIME_TYPES[ext] || 'application/octet-stream';

  fs.readFile(filePath, (err, content) => {
    if (err) {
      res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
      res.end('404 Not Found');
    } else {
      res.writeHead(200, { 'Content-Type': contentType });
      res.end(content);
    }
  });
});

server.listen(PORT, () => {
  console.log(`🚀 Prototype PRD Pinning Server running at: http://localhost:${PORT}`);
});
```

---

## ⌨️ Shortcuts & Interaction Tips

- **Add Pin**: Click `📍 Add Pin` at the bottom of the drawer, click any UI element on the page with the crosshair cursor to bind and open the editor;
- **Visual Table Shortcuts**:
  - `Shift + Enter`: Insert a newline inside the active cell (auto-serialized to Markdown `<br>`);
  - `Enter`: Navigate to the same column in the next row (automatically creates a new row at the bottom);
  - `Tab`: Navigate to the next cell to the right (automatically creates a new row if at the end);
  - `Shift + Tab`: Navigate back to the previous cell;
- **Minimize Draft**: Click `➖ Minimize / View Page` in the top right of the editor to dock the draft into a floating pill at the bottom-right, allowing you to freely explore the prototype UI and restore the draft losslessly at any time;
- **Export to PDF**: Click `📑 Full PRD View` → `↗️ Open in New Tab` → press `Ctrl+P / Cmd+P` in the browser to export delivery-ready PDF documents.

---
---

# 🇨🇳 中文说明文档

## 🌟 核心特性概览

| 特性模块 | 核心能力 | 解决痛点 |
|---|---|---|
| **📊 可视化表格直编** | 支持直接在单元格打字、`Shift+Enter` 内换行、`Enter/Tab` 智能跳格增行，自动双向序列化 Markdown | 告别繁琐的 `| col |` 竖线语法，像 Excel 一样自然直观 |
| **✍️ 逐行即时可视化** | Obsidian / Typora 级行内所见即所得：当前行源码输入，非编辑行全自动实时富文本渲染 | 无需来回点击切换预览，所见即所得，文档流畅手感 |
| **🏷️ 严格多版本隔离** | 物理级版本隔离（互相版本打点绝对互不可见）、新建默认为全新空白版本、多策略导入冲突处理 | 满足多迭代需求规划，避免不同版本需求混淆污染 |
| **🔄 纯白防截断图表** | Mermaid 矢量流程图纯白优雅容器，根据 SVG viewBox 动态补足 +28px 底部安全高度 | 消除暗色代码块杂乱感，复杂多层流程图永不截断 |
| **🔍 标题完全模糊搜索** | 拼音/字符流/分词模糊检索，抽屉卡片与页面大头针徽标毫秒级联动响应 | 需求过多时一秒定位目标规约 |
| **🔒 安全管理锁模式** | 默认安全浏览防误触；开启管理模式后方可拖拽排序、`🔢 移至` 输入序号或删除 | 杜绝日常查看和定位时的误触 |
| **🎯 帧率追踪精准定位** | `position: fixed` 绝对坐标系统 + 800ms 动态帧率追踪发光框 | 彻底消除页面滚动导致的位移漂移偏差 |
| **📑 全景 PRD 大屏 & PDF** | 内置固定 TOC 大纲导航，支持 `↗️ 在新网页打开` 与按 `Ctrl+P / Cmd+P` 一键导出交付级 PDF | 随时随地生成交付级专业 PRD 说明文档 |
| **🌐 原生多语言架构** | 内置中、英、日、韩四国语言，支持界面实时无缝切换与持久化存储 | 适应多语种团队与跨国产品研发协作 |

---

## ⌨️ 常用快捷键与操作指南

- **新增打点**：点击抽屉底部 `📍 新增打点`，鼠标变为十字准星，直接点击原型界面任意元素即可完成绑定并呼出编辑窗；
- **表格快捷键**：
  - `Shift + Enter`：在单元格内直接换行（自动转为 Markdown `<br>`）；
  - `Enter`：跳转至下一行同列单元格（末行自动新增一行）；
  - `Tab`：跳转至右侧下一单元格（末尾自动新增一行）；
  - `Shift + Tab`：返回上一单元格；
- **最小化草稿**：点击编辑窗右上角 `➖ 最小化/看页面`，折叠至右下角悬浮胶囊，随意查阅原型界面并一键无损还原；
- **导出 PDF**：点击 `📑 查看完整PRD` → `↗️ 在新网页打开` → 在浏览器按 `Ctrl+P / Cmd+P` 直接打印导出。
