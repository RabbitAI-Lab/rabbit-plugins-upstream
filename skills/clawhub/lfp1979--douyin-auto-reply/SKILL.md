---
name: douyin-auto-reply
description: "通过 CLI 抓取抖音创作者中心评论并批量回复。触发词：'抖音评论'、'douyin 评论'、'抓抖音评论'、'回复抖音评论'、'douyin 自动回复'、'douyin auto reply'、'批量回复评论'、'douyin creator center comment'、'douyin comment manager'、'对作品自动回复'、'批量自动回复'、'按序号回复作品'、'按作品编号回复'。两个动作：--comment-list（只抓评论）、--reply（按作者+内容批量回复）。选作品：--title 按标题（可省略，省略则选第一个），或 --index 按序号（0-based）。工作流：抓评论 → 规则判断 → LLM 生成文案 → 直接发送（无审批节点、无 dry-run 中间步）。"
---

# 抖音自动回复

通过 CLI 抓取抖音创作者中心评论并批量回复。

## 何时使用

- 抓 / 列出 / 导出某条抖音视频下的评论。
- 回复某条抖音视频下的一条或多条评论。
- 用户说「对作品"xxx"进行自动回复」「批量自动回复」→ 触发完整工作流。

**不适用**：B 站 / 小红书 / 知乎（用 opencli skill）；下载视频；编辑资料 / 上传视频。

## 首次使用 — 环境检查与安装

⚠️ **agent 跑 `--comment-list` / `--reply` 之前，先检查环境**，缺失就装：

```bash
cd <SKILL_DIR>/scripts

# 1. 检查 playwright npm 包（缺失则装，约 30 秒）
node -e "require('playwright')" 2>/dev/null || npm install

# 2. 检查 chromium 浏览器（缺失则装，约 1-2 分钟）
npx playwright install chromium --dry-run 2>&1 | grep -q "is already installed" || npx playwright install chromium

# 3. 检查登录态（缺失 → 让用户在浏览器里手动登录抖音创作者中心）
test -d ./user-data && echo "已登录：cookie 复用" || echo "首次使用：CLI 启动后会弹出 Chromium 让用户手动登录"
```

检查通过后再跑工作流命令。如果第 1/2 步执行安装，告诉用户「正在装 playwright / chromium，约 X 秒」。

## 两个动作

### 1) 抓评论

```bash
cd <SKILL_DIR>/scripts
node index.js --comment-list [--title "xxx" | --index N]
```

stdout 一行 JSON：`{ video, stats, comments }`，评论 id 形如 `c1`、`c2-r1`（详见 [matching-rules.md](references/matching-rules.md)）。

### 2) 批量回复

```bash
cd <SKILL_DIR>/scripts
node index.js --reply [--title "xxx" | --index N] --replies-file ./replies.json
# 或：--replies '<json>' 内联 / --author --content --text 单条便捷写法
```

⚠️ **`--reply` 直接发送**，无审批节点、无 dry-run 中间步。文案一旦调 `--reply` 就发出去了。

返回 JSON 的 `result.replies[]`，每条：

| 状态 | 含义 |
|---|---|
| `ok: true` | 匹配 + 发送成功 |
| `reason: "not-found"` | 0 条匹配，没发出去 |
| `reason: "ambiguous"` | 多条匹配，没发出去 |
| `reason: "toolbar-failed"` / `"send-failed"` | 发到一半出错，需人工核对 |

## 选作品

| flag | 说明 |
|---|---|
| `--title "<视频名>"` | 按标题子串匹配（忽略大小写） |
| `--index <N>` | 按 0-based 序号 |
| 都省略 | 选第一个作品 |
| ⚠️ | `--title` 与 `--index` 互斥 |

## 回复条目形状

```json
{ "author": "亮有一计", "content": "免费", "text": "感谢推荐" }
```

| 字段 | 说明 |
|---|---|
| `author` | 评论抓取的实际作者显示名（子串匹配） |
| `content` | 评论抓取的实际内容片段（子串匹配） |
| `text` | 要发送的回复文本 |

⚠️ `author` / `content` 必须是抓评论时拿到的**实际值**（agent 改写会导致 not-found）。

> LLM 生成的文案字段叫 `reply_text`，写到 `replies.json` 时**改名为 `text`**。

## 工作流（3 步）

⚠️ 用户说「对作品"xxx"自动回复」「批量自动回复」时走这个流程。

1. **抓评论** —— `--comment-list`
2. **判断 + 生成文案** —— 按规则筛 target，LLM 看上下文生成 `reply_text`
3. **直接发送** —— 转 `replies.json` → 调 `--reply`

### 规则（精简版）

| # | 规则 |
|---|---|
| 1 | 跳过作者本人评论（`is_author: true`） |
| 2 顶级 | 作者是否**直接回过**（`reply_to: null` 且挂在本顶级下、时间 >= 评论时间） |
| 2 二级 | 作者是否**回过这个人**（`reply_to === 该二级 user.name` 且时间 >= 该二级时间） |

⚠️ **不能**用 `top.replies[]` 是否非空判断——`replies[]` 是该顶级下**所有**二级对话（包括二级之间互回），不等于"作者是否回过这条顶级"。**必须用 `reply_to` + 时间对比**。

完整规则、判断算法伪代码见 [auto-reply-workflow.md](references/auto-reply-workflow.md)。

## agent 调 `--reply` 的 3 种方式

### 方式 A（推荐）：subprocess + 文件

```bash
cd <SKILL_DIR>/scripts
node index.js --reply [--title "x" | --index N] --replies-file ./replies.json
```

### 方式 B：内联 JSON 一行命令

```bash
node index.js --reply --replies '[{"author":"x","content":"y","text":"z"}]'
```

⚠️ PowerShell 务必用单引号包裹双引号 JSON。

### 方式 C：in-process require（已有 Playwright page 时）

```js
const { run } = require('<SKILL_DIR>/scripts/index');
const result = await run(
  { action: 'reply', title: 'x', list: [{ author: 'x', content: 'y', text: 'z' }] },
  page  // 已登录的 douyin 评论管理页
);
```

`page` 必须是同一 douyin 评论管理页且已登录。

完整 CLI 参数 + 返回结构见 [cli.md](references/cli.md)。

## 故障排查速查

| 现象 | 处理 |
|---|---|
| `Error: exit(2)` | CLI 参数错，检查 `--title` / `--index` 和回复来源 flag（见 [cli.md](references/cli.md)） |
| 卡在登录 5 分钟 | 浏览器手动登录 + 确认 URL 是 `creator.douyin.com/creator-micro/interactive/comment` |
| `Cannot find module 'playwright'` | `cd <SKILL_DIR>/scripts && npm install` |
| `reason: not-found` | 重跑 `--comment-list`，复制实际的作者名 / 内容片段 |
| `reason: ambiguous` | 加更精确的关键词 |

完整排查见 [troubleshooting.md](references/troubleshooting.md)。

## 参考文档

- [cli.md](references/cli.md) — 完整 CLI 参数表 + JSON 返回结构
- [matching-rules.md](references/matching-rules.md) — 评论 ID 命名 + 作者/内容匹配规则
- [auto-reply-workflow.md](references/auto-reply-workflow.md) — 「对作品自动回复」完整工作流（规则 / 判断 / 文案 / 发送，无审批节点）
- [troubleshooting.md](references/troubleshooting.md) — 错误码 + 常见坑