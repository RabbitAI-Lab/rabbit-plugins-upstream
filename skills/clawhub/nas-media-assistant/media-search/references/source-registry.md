# 数据源注册表 (source_registry.md)

本文件是网页检索（链路1）的「数据源账本」。网页源失效时，**只改本文件，不改代码**。
本注册表仅承载网页磁力/种子数据源（链路1）。

## 注册条目格式

### 网页源 (web_sources)

```json
{
  "id": "唯一标识，如 site-a",
  "name": "展示名",
  "domains": ["主域名", "备用域名1", "备用域名2"],
  "parser": "fetcher 标识，对应 search_sources/web/<id>.py",
  "search_url": "搜索URL模板，{q} 为查询词",
  "credibility": 0.0~1.0 来源可信度，
  "enabled": true|false,
  "priority": 1
}
```

- `domains`: 多域名镜像。主域名请求失败自动切备用，配合 health_check 降级
- `parser`: fetcher 只抓标题串+链接，不做信息提取（信息提取由 title_parser 统一负责）
- `credibility`: 影响聚合评分，正规站设高，资源论坛设中，不明来源设低
- `priority`: 数值越小越优先，决定分层检索的 tier-1/tier-2 归属（见 search_strategy.md 1.7）
- 顶层 `tier1_size`（默认 3）控制 tier-1 常用源数量

## 网页源 parser 位置

网页源 parser 放 scripts/search_sources/web/<parser>.py，统一接口 `parse(query, source_cfg)`。
调度器按 `source_cfg["parser"]` 动态加载，新增站点无需改调度器。

## 维护要点

- 站点挂了: `enabled` 设 false 或更新 `domains`，无需改代码
- 站点改版: 更新对应 parser 文件
- 新增站点: 新增 parser 文件 + registry 注册一行
- 健康度: health_check.py 自动维护，连续失败 3 次摘除，1 小时后重试
- 死链过滤: 由 L4 验证层自动过滤（基于 seeders/响应码），无需在 parser 处理

## 示例条目（占位，需替换为真实站点）

```json
{
  "web_sources": [
    {
      "id": "demo-movie-site",
      "name": "示例电影站",
      "domains": ["https://demo-movie.example.com"],
      "parser": "demo_movie",
      "search_url": "https://demo-movie.example.com/search?q={q}",
      "credibility": 0.7,
      "enabled": false
    }
  ]
}
```

## 已注册网页源清单

权威清单以 `assets/config.json` 的 `web_sources` 为准（运行时读取）；本表为人工可读账本。
新增/下线源时同步更新 config.json 与本表。

| id | 名称 | priority | enabled | parser | 链接形态 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| souxunlei | 搜迅雷 | 2 | ✅ | souxunlei | magnet | 关键词转 UTF-8 hex，hash 即 btih，直构磁力 |
| yilu | 1lou | 3 | ✅ | yilu | torrent | Xiuno BBS 论坛，多域名 failover，详见下节 |
| xl720 | 迅雷电影天堂 | 4 | ✅ | xl720 | magnet/playpage | 详情页抽 magnet，兜底 thunder |
| dongmanhuayuan | 动漫花园 | 5 | ✅ | dongmanhuayuan | magnet/playpage | 论坛详情页抽 magnet |
| nyaa | Nyaa | 6 | ✅ | nyaa | magnet | 国际动漫+影视，requests 直接拿 magnet |

> `tier1_size=3`：tier-1 = priority 1~3（souxunlei/yilu/nyaa），不足才回退 tier-2（priority 4~5：dongmanhuayuan/xl720）。
> 2026-08 移除 btsearch（依赖 Playwright+Chrome，普通环境不可用）与 heimacili（Cloudflare 高级反爬），5 源精简。

### 1lou（yilu）特性

> 以下为 2026-08 实连 1lou.me 验证所得（首页标题「BT之家1LOU站」）。

- **站点**：Xiuno BBS 资源论坛（BT之家1LOU站）。7 个镜像域名按优先级：`1lou.me` -> `one` -> `icu` -> `xyz` -> `info` -> `vip` -> `pro`。实测 `me/one/xyz` 可达、`icu` 不通，failover 有效。
- **下载方式（重要）**：帖子详情页**无 magnet 链接**，下载物为 `.torrent 种子文件`：
  - `attach-download-{aid}.htm` -> 直接返回 `application/octet-stream` 的 bencode 种子（如 `d8:announce39:http://tracker1.it...`）。
  - 因此本源 `link_type` 恒为 `torrent`；downloader-manager 下载该 URL 得 .torrent 再喂 qBittorrent。
  - 站方推荐纯 BT 客户端（Transmission/BitComet/**qBittorrent**/uTorrent），**不支持迅雷**（吸血）。本架构用 qBittorrent，天然契合。
- **多域名 failover**：dispatcher 不做域名切换，由 `yilu.py` 内部逐个遍历 `domains[]`；首个能连通并返回结果的域名即采用。最多试前 `MAX_DOMAIN_ATTEMPTS`（默认 3）个域名。不可达切下一个；可达但无结果则不切。
- **搜索 URL**：`{base}/search.htm?keyword={q}`（Xiuno GET 表单，第1页；`{q}` 已 URL 编码）。分页为 `search-{kw}-{type}-{page}.htm`（kw 未编码，故 parser 用 GET 形式）。格式若变，只改 `config.json` 的 `search_url`，无需改代码；failover 时 parser 会把 host 自动换成当前 base。
- **结果页 thread 链接**：主体 `.threadlist` 内格式为 `thread-{tid}.htm`（**单段 tid**，非 `thread-tid-1-1`）。
- **解析路径**：搜索结果页取 `thread-{tid}.htm` 帖子链接 + 帖子标题 -> 进帖子详情页取 `attach-download-{aid}.htm` 种子链接（一帖可能有多个种子，取首个）。
  - 标题用搜索结果的帖子链接文本（文件名格式，信息最丰，如 `庆余年.第二季[全36集][国语配音/中文字幕].Joy.of.Life.S02.1080p.WEB-DL...-BlackTV`）。
  - 防御性保留 magnet 检测（实测均无），以防个别帖或将来改版。
  - 拿满 `TARGET_RESULTS`（默认 5）条种子即提前停止抓详情，控制请求数。
- **站内杂质过滤**：站内偶尔混杂非种子内容（在线播放页、外部资源分享页等），与 `[BT下载]` 种子帖并列。parser 在搜索结果层按标题关键词过滤（默认 `网盘/夸克/片源/无字/在线`），可由 `source_cfg.exclude_keywords` 覆盖。
- **架构约束**：parser 只抓「标题串 + 链接」原始字段，不做信息提取（年份/分辨率/编码等交由 aggregator 调 `title_parser` 统一解析）。
- **站点失效应对**：换镜像域名更新 `domains`；搜索格式变更新 `search_url`；连续失败由 `health_check` 自动摘除。
