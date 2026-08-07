# media-search · 技术设计

> **受众**：人 / Codex / 开发者。本文解释技术方案、架构决策、稳定性机制与维护指南。
> Agent 操作手册见 [`SKILL.md`](./SKILL.md)。检索策略细节见 [`references/search_strategy.md`](./references/search_strategy.md)，
> 数据源账本见 [`references/source_registry.md`](./references/source_registry.md)，
> 评分公式见 [`references/quality_scoring.md`](./references/quality_scoring.md)，
> 源实测评估见 [`references/source_evaluation.md`](./references/source_evaluation.md)。

---

## 一、架构原则

### 1.1 标题解析是稳定核心，网页抓取是脆弱外围

资源标题串（磁力名 / 种子名 / 文件名）内嵌了 90% 有用信息——分辨率/编码/音轨/字幕/年份/大小/来源/发行组，
**与具体网站无关**。任何站点都会改版、宕机、被反爬，但「范式化的标题串」长期稳定。

由此推出**分工原则**：

| 组件 | 职责 | 是否能跨站点复用 |
| --- | --- | --- |
| `title_parser.py` | 从标题串提取全部元数据 | ✅ 完全独立于站点 |
| `scripts/search_sources/web/*.py` | 把页面文本抓下来（标题串 + 链接） | ❌ 一站一文件 |
| `aggregator.py` | 调 title_parser 统一解析 + 去重 + 评分 + 排序 + 过滤 | ✅ 完全独立于站点 |
| `search_dispatcher.py` | 分层调度 + 充足性判定 + 缓存 | ✅ 完全独立于站点 |

**工程后果**：新站点失效只影响 fetcher 一处；新字段（如 HDR、Atmos）发现后只改 title_parser 一处即全局生效。
**反之**：把信息提取塞进 fetcher 会导致每站重复实现解析、改一处要全站回归。

### 1.2 解析-抓取-评分三层解耦

```
网页源 fetcher        title_parser        aggregator
   (脆弱外围)         (稳定核心)         (策略层)
     │                   ▲                  ▲
     │   原始 title      │  结构化字段       │  评分/排序
     │   + url           │  (10+ 字段)       │  + 过滤
     └──────────────────►│                  │
                        │                  │
                        │  parsed ─────────►│
                        └──────────────────┘
```

- fetcher 只见「标题串」+「链接」，输出**瘦 schema**（见 references/search_strategy.md §1.4）。
- title_parser 输入是任意标题串，输出标准 JSON，**任何字段提取不到则为空，绝不抛异常**。
- aggregator 只见解析后的字段做评分，不读原始标题——保证评分规则与 fetcher 完全解耦。

---

## 二、分层检索调度

### 2.1 为什么要分层

- 5 站并行打满 → 平均 6~9s、对易失源依赖大、单源噪声会被全量带进候选
- 2~3 站优先并行 → 2~4s 出结果、Top-N 命中率 95%+、失败时回退兜底

### 2.2 tier-1 / tier-2 划分

按 `assets/config.json` 的 `web_sources[].priority` 升序排序，取前 `tier1_size`（默认 3）个启用源作为 **tier-1**，
剩余为 **tier-2**。

```
config.tier1_size = 3

web_sources (按 priority 升序):
  [0] souxunlei        priority=2   ← tier-1
  [1] yilu             priority=3   ← tier-1
  [2] nyaa             priority=6   ← tier-1
  [3] dongmanhuayuan   priority=5   ← tier-2
  [4] xl720            priority=4   ← tier-2
```

### 2.3 tier-1 并行 → 充足性判定 → 可选回退 tier-2

```
tier-1 源并行检索 (ThreadPoolExecutor)
  │
  ▼
充足性判定(v2):
  ├─ 条件 A: 至少 MIN_OK_SOURCES (默认 2) 个 tier-1 源成功返回结果
  ├─ 条件 B: 至少 1 条高分完整资源(非单集 且 quality_score ≥ HIGH_SCORE_THRESHOLD=60)
  └─ 同时满足 → 视为充足, 不检索 tier-2
  │
  ▼ (任一不满足)
tier-2 源并行检索补充
  │
  ▼
合并所有结果 → aggregator 统一解析+去重+评分+过滤 → Top-N 输出
```

**为什么 v2 改判定（2026-08）**：v1 只看「数量 ≥ top_n」就返回，但遇到「单源 3 条全单集」会误判充足，
导致用户拿到一堆单集无法下载。v2 引入「源数量 + 高分完整资源」双约束。

### 2.4 parser 动态加载

`search_dispatcher.py` 按 `source_cfg["id"]` 动态 import `scripts/search_sources/web/<id>.py`，
调用其 `parse(query, source_cfg)`。新增站点 = 新增一个 parser 文件 + registry 注册一行，**不碰调度器主干**。

---

## 三、fetcher 契约

### 3.1 输入参数

