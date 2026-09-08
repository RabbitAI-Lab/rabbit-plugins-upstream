---
name: lan-folder-share
description: Publish any local folder as a web link everyone on your LAN can open in one click — browse and search Markdown docs, Excel/CSV sheets, HTML reports, images and videos online. No database, no pre-configuration; file changes appear on refresh. 一键把本地文件夹/目录打包发布为局域网内人人可打开访问的网页链接，无需数据库与任何预配置，同事可在线浏览 Markdown 文档、Excel/CSV 表格、HTML 报告、图片画廊、视频并全文搜索，文件增删改动刷新页面即生效（服务端实时扫描目录，无需重启）。Use when user wants to share a local folder or files with colleagues over the LAN ("share this folder on the LAN", "give the team an online link to browse docs", "LAN knowledge base / file server", "one-click web sharing of a directory"), or 当用户想把本地目录/文档/文件分享给同事或局域网内其他人访问，如"把 XX 文件夹分享到局域网""给团队一个在线看文件的链接""局域网共享文件夹/文件""一键把目录发布成可访问网页/链接"等诉求。
slug: lan-folder-share
displayName: Lan Folder Share (共享文件)
summary: Share any local folder over LAN in one click — colleagues can open, browse and search Markdown/Excel/CSV/HTML/images/video in the browser. 一键把本地文件夹打包发布为局域网可访问的网页链接，支持在线浏览与全文搜索，无需数据库与预配置，文件改动刷新即生效。
tags: [文件共享, 局域网, 文档分享, 网页发布, Web服务, file-sharing, lan, document-server]
category: 文件共享
platforms: [codebuddy, skillhub]
version: 1.0.4
metadata:
  openclaw:
    requires:
      bins:
        - node
---

# Lan Folder Share — 局域网文件夹一键共享 (One-Click LAN Folder Sharing)

> **English summary:** Turn any local folder into a web link everyone on your LAN can open: browse Markdown docs, preview Excel/CSV sheets, view HTML reports and image galleries, search everything. No database, no config files — drop files in a folder and they are live on refresh.

把任意本地文件夹/目录变成一个**局域网内所有人都能打开访问的网页链接**：支持 Markdown 文档、Excel/CSV 表格在线预览、HTML 网页报告、图片画廊与全站搜索；不需要建数据库、不需要预生成任何配置文件，**目录里文件怎么放，网页就是什么样**。

---

## 何时使用 · When to Use

用户出现以下诉求时使用本技能 / Use this skill when the user asks for:

- "把这个文件夹/知识库分享到局域网，让同事都能看"
  ("Share this folder / knowledge base on the LAN so colleagues can view it")
- "把这些文档/表格/报告给团队在线查看"
  ("Give the team online access to these docs / sheets / reports")
- "一键在局域网起个知识库/文档站/共享浏览服务"
  ("Spin up a LAN knowledge base / document site / shared browsing service in one click")
- 目录内容以文档为主（md / 表格 / 图片 / 网页报告 / 视频音频），无需登录鉴权即可共享浏览
  (Content is mostly documents — md / spreadsheets / images / HTML reports / media — and browsing is shared without login or auth)

---

## 前置条件 · Prerequisites

1. 本机已安装 **Node.js**（12+）。执行 `node -v` 确认；缺失时先引导用户安装，不要自行跳过。
   (Node.js 12+ must be installed. Confirm with `node -v`; if missing, guide the user to install it first — do not skip this step.)
