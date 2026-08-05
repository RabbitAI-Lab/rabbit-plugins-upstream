# 检索策略 (search_strategy.md)

本文档是网页磁力检索的可执行细化方案（链路1）。

---

## 一、网页检索

### 1.1 资源站分类与检索方式

| 类型 | 特点 | 检索方式 | 稳定性 |
|------|------|----------|--------|
| BT/磁力站 | 直链/磁力，有搜索 | 搜索接口/HTML | 较稳定 |
| 采集站（在线播放） | 播放页，易失 | 多为采集API | 易失 |
| 资源论坛 | 帖子含磁力/种子 | 帖子正文爬取 | 中 |

### 1.2 探查策略（按稳定性降级，逐一尝试）

接入新站时按此优先级探查，命中即停：

**优先级 1 — JSON API（最稳）**
现代资源站前端多用 Vue/React，背后有 JSON 接口。
- 浏览器开 F12 → Network → 触发一次搜索 → 找 XHR/Fetch 返回 JSON 的请求
- 直接复用该接口（带其参数签名/cookie），解析 JSON
- 比 HTML 稳 10 倍，站点改版通常只动前端不动接口

**优先级 2 — HTML 爬取**
无 API 时用 `requests + lxml`（或 BeautifulSoup）。
- 用 CSS Selector / XPath 定位结果列表
- 解析标题、链接、大小、清晰度
- 适合结构固定的老站

**优先级 3 — 浏览器渲染兜底**
JS 渲染且无 API 时用 Playwright。
- 仅当前两级都失败才启用（重、慢）
- skill 默认不引入 Playwright，按需安装

**何时用 WebFetch**：WorkBuddy 内置 WebFetch 走代理，对 Cloudflare/地域限制更友好。
优先用 WebFetch 抓页面，再本地正则解析；比裸 requests 成功率高。

### 1.3 反爬应对

- **UA 轮换**：维护 5~10 个真实浏览器 UA，随机选
- **限速**：每站 QPS ≤ 1，请求间随机 sleep 0.5~2s
- **重试退避**：失败重试 2 次，指数退避（1s/2s/4s）
- **WebFetch 优先**：遇 403/Cloudflare 切 WebFetch
- **cookie**：论坛类需登录，cookie 填入 source_cfg

### 1.4 统一输出 schema（瘦：只装网页能直接拿到的原始字段）

fetcher 只负责把页面文本抓下来，**不做任何信息提取**（年份/分辨率/编码/音轨等由
`title_parser.py` 在聚合层统一解析）。`title` 是后续一切信息提取的来源，最重要：

```json
{
  "title": "消失的人[国语配音/中文字幕].Vanishing.Point.2026.2160p.WEB-DL.H.265.HDR-PandaQT 2.42GB",
  "url": "magnet:?xt=... 或 https://...",
  "link_type": "magnet|direct|playpage|torrent",
  "source_type": "web",
  "credibility": 0.7,
  "source_id": "site-a",
  "size": "2.3GB",
  "seeders": 142,
  "detail_url": "..."
}
```

`link_type` 决定可用性系数：
- `direct`/`magnet`/`torrent`：可直接下载，availability=1.0
- `playpage`：仅播放页，availability=0.5（需二次解析）

> 用 `common.build_candidate(title, url, source_cfg, link_type=...)` 拼装，无需手写字段。
> 信息提取零代码：年份/分辨率/编码/音轨/字幕/大小/低质判定全由 `title_parser` 从 `title` 串解析。

### 1.5 parser 注册机制

每个网页源一个 parser 文件，放 `scripts/search_sources/web/`，统一接口：

```python
def parse(query, source_cfg):
    """query: 标准化查询; source_cfg: 该源配置. 返回候选列表."""
    return [{"title":..., "url":..., "link_type":..., ...}]
```

调度器按 `source_cfg["id"]` 动态加载对应 parser，无需改主干。
新增站点 = 新增一个 parser 文件 + registry 注册一行。

### 1.6 接入新网页源 checklist

1. F12 抓搜索请求，判断走 API 还是 HTML
2. 写 fetcher 文件实现 `parse()`，**只抓标题串 + 链接 + 可选大小/做种**，不做信息提取
3. 在 `config.json` / `source_registry.md` 注册（id/domains/credibility/enabled/priority）
4. 本地测一次 `parse(query, cfg)` 确认拿得到标题串
5. 观察健康度，连续失败调整限速或换镜像
6. 若标题解析不全（新格式），改 `title_parser.py` 一处即全局生效，不碰 fetcher

## 1.7 分层检索配置

`config.json` 中 `web_sources` 按 `priority` 升序，`tier1_size`（默认 3）决定 tier-1 常用源数量：

```json
{ "tier1_size": 3, "top_n": 3, "min_relevance": 0.6 }
```

- tier-1 = priority 前 `tier1_size` 个启用源（如 souxunlei/yilu/nyaa）
- tier-1 并行检索后聚合评分，相关候选数 ≥ `top_n` 即视为充足，**不检索 tier-2**
- 不足才回退 tier-2（剩余源）补充检索

---
