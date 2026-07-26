# Phase 6 Reference — 效果追踪

## TOC

- §1 单帖 24h 追踪（6.1）
- §2 批量数据回收（6.2）
- §3 查看评论并回复（6.3）
- §4 生成汇总报告（6.4）
- §5 数据存储结构

---

## §1 单帖 24h 追踪（6.1）

### 1.1 触发时机

Phase 5 发布成功后，向用户提示：

```
已发布。24 小时后运行 `/x-auto-posting 追踪效果 {tweet_id}` 可采集初始数据。
```

或用 `/schedule` 系统排程：

```
在 {发布时间 + 24h} 运行 `/x-auto-posting 追踪效果 {tweet_id}`
```

### 1.2 执行步骤

```bash
# TWEET_ID 从 published.json 读取，或由用户传入
# HANDLE 从 published.json.url 解析（x.com/{handle}/status/{id}）

browser-act --session <session_name> network clear
browser-act --session <session_name> navigate "https://x.com/<HANDLE>/status/<TWEET_ID>"
browser-act --session <session_name> wait stable

# 取 TweetDetail 响应
browser-act --session <session_name> network requests --type xhr,fetch --filter TweetDetail --format json > tmp/td_reqs.json

REQ_ID=$(python -c "import json; d=json.load(open('tmp/td_reqs.json','r',encoding='utf-8')); print([r['request_id'] for r in d['requests'] if 'TweetDetail' in r['url']][-1])")

browser-act --session <session_name> network request $REQ_ID --format json | python scripts/parse-tweet-detail.py <TWEET_ID> > tmp/metrics.json
```

返回：

```json
{
  "id": "2053123456789012345",
  "url": "https://x.com/SisilyNora/status/2053123456789012345",
  "text": "...",
  "metrics": {"likes": 12, "replies": 3, "retweets": 1, "quotes": 0, "bookmarks": 5, "views": 348}
}
```

### 1.3 写入追踪记录

更新 `published.json` 中对应推文的 `tracking.metrics_24h` 和 `tracking.last_checked`：

```json
{
  "tracking": {
    "metrics_24h": {"likes": 12, "replies": 3, "retweets": 1, "quotes": 0, "bookmarks": 5, "views": 348, "checked_at": "2026-05-10T04:15:10Z"},
    "metrics_7d": null,
    "last_checked": "2026-05-10T04:15:10Z"
  }
}
```

---

## §2 批量数据回收（6.2）

### 2.1 场景

- 用户触发 "看数据" / "批量追踪"
- 每周例行（用户可用 `/schedule` 排程）

### 2.2 执行步骤

```bash
# 从 published.json 读取最近 N 天（默认 30）的推文列表
python -c "
import json, datetime
with open('workspaces/x-posting/tracking/published.json', 'r', encoding='utf-8') as f:
    posts = [json.loads(line) for line in f if line.strip()]
cutoff = datetime.datetime.utcnow() - datetime.timedelta(days=30)
recent = [p for p in posts if datetime.datetime.fromisoformat(p['published_at'].rstrip('Z')) > cutoff]
print(json.dumps([{'id': p['id'], 'url': p['url']} for p in recent]))
" > tmp/to_track.json

# 逐条执行 §1.2，每条之间 sleep 3-5 秒
for TWEET_ID in ...; do
    # 重复 §1.2
    # sleep 3
done
```

**并行限制**：不要并行，X 对同一账号高频刷推文详情页会触发风控。串行 + 3 秒间隔即可覆盖 50-100 条。

### 2.3 增量更新

- 首次回收 → 写入 `metrics_24h`（如果距发布 24-48h）或 `metrics_7d`（距发布 > 7 天）
- 对同一推文重复回收 → 覆盖 `last_checked`，并在 `tracking.history[]` 追加历史快照

```json
{
  "tracking": {
    "metrics_24h": {...},
    "metrics_7d": {...},
    "history": [
      {"checked_at": "2026-05-10T04:15:10Z", "likes": 12, "views": 348},
      {"checked_at": "2026-05-17T04:15:10Z", "likes": 34, "views": 1203}
    ],
    "last_checked": "2026-05-17T04:15:10Z"
  }
}
```

---

## §3 查看评论并回复（6.3）

### 3.1 获取 replies

推文详情页 `TweetDetail` 响应除主推文外，还包含 `conversationthread-{id}` 条目（回复线程）。可从同一响应中提取：

```python
# 在 parse-tweet-detail.py 基础上扩展（或编写新 parse-tweet-replies.py）
# 遍历 instructions[].entries[]，找 entryType == "TimelineTimelineModule" 的 conversation thread
# 每个 thread 下 items[] 是单条 reply
```

