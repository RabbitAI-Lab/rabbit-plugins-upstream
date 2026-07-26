# CLI 参考

## 命令模板

```bash
cd <SKILL_DIR>/scripts
node index.js [动作] --title "<视频标题>" [选项]
```

`<SKILL_DIR>` 指 skill 根目录的绝对路径（agent 加载 SKILL.md 时能解析）。CLI 全程无 stdin 交互，自动启动持久化 Chromium profile、跳创作者中心、自动检测登录、跑动作、stdout 打一行 JSON、关浏览器。

## 动作 flag（二选一，必填）

| Flag | 作用 |
|---|---|
| `--comment-list` | 只抓 `--title` 下的评论。返回 `{ video, stats, comments }`。 |
| `--reply`        | 批量回复。必须配合下方任一种「回复列表来源」flag。 |

## 全局 flag

| Flag | 必填 | 说明 |
|---|---|---|
| `--title "<text>"` | ❌ 可选 | 按视频标题匹配（忽略大小写的子串匹配）。多条匹配时取第一条。底层：`clickWorkByName`。 |
| `--index <N>` | ❌ 可选 | 按 0-based 序号选作品。底层：`clickWorkByIndex`。N 必须是 ≥ 0 的整数。 |
| `--title` 与 `--index` | — | **互斥**，不能同时存在。两者都省略 → 选第一个作品（`index=0`）。 |

## 回复列表来源 flag（三选一，互斥）

| Flag | 形式 | 适用场景 |
|---|---|---|
| `--replies-file <path>` | JSON 数组（文件路径） | **推荐**：批量（>1 条）回复。每条：`{ author, content, text }`。 |
| `--replies '<json>'` | JSON 数组（内联字符串） | 临时一行命令。PowerShell 用**单引号**包裹 JSON 让双引号存活。 |
| `--author "<x>" --content "<y>" --text "<z>"` | 3 个标量 | 单条回复便捷写法，等价于 1 条 list。 |

JSON 条目形状（三个字段都是**字符串**）：

```json
{ "author": "亮有一计", "content": "免费", "text": "感谢推荐" }
```

- `author`：评论作者显示名的子串（同时扫顶级评论和二级回复）
- `content`：评论正文的子串
- `text`：要发送的回复文本

匹配语义详见 [matching-rules.md](matching-rules.md)。

## 回复选项

| Flag | 默认 | 作用 |
|---|---|---|
| `--delay-ms <ms>`  | 5000 | 多条回复之间的防爬间隔。首条不等待。 |

> ⚠️ **没有 `--dry-run` 选项**，**没有审批节点**。`--reply` 直接发送，agent 自己负责完整链路（判断 + 文案 + 发送）。

## 退出码

| Code | 含义 |
|---|---|
| `0` | 全部回复成功（或 `comment-list` 完成）。 |
| `1` | 有回复失败。JSON 仍会打印——看 `result.replies[i].ok`。 |
| `2` | CLI 参数错误（flag 写错、缺 `--title`、JSON 不合法等）。stderr 有原因。 |

注意：失败时设的是 `process.exitCode = 1`，脚本仍然正常退出（所以 `JSON.parse(stdout)` 一定能跑）。它**不会**抛异常或跳过 JSON 输出。

## 返回结构：`--comment-list`

Schema 与 `fetch_comments.js` 中的 `fetchComments` 一致：

```ts
{
  fetched_at: string,                    // ISO 时间戳
  video: { title: string, video_id: null },
  stats: { top_count: number, reply_count: number, total: number },
  comments: [
    {
      id: "c1",                         // 顶级 "cN"，二级 "cN-rM"
      parent_id: null,                  // 二级时为 "cN"
      level: 1,                         // 1 = 顶级，2 = 二级
      user: { name: string, avatar: string, is_author: boolean },
      content: string,                  // 可能含换行
      time: string,                     // 例 "06-17 17:06"
      like_count: number,
      replies: [                        // 仅顶级评论有
        { id: "c1-r1", parent_id: "c1", level: 2, ... 同上,
          reply_to: "用户名" /* 被回复者 */ }
      ]
    }
  ]
}
```

## 返回结构：`--reply`