```python
def parse(query: dict, source_cfg: dict) -> list[dict]:
    """
    query: 标准化查询
      {"title": str, "type": "movie|tv", "year": str|None, "quality": str|None}
    source_cfg: 该源配置（来自 assets/config.json 的 web_sources[i]）
      {"id": str, "domains": [str], "search_url": str, "credibility": float,
       "exclude_keywords": [str], "...": 源专属参数}
    """
```

### 3.2 输出 schema（瘦：只装网页能直接拿到的原始字段）

```json
{
  "title": "消失的人[...].Vanishing.Point.2026.2160p.WEB-DL.H.265.HDR-PandaQT 2.42GB",
  "url": "magnet:?xt=urn:btih:...",
  "link_type": "magnet|direct|playpage|torrent",
  "source_type": "web",
  "credibility": 0.7,
  "source_id": "souxunlei",
  "size": "2.3GB",
  "seeders": 142,
  "detail_url": "https://..."
}
```

> **硬性约束**：fetcher **不做任何信息提取**（年份/分辨率/编码/音轨/字幕/大小判定）。
> 任何信息提取都由 aggregator 调 title_parser 完成。违反 = 重复实现解析 + 跨站点回归噩梦。

### 3.3 link_type 与可用性系数

| `link_type` | 含义 | availability 系数 |
| --- | --- | --- |
| `magnet` | 磁力链接（BT/磁力站直出） | 1.0 |
| `torrent` | `.torrent` 种子文件（需 qBittorrent 解析） | 1.0 |
| `direct` | HTTP/直链（迅雷/电驴可用） | 1.0 |
| `playpage` | 仅在线播放页（需二次解析） | 0.5 |

`aggregator.score()` 把 availability 系数乘到总分上，让纯播放页候选自动下沉。

### 3.4 反爬应对（fetcher 内部）

- **UA 轮换**：5~10 个真实浏览器 UA 随机选
- **限速**：每站 QPS ≤ 1，请求间 sleep 0.5~2s
- **重试退避**：失败重试 2 次，指数退避（1s / 2s / 4s）
- **多域名 failover**：源配置 `domains[]` 多镜像，首个不通自动切下一个（实例如 yilu 7 镜像）
- **Cloudflare/403 兜底**：未来若引入 WebFetch 走代理，可由 `common.py` 统一接管

详见 `references/search_strategy.md` §1.3。

---

## 四、title_parser 字段说明

输入：任意资源标题串。输出：标准 JSON，**任何字段提取不到则为空，绝不抛异常**。

| 字段 | 类型 | 提取自 | 示例 |
| --- | --- | --- | --- |
| `title_cn` | str | 标题前缀中文段 | `消失的人` |
| `title_en` | str | 标题英文段 | `Vanishing Point` |
| `year` | str | 4 位年份 | `2026` |
| `resolution` | str | 数字 + p / 4k / 8k | `2160p` / `4K` |
| `source` | str | 介质来源关键词 | `WEB-DL` / `BluRay` / `REMUX` |
| `codec` | str | 视频编码 | `H.265` / `H.264` / `x265` |
| `audio` | str | 音轨（取首个命中） | `DTS5.1` / `Atmos` / `AAC2.0` |
| `hdr` | str | HDR 标志 | `HDR` / `Dolby Vision` / 空 |
| `language` | list[str] | 语言标签 | `["国语"]` / `["日语"]` |
| `subtitle` | list[str] | 字幕标签 | `["中文"]` / `["简日"]` |
| `release_group` | str | `-` 前的发行组 | `PandaQT` |
| `size_bytes` | int | 大小字符串解析 | `2420000000` |
| `is_single_episode` | bool | 是否单集资源 | `False` |
| `is_low_quality` | bool | 枪版/样片/CAM/TS/TC | `False` |
| `info_tags` | list[str] | 综合关键标签 | `["DTS", "字幕", "HDR"]` |

**实现要点**：
- 所有正则带「不嵌入英文单词」边界（`(?<![a-zA-Z])` + `(?![a-zA-Z])`），避免 `WEBRip` 误匹配 `RipRip`
- 清晰度按显式优先级匹配（4k > 2160p > 1080p > 720p > 480p），未知回退 50（默认）
- 低质判定独立于 source 字段，专判 `CAM / TS / TC / HDTC / R5 / 枪版 / 样片` 等关键词

详见 `scripts/title_parser.py`（350 行，纯函数，零网络依赖）。

---

## 五、筛选与排序

### 5.1 评分公式

```
quality_score = (清晰度权重 + 来源加分 + 音频加分 + HDR加分 + 编码加分 + 语言加分 + 做种加分)
                × 来源可信度 × 可用性系数 × 标题相关度 × 大小合理性
```

详细分值表见 `references/quality_scoring.md`。

### 5.2 硬性过滤（在评分前先排除）

| 过滤项 | 来源字段 | 备注 |
| --- | --- | --- |
| 枪版/样片 | `is_low_quality=True` | 直接排除，不计入 excluded（避免噪声） |
| 低相关度 | `relevance < min_relevance` | 标题/年份与查询不匹配，默认阈值 0.6 |
| 死链 | seeders=0 / 404 | 站内过滤后产出，外部死链由 L4 验证层处理 |

