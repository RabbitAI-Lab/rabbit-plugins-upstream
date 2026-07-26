---
name: Playwright-browser-use
description: 浏览器自动化 CLI（Playwright 版，纯 Node.js 实现）。除常规自动化（打开网页/截图/点击/填表/翻页）外，提供两项代码执行能力：`eval` 在页面上下文执行任意 JavaScript（可读 cookie/存储、发起带凭证请求），`run-code` 在守护进程上下文执行 Playwright/Node 代码（vm 沙箱隔离）；两者经持久化本地守护进程（127.0.0.1:19223，浏览器状态跨命令保持）控制浏览器，全部命令受随机 token 认证保护，并可经 PW_BROWSER_SAFE_MODE=1 彻底禁用代码执行。仅在可信、用户可见的本地环境中授权使用。
allowed-tools: Bash(node:*), Bash(pw-browser:*), Bash(curl:*)
capabilities:
  - "code-execution: page-context (eval — arbitrary JS in current page)"
  - "code-execution: daemon-vm (run-code — null-prototype VM sandbox, no host fs/process)"
  - "network: arbitrary via browser/page context (credentialed requests possible)"
  - "browser-state: persistent credentialed session across commands"
  - "file: write to local disk (run-code can trigger downloads)"
disable: false
---

# 浏览器自动化 — Playwright 版（`pw-browser`）

> `pw-browser` 是基于 Playwright 的浏览器自动化 CLI，仅依赖 Node.js 和 Playwright。
>
> ⚠️ **完整能力（含代码执行）**：本工具**不只是"点开网页"**——它包含 `eval`（页面上下文**任意 JavaScript** 执行）与 `run-code`（守护进程上下文执行 Playwright/Node 代码）两项代码执行能力，并通过**持久化本地守护进程**控制浏览器状态（状态跨命令保持）。所有代码执行均受 daemon token 认证保护，可用 `PW_BROWSER_SAFE_MODE=1` 彻底禁用。请先阅读下方「⚠️ 安全边界与使用场景」了解完整攻击面与适用边界，再决定是否授权。

## ⚠️ 安全边界与使用场景

本工具为 **本地 AI 助手对话环境**设计，运行在用户完全可视、可中断的场景中。

| 场景 | 风险 | 说明 |
|------|------|------|
| AI 助手对话交互（推荐） | 🟡 低 | 用户全程可见浏览器操作，可随时中断 |
| 本地开发/测试 | 🟡 低 | 在受控环境中操作测试页面 |
| 手动触发的数据采集 | 🟡 低 | 用户明确指定的页面和操作 |

以下场景 **不推荐**直接使用，需要额外安全措施：

| 场景 | 风险 | 需要的额外措施 |
|------|------|-------------|
| 被不可信 agent 调用 | 🔴 高 | 已内置 daemon token 认证 + 可选 `PW_BROWSER_SAFE_MODE` 禁用代码执行；若来源仍不可信，应进一步沙箱隔离 |
| 作为公开 API 服务 | 🔴 极高 | 必须加认证 + 操作白名单 |
| CI/CD 自动化流水线 | 🟡 中 | 需限定操作范围，禁止生产环境 |