> 注：Skill 当前仅封装了提取主推文的 `parse-tweet-detail.py`。若需要 replies 列表，参照 `scripts/parse-search-timeline.py` 的结构自行扩展；Phase 1 采集的通用 tweet 解析逻辑可复用。

### 3.2 起草回复

对每条 reply，调用 AskUserQuestion 工具展示 reply 原文，起草回复后询问：

```
对 @{reply_author} 的评论「{reply_text}」起草回复：
---
{draft_reply_text}
---
是否发送？
选项：
- ok — 发送回复
- edit — Other 提供修改指令
- skip — 跳过本条
```

### 3.3 发送回复

回复使用 compose 的 `in_reply_to` 模式：

```bash
# 直接导航到原推文页面，点击某条评论下方的 Reply 按钮
browser-act --session <session_name> navigate "https://x.com/<HANDLE>/status/<ORIGINAL_ID>"
browser-act --session <session_name> wait stable
browser-act --session <session_name> state
# 找到目标 reply 下的 "Reply" 按钮索引
browser-act --session <session_name> click <reply_btn_index>
browser-act --session <session_name> wait stable
# 现在打开了回复 compose 模态，复用 Phase 5 §3-§6 的流程
```

**频率控制**：回复行为也受 X 风控，每小时回复 ≤ 10 条，每条间隔 ≥ 1 分钟。

---

## §4 生成汇总报告（6.4）

### 4.1 触发

用户说 "生成报告" / "导出数据" 时。

### 4.2 数据源

`workspaces/x-posting/tracking/published.json` 中所有带 `tracking.metrics_*` 的条目。

### 4.3 输出

写入 `workspaces/x-posting/tracking/report_<YYYY-MM-DD>.md`：

```markdown
# X Posting Report — 2026-05-17

时段：2026-05-01 到 2026-05-17（17 天）
总发帖：23 条
总 views：142,857 · 总 likes：1,203 · 总 replies：87 · 总 bookmarks：412

## Top 5 推文（按 likes）

| # | 发布时间 | likes | replies | retweets | bookmarks | views | 链接 |
|---|---------|-------|---------|----------|-----------|-------|------|
| 1 | 2026-05-08 | 234 | 12 | 18 | 56 | 8,432 | {url} |
| ... |

## 每日发帖与互动趋势

| 日期 | 发帖数 | 总 likes | 总 views | 平均 like/贴 |
|------|--------|----------|----------|--------------|
| 2026-05-01 | 2 | 34 | 1,234 | 17.0 |
| ... |

## 关键词表现排序

| 关键词 | 发帖数 | 平均 likes | 平均 views |
|--------|--------|------------|------------|
| browser automation | 5 | 87.4 | 2,340 |
| AI agent | 3 | 34.2 | 1,203 |

## 建议

- 关键词 `{best_kw}` 平均互动最高，下周增加权重
- 关键词 `{worst_kw}` 平均 views < 500，建议暂停或更换题材
- 最佳发布时段：{hour}:00-{hour+1}:00 UTC（互动密度最高）
```

建议段由 Agent 基于数据分析得出，不硬编码。

---

## §5 数据存储结构

```
workspaces/x-posting/
├── session_state.json                          账号 + 配额 + 最后发帖时间
├── 2026-05-09/                                  按日期分文件夹，便于回溯
│   ├── topics/
│   │   └── TOPICS_browser-automation.md        Phase 1 报告
│   ├── selected_topics.json                     Phase 3 选中话题
│   ├── style_fingerprint.json                   Phase 2 风格指纹
│   └── drafts/
│       └── <slug>/
│           ├── text.md                          Phase 4 纯文本
│           ├── preview.html                     Phase 4 HTML 预览
│           ├── final.json                       Phase 4 审批通过后的元数据
│           └── pre_publish.png                  Phase 5 发布前截图
└── tracking/
    ├── published.json                           历史所有已发推文（append-only）
    ├── incidents.log                            风控事件记录（403 / 429 / duplicate）
    └── report_<YYYY-MM-DD>.md                   周期性报告
```

`published.json` 使用 **JSON Lines** 格式（每行一个 JSON 对象），便于 append 和流式读取。如果选择标准 JSON 数组，读写前后都要完整解析，文件大时较慢。

示例（JSON Lines）：

```
{"id":"2053123...","url":"...","text":"...","published_at":"2026-05-09T04:15:10Z",...}
{"id":"2053124...","url":"...","text":"...","published_at":"2026-05-09T08:30:00Z",...}
```
