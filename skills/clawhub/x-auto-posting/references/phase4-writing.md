# Phase 4 Reference — 内容撰写

## TOC

- §1 Pre-Write Gate（撰写前强制确认）
- §2 X 字符数与格式约束
- §3 写作框架
- §4 质量检查清单
- §5 HTML 预览生成
- §6 预览展示与审批

---

## §1 Pre-Write Gate

撰写每一篇推文之前，必须先确认以下来源数据齐全。任何一项缺失 → 告知用户缺什么 + 中止本话题的写作，不要凭空编造。

| 项目 | 来源 | 用途 |
|------|------|------|
| `key_quote` | `selected_topics.json` | 作为推文中的引用或对比锚点 |
| `pain_description` | `selected_topics.json` | 作为推文的痛点陈述 |
| `source_tweet_url` | `selected_topics.json` | 避免内容雷同，写之前对比原推文确保差异化 |
| 产品/项目信息 | `session_state.json.product` | 末尾 CTA 指向该产品的 URL 或 value prop |
| `fingerprint` | `style_fingerprint.json` | 控制开篇、节奏、emoji、hashtag 风格 |

---

## §2 X 字符数与格式约束

### 2.1 字符计数规则（免费账号）

- **硬限制**：280 字符
- URL：任何 URL 被 X 计为 **23 字符**（包括已经短化的 `t.co/xxx` 和原始 URL）
- 英文字母/数字/常用标点：每字符 **1 计数**
- 中文 / 日文 / 韩文 / Emoji：每字符 **2 计数**

写作时用以下 Python 片段估算：

```python
def x_char_count(text: str) -> int:
    import re, unicodedata
    # 先提取所有 URL，每个按 23 计数
    urls = re.findall(r'https?://\S+', text)
    text_no_url = re.sub(r'https?://\S+', '', text)
    count = len(urls) * 23
    for ch in text_no_url:
        if ord(ch) > 0x7f or unicodedata.east_asian_width(ch) in ('W', 'F'):
            count += 2
        else:
            count += 1
    return count
```

必须 `x_char_count(text) <= 280`，否则不通过 Gate。

### 2.2 格式硬性要求

- 禁止 `http://`（必须 HTTPS）
- 禁止在正文中出现联系方式：`@` + 邮箱域名、手机号正则 `[+]?\d{8,}`、微信号 / WeChat ID 字样、QQ 号、Telegram @ handle
- Hashtag 数量：0-2 个，且必须出现在正文末尾（不打断阅读节奏）
- Mention 数量：0-1 个。除非是回复 / 回应场景，否则不主动 @ 其他账号

---

## §3 写作框架

套用 **钩子 → 洞察 → 佐证 → CTA** 的四段式（全部压缩进 280 字符），每段 1-2 句：

```
[HOOK]        反直觉断言 / 具体数字 / 问题 / 故事起点 — 抓住读者第一眼
[INSIGHT]     围绕话题的核心观察 / 原因 / 反常识机制
[PROOF]       具体佐证：数字、对比、引用 key_quote、截图提示（若有图）
[CTA]         行动邀请：评论讨论 / 访问产品链接 / 关注获取更多
```

### 3.1 三种典型结构模板

**模板 A：教学型**
```
{数字开头}: {反直觉现象}.

{一句话解释 WHY}.

{对比/证据}.

{行动邀请}
```

**模板 B：引用转述型**
```
"{key_quote}" — @{source_author}

{自己的视角 / 补充 / 反驳}.

{产品链接或 CTA}
```

**模板 C：故事型**
```
{一个场景 / 瞬间}.

{发生了什么（1-2 行）}.

{得到什么启示 / 行动建议}.

{hashtag 或链接}
```

选哪个模板由 `style_fingerprint.hook_style` 决定：
- `反直觉断言` → 模板 A
- `引用` → 模板 B
- `故事开头` → 模板 C

### 3.2 必须有"可验证细节"

X 用户对空泛口号极度免疫。推文正文必须出现**至少一个具体细节**：
- 数字（时间、比例、金额、条数）
- 专有名词（工具名、公司名、协议名）
- 场景描述（"beta 昨晚发布" / "M4 Max 24GB 实测"）

如果找不到具体细节 → 回到 Phase 1 的 `key_quote` 和 `pain_description` 里挖，或放弃该话题。

---

## §4 质量检查清单

写完 draft 之后，运行以下自检（Agent 自己 walk through）：