### 5.3 软性排序

按 `quality_score` 降序排，取 Top-N（默认 3）。同分时优先 `credibility` 高者。

### 5.4 大小合理性启发式

- 单集资源 < 100MB → 视为不完整 / 试看版，标注「无大小·试看」
- 整季资源过大（>50GB 且集数 ≤ 12）→ 提示「过大·高码」
- 标题无 size 字段 → 标「无大小」，评分不扣（不阻断），仅提示用户注意

`format_results.py` 渲染时把「总大小 / 集数 = 集均大小」展示给用户，帮其快速判断码率合理性。

---

## 六、稳定性机制

### 1️⃣ 健康度管理（health_check.py）

- 连续失败 3 次 → 摘除该源 1 小时（不发请求）
- 1 小时后自动重试
- 健康度记录持久化到 `.cache/source_health.json`（gitignore）

### 2️⃣ 缓存机制

- 按 query 标准化后 MD5 作为 key
- 1 小时 TTL（避免过期结果污染）
- 缓存目录 `.cache/queries/`（gitignore）
- 编排器可加 `--no-cache` 强制重检索

### 3️⃣ parser 容错

- 单个 parser 抛异常 → 捕获并标记该源失败，不影响其他源
- 整个 tier-1 全挂 → 自动回退 tier-2
- 所有源全挂 → 回报 `全源失败`，建议检查 `references/README.md` 配置

### 4️⃣ 反爬协同

- 全局信号量限制并发（默认 8 线程）
- 每源独立 sleep，避免被识别为同 IP 行为
- 失败重试 + 退避，但不无限重试（最多 2 次）

### 5️⃣ 评分与抓取解耦带来的稳定性

- fetcher 改了不影响评分（评分基于 parsed 字段）
- title_parser 改了不影响 fetcher（fetcher 不解析）
- 任何一处失败不会传导到其他层

---

## 七、维护指南

### 场景 1: 站点挂了

```
1. 立即止血: assets/config.json 的 web_sources[i].enabled = false
   （或更新 domains[] 换镜像）
2. 提交 PR 同步: references/source_registry.md 与 source_evaluation.md
3. 健康度管理 1 小时后自动重试，无需手动介入
```

### 场景 2: 站点改版

```
1. 改对应 scripts/search_sources/web/<id>.py 的 parse()
2. 解析逻辑（如果仅页面结构变）只需调整页面解析
3. 标题解析逻辑**保持原样**——改版不该影响 title_parser
4. 本地测一次 parse(query, cfg) 确认能拿标题串
5. 观察 health_check 1 周期后健康度
```

### 场景 3: 新增站点

```
1. F12 抓搜索请求，判断走 API 还是 HTML
2. 写 scripts/search_sources/web/<id>.py 实现 parse()
   **只抓标题串 + 链接 + 可选大小/做种**，不做信息提取
3. 在 assets/config.json + references/source_registry.md 注册
4. 本地测一次确认能拿标题串
5. 提交 PR 同步 source_evaluation.md 补测
```

### 场景 4: 评分规则调整

```
1. 改 scripts/aggregator.py 的 score()
2. 同步 references/quality_scoring.md 文档（分数表）
3. 改完立即影响全源——评分与 fetcher 解耦的好处
```

### 场景 5: 新字段需求（如「杜比视界」）

```
1. 改 scripts/title_parser.py 一处
   （在 _PATTERNS 加正则 + 字段赋值）
2. aggregator 自动识别新字段，评分表加新加分项
3. 完——全源全场景立即受益，无需逐站改
```

---

## 八、资源索引

| 文档 | 用途 | 受众 |
| --- | --- | --- |
| `SKILL.md` | Agent 操作手册（8 段标准模板） | Codex / Agent |
| `design.md` | 本文：架构/技术细节/维护指南 | 开发者 / Codex |
| `references/source_registry.md` | 数据源账本 + 注册格式 | 开发者 |
| `references/search_strategy.md` | 探查/反爬/分层/parser 契约 | 开发者 |
| `references/quality_scoring.md` | 评分公式 + 加分明细 | 开发者 |
| `references/source_evaluation.md` | 源实测评估（耗时/命中/质量） | 决策参考 |
| `scripts/title_parser.py` | 标题解析器（稳定核心） | 开发者 |
| `scripts/search_dispatcher.py` | 分层调度器 | 开发者 |
| `scripts/aggregator.py` | 富集 + 去重 + 评分 + 排序 + 过滤 | 开发者 |
| `scripts/format_results.py` | JSON → 带号列表渲染 | Agent |
| `scripts/health_check.py` | 源健康度管理 | 自动化 |
| `scripts/search_sources/web/*.py` | 各网页源 fetcher | 开发者（按需） |
| `assets/config.json` | 运行时配置（不入库） | 部署 |
| `assets/config_template.json` | 配置模板 | 部署 |
| `.cache/` | 运行时缓存（gitignore） | 运行时 |