**核心能力声明：**
- `eval`：在**浏览器上下文**（`page.evaluate`）执行**任意 JavaScript**——即完整的页面级代码执行能力。它无法访问 Node.js API（`require`/`fs`/`process`），作用域仅限于当前页面；但正因如此，它能读取 `document.cookie`/`localStorage`/`sessionStorage`、发起**带页面凭证的 `fetch` 请求**、操控 DOM 并触发页面内动作（点击、提交等）。**这是与 `run-code` 同级的"代码执行"能力，仅场景不同（页面 vs Node）**：同样受 daemon token 认证保护，同样在 `PW_BROWSER_SAFE_MODE=1` 下被禁用；只在用户明确指定、且页面可信时使用，不对高权限/来源不明页面执行
- `run-code`：在 daemon 进程的**受限沙箱**（`vm` 模块）中执行 Playwright 代码，仅暴露 `page` 和安全 JS 全局；**无法直接调用** `fs`/`child_process`/`process`/`require`。但浏览器上下文可经 `download.saveAs`/`setInputFiles` 在本地磁盘读写文件、能发起任意网络请求（沙箱不阻止）。它仍拥有完整浏览器控制权（导航、读写存储、下载、提交表单、改页面内容），**仅限本地信任环境使用**
- daemon：监听 `127.0.0.1:19223`，仅本机可访问，不暴露到公网；**所有命令（除 `/health` 存活探针）均要求随机 `token` 认证**，token 在 daemon 启动时生成并写入 `~/.pw-browser/daemon.json`（默认仅当前用户可读），CLI 自动携带，外部进程无法在未读取该文件的情况下调用
- 安全模式：设置环境变量 `PW_BROWSER_SAFE_MODE=1` 启动 daemon 可**彻底禁用** `run-code` / `eval`，仅保留受限的 snap/click/fill 等白名单命令，适合不需要自定义代码的场景
- 非 headless 模式：浏览器窗口始终可见，用户可直接监控所有操作
- 文件下载：通过 `run-code` 触发页面下载（`download.saveAs`）会写入本地磁盘，注意目标路径

## 📝 文档语言与本地化说明

- **文档语言**：本技能文档为**简体中文**。若你或下游 agent 的默认语言非中文，请以代码块中的命令、URL、CSS 选择器与 `snap` 返回的 `ref` 为准——这些是**与语言无关**的自动化锚点。
- **界面文本匹配是启发式的**：识别分页 / 按钮类型时，文档列出的中文、英文关键词（如"下一页"/"Next"、"更新"/"保存"/"发布"）只是**识别信号示例，并非穷举**；非中文页面的实际文案会不同。
- **优先用 DOM 锚点，而非可见文字**：跨语言页面请尽量用 `snap` 得到的 `ref` 或 CSS 选择器（`page.locator('.xxx')`）定位元素，避免依赖本地化后的可见文本，以防因文案不同导致误点 / 误操作。
- **适用区域**：技能本身不限定网站区域；文档示例与中文 UI 关键词面向中文环境，各"识别信号"表已并列给出英文界面关键词。

## 前置条件（首次使用）

本 Skill 所在目录需已执行 `npm install` 安装 playwright。**无需单独下载浏览器** — daemon 启动时自动检测并使用系统的 Chrome 或 Edge。

> 下文所有命令中的 `{SKILL_DIR}` 请替换为实际的 skill 安装目录路径。

## 架构

`pw-browser` 采用 daemon + client 架构：

```
┌──────────────┐     HTTP (localhost:19223)     ┌──────────────┐
│  pw-browser  │ ──────────────────────────────→│   Daemon     │
│  (CLI 客户端) │                                │  (浏览器进程)  │
└──────────────┘                                └──────┬───────┘
                                                       │
                                                       ├─ Playwright
                                                       ├─ Chromium 浏览器
                                                       └─ 页面状态持久化
```

**daemon 启动后持续运行**，浏览器和页面状态跨命令保持。CLI 每次通过 HTTP 调用 daemon。

## 启动 Daemon

**每次会话开始前**，在后台启动 daemon。以下命令使用 Skill 所在目录的绝对路径和 shim 脚本：

```bash
SKILL_DIR="{SKILL_DIR}"
NODE_PATH="${SKILL_DIR}/node_modules" node "${SKILL_DIR}/pw-browser.js" daemon &
sleep 4
```

> daemon 会在 `127.0.0.1:19223` 监听，首次启动会用 Playwright 的 `channel: 'chrome'` 自动连接系统 Chrome 浏览器（如已安装了 Edge 也会尝试）。无需下载额外的 Chromium。

验证 daemon 可用：

```bash
SKILL_DIR="{SKILL_DIR}"
NODE_PATH="${SKILL_DIR}/node_modules" node "${SKILL_DIR}/pw-browser.js" init
```