| # | 检查项 | 通过条件 |
|---|--------|----------|
| 1 | 字符数 | `x_char_count(text) <= 280` |
| 2 | 开篇是否抓人 | 第一行能独立成为吸引点击的理由 |
| 3 | 是否有可验证细节 | 至少一个数字 / 专有名词 / 具体场景 |
| 4 | 与原推文差异化 | 非改写，提供新视角 / 反驳 / 补充 |
| 5 | CTA 是否明确 | 读者知道下一步做什么（看链接 / 评论 / 关注） |
| 6 | 格式合规 | 无禁用联系方式、hashtag ≤ 2、mention ≤ 1 |
| 7 | 品牌/产品提及自然 | 不是硬广告，CTA 与内容相关 |

任何一项不过 → 改写后重新自检，不跳过。

---

## §5 HTML 预览生成

写入 `workspaces/x-posting/<date>/drafts/<slug>/preview.html`：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>X Draft Preview</title>
  <style>
    body { font-family: -apple-system, Segoe UI, sans-serif; background: #15202b; color: #e7e9ea; padding: 40px; }
    .card { max-width: 540px; margin: 0 auto; background: #192734; border: 1px solid #38444d; border-radius: 16px; padding: 16px 20px; }
    .head { display: flex; align-items: center; gap: 12px; margin-bottom: 8px; }
    .avatar { width: 40px; height: 40px; border-radius: 50%; background: #38444d; }
    .name { font-weight: 700; }
    .handle { color: #8899a6; font-size: 14px; }
    .text { font-size: 15px; line-height: 20px; white-space: pre-wrap; word-break: break-word; }
    .meta { margin-top: 12px; color: #8899a6; font-size: 13px; display: flex; gap: 16px; }
    .char-count { color: {CHAR_COLOR}; font-weight: 600; }
  </style>
</head>
<body>
  <div class="card">
    <div class="head">
      <div class="avatar"></div>
      <div>
        <div class="name">{DISPLAY_NAME}</div>
        <div class="handle">{HANDLE}</div>
      </div>
    </div>
    <div class="text">{TWEET_TEXT_HTML_ESCAPED}</div>
    {MEDIA_BLOCK}
    <div class="meta">
      <span class="char-count">{CHAR_COUNT} / 280</span>
      <span>source: @{SOURCE_AUTHOR}</span>
    </div>
  </div>
</body>
</html>
```

- `CHAR_COLOR`：`<= 260 → #1d9bf0`，`261-280 → #ffd400`，`> 280 → #f4212e`（后者不应出现）
- `MEDIA_BLOCK`：有图时为 `<img src="{PATH}" style="margin-top:12px;border-radius:12px;max-width:100%;">`
- `SOURCE_AUTHOR` 来自 `selected_topics.json.author_screen_name`

---

## §6 预览展示与审批

> ⚠️ **强制**：生成 preview.html 和 text.md 之后，**必须立即调用 AskUserQuestion 工具**阻断会话，等待用户在结构化 UI 中选择。**不能**在对话中打印预览文字然后让模型自行 `end_turn`——这会让整个 Phase 中断，运行环境没有人工在读对话文字。AskUserQuestion 是本 Phase 唯一的合法暂停方式，每篇预览一次调用，一一对应。

调用方式：

- **question** 字段：一段 string，包含预览路径、字符数、纯文本正文三项（让用户能在结构化 UI 里直接看到关键信息，不依赖对话滚动）
- **options** 字段（固定 4 项）：
  - `ok` — 直接进入 Phase 5 发布
  - `draft` — 保存草稿，不发布
  - `edit` — 需要修改（用户通过 UI 自动提供的 Other 输入具体指令）
  - `skip` — 本条跳过，不保存

**AskUserQuestion 返回结果后才执行分支**：

- `edit`：按用户提供的 Other 文本重新撰写 → 跑一次 §4 自检 → 重新生成预览 → **再次调用 AskUserQuestion**（不要累积多个预览靠对话文本区分）
- `draft`：保留 preview.html 和 text.md 到 `workspaces/x-posting/<date>/drafts/<slug>/`，同时写入 `draft.json`（`status: "drafted"`），本篇结束
- `skip`：不保存任何产物，本篇结束
- `ok`：写入 `workspaces/x-posting/<date>/drafts/<slug>/final.json`，进入 Phase 5：

```json
{
  "text": "...",
  "char_count": 217,
  "media_path": null,
  "source_topic_id": "2045568934254960835",
  "source_topic_url": "https://x.com/ctatedev/status/2045568934254960835",
  "keyword": "browser automation",
  "written_at": "2026-05-09T12:41:00Z"
}
```

进入 Phase 5 发布。