```ts
{
  ok: true,
  replies: [
    // 成功：
    { ok: true, target_id: "c2-r4", reply_text: "感谢推荐" },

    // 失败 — not-found：
    { ok: false, reason: "not-found",
      detail: "作者含 \"亮有一计\" 且内容含 \"免费\" 的评论不存在",
      author: "...", content: "..." },

    // 失败 — ambiguous（多条匹配）：
    { ok: false, reason: "ambiguous",
      detail: "匹配到 3 条，加更精确的关键词或用 --id",
      author: "...", content: "...",
      candidates: [ { id, level, user, content }, ... ] },

    // 失败 — replyToComment 抛错（UI 层）：
    { ok: false, reason: "<replyToComment reason>",
      detail: "...", screenshot: "path/to/png" }
  ]
}
```

### `reason` 枚举

| Reason | 何时 | 修复 |
|---|---|---|
| `not-found` | 0 条评论匹配 `author + content` | 重跑 `--comment-list`，复制实际的作者名 + 内容片段 |
| `ambiguous` | 多条评论匹配 | 收窄 `author` / `content` 关键词，或直接按 ID 定位（见 [matching-rules.md](matching-rules.md)） |
| `not-logged-in` | 登录等待超时 | 在浏览器里手动登录，确认页面在「互动管理 > 评论管理」 |
| `toolbar-failed` / `input-failed` / `send-failed` | DOM 状态变化 / 反爬 | 看 `screenshot`，必要时重试 |
| 其它 | 罕见的 UI 竞争 | 加大 `--delay-ms` 重试 |

## 「对作品"xxx"自动回复」工作流

CLI `--comment-list` + `--reply` 是两个底层动作。**完整自动回复工作流**（agent 主导：抓评论 → 规则判断 → LLM 生成文案 → 直接发送，无审批节点）见 [auto-reply-workflow.md](auto-reply-workflow.md)。

适用场景：用户说「对作品"xxx"自动回复」「批量自动回复」时走工作流；用户自己知道 author / content / text 直接敲 `--reply` 命令行则不需要走工作流。

## 3 种调用方式

| 方式 | 适合 | 命令 |
|---|---|---|
| **A. 写文件 + subprocess**（推荐） | agent 通过 `execSync` / `child_process` 跑 | `node index.js --reply --title "x" --replies-file ./replies.json` |
| **B. 内联 JSON** | 临时一行命令 | `node index.js --reply --title "x" --replies '[{...}]'` |
| **C. 模块 require** | agent 已有 Playwright `page` 时，in-process 调用 | 见下方代码 |

### 方式 C 详解

CLI 入口文件 `index.js` 同时导出 `run` + `parseArgs`，agent 可直接 require：

```js
// agent 准备 Playwright context + page（复用已有浏览器）
const { chromium } = require('playwright');
const context = await chromium.launchPersistentContext('<user-data>', { headless: false });
const page = context.pages()[0] || await context.newPage();
await page.goto('https://creator.douyin.com/creator-micro/interactive/comment');
// 等登录...

// 然后调 run() —— 直接拿返回对象，无需解析 stdout
const { run } = require('<SKILL_DIR>/scripts/index');
const result = await run(
  {
    action: 'reply',
    title: '<作品名>',
    list: [
      { author: '<作者显示名>', content: '<内容片段>', text: '<回复文本>' },
      // ...
    ],
  },
  page
);

// result 形状与 CLI stdout 解析后一致：
// { ok: true, replies: [ { ok, target_id, reply_text, reason, detail, ... }, ... ] }
```

**适用**：
- 已有持久化 Chromium context 的 agent（避免反复启动浏览器）
- 想绕开 shell 转义（PowerShell 单引号 / bash 双引号麻烦）
- 想拿完整返回对象而不是 stdout JSON

**不适用**：
- 没有 Playwright 环境的 agent（用方式 A）
- 一次性脚本（用方式 A）

方式 C 的 `page` 必须已登录 douyin 评论管理页，否则 `waitForLogin` 会等 5 分钟超时。

## 示例

```bash
# 只看某视频下有哪些评论
cd <SKILL_DIR>/scripts
node index.js --comment-list --title "AI 靠不住啊"

# 省略 --title → 选第一个作品
node index.js --comment-list

# 用 --index 选第 N 个作品（0-based）
node index.js --comment-list --index 3

# 单条回复（直接发送，没有 dry-run）
node index.js --reply --title "AI 靠不住啊" \
  --author "亮有一计" --content "免费" --text "感谢推荐"

# 批量（文件，直接发送）
node index.js --reply --title "AI 靠不住啊" \
  --replies-file ./replies.json
```