**关闭 daemon：**

```bash
pw-browser close --all
```

## 核心工作流

> **注意**：下面所有 `pw-browser` 命令都需要设置 `NODE_PATH`。Agent 执行时应使用完整形式：
> ```bash
> SKILL_DIR="{SKILL_DIR}"
> NODE_PATH="${SKILL_DIR}/node_modules" node "${SKILL_DIR}/pw-browser.js" <cmd> [args] [--json]
> ```
> 为简洁起见，下文示例省略前缀，用 `pw-browser` 表示。

```bash
# 1. 启动 daemon（会话开始一次）
pw-browser daemon &

# 2. 打开页面
pw-browser open https://www.baidu.com

# 3. 获取页面快照（必须！每次交互前都要 snap）
pw-browser snap

# 4. 交互 — 基于快照中的 e0, e1, e2... ref 引用
pw-browser click e8          # 点击 ref=e8 的元素
pw-browser fill e5 "hello"   # 在 ref=e5 的输入框填入文本
pw-browser press Enter       # 键盘按键

# 5. 等待
pw-browser wait-for "text=加载完成" --timeout 8000
pw-browser wait-for "url:https://example.com/*"
pw-browser wait-for "state:networkidle"

# 6. Tab 管理
pw-browser tab list
pw-browser tab select 1
pw-browser tab close 0

# 7. 关闭
pw-browser close             # 关闭当前页面
pw-browser close --all       # 关闭浏览器 + daemon
```

## 语义规则（必须遵守）

### 规则 1：先观察再操作

CLI **不会**在 open/click 后自动获取快照。**每次交互前，Agent 必须主动执行 `pw-browser snap`**，基于最新快照选择 ref。

```
正确: pw-browser open URL → pw-browser snap → pw-browser click e5
错误: pw-browser open URL → pw-browser click e5（缺少 snap）
```

### 规则 2：点击链接后处理导航

点击可能触发导航的链接（`<a>` 标签、按钮等）后：
1. `pw-browser snap` — 检查页面是否已变化
2. 如有新 tab → `pw-browser tab list` → `pw-browser tab select <idx>`
3. `pw-browser snap` — 获取新页面内容

### 规则 3：页面内容不全

如果快照中元素不全（列表不完整等）：
- `pw-browser mousewheel 0 500` 滚动
- 或点击"加载更多"/"下一页"
- 重新 `pw-browser snap`

### 规则 4：登录与验证码（人机协作）

pw-browser 使用非 headless 模式打开实体 Chrome 窗口，用户可直接看到并操作浏览器。遇到需要人工介入的认证场景时，**不要用 `fill`/`click` 盲目尝试**，应按以下流程交接：

#### 触发条件

从 `snap` 中发现以下任一信号时，启动人工协作流程：

- 页面 title 为「登录」/「Login」/「Sign In」
- 页面 `url` 包含 `/login`、`/auth`、`/signin`
- 快照中出现「登录」按钮 + 用户名/密码输入框
- 快照中出现「验证码」「短信验证」「扫码登录」「滑块验证」等关键字
- `open` 后自动跳转到登录页（URL 变化）

#### 协作流程

```
第1步：通报用户
  告知当前页面需要登录/验证，简明描述页面内容（输入框、验证码类型等）

第2步：询问凭据（可选）
  如果用户无凭据 → 跳过，直接等用户操作
  如果用户提供凭据 → 用 fill/click 填入账号密码，点击登录按钮

第3步：等待用户完成验证
  明确告诉用户"请在浏览器中完成验证码/二次验证"
  用户说"好了""完成了""继续"之后才继续

第4步：验证登录状态
  执行 pw-browser snap
  检查是否进入目标页面 → 如果还是登录页，询问用户是否还需要操作
  如果已进入 → 继续自动化流程
```

#### 示例对话

