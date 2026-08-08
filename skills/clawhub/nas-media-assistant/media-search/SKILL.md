---
name: media-search
description: |
  网页磁力/直链资源检索与筛选。输入：已识别的影视查询（片名+年份+类型）。
  输出：经过筛选与排序的候选下载链接列表（磁力/直链/种子/播放页）。
  分层检索网页源（tier-1 优先，不足回退 tier-2），由标题解析器从标题串提取全部
  资源信息（分辨率/编码/音轨/字幕/大小/年份…），统一去重评分后按"优先高清"排序，
  过滤低质资源（枪版/样片）。
homepage: https://openclaw.example.com/skills/media-search
metadata:
  openclaw:
    emoji: 🔗
    requires:
      binaries: [python3, curl]
  security:
    credentials_usage: |
      检索仅发往用户自有检索引擎/代理（局域网/本地）或公开资源站。不发往第三方用户密钥。
    allowed_domains:
      - '*.local'
      - '*.lan'
agent_created: true
---

# media-search（网页磁力/直链检索与筛选）

> **Agent 总规则**见 [`../../AGENT.md`](../../AGENT.md)。
> 架构原则 / 分层调度 / fetcher 契约 / 健壮性机制见 [`references/design.md`](./references/design.md)。
> 探查/反爬策略见 [`references/search-strategy.md`](./references/search-strategy.md)，
> 数据源账本见 [`references/source-registry.md`](./references/source-registry.md)，
> 评分公式见 [`references/quality-scoring.md`](./references/quality-scoring.md)，
> 源实测评估见 [`references/source-evaluation.md`](./references/source-evaluation.md)。

## 1. 职责

把"识别好的影视查询"变成"可下载的候选列表"，交给下游派发。
不负责：媒体识别（消歧/TMDB 元数据查询）、下载派发、文件归档、网盘分享检索。

## 2. 触发

- 用户意图"搜索/下载/找资源 + 片名" → 编排器主动调用
- 上游已完成媒体识别（按需），或查询自带清晰年份可直接跳过识别
- 编排器需呈现带号资源列表，或顶层候选命中即下

## 3. 工作流

```
编排器传入查询（片名/类型/年份/期望清晰度/编码/语言）
  │
  ▼
① search_dispatcher.py 分层检索（tier-1 优先，不足回退 tier-2）
  │
  ▼
② 各网页源 fetcher 并行抓取（标题串 + 链接 + 大小）
  │
  ▼
③ aggregator 富集 → title_parser 解析全部元信息
  │
  ▼
④ 硬性过滤（枪版/低质/低相关度）→ 软性排序（HD 优先评分）
  │
  ▼
⑤ 输出 Top-N 候选（默认 3）含 stats + excluded
```

## 4. CLI

```bash
# 标准检索（输出 JSON 给编排器）
python3 media-search/scripts/search_dispatcher.py '{"title":"消失的人","type":"movie","year":"2026","quality":"1080p"}'

# 检索 + 渲染为带号列表（agent 透传给用户）
python3 media-search/scripts/search_dispatcher.py '{"title":"乡村爱情18","type":"tv","year":"2026"}' \
  | python3 media-search/scripts/format_results.py --query "乡村爱情18 (tv)"

# 单跑 title_parser 调试
python3 media-search/scripts/title_parser.py '消失的人[国语配音].Vanishing.Point.2026.2160p.WEB-DL.H.265-PandaQT 2.42GB'
```

## 5. 输出

```json
{
  "candidates": [
    {
      "title": "消失的人[国语配音].Vanishing.Point.2026.2160p.WEB-DL.H.265-PandaQT 2.42GB",
      "title_cn": "消失的人", "year": "2026", "resolution": "2160p",
      "source": "WEB-DL", "codec": "H.265", "audio": "DTS5.1",
      "language": ["国语"], "subtitle": ["中文"],
      "source_type": "web", "link_type": "magnet",
      "url": "magnet:?xt=urn:btih:...",
      "credibility": 0.7, "source_id": "souxunlei",
      "quality_score": 96.0, "info_tags": ["DTS", "字幕", "HDR"]
    }
  ],
  "excluded": [
    { "url": "magnet:...", "reason": "low_quality", "title": "消失的人.2026.CAM.枪版" }
  ],
  "from_cache": false, "link": "web",
  "stats": {"raw": 12, "final": 3, "excluded": 4, "tiers": ["tier1"], "tier1_sufficient": true}
}
```

> `link:"web"` 标识本链路。`excluded` 含 `url+reason`，供下游失败换链时排除已试链接。

## 6. 选号协议（用户→agent）

| 用户原话 | 匹配 | 派发 |
|---|---|---|
| `1` / `下 1` / `下1` / `第一个` / `要 2` | `candidates[0]` | 派发到下游下载派发器（`url`+`title`+`metadata`） |
| `下载第 3 个` / `第 3` / `三` | `candidates[2]` | 同上 |
| `都要` / `全部` | `candidates[*]` | 逐个派发 |
| `换一批` / `更多` | - | 调整 `top_n` 或换关键词重检索 |
| `不下了` / `取消` | - | 终止，不写缓存 |

> **回查要求**：必须用本会话上一次 `candidates` 列表的**实际 JSON**，不能凭印象。
> 跨端点切换时主动确认「刚才展示的列表还作数吗」。

## 7. 何时跳过列表直接下载（下载模式）

满足任一条件即直接派发，不再列列表：
1. 顶层候选 `quality_score ≥ 80` 且 `credibility ≥ 0.8` 且唯一匹配
2. 用户原话含明确单一目标（`下 4K 的 XX` / `下 1080p 简体的 XX`）→ 命中即下
3. 之前已确认过选号 → 沿用会话内的选号

## 8. 能力边界

- ✅ 网页磁力/直链/种子/播放页检索 + 标题解析 + 高清优先排序 + 枪版过滤
- ✅ 分层检索（tier-1 优先 + tier-2 兜底）/ 源健康度管理
- ❌ 媒体识别 / TMDB 查询（上游）/ 下载与监控（下游）/ 文件归档（归档器）/ 网盘分享（已下线）
