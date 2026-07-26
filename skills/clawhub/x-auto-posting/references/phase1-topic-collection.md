# Phase 1 Reference — 话题采集

## TOC

- §1 关键词轮转
- §2 搜索执行与流量捕获
- §3 打分与排序
- §4 报告输出
- §5 话题展示与选择

---

## §1 关键词轮转

读取 `config/keywords.json`：

```json
{
  "mode": "sequential",
  "last_index": -1,
  "keywords": ["browser automation", "AI agent", "web scraping", "..."]
}
```

**sequential 模式**：`next_index = (last_index + 1) % len(keywords)`，取 `keywords[next_index]`。

**轮转时机**：Phase 5 发布**成功**后才更新 `last_index`；否则 Phase 3 `skip` / 发布失败 / 用户中途退出均不推进，避免跳过同一关键词。

运行时将选中的关键词 slug 化（小写 + 空格转 `-`）供文件名使用，例如 `browser-automation`。

---

## §2 搜索执行与流量捕获

### 2.1 导航

```bash
# KEYWORD = 原始关键词，URL-encode 后拼入
browser-act --session <session_name> network clear
browser-act --session <session_name> navigate "https://x.com/search?q=<ENCODED_KEYWORD>&src=typed_query&f=top"
browser-act --session <session_name> wait stable
```

- `f=top`：按相关性排序（X 默认的 Top tab，结果质量高）
- `f=latest`：按时间倒序（用于追热点时使用）
- `f=media`：只看带图/视频（若产品类内容需要视觉参考）

### 2.2 读取 SearchTimeline 响应

```bash
browser-act --session <session_name> network requests --type xhr,fetch --filter SearchTimeline --format json > tmp/search_reqs.json
```

从 JSON 中取最新一条 `SearchTimeline` 的 `request_id`（数组按时间顺序，最后一条最新）：

```bash
REQ_ID=$(python -c "import json; d=json.load(open('tmp/search_reqs.json','r',encoding='utf-8')); print([r['request_id'] for r in d['requests'] if 'SearchTimeline' in r['url']][-1])")

browser-act --session <session_name> network request $REQ_ID --format json | python scripts/parse-search-timeline.py --top 20 --non-reply-only > tmp/tweets.json
```

### 2.3 失败兜底

- `SearchTimeline` 无命中 → 检查页面是否登录态失效、是否被 X 跳转到 `/login`；必要时登录后重试
- 请求已过期（列表只保留最近 N 条流量）→ 重新 `browser-act reload` + `wait stable` 触发一次新的 SearchTimeline
- 极端情况（X 改版移除该端点）→ 降级到 DOM 提取：`browser-act eval` 读取 `article[data-testid="tweet"]` 列表并从 `aria-label` 解析互动数字（准确度降低，views 不可得）

---

## §3 打分与排序

`parse-search-timeline.py` 默认输出按 `score` 倒序的前 20 条，其中：

```
score = likes + retweets*2 + replies*1.5 + bookmarks*1.5 + quotes*2
```

可选过滤：
- `--non-reply-only`：过滤掉 `is_reply=true` 的回复（降低噪音，优先主帖）
- `--min-score 100`：忽略低互动推文
- `--top 10`：只返回前 N 条

**选题策略**：高 bookmarks + 中等 likes 通常意味着"收藏但未公开互动"，这类题材最适合重述 / 科普。单看 likes 会偏向情绪化短推文。

---

## §4 报告输出

写入 `workspaces/x-posting/<YYYY-MM-DD>/topics/TOPICS_<kw-slug>.md`：

```markdown
# X Topics — {KEYWORD}
Generated: {YYYY-MM-DD HH:MM}

## Top 5 Candidates

### 1. {score=13402} — @{screen_name}
- URL: {tweet_url}
- Posted: {created_at}
- Metrics: 👍 {likes} · 💬 {replies} · 🔁 {retweets} · 🔖 {bookmarks} · 👁 {views}
- Has media: {Yes / No}
- Full text:
  > {full_text}
- Key quote (for Phase 4): "{挑一句最有张力的原文}"
- Pain description (for Phase 4): {一句话描述该推文揭示的痛点或洞察}
- Tools tried (if applicable): {对方尝试过/对比的工具}

### 2. ...
```

`Key quote` / `Pain description` / `Tools tried` 由 Agent 根据原文提炼，必须来自推文正文的原始内容，不允许编造。

---

## §5 话题展示与选择

> ⚠️ **强制**：向用户展示 Top 5 摘要后，**必须**调用 AskUserQuestion 工具阻断会话收集用户选择。**不能**只在对话文字里展示 Top 5 然后 `end_turn` 等用户主动回复——这会让整个流程停住。

在对话中简要输出 Top 5 摘要（标题 + 作者 + 互动数 + 一句话概括）供上下文参考，然后**立即**调用 AskUserQuestion：

- question：「Phase 1 采集到 Top 5 话题，选一个方向来写」
- options（最多 4 项 + 自动的 Other）：
  - `#1 {一句话概括}`
  - `#2 {一句话概括}`
  - `#3 {一句话概括}`
  - `skip` — 今天不发
  - （Other 自动提供，供用户输入 `"1 3 5"` 等多选组合）

用户回复后：
- 选中编号 → **必须**将选中话题写入 `workspaces/x-posting/<date>/selected_topics.json`，然后进入 Phase 3
- `skip` → 结束 run，`last_index` 不变，不创建 selected_topics.json

`selected_topics.json` 是 Phase 4 Pre-Write Gate 的输入契约，**必须存在**才能起稿。schema：

```json
[
  {
    "index": 1,
    "source_tweet_id": "2045568934254960835",
    "source_tweet_url": "https://x.com/ctatedev/status/2045568934254960835",
    "keyword": "browser automation",
    "key_quote": "...",
    "pain_description": "...",
    "tools_tried": [],
    "has_media": true,
    "author_screen_name": "ctatedev",
    "publish_mode": "pending"
  }
]
```

`publish_mode` 初始填 `pending`，Phase 3 追加的第二次 AskUserQuestion（立即发布 / 暂存草稿）返回后再更新为 `immediate` 或 `draft`。
