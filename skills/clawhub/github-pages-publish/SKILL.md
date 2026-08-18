---
name: github-pages-publish
display_name: 静态网页发布器
description: 把「已有的」静态网页文件（单个 HTML 或整个网站目录）安全发布到 GitHub Pages，生成可公开访问、能分享的网址链接。当用户已有现成网页，想「发到网上」「部署上线」「发布网页」「生成分享链接」时使用；本技能只做「发布已有文件」，不负责从零生成网站。提供可执行的 deploy.py 脚本（整站增量上传 / 单文件上传 / 仅启用 Pages 三种模式），纯标准库无额外依赖，逐文件增量上传、绝不覆盖远程已有内容，并已回写真实踩坑（token 写权限、连接器只读、force 覆盖风险）。仅适用于纯静态内容；涉及后端、数据库、登录或敏感数据时不要用。
agent_created: true
---

# 静态网页发布器（GitHub Pages）

## 概述

本技能把「本地静态文件 → 公开网址」这条链路自动化：创建 GitHub 仓库、上传网页文件、启用 GitHub Pages 自动发布、验证并返回访问地址。适合个人主页、项目介绍页、文档站、汇报页等纯静态站点。

## 适用与不适用

**适用**：纯 HTML/CSS/JS 静态内容，无服务端逻辑、无数据库、无登录。

**不适用（先提醒用户）**：
- 需要后端接口、数据库、用户系统的站点 → 改用 Vercel / 云托管等
- 含敏感数据或客户信息的页面 → Pages 免费版公开可见，禁止托管

## 前置检查

1. 确认要部署的静态文件目录，必须包含 `index.html`（否则访问返回 404）。
2. 确认仓库名。规则：
   - 用户/组织主页：仓库名必须是 `<owner>.github.io`，访问地址即 `https://<owner>.github.io`，发布分支用 `main`
   - 项目页：任意仓库名 `repo`，访问地址为 `https://<owner>.github.io/<repo>`，发布分支默认 `gh-pages`
3. 确认站点是否有构建步骤（如 Hugo / Jekyll / 静态生成器）：
   - 无构建 → 直接托管静态文件
   - 有构建 → 需搭配 GitHub Actions workflow（见 `references/pages-api.md`）

## 部署流程

### 第一步：确定认证方式

按优先级探测可用能力，决定走哪条通道：

1. **GitHub MCP 已连接**（推荐）→ 用 MCP 工具完成仓库创建与文件上传，无需本地 token。注意：MCP 连接器可能是**只读**权限，创建仓库/推送一旦返回 403 `Resource not accessible by integration`，立即改走通道 B（PAT），不要反复重试。
2. **本地有 GitHub token**（环境变量 `GITHUB_TOKEN` / `GH_TOKEN`，或用户提供 PAT）→ 直接运行 `scripts/deploy.py` 或调 REST API 全自动完成。
3. 两者都没有 → 询问用户提供 PAT，或改用 MCP + 手动启用 Pages。

### 第二步：通道 A —— 通过 GitHub MCP（无需本地 token）

1. 创建仓库（如不存在）：
   - 调用 GitHub MCP `create_repository`，参数 `name`（仓库名）、`visibility` 设为 `public`（Pages 免费版要求公开）。
2. 上传静态文件：
   - 优先调用 `push_files` 批量上传目录内全部文件（保持相对路径）。
   - 文件多时可用 `create_or_update_file` 逐个创建。
3. 启用 Pages：
   - 运行 `python scripts/deploy.py --enable-only --repo <repo> [--owner <owner>] [--branch <branch>]`；脚本会探测本地 token。
   - 若无 token，脚本会输出精确的手动启用步骤（Settings → Pages → Source 选分支 → Save），引导用户完成这一下。

### 第三步：通道 B —— 本地脚本全自动（需要 token）

运行：

```bash
python scripts/deploy.py --dir <静态文件目录> --repo <仓库名> [--owner <owner>] [--branch gh-pages]
```

脚本自动完成：创建/复用仓库 → 用 contents API 增量上传文件 → 启用 Pages → 轮询部署状态 → 输出 URL。整站上传采用「逐文件增量同步」：只创建/更新本地有的文件，**绝不覆盖或删除远程已有的其他文件**，从机制上彻底规避 `git push --force` 丢数据的风险。

token 来源：`--token` 参数 > `GITHUB_TOKEN` > `GH_TOKEN`。若均缺失，脚本报错并给出获取 PAT 的指引。

PAT 权限要求（务必先向用户讲清，否则上传会被 403 拒绝）：
- **classic token**（`ghp_` 开头）：生成时勾选 `repo` 即可。
- **fine-grained token**（`github_pat_` 开头）：默认「Contents」权限为**只读**，必须把 Permissions → Contents 改为 **Read and write**，且 Repository access 覆盖目标仓库（或选 All repositories）。

### 变体：上传单个文件到现有仓库（不覆盖 index.html）

当目标仓库已存在且已启用 Pages，只需追加一个页面时，直接用 `deploy.py --file` 或 REST API 上传单个文件，不依赖 git、不会覆盖现有 `index.html`：

```
PUT /repos/{owner}/{repo}/contents/{英文文件名}.html
Body: { "message": "...", "content": "<base64 文件内容>", "branch": "main" }
```

文件名用英文（如 `jiuzhaigou-vs-leshan.html`），避免中文文件名导致 URL 被百分号编码。

### 第四步：验证与交付

1. 构造访问地址并验证（HTTP 200）：
   - 用户/组织主页：`https://<owner>.github.io`
   - 项目页：`https://<owner>.github.io/<repo>`
   - 单文件：`https://<owner>.github.io/<repo>/<remote-path>`
2. 注意：GitHub Pages 首次部署通常需要 1–3 分钟，刚启用时可能 404，稍等重试。
3. 把最终网址告知用户，或通过 `present_files` 的 URL 模式让用户直接访问。
4. **安全收尾**：部署完成后主动提醒用户，临时 PAT 已用完，可去 `https://github.com/settings/tokens` 撤销（Delete），下次再生成。

## 自动发布说明

GitHub Pages 采用「提交即自动发布」：每次向发布分支提交新内容（无论 git push 还是 contents API），GitHub 自动重新构建并部署，无需手动操作。因此「自动发布」无需额外配置即生效。若站点需要构建步骤（静态生成器），改用 GitHub Actions 实现自动构建发布，workflow 模板见 `references/pages-api.md`。

## 常见问题

- **刚部署 404**：首次部署需 1–3 分钟；用 REST API `GET /repos/{owner}/{repo}/pages` 查 `status`（building → built），轮询直到 built 再验证。确认仓库 public；确认 `index.html` 在发布分支根目录。
- **上传返回 403 `Resource not accessible by integration`**：GitHub MCP 连接器是只读权限，改用 PAT（通道 B）。
- **上传返回 403 `Resource not accessible by personal access token`**：PAT 缺写入权限——fine-grained token 需把 Contents 设为 Read and write，或改用 classic token 勾 `repo`。
- **更新不生效**：可能是浏览器/CDN 缓存，稍等或强制刷新；确认 push 到了正确的发布分支。
- **私有仓库能否用 Pages**：免费版不行，需 GitHub Pro 等付费订阅。
- **URL 路径**：项目页 URL 包含仓库名，路径区分大小写。

## 资源

- `scripts/deploy.py` —— 全自动部署脚本（token 模式）：`--dir` 整站增量上传、`--file` 单文件上传、`--enable-only` 仅启用 Pages；全部走 contents API，无 git、无 force 覆盖
- `references/pages-api.md` —— REST API 端点、GitHub Actions workflow 模板、故障排查
