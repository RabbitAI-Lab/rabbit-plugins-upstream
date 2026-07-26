---
name: prd-html-prototype
description: This skill should be used when the user wants to author a product requirements document (PRD) that pairs a structured written spec with an interactive single-file HTML prototype (mini-program / back-office screens, tab navigation, connector lines, rounded cards) in a clean big-tech visual style, then deploy it to GitHub Pages. Trigger phrases include "写PRD", "做带原型的PRD", "产品原型与需求说明", "把产品方案做成可交互HTML", "PRD需求文档", "PRD文档", "带原型的需求说明".
agent_created: true
---

# PRD 原型与需求说明制作

把产品需求整理成一份"文字 PRD + 可交互 HTML 原型"合一的单文件文档，视觉走大厂简约风，最终发布到 GitHub Pages 供评审/分享。

## 何时使用

- 用户要"写一份 PRD""做带原型的 PRD""产品原型与需求说明""把产品方案做成可交互 HTML"。
- 用户已有一份 PRD 草稿，要求诊断缺什么、补全章节、或加上原型。
- 用户要把 PRD 原型发布成可访问的静态站点。

## 工作流

### 1. 确定 PRD 章节结构

加载 `references/prd-structure.md`，按标准 12 章清单组织内容（概览 / 背景目标 / 范围 / KPI / NFR / 角色权限 / 流程闭环 / 接口契约 / 原型 / 上线运营 / 风险 / 术语表）。

拿到草稿时先**诊断缺失**（仅诊断、先不改）：逐项对照清单，标记缺失/薄弱项与优先级。补全时遵循文中要点——尤其 KPI 优先用**时间节点**而非"试点覆盖 X 家"这类无意义指标。

### 2. 基于模板搭建单文件 HTML

复制 `assets/prd-template.html` 作为起点（自包含、无外部依赖、图片用 base64 / 内联 SVG）。模板已内置四大核心模式，按需填充业务内容：

- **顶栏 3 tab 居中 + 滑动下划线 + 淡入切换**：`.top-bar` 用 `grid-template-columns:1fr auto 1fr` 把 tab 放中间；`switchTab(i)` 用 `cubic-bezier(.22,1,.36,1)` 移动 `.tab-indicator` 并切换 `.tab-pane`（含 `fade-in-up` 动画）。
- **PRD 概览左侧 sticky 目录 + 滚动高亮**：`scrollToPRD(id)` 用 `easeInOutCubic` 自定义缓动平滑滚动；`IntersectionObserver`（`rootMargin:-40% 0px -55% 0px`）高亮当前章节对应的目录项。
- **原型区（小程序 / 后台）**：小程序用 `.phone-frame` 手机框 + 页面 chip 切换；后台用 `.admin-layout`（侧栏 + 内容 + 中间连接线区 + 右侧功能说明面板）。
- **后台连接线 `drawLines()`**：SVG `position:fixed` 全屏，用 `getBoundingClientRect` 从左侧导航节点画曲线到右侧说明锚点。

### 3. 视觉规范（大厂简约）

- 拒绝滥用渐变；紧凑间距、自然缓动。
- 统一圆角：卡片 14px、面板 16px（CSS 变量 `--radius-card` / `--radius-panel`）。
- 作者区走简约通透风：无边框胶囊、头像细环 + 投影、发丝分隔线（见模板 `.author-chip`）。
- 内部说明卡片 `.sp-block` 默认"左紫条 + 右圆角"；若要求左右都圆角，去掉 `border-left` 并把 `border-radius` 改为 `8px`（见模板注释）。

### 4. 数据联动（演示自洽）

原型前序页面的选择要驱动后序页面：如商品选择页 → 交易完成页的金额/优惠实时计算。在对应 `switchMP` / 渲染函数里读取前序状态并 `renderPOS()` 类函数刷新，保证演示不自相矛盾。

### 5. 实机验证（发布前必做）

用 Playwright-core + 系统 Chrome（`executablePath: /Applications/Google Chrome.app/Contents/MacOS/Google Chrome`）渲染：
- 无 JS 错误（`pageerror` / `console error` 应为 0）。
- div 平衡：标准 HTML 解析器统计未闭合 / 额外闭合标签为 0。
- 逐一切换 tab / 页面，确认连接线点位、圆角、数据联动正确。

### 6. 部署到 GitHub Pages

加载 `references/deploy-github-pages.md` 执行：
- 仓库根放 `.nojekyll`（禁用 Jekyll，避免吞内容）。
- 用 `gh api` PUT 更新 `index.html`，每次注入新 `deploy-cache-bust` 时间戳（改内容 → 变 ETag → 根治"硬刷新打不开"的缓存问题）。
- 轮询 ETag / 时间戳确认线上已重建（注意 header 行尾 `\r` 干扰比较，用 `tr -d '\r'`）。
- 用户侧兜底：仍异常时清浏览器缓存（`chrome://settings/clearBrowserData`，仅清"缓存的图片和文件"）。

## 资源

- `references/prd-structure.md` — PRD 12 章清单、诊断方法、KPI 写法坑点。
- `references/deploy-github-pages.md` — `.nojekyll`、cache-bust、gh api 更新、轮询与清缓存。
- `assets/prd-template.html` — 可运行的单文件骨架（顶栏 tab、左目录、小程序/后台原型、连接线、圆角规范的完整结构与 JS）。