2. 页面样式与渲染库（docsify 等）从公共 CDN 加载，**服务器与局域网用户浏览器需能访问外网**；如纯内网无外网环境，须先告知用户此限制。
   (Page styles and rendering libraries are loaded from public CDNs, so the server and LAN users' browsers need internet access. If the network is fully offline, tell the user about this limitation upfront.)
3. Windows 首次启动可能触发防火墙弹窗，需放行 node.exe，否则其他机器无法访问。
   (On Windows, the first launch may trigger a firewall prompt — allow `node.exe`, otherwise other machines cannot reach the site.)

---

## 使用步骤 · Usage Steps

### 1. 明确部署参数 · Confirm Deployment Parameters

与用户确认（缺省值可直接采用，不必反复追问）/ Confirm with the user (defaults are fine to use without asking repeatedly):

| 参数 Parameter | 默认 Default | 说明 Description |
|---|---|---|
| 内容目录 Content dir | 当前目录 Current dir | 要共享的文件夹（含 md/表格/图片等）Folder to share (md / sheets / images, etc.) |
| 站名 Site name | 目录名 Dir name | 页面标题与左上角站名 Page title and top-left site name |
| 端口 Port | 8089 | 被占用时脚本自动 +1 重试 Auto-increments if occupied |

### 2. 启动服务 · Start the Server

**启动前必须向用户说明并取得确认**（不要未经确认直接启动）：该服务会把所选内容目录以网页形式暴露给**局域网内任意可达设备**（无鉴权，任何同网段设备打开链接即可浏览）。提醒用户：不要选择家目录、代码仓库、含凭证或敏感业务数据的目录，优先选择一个范围受限、只含拟共享文件的子目录；如需内容目录保持只读（不写入任何站点文件）请加 `--no-readme`。
(Before starting, you MUST explain to the user and get their confirmation — do not start without it. This server exposes the chosen folder as a website readable by any device that can reach your LAN address, with no authentication. Warn them: do not point it at home directories, repositories, credential folders or sensitive business data; prefer a tightly scoped subfolder containing only files meant for sharing. Use `--no-readme` to keep the content directory strictly read-only.)

脚本路径固定为技能内 `scripts/deploy.js`，用 `node` 直接执行（零第三方依赖，无需 `npm install`）。
(The script lives at the skill's `scripts/deploy.js` and runs directly with `node` — zero third-party dependencies, no `npm install` needed.)

```
node <skill目录/skill-dir>/scripts/deploy.js "<内容目录/content-dir>" -n "站名/site-name" -p 8089
```

常用组合 / Common combinations:

- 分享指定目录：`node deploy.js "D:\团队资料" -n "团队资料"`
  (Share a specific folder)
- 服务已建好，想同时打开浏览器：加 `--open`
  (Server started, also want to open the browser — add `--open`)
- 内容目录不应生成默认首页（保持目录只读、不落任何文件）：加 `--no-readme`；
  此时根目录若无 README，首页自动显示「目录索引页」，不会出现 404
  (Keep the content dir read-only and write nothing into it — add `--no-readme`. If the root then has no README, the home page renders a directory index instead of a 404.)
- 端口/站名自定义：`-p 9000 -n "XX知识库"`
  (Customize the port / site name)

### 3. 确认启动结果并交付地址 · Confirm Startup and Hand Over the URL

启动日志会打印 / The startup log prints:

- 本机访问地址：`http://127.0.0.1:<端口>`
  (Local access URL)
- 局域网分享地址：`http://<局域网IP/LAN-IP>:<端口>`（自动探测网卡，可能有多个）
  (LAN share URL — auto-detected NICs, there may be several)
- 站名、内容目录绝对路径、预热统计（md / 表格数量）
  (Site name, absolute content path, warm-up stats — md / sheet counts)

把**局域网分享地址**交给用户/同事即可访问。该地址仅在同一局域网内可达（离开该网段无法打开），并提醒用户不要把这个地址转发到不可信的公共网络环境。若日志提示"未检测到局域网 IPv4"，说明网卡未连局域网，提示用户确认网络状态。
(Hand the LAN share URL to the user/colleagues. If the log says "no LAN IPv4 detected", the NIC is not on a LAN — ask the user to check the network.)

### 4. 向用户说明使用方式 · Explain Usage to the User

- 目录增删文件后**刷新页面**即生效（侧边栏/目录页/搜索实时扫描文件系统），无需重启服务
  (After adding/removing files, a page refresh is enough — sidebar, index and search scan the filesystem live; no restart needed.)
- Markdown 页面内点击 `#` 链接可展开任意站内文档；表格文件点击在页面内预览/搜索；`.html` 报告点击后内容区 iframe 展示；目录内图片自动组成画廊（支持 ←/→/↑/↓ 切换）
  (Inside a Markdown page, click `#` links to expand any site doc; clicking a spreadsheet previews/searches it in-page; `.html` reports render in an iframe; images in the dir auto-form a gallery navigable with ←/→/↑/↓.)
- 停止服务：终端 `Ctrl+C`
  (Stop the server with `Ctrl+C` in the terminal)

---

## 部署形态（自动识别，无需配置）· Deployment Modes (Auto-detected, No Config)

| 形态 Mode | 判定 Detection | 行为 Behavior |
|---|---|---|
| 纯内容目录 Plain content dir | 根目录无 `index.html` No `index.html` in root | 内容目录本身**不落任何站点文件**，前端运行时来自技能包 `assets/runtime/`；根目录无 README 时会自动生成一个可编辑的默认首页（加 `--no-readme` 则不落盘，首页自动显示目录索引页）Nothing is written into the content dir; the front-end runtime ships from the skill's `assets/runtime/`. If the root has no README, an editable default home page is auto-generated (with `--no-readme`, nothing is written and the home page shows a directory index). |
| 自包含知识库 Self-contained site | 根目录已有 `index.html + assets/` Has `index.html + assets/` in root | 完全按原有站点逻辑托管（如本仓库自身），内置运行时仅作缺失资源兜底 Host the existing site as-is (like this repo itself); the built-in runtime only backfills missing assets. |

---

## 排除与保留路径 · Excluded & Reserved Paths

- 自动排除常见噪音目录（`.git`、`node_modules`、`venv` 等），自包含形态额外排除站点内部目录（`assets`、`sync` 等）；可用 `--exclude a,b` 追加
  (Common noise dirs — `.git`, `node_modules`, `venv`, etc. — are auto-excluded; the self-contained mode additionally excludes site-internal dirs like `assets`/`sync`. Append more with `--exclude a,b`.)
- `/api/` 为系统保留前缀（tree/manifest/search 数据接口），内容目录中请勿放置同名顶层目录
  (`/api/` is a reserved prefix for the tree/manifest/search endpoints — do not put a top-level folder with that name in the content dir.)
- 仅展示可浏览内容文件（md/表格/网页/PDF/Office/图片/音视频），其余文件不影响浏览
  (Only browsable files are shown — md/sheets/HTML/PDF/Office/images/audio/video; other files do not affect browsing.)

---

## 验证清单 · Verification Checklist

启动后至少验证一次 / Verify at least once after startup:

1. 浏览器/请求访问 `http://127.0.0.1:<端口>/` 返回注入站名的页面
   (Accessing `http://127.0.0.1:<port>/` returns the page with the injected site name)
2. `http://127.0.0.1:<端口>/api/tree` 返回 JSON 目录树
   (Returns the JSON directory tree)
3. `http://127.0.0.1:<端口>/api/search?q=关键词` 返回命中结果
   (Returns search hits for the keyword)
4. 局域网地址（非 127.0.0.1）可从同网段另一台设备打开
   (The LAN URL — not 127.0.0.1 — opens from another device on the same subnet)

---

## 常见问题 · FAQ

- **其他电脑打不开 / Other computers cannot open the site**：多为 Windows 防火墙未放行 node.exe（首次启动弹窗需允许"专用网络"），或两台设备不在同一网段。
  (Usually the Windows firewall blocks `node.exe` — allow "Private networks" on the first-launch prompt — or the two devices are not on the same subnet.)
- **页面样式空白 / Blank page styles**：CDN（jsdelivr）不可达，需外网；可让部署机代理外网后重试。
  (The CDN — jsdelivr — is unreachable; internet is required. Retry after the host gets internet access, e.g. via a proxy.)
- **表格无法搜索 / Spreadsheet search fails**：未找到内置 `xlsx.full.min.js` 时的降级表现，页面内预览不受影响。
  (Degraded mode when the bundled `xlsx.full.min.js` is missing; in-page preview still works.)
- **改了文件不生效 / File changes not reflected**：浏览器缓存导致，强制刷新（Ctrl+F5）；服务端每次都实时扫描，无需重启。
  (Browser cache — hard refresh with Ctrl+F5. The server rescans in real time; no restart needed.)
- **用 `--no-readme` 后首页显示什么 / What the home page shows with `--no-readme`**：内容目录保持只读、不生成默认首页；若根目录本来没有 README，首页自动渲染为「目录索引页」（根目录下的图片/视频/网页报告可直接浏览，纯文档目录则提示从左侧导航进入），不会出现英文 404。
  (The content dir stays read-only and no default home page is generated; if the root had no README, the home page renders a directory index — images/videos/HTML reports at the root are directly browsable, pure-doc dirs hint to use the left nav — never an English 404.)
- **视频打不开或无法拖动进度条 / Video won't play or seek**：服务端已支持标准 HTTP Range 分片（206），Safari/iOS 可直接播放与 seek；仍异常时请先强制刷新页面排除浏览器缓存。
  (The server supports standard HTTP Range requests — 206 — so Safari/iOS can play and seek. If it still fails, hard-refresh first to rule out browser cache.)