```
Agent: 页面跳转到了登录页 (https://xxx.com/login)，页面上有：
       用户名输入框、密码输入框、登录按钮、滑块验证码。
       需要我帮你填入账号密码吗？还是你在浏览器里自己操作？

User:  我来操作

Agent: 好的，Chrome 窗口已打开 — 请完成登录后告诉我。

User:  好了

Agent: [执行 snap]
       登录成功！当前是「工作台」页面，左侧菜单有...
```

#### 重要约束

- **不猜测凭据**：永远不要尝试默认密码或遍历登录
- **不绕过验证码**：遇到验证码/滑块/短信验证时，立即交给用户
- **不过度等待**：用户说继续后立即 snap，不额外 sleep
- **登录失败回环**：snap 后发现仍在登录页 → 告知用户"看起来还没登录成功，密码错误或验证未通过，请再试试"

### 规则 5：不要主动新建 tab

点击导致新 tab 时用 `tab list/select/close` 处理。没有 `tab new` 命令。

### 规则 6：翻页前读取策略

涉及翻页、统计、收集、遍历时，参考下面的"分页策略"章节。

### 规则 7：不手动读取快照文件

快照通过 `pw-browser snap` 命令获取，不要直接读 `~/.pw-browser/snap.yml`。

### 规则 8：SPA / 富文本编辑器

遇到知识库、文档系统、CMS 等 SPA 页面，参考下面的"SPA 与富文本编辑器"章节。

### 规则 9：daemon 故障恢复

如果 CLI 返回连接错误：

```bash
# 删除旧的 daemon 状态文件
rm -rf ~/.pw-browser/daemon.json
```

**杀掉占用端口 19223 的旧进程：**

```bash
# Windows (PowerShell)
powershell -Command "Get-NetTCPConnection -LocalPort 19223 -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id \$_.OwningProcess -Force }"

# macOS / Linux
lsof -ti:19223 | xargs kill -9 2>/dev/null
# 或: fuser -k 19223/tcp 2>/dev/null
```

**重新启动：**

```bash
SKILL_DIR="{SKILL_DIR}"
NODE_PATH="${SKILL_DIR}/node_modules" node "${SKILL_DIR}/pw-browser.js" daemon &
sleep 4
```

---

## 命令速查

### 生命周期
| 命令 | 说明 |
|------|------|
| `pw-browser init` | 连接 daemon，确认浏览器可用 |
| `pw-browser open <url>` | 导航到 URL |
| `pw-browser close` | 关闭当前页面 |
| `pw-browser close --all` | 关闭浏览器 + daemon |
| `pw-browser recover` | 重启浏览器连接 |

### 状态感知
| 命令 | 说明 |
|------|------|
| `pw-browser snap` | 获取页面可访问性快照（YAML 格式，含 ref 引用） |
| `pw-browser wait-for <target> [--timeout ms]` | 等待条件满足 |

### 交互
| 命令 | 说明 |
|------|------|
| `pw-browser click <ref>` | 点击元素 |
| `pw-browser fill <ref> "text"` | 填入文本 |
| `pw-browser type "text"` | 键盘输入 |
| `pw-browser press <key>` | 按下按键（Enter, Escape, Tab 等） |
| `pw-browser hover <ref>` | 悬停 |
| `pw-browser select <ref> <option>` | 选择下拉选项 |
| `pw-browser check <ref>` | 勾选复选框 |
| `pw-browser uncheck <ref>` | 取消勾选 |

### 页面导航
| 命令 | 说明 |
|------|------|
| `pw-browser goto <url>` | 同 open |
| `pw-browser go-back` | 后退 |
| `pw-browser go-forward` | 前进 |
| `pw-browser reload` | 刷新 |

