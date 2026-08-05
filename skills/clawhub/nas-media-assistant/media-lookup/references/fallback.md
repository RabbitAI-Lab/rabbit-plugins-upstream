# media-lookup/references/fallback.md · TMDB→豆瓣降级策略

> **受众**：编排器 / Agent / 开发者。本文件承载 TMDB 不可达时的两级降级策略与缓存机制。
> 完整技术方案见 `media-lookup/references/design.md`。

---

## 一、两级降级

| 级别 | 数据源 | 触发条件 | 提供能力 |
| --- | --- | --- | --- |
| **L1** | TMDB | 有 `TMDB_API_KEY` 且网络可达 | 全字段：合集/季集/类型/简介/海报/原名 |
| **L2** | 豆瓣 suggest | TMDB 不可达 / 限流 | 仅 年份/季/标题（无 overview/genres/collection） |

> L1/L2 均未命中时返回 `{"error":"未找到匹配媒体","query":...,"year":...}`，由调用方决定后续处理（换关键词 / 放弃）。

## 二、降级触发链

```
search_movie (TMDB)
  ├─ 启动时 _check_dns_health 探测 -> 不可达则 _setup_ip_override
  ├─ HTTP 429 -> Retry-After / 指数退避 (1→2→4→8s, 最多 4 次)
  ├─ 首次网络失败 -> 启用 IP 覆盖并重试一次
  ├─ 二次失败 -> _NET_DOWN=True (fail-fast, 后续全跳网络)
  ├─ 无结果 + 有年份 -> 去年重试一次
  └─ 仍无结果 -> _douban_search_movie (豆瓣兜底)
       └─ 0.5s 最小间隔 + 3 次重试（空列表视为被限流）
```

## 三、缓存机制

- 文件：`media-lookup/.cache/tmdb_cache.json`
- 键：`movie:<title>:<year>` / `tv:<title>:<year>` / `collection:<id>`
- TTL：`CACHE_TTL = 86400 * 7`（7 天）
- 命中缓存即跳过网络请求，降低 429 风险、加速响应
- 缓存以 `movie:` / `tv:` / `collection:` 键索引，按时间戳判定是否过期

## 四、输出约定

| `source` 字段 | 含义 | 字段可用性 |
| --- | --- | --- |
| `"tmdb"` | L1 命中,数据完整 | `overview` / `genres` / `collection` / `seasons`(tv) / `poster_path` 全有 |
| `"douban_fallback"` | L2 兜底 | `tmdb_id=null`、无 `overview` / `genres` / `collection`、仅年份/季/标题 |

> Agent 应根据 `source` 决定下游消费策略：tmdb 完整数据可直接用于规范命名；douban_fallback 仅能补年份消歧，归档时仍需 pending_lookup 补全元数据。
