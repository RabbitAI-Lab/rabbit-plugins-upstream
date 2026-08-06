# media-lookup · 技术设计

> **受众**：人 / Codex / 开发者。本文解释技术方案、架构决策、未来扩展。
> Agent 调用说明见 [`SKILL.md`](./SKILL.md)。

---

## 一、技术方案

### 1.1 总体定位

TMDB 为主源 + 豆瓣兜底。把片名查成一条消歧过的标准 JSON 媒体条目。
本工具只读、零副作用，仅写自身缓存，不关心下游如何消费返回结果。

### 1.2 请求元信息生命周期

`identify` 子命令的完整生命周期（`tv` 路径同构）：

```
identify(title, year)
  |
  v
search_movie(title, year)
  |-- 缓存命中 (movie:<title>:<year>, TTL 7d) ---------> 直接返回缓存
  |-- _acquire_rate_slot (滑动窗口限频)
  |-- _api_get /search/movie
  |     |-- 启动时 _check_dns_health 探测 -> 不可达则 _setup_ip_override
  |     |-- HTTP 429 -> Retry-After / 指数退避 (1->2->4->8s, 最多 4 次)
  |     |-- 首次网络失败 -> 启用 IP 覆盖并重试一次
  |     |-- 二次失败 -> _NET_DOWN=True (fail-fast, 后续全跳网络)
  |-- 无结果且带年份 -> 去年重试一次
  |-- 仍无结果 -> _douban_search_movie (豆瓣兜底, dict 带 _source=douban)
  v
_normalize_movie (标准 JSON 唯一出口)
  |
  v
标准 JSON { media_type:"movie", source:"tmdb"|"douban_fallback", ... }
```

`identify` 依次尝试 movie -> tv -> 豆瓣，命中即返回；全未命中返回 `{"error":...}`。

### 1.3 两级降级策略

| 级别 | 数据源 | 触发条件 | 提供能力 |
| --- | --- | --- | --- |
| L1 | TMDB | 有 Key 且网络可达 | 全字段（合集/季集/类型/简介/海报） |
| L2 | 豆瓣 suggest | 无 Key 或 TMDB 不可达 | 仅年份/季/标题（无 overview/genres/collection） |

> L1/L2 均未命中时返回 `{"error":...}`，由调用方决定后续处理。

### 1.4 健壮性机制

| 机制 | 实现 | 位置 |
| --- | --- | --- |
| DNS 修复 | 启动时 `_check_dns_health` 探测 443 连通；不可达则 `_setup_ip_override` 把 `api.themoviedb.org` 重定向到 AWS CloudFront IP | 模块加载时 |
| 滑动窗口限频 | `_acquire_rate_slot`：认证 40 次/10s、未认证 10 次/10s，超限阻塞等待腾出配额 | `_api_get` 调用前 |
| 429 退避 | `Retry-After` 头优先，否则指数退避 1->2->4->8s，最多 4 次 | `_api_get` |
| fail-fast | 首次网络失败 -> IP 覆盖重试；二次失败 -> `_NET_DOWN=True`，后续全部跳过网络 | `_api_get` |
| gzip 解压 | 响应头 `1f 8b` 时自动 `gzip.decompress`（部分代理忽略 `Accept-Encoding: identity`） | `_api_get` |
| 豆瓣限流保护 | 0.5s 最小间隔 + 3 次重试（空列表视为被限流） | `_douban_suggest` |

### 1.5 缓存

- 文件：`media-lookup/.cache/tmdb_cache.json`
- 键：`movie:<title>:<year>` / `tv:<title>:<year>` / `collection:<id>`
- TTL：`CACHE_TTL = 86400 * 7`（7 天）
- 结构：`{ "<key>": {"data": <原始 dict>, "ts": <epoch>} }`
- 命中缓存即跳过网络请求，减少 TMDB 配额消耗与 429 风险。

### 1.6 函数职责与依赖图

```
CLI main() --> identify --+-> search_movie --+-> _api_get --> _acquire_rate_slot
                          |                  +-> _load_cache / _save_cache
                          |                  +-> _douban_search_movie --> _douban_suggest
                          +-> search_tv -----+-> _api_get
                          |                  +-> _load_cache / _save_cache
                          |                  +-> _douban_search_tv --> _douban_suggest
                          +-> _normalize_movie / _normalize_tv / _normalize_douban

lookup_collection --> search_movie --> _api_get (collection 端点)
```

> 归一化三函数（`_normalize_movie` / `_normalize_tv` / `_normalize_douban`）是标准 JSON 契约的**唯一出口**，所有 CLI 子命令最终都经它们输出。

**函数式调用**：同目录 Python 脚本可直接 import 本模块：

```python
import tmdb_lookup as t
t.identify("功夫", "2004", api_key=t.get_api_key())            # -> 标准 JSON dict
t.search_movie("功夫", "2004", api_key=t.get_api_key())        # -> 原始 TMDB dict
t.lookup_collection("功夫", "2004", api_key=t.get_api_key())  # -> 合集详情 dict 或 None
```

> `search_*` / `lookup_collection` 返回原始 dict（含 `belongs_to_collection`、`genres`、`seasons` 等完整字段），供需要完整数据的调用方使用；`identify` 及各 CLI 子命令经 `_normalize_*` 输出标准 JSON。

---

## 二、核心规则

### 为何 TMDB + 豆瓣双源

TMDB 是免费、权威、中文友好的媒体元数据源。国内 TMDB 常因 DNS/IP 封锁不可达，豆瓣 suggest API 国内直连、免 Key、响应快（~0.1s），虽仅能补年份/季，但足以支撑文件命名消歧。双源互为兜底，成本极低。

### 为何 `_normalize_*` 统一出口 + `_source` 标记

所有出口经归一化函数，保证下游拿到统一形状。豆瓣兜底 dict 携带 `_source="douban"` 私有标记，归一化时据此置 `source="douban_fallback"`、`tmdb_id=None`，下游无需关心数据来自哪一级。

### 为何 `search_*` 返回原始 dict 而非标准 JSON

`search_movie` / `search_tv` 返回 TMDB/豆瓣的**原始 dict**（含 `belongs_to_collection`、`genres`、`seasons` 等完整字段），作为查询构建块。`_normalize_*` 是标准 JSON 的唯一出口。这种分离让 CLI 输出统一，同时保留原始字段供需要完整数据的调用方使用。

### 为何使用文件缓存

TMDB 有频率限制（认证 40 次/10s），重复查询同一片名浪费配额。文件缓存（7 天 TTL）让命中查询直接跳过网络，降低 429 风险、加速响应。缓存以 `movie:` / `tv:` / `collection:` 键索引，按时间戳判定是否过期。

---