### 高级
| 命令 | 说明 |
|------|------|
| `pw-browser screenshot [ref] [--path file]` | 截图 |
| `pw-browser mousewheel <dx> <dy>` | 滚动 |
| `pw-browser eval "<expr>" [ref]` | ⚠️ 执行**任意 JavaScript**（页面上下文，完整页面级代码执行：可读 cookie/存储、发起带凭证请求；受 token 认证保护，safe-mode 下禁用） |
| `pw-browser run-code "<code>"` | ⚠️ 执行 Playwright 代码（受限沙箱：无直接 Node fs/process 权限，但可经浏览器下载/上传读写本地文件） |
| `pw-browser dialog-accept [text]` | 确认对话框 |
| `pw-browser dialog-dismiss` | 取消对话框 |

### Tab
| 命令 | 说明 |
|------|------|
| `pw-browser tab list` | 列出所有 tab |
| `pw-browser tab select <idx>` | 切换到指定 tab (0-based) |
| `pw-browser tab close <idx>` | 关闭指定 tab |

### 延时
| 命令 | 说明 |
|------|------|
| `pw-browser sleep <seconds>` | 等待 N 秒 |

---

## 等待策略

`wait-for` 支持多种目标格式：

```bash
# 等待 URL 匹配
pw-browser wait-for "url:**/dashboard"

# 等待文本出现
pw-browser wait-for "text=加载完成"

# 等待页面加载状态（load / domcontentloaded / networkidle）
pw-browser wait-for "state:networkidle"

# 等待 CSS 选择器
pw-browser wait-for ".result-list" --timeout 15000
```

---

## 运行自定义代码（`run-code`）⚠️ 高级功能

> ⚠️ **安全警告：** `run-code` 在 daemon 进程的 **受限沙箱（`vm` 模块）** 中执行 Playwright 代码。它**无法直接调用** Node.js 系统 API（`fs` / `child_process` / `process` / `require`）；但浏览器上下文本身可经下载（`download.saveAs`）或文件上传（`setInputFiles`）在本地磁盘读写文件、并能发起任意网络请求（沙箱不阻止），因此**仍能持久化数据到本地磁盘**。仅在用户明确指定的任务中使用，不要执行来源不明的代码片段。

当内置命令不够用时，用 `run-code` 执行自定义 Playwright 代码：

```bash
# 获取页面标题
pw-browser run-code "return await page.title();"

# 获取页面 HTML
pw-browser run-code "return await page.content();"

# 在页面中执行 JS
pw-browser run-code "return await page.evaluate(() => document.title);"

# 等待网络空闲
pw-browser run-code "await page.waitForLoadState('networkidle');"

# 复杂场景：提取列表数据
pw-browser run-code "
  const items = await page.locator('.product-item').all();
  const results = [];
  for (const item of items) {
    results.push({
      title: await item.locator('.title').textContent(),
      price: await item.locator('.price').textContent()
    });
  }
  return JSON.stringify(results);
"
```

**注意：**
- `run-code` 中直接使用 Playwright Page API
- 代码在 async 函数中执行，`page` 对象已注入
- 返回值自动序列化为字符串
- ⚠️ 此命令可以触发实际的业务操作（提交订单、发送消息、删除数据等），执行前确认用户意图

---

## 分页策略

### 步骤 1：识别分页类型

> ⚠️ 下表关键词为**识别启发式**：中文 / 英文示例（"下一页"/"Next"、"加载更多"/"Load more"）并不穷举，非中文页面的文案会不同。实际定位请优先用 `snap` 的 `ref` 或 CSS 选择器，勿仅依赖可见文本。

从 snap 判断：

| 类型 | 识别信号 | 翻页方式 |
|------|---------|---------|
| **页码分页** | 底部有 1/2/3...页码、"下一页"/"Next"/">" | 点击页码或"下一页" |
| **无限滚动** | 底部无分页控件，内容随滚动增加 | `mousewheel` 滚动 |
| **加载更多** | 底部有"加载更多"/"Load more"/"查看更多" | 点击该按钮 |

### 步骤 2：执行翻页

**页码分页：**
```bash
pw-browser snap                          # 找到"下一页"按钮的 ref
pw-browser click e42                     # 点击
pw-browser sleep 2 && pw-browser snap    # 验证
```

**无限滚动：**
```bash
pw-browser mousewheel 0 800
pw-browser sleep 2 && pw-browser snap
```

**加载更多按钮：**
```bash
pw-browser click <ref>
pw-browser sleep 2 && pw-browser snap
```

### 步骤 3：判断翻页成功

| 方式 | 成功信号 | 失败/结束信号 |
|------|---------|-------------|
| 页码 | 内容更新，URL 变化 | "下一页"按钮 disabled 或消失 |
| 滚动 | 内容增加，新元素出现 | 内容不变，"没有更多了" |
| 按钮 | 新内容加载，按钮仍可点击 | "已加载全部"，按钮消失 |

---

## SPA 与富文本编辑器 ⚠️ 破坏性操作

> ⚠️ **警告：** 以下操作会**真实修改**网页内容（知识库文档、CMS 页面等）。执行前确认当前处于编辑/草稿状态、修改内容已经用户确认。保存/发布操作不可逆。

处理知识库、文档系统、CMS 等 SPA 页面的编辑操作：

### 识别信号

- 点击"编辑"后 URL 不变但按钮变化
- snap 中出现 `contenteditable`、编辑器 toolbar
- 不是普通 `input/textarea`，而是复杂编辑器

### 编辑流程

1. **进入编辑态：** `pw-browser click <编辑按钮的ref>`
2. **验证进入：** `pw-browser snap` — 检查是否出现"更新"/"保存"按钮
3. **写入内容（RTE）：**
```bash
pw-browser run-code "
  const editor = page.locator('[contenteditable=\"true\"]').first();
  await editor.click();
  await page.keyboard.press('Control+A');
  await page.keyboard.type('要写入的内容');
  await page.waitForTimeout(500);
"
```
4. **保存：**
```bash
pw-browser run-code "
  await page.evaluate(() => {
    const btn = Array.from(document.querySelectorAll('button'))
      .find(b => ['更新','保存','发布'].includes(b.textContent.trim()));
    btn?.click();
  });
  await page.waitForTimeout(3000);
"
```
5. **验证：** `pw-browser snap` — 确认保存成功、内容正确

> **不要**直接用 `innerText`/`textContent` 修改 RTE 内容。Playwright 的 `keyboard.type` 和 `fill` 是正确方式。

---

## 结构化输出

所有命令在 daemon 端返回 JSON：

```json
{"ok": true, "data": {...}, "elapsedMs": 123}
{"ok": false, "error": {"kind": "ElementNotFound", "message": "..."}, "elapsedMs": 50}
```

CLI 客户端默认以人类可读格式输出；加 `--json` 标志输出原始 JSON。

## 错误处理

| 错误类型 | 原因 | 处理 |
|---------|------|------|
| `ElementNotFound` | snap 后 ref 已失效 | 重新 snap 获取新 ref |
| `NavigationTimeout` | 页面加载超时 | 先 snap 检查实际状态 |
| 连接拒绝 | daemon 未运行 | 重新启动 daemon |
| 空快照 | 页面未加载完成 | wait-for state:load 后重新 snap |

---

## 完整示例：百度搜索

```bash
SKILL_DIR="{SKILL_DIR}"
PW="NODE_PATH=${SKILL_DIR}/node_modules node ${SKILL_DIR}/pw-browser.js"

# 启动 daemon（首次）
$PW daemon &
sleep 4

# 打开百度
$PW open https://www.baidu.com

# 快照 → 找到搜索框和按钮的 ref
$PW snap
# 例如：e12 = textarea（搜索框），e13 = button（百度一下）

# 填搜索关键词
$PW fill e12 "天气预报"

# 点击搜索
$PW click e13
sleep 2

# 检查搜索结果
$PW snap | head -30

# 清理
$PW close --all
```

---

## 深入参考

| 场景 | 文件 |
|------|------|
| 翻页策略详解 | `references/pagination.md` |
| 富文本编辑器策略 | `references/rich-text-editor.md` |
| 运行自定义代码 | `references/running-code.md` |